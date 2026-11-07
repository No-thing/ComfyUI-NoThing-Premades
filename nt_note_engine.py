"""No_Thing Workflow Note engine: scan folders, resolve links, download safely.
Pure python (no ComfyUI import at module level) so it can be tested alone."""
import os, json, threading, time, urllib.request, urllib.parse, urllib.error

ALLOWED_HOSTS = ("huggingface.co", "hf.co", "civitai.com", "civitai.red", "github.com",
                 "objects.githubusercontent.com", "cdn-lfs.huggingface.co", "cdn-lfs.hf.co",
                 "cas-bridge.xethub.hf.co", "xethub.hf.co", "cdn.civitai.com", "civitai-delivery-worker-prod.5ac0637cfd0766c97916cefa3764fbdf.r2.cloudflarestorage.com")
MODEL_EXT = (".safetensors", ".ckpt", ".pt", ".pth", ".bin", ".gguf", ".sft")
MIN_OK = 0.97          # a file smaller than 97% of the expected size counts as broken
JOBS = {}              # id -> job dict (progress)
_lock = threading.Lock()


def host_ok(url):
    h = (urllib.parse.urlparse(url).hostname or "").lower()
    return any(h == a or h.endswith("." + a) for a in ALLOWED_HOSTS)


def hf_resolve_url(url):
    """huggingface blob/tree page link -> direct resolve link"""
    p = urllib.parse.urlparse(url)
    if (p.hostname or "").endswith("huggingface.co") and "/blob/" in p.path:
        return urllib.parse.urlunparse(p._replace(path=p.path.replace("/blob/", "/resolve/", 1), query="download=true"))
    return url


def civitai_version_id(url):
    p = urllib.parse.urlparse(url)
    q = urllib.parse.parse_qs(p.query)
    if "/api/download/models/" in p.path:   # direct download link: .../models/<versionId>?fileId=
        return p.path.rstrip("/").split("/")[-1]
    return (q.get("modelVersionId") or [None])[0]


def civitai_file_id(url):
    return (urllib.parse.parse_qs(urllib.parse.urlparse(url).query).get("fileId") or [None])[0]


def civitai_resolve(url, key=None, api=None):
    """-> dict(file, size, download) from a Civitai model-version link. api = base (for tests)."""
    vid = civitai_version_id(url)
    p = urllib.parse.urlparse(url)
    base = api or f"{p.scheme}://{p.hostname}"
    if not vid:  # model page without version: take latest
        mid = p.path.strip("/").split("/")[1]
        d = _get_json(f"{base}/api/v1/models/{mid}", key)
        vid = str(d["modelVersions"][0]["id"])
    d = _get_json(f"{base}/api/v1/model-versions/{vid}", key)
    fs = [f for f in d.get("files", []) if f.get("type", "Model") in ("Model", "Pruned Model")] or d.get("files", [])
    fid = civitai_file_id(url)
    fs.sort(key=lambda f: (str(f.get("id")) != str(fid), not f.get("primary", False)))
    f = fs[0]
    return dict(file=f["name"], size=int(float(f.get("sizeKB", 0)) * 1024), download=f.get("downloadUrl"),
                version=d.get("name"))


def _get_json(url, key=None):
    req = urllib.request.Request(url, headers={"User-Agent": "NoThing-Note/1.0"})
    if key: req.add_header("Authorization", "Bearer " + key)
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())


def similar(name, candidates, n=3):
    """installed files that look like `name` (same words, other version/precision). Best first."""
    import difflib, re
    def key(x): return re.sub(r"[^a-z0-9]+", "", os.path.basename(x.replace("\\", "/")).lower().rsplit(".", 1)[0])
    k = key(name)
    scored = []
    for c in candidates:
        kc = key(c)
        r = difflib.SequenceMatcher(None, k, kc).ratio()
        if r >= 0.62: scored.append((r, c))
    scored.sort(reverse=True)
    return [c for _r, c in scored[:n]]


def file_state(path, expect=0):
    """found | broken (half-downloaded or empty)"""
    sz = os.path.getsize(path)
    if expect and sz < expect * MIN_OK: return "broken"
    if sz < 1024 * 100: return "broken"
    return "found"


def start_download(job_id, url, dest_dir, filename, size=0, key=None, headers_extra=None):
    if not host_ok(url):
        raise ValueError("host not allowed: " + url)
    filename = os.path.basename(filename.replace("\\", "/"))
    if not filename.lower().endswith(MODEL_EXT):
        raise ValueError("not a model file: " + filename)
    os.makedirs(dest_dir, exist_ok=True)
    final = os.path.join(dest_dir, filename)
    job = dict(id=job_id, file=filename, done=0, total=size, speed=0, state="running", error=None, path=final, cancel=False)
    with _lock: JOBS[job_id] = job
    threading.Thread(target=_run, args=(job, url, final, key, headers_extra), daemon=True).start()
    return job


def _run(job, url, final, key, headers_extra):
    part = final + ".part"
    try:
        have = os.path.getsize(part) if os.path.exists(part) else 0
        for _ in range(6):  # follow redirects manually so every hop is host-checked
            hdr = {"User-Agent": "NoThing-Note/1.0"}
            if have: hdr["Range"] = f"bytes={have}-"
            if key and (urllib.parse.urlparse(url).hostname or "").endswith(("huggingface.co", "civitai.com", "civitai.red", "hf.co")):
                hdr["Authorization"] = "Bearer " + key
            hdr.update(headers_extra or {})
            req = urllib.request.Request(url, headers=hdr)
            opener = urllib.request.build_opener(_NoRedirect)
            try:
                r = opener.open(req, timeout=30)
            except urllib.error.HTTPError as e:
                if e.code in (301, 302, 303, 307, 308):
                    url = urllib.parse.urljoin(url, e.headers["Location"])
                    if not host_ok(url): raise ValueError("redirect to blocked host: " + url)
                    if "Authorization" in hdr and not url.startswith(("https://huggingface.co", "https://civitai.")): pass
                    continue
                if e.code == 416 and have: break
                raise
            with r:
                if r.status == 200 and have: have = 0  # server ignored Range
                total = int(r.headers.get("Content-Length") or 0) + have
                if total: job["total"] = total
                mode = "ab" if have else "wb"
                t0, b0 = time.time(), have
                with open(part, mode) as out:
                    while True:
                        if job["cancel"]: job["state"] = "cancelled"; return
                        chunk = r.read(1 << 20)
                        if not chunk: break
                        out.write(chunk); have += len(chunk)
                        job["done"] = have
                        dt = time.time() - t0
                        if dt > 0.5: job["speed"] = (have - b0) / dt
            break
        else:
            raise RuntimeError("too many redirects")
        if job["total"] and os.path.getsize(part) < job["total"] * MIN_OK:
            raise RuntimeError("download ended early")
        os.replace(part, final)
        job["state"] = "done"; job["done"] = os.path.getsize(final)
    except Exception as e:
        job["state"] = "error"; job["error"] = str(e)


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k): return None
