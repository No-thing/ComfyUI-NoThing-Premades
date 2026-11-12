"""
No_Thing Workflow Note - checks a workflow's models and node packs, fetches what is missing,
and puts the right file name into the right loader slot.

The node never runs (no outputs). Its one hidden text field stores the card's extra links as JSON.
The card itself (web/nothing_note.js) reads every loader in the workflow, asks the routes below
what is installed, and calls them to download. Keys (Hugging Face / Civitai) stay in the browser
and travel with each request; the server never writes them to disk.
"""
import json
import os
import threading
import uuid

from . import nt_note_engine as E

try:
    from aiohttp import web
except Exception:
    web = None

try:
    import folder_paths
except Exception:
    folder_paths = None
try:
    from server import PromptServer
except Exception:  # the node still registers; only the download routes would be missing
    PromptServer = None

ALIAS = {"diffusion_models": ["diffusion_models", "unet"], "text_encoders": ["text_encoders", "clip"],
         "checkpoints": ["checkpoints"], "vae": ["vae"], "loras": ["loras"],
         "upscale_models": ["upscale_models"], "controlnet": ["controlnet"]}


class NoThingWorkflowCheck:
    CATEGORY = "No_Thing"
    DESCRIPTION = ("Checks the models and node packs this workflow needs, downloads what is missing, and puts "
                   "the right file into each loader slot. Nothing runs - the node has no outputs.")
    SEARCH_ALIASES = ["note", "workflow note", "workflow check", "model check", "download models", "installer", "no_thing"]
    FUNCTION = "run"
    RETURN_TYPES = ()

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"note": ("STRING", {"default": "{}", "multiline": True,
                "tooltip": "Storage for the card (extra links). Edited by the card, not by hand."})}}

    def run(self, note):
        return ()


def _norm(f):
    return (f or "").replace("\\", "/")


def _bad(f):
    f = _norm(f)
    return (not f) or f.startswith("/") or ".." in f.split("/") or ":" in f


def _names(kind):
    out = []
    for k in ALIAS.get(kind, [kind]):
        try:
            out += list(folder_paths.get_filename_list(k))
        except Exception:
            pass
    return list(dict.fromkeys(out))


def _find(kind, f):
    """exact file (with its sub-folder) in any folder ComfyUI knows for this kind -> path or None"""
    for k in ALIAS.get(kind, [kind]):
        try:
            p = folder_paths.get_full_path(k, f) or folder_paths.get_full_path(k, _norm(f).replace("/", os.sep))
        except Exception:
            p = None
        if p and os.path.isfile(p):
            return p
    return None


def check_item(kind, f, size=0):
    if kind not in ALIAS or _bad(f):
        return dict(state="bad")
    p = _find(kind, f)
    if p:
        return dict(state=E.file_state(p, size), path=p)
    # same name but filed in another sub-folder counts as a match, never as installed
    base = _norm(f).split("/")[-1].lower()
    same = [n for n in _names(kind) if _norm(n).split("/")[-1].lower() == base]
    near = E.similar(f, [n for n in _names(kind) if n not in same])
    return dict(state="missing", matches=(same + near)[:3])


def _dest(kind, f):
    for k in ALIAS.get(kind, [kind]):
        try:
            roots = folder_paths.get_folder_paths(k)
        except Exception:
            roots = []
        if roots:
            return os.path.join(roots[0], *_norm(f).split("/")[:-1]), _norm(f).split("/")[-1]
    raise ValueError("ComfyUI has no folder for " + kind)


def _is_civitai(url):
    h = (E.urllib.parse.urlparse(url).hostname or "")
    return "civitai" in h


def start_get(kind, f, url, key=None, size=0):
    if kind not in ALIAS or _bad(f):
        raise ValueError("bad file name")
    url = E.hf_resolve_url(url or "")
    if not url or not E.host_ok(url):
        raise ValueError("no usable link (only Hugging Face, Civitai and GitHub are allowed)")
    if _is_civitai(url):
        r = E.civitai_resolve(url, key)
        url, size = r["download"], r["size"] or size
    dest, name = _dest(kind, f)
    jid = uuid.uuid4().hex[:10]
    E.start_download(jid, url, dest, name, size, key)
    return jid


def _register_routes():
    routes = PromptServer.instance.routes

    @routes.post("/nothing_check/check")
    async def nt_check(request):
        b = await request.json()
        res = []
        for it in b.get("items", [])[:200]:
            try:
                res.append(check_item(it.get("kind"), it.get("file"), it.get("size") or 0))
            except Exception as e:
                res.append(dict(state="error", error=str(e)))
        return web.json_response(dict(items=res))

    @routes.post("/nothing_check/get")
    async def nt_get(request):
        b = await request.json()
        try:
            jid = start_get(b.get("kind"), b.get("file"), b.get("url"), b.get("key") or None, b.get("size") or 0)
            return web.json_response(dict(id=jid))
        except Exception as e:
            return web.json_response(dict(error=str(e)), status=400)

    @routes.get("/nothing_check/progress")
    async def nt_progress(request):
        out = {}
        for i in [i for i in request.query.get("ids", "").split(",") if i]:
            j = E.JOBS.get(i)
            if j:
                out[i] = {k: j.get(k) for k in ("file", "done", "total", "speed", "state", "error", "note")}
        return web.json_response(out)

    @routes.post("/nothing_check/cancel")
    async def nt_cancel(request):
        j = E.JOBS.get((await request.json()).get("id"))
        if j:
            j["cancel"] = True
        return web.json_response(dict(ok=True))


if PromptServer is not None and web is not None:
    try:
        _register_routes()
    except Exception as e:                      # a clashing route must never stop the node from existing
        print(f"[No_Thing] Workflow Check: download routes not registered ({e})")


NODE_CLASS_MAPPINGS = {"NoThingWorkflowCheck": NoThingWorkflowCheck}
NODE_DISPLAY_NAME_MAPPINGS = {"NoThingWorkflowCheck": "No_Thing Workflow Check (models + packs)"}
