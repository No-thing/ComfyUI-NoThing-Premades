import { app } from "../../scripts/app.js";
import { api } from "../../scripts/api.js";
import { hit } from "./nt_interact.js";

// No_Thing Workflow Note v2 - an automatic checker / installer card.
// It reads every loader in the workflow (subgraphs included), asks the server which files exist,
// downloads what is missing, and puts the right file name into the right loader slot.
// Drawn on canvas with the shared hit-region system (same one the roulettes use).

const COL = { bg: "#1D1D1D", head: "#2B2B2B", row: "#232326", line: "#383838", or: "#E0893F", wh: "#EAE5DC", mut: "#9A968D", dark: "#1A1A1D" };
const W = 700, PAD = 16, ROW = 34, KEYSTORE = "nothing_note_keys";
const font = (w, s, f) => `${w} ${s}px ${f || '"Montserrat Alternates", "Segoe UI", sans-serif'}`;

(function loadFonts() {
  [["Audiowide", "./fonts/Audiowide-Regular.ttf", "400"], ["Montserrat Alternates", "./fonts/MontserratAlternates-Light.ttf", "300 700"]].forEach(([fam, rel, wt]) => {
    try {
      if ([...document.fonts].some((f) => f.family.replace(/"/g, "") === fam)) return;
      const f = new FontFace(fam, `url(${new URL(rel, import.meta.url).href})`, { weight: wt });
      f.load().then(() => { document.fonts.add(f); app.graph?.setDirtyCanvas(true, true); }).catch(() => {});
    } catch (e) { /* ignore */ }
  });
})();

// ---- what we know how to fetch (file name -> link). The note's own links override these. ------
const HF = "https://huggingface.co/";
const KNOWN = {
  "qwen_image_2.1_int8_convrot.safetensors": HF + "Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_int8_convrot.safetensors",
  "qwen_image_2.1_bf16.safetensors": HF + "Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_bf16.safetensors",
  "qwen3vl_8b_int8_convrot.safetensors": HF + "Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3vl_8b_int8_convrot.safetensors",
  "qwen3vl_8b_bf16.safetensors": HF + "Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3vl_8b_bf16.safetensors",
  "qwen_image_2.1_vae_bf16.safetensors": HF + "Comfy-Org/Qwen-Image-2.1/resolve/main/vae/qwen_image_2.1_vae_bf16.safetensors",
  "qwen_image_vae.safetensors": HF + "Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors",
  "flux2-vae.safetensors": HF + "Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors",
  "qwen-image-2.1-outpaint-v2.safetensors": HF + "ausboss/Qwen-Image-2.1-Outpaint-LoRA/resolve/main/qwen-image-2.1-outpaint-v2.safetensors",
};
const PACKS = [
  { name: "Krea2T Enhancer", url: "https://github.com/capitan01R/ComfyUI-Krea2T-Enhancer", re: /krea2t/i },
];
const KIND = { ckpt_name: "checkpoints", unet_name: "diffusion_models", clip_name: "text_encoders", clip_name1: "text_encoders", clip_name2: "text_encoders", clip_name3: "text_encoders", vae_name: "vae", lora_name: "loras", control_net_name: "controlnet" };
const KIND_LABEL = { checkpoints: "CHECKPOINT", diffusion_models: "MODEL", text_encoders: "TEXT ENC", vae: "VAE", loras: "LORA", upscale_models: "UPSCALER", controlnet: "CONTROLNET" };
const SKIP_TYPES = new Set(["Reroute", "Note", "MarkdownNote", "PrimitiveNode", "NoThingWorkflowCheck"]);

const keys = () => { try { return JSON.parse(localStorage.getItem(KEYSTORE) || "{}"); } catch (e) { return {}; } };
const setKeys = (k) => { try { localStorage.setItem(KEYSTORE, JSON.stringify(k)); } catch (e) { /* ignore */ } };
const keyFor = (url) => { const h = (url || "").match(/\/\/([^/]+)/)?.[1] || ""; return /civitai/.test(h) ? keys().civitai : /huggingface|hf\.co/.test(h) ? keys().hf : ""; };
const DIRS = ["diffusion_models", "text_encoders", "vae", "loras", "checkpoints", "upscale_models", "controlnet"];
const DIR_KIND = { unet: "diffusion_models", clip: "text_encoders" };
const kindOfDir = (d) => { d = DIR_KIND[d] || d; return DIRS.includes(d) ? d : ""; };
const okUrl = (u) => (/^https?:\/\/\S+$/i.test(String(u || "").trim()) ? String(u).trim() : "");
const parse = (s) => {
  let d = {}; try { d = JSON.parse(s) || {}; } catch (e) { /* ignore */ }
  const models = (Array.isArray(d.models) ? d.models : []).filter((m) => m && m.name).map((m) => ({ name: String(m.name).trim(), dir: String(m.dir || ""), size: String(m.size || ""), url: okUrl(m.url), note: String(m.note || "") }));
  const packs = (Array.isArray(d.packs) ? d.packs : []).filter((p) => p && (p.name || p.node)).map((p) => ({ name: String(p.name || p.node), url: okUrl(p.url), node: String(p.node || "") }));
  // notes made by the first version kept links as { file: url }
  if (d.links && !Array.isArray(d.links)) for (const [f, u] of Object.entries(d.links)) if (okUrl(u) && !models.some((m) => base(m.name) === base(f))) models.push({ name: f, dir: "", size: "", url: okUrl(u), note: "" });
  return { models, packs };
};
const base = (f) => String(f).replace(/\\/g, "/").split("/").pop().toLowerCase();
const gb = (n) => (n >= 1e9 ? (n / 1e9).toFixed(1) + " GB" : n >= 1e6 ? Math.round(n / 1e6) + " MB" : "");

// ---- reading the workflow ---------------------------------------------------------------------
function allNodes(g, out, depth) {
  if (!g || depth > 6) return out;
  for (const n of (g._nodes || g.nodes || [])) {
    out.push(n);
    if (n.subgraph) allNodes(n.subgraph, out, depth + 1);
  }
  return out;
}

function scanGraph(extra) {
  const rows = new Map(), missingTypes = new Map();
  const reg = (window.LiteGraph && window.LiteGraph.registered_node_types) || {};
  for (const n of allNodes(app.graph, [], 0)) {
    const type = n.comfyClass || n.type;
    const off = n.mode === 2 || n.mode === 4;
    if (type && !SKIP_TYPES.has(type) && !n.subgraph && !reg[type] && !/^[0-9a-f]{8}-[0-9a-f]{4}-/.test(type)) {
      const m = missingTypes.get(type) || { type, off: true }; if (!off) m.off = false; missingTypes.set(type, m);
    }
    for (const w of (n.widgets || [])) {
      let kind = KIND[w.name];
      if (!kind && w.name === "model_name" && /upscale/i.test(type || "")) kind = "upscale_models";
      if (!kind || typeof w.value !== "string" || !w.value || /^(none|undefined|null)$/i.test(w.value)) continue;
      const id = kind + "|" + w.value;
      const r = rows.get(id) || { id, kind, file: w.value, refs: [], off: true };
      r.refs.push(w); if (!off) r.off = false;
      rows.set(id, r);
    }
  }
  const S = (extra && extra.data) || { models: [], packs: [] };
  for (const m of S.models) {                                   // rows typed into the note that no loader asks for (yet)
    const kind = kindOfDir(m.dir); if (!kind || [...rows.values()].some((r) => r.kind === kind && base(r.file) === base(m.name))) continue;
    rows.set(kind + "|" + m.name, { id: kind + "|" + m.name, kind, file: m.name, refs: [], off: false, manual: true });
  }
  for (const p of S.packs) if (p.node && !reg[p.node] && !missingTypes.has(p.node)) missingTypes.set(p.node, { type: p.node, off: false });
  return { rows: [...rows.values()], missingTypes: [...missingTypes.values()] };
}

function linkFor(S, file) { const m = S.data.models.find((x) => base(x.name) === base(file) && x.url); return (m && m.url) || KNOWN[base(file)] || ""; }
const save = (node) => { const S = node.__ntn; S.w.value = JSON.stringify(S.data); };

// ---- talking to the server ----------------------------------------------------------------------
async function check(node) {
  const S = node.__ntn; if (S.busy) return;
  S.busy = true; S.err = ""; node.setDirtyCanvas(true, true);
  try {
    const sc = scanGraph(S);
    const r = await api.fetchApi("/nothing_check/check", { method: "POST", body: JSON.stringify({ items: sc.rows.map((x) => ({ kind: x.kind, file: x.file })) }) });
    const j = await r.json();
    sc.rows.forEach((x, i) => Object.assign(x, j.items[i] || { state: "error" }));
    S.rows = sc.rows; S.types = sc.missingTypes; S.when = Date.now();
  } catch (e) { S.err = "Could not reach ComfyUI to check the files."; }
  S.busy = false; relayout(node); node.setDirtyCanvas(true, true);
}

function poll(node) {
  const S = node.__ntn; if (S.polling) return;
  S.polling = true;
  const tick = async () => {
    const ids = Object.values(S.jobs).filter((j) => j.state === "running").map((j) => j.id);
    if (!ids.length) { S.polling = false; return; }
    try {
      const j = await (await api.fetchApi("/nothing_check/progress?ids=" + ids.join(","))).json();
      let finished = false;
      for (const k of Object.keys(S.jobs)) {
        const job = S.jobs[k], u = j[job.id]; if (!u) continue;
        const was = job.state; Object.assign(job, u);
        if (was === "running" && u.state !== "running") finished = true;
      }
      node.setDirtyCanvas(true, true);
      if (finished) { try { await app.refreshComboInNodes?.(); } catch (e) { /* ignore */ } S.polling = false; await check(node); poll(node); return; }
    } catch (e) { /* try again */ }
    setTimeout(tick, 700);
  };
  tick();
}

async function getOne(node, r) {
  const S = node.__ntn, url = linkFor(S, r.file);
  if (!url) { addLink(node, r); return; }
  if (S.jobs[r.id]?.state === "running") return;
  try {
    const res = await api.fetchApi("/nothing_check/get", { method: "POST", body: JSON.stringify({ kind: r.kind, file: r.file, url, key: keyFor(url) }) });
    const j = await res.json();
    if (j.error) { S.jobs[r.id] = { state: "error", error: j.error }; }
    else { S.jobs[r.id] = { id: j.id, state: "running", done: 0, total: 0, speed: 0 }; poll(node); }
  } catch (e) { S.jobs[r.id] = { state: "error", error: "Could not start the download." }; }
  node.setDirtyCanvas(true, true);
}

function getAll(node) {
  const S = node.__ntn;
  for (const r of S.rows || []) if (r.state === "missing" && !r.off && linkFor(S, r.file)) getOne(node, r);
}

function assign(node, r, name) {
  for (const w of r.refs) {
    try { w.value = name; w.callback?.(name); } catch (e) { /* ignore */ }
  }
  app.graph?.setDirtyCanvas?.(true, true);
  check(node);
}

function ask(title, value, cb) {
  const ev = new MouseEvent("click");
  if (app.canvas?.prompt) app.canvas.prompt(title, value, cb, ev); else { const v = window.prompt(title, value); if (v !== null) cb(v); }
}

function addLink(node, r) {
  ask("Download link for " + base(r.file) + " (Hugging Face, Civitai)", "", (v) => {
    v = String(v || "").trim(); if (!v) return;
    v = okUrl(v); if (!v) return;
    const D = node.__ntn.data, m = D.models.find((x) => base(x.name) === base(r.file));
    if (m) m.url = v; else D.models.push({ name: r.file, dir: r.kind, size: "", url: v, note: "" });
    save(node); node.setDirtyCanvas(true, true);
  });
}

function setKeysPrompt(node) {
  const k = keys();
  ask("Hugging Face token (only needed for gated files; stays in this browser). Empty = none", k.hf || "", (hf) => {
    ask("Civitai API key (stays in this browser). Empty = none", k.civitai || "", (cv) => { setKeys({ hf: String(hf || "").trim(), civitai: String(cv || "").trim() }); });
  });
}

async function installPack(node, key, url) {
  const S = node.__ntn;
  try {
    const j = await (await api.fetchApi("/nothing_check/install_pack", { method: "POST", body: JSON.stringify({ url }) })).json();
    S.jobs[key] = { id: j.id, state: "running", note: "starting" }; poll(node);
  } catch (e) { S.jobs[key] = { state: "error", error: "Could not start the install." }; }
  node.setDirtyCanvas(true, true);
}

// ---- the editor: a plain dialog over the page (never inside the node, so it cannot squeeze) -----
const CSS = `
.ntn-ov{position:fixed;inset:0;z-index:10000;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,.6);font:13px "Montserrat Alternates","Segoe UI",sans-serif}
.ntn-dg{width:min(1000px,95vw);max-height:92vh;display:flex;flex-direction:column;background:#1D1D1D;border:1px solid #383838;border-radius:12px;color:#EAE5DC;box-shadow:0 14px 50px rgba(0,0,0,.7)}
.ntn-dg *{box-sizing:border-box}
.ntn-h{padding:14px 18px;border-bottom:1px solid #383838;display:flex;align-items:center;gap:10px}
.ntn-h b{font:400 22px Audiowide,serif;color:#E0893F;flex:1}
.ntn-b{padding:14px 18px;overflow:auto;display:flex;flex-direction:column;gap:12px}
.ntn-f{padding:12px 18px;border-top:1px solid #383838;display:flex;gap:8px;align-items:center}
.ntn-f .sp{flex:1}
.ntn-t{display:flex;flex-direction:column;gap:5px}
.ntn-r{display:grid;gap:6px;align-items:center}
.ntn-r.m{grid-template-columns:1.5fr 160px 70px 2fr 1fr 26px}
.ntn-r.p{grid-template-columns:1fr 2fr 1.2fr 26px}
.ntn-r.hd{color:#9A968D;font-size:10px;letter-spacing:.08em;text-transform:uppercase}
.ntn-dg input,.ntn-dg select,.ntn-dg textarea{width:100%;padding:6px 8px;background:#2B2B2B;border:1px solid #444;border-radius:6px;color:#EAE5DC;font:12px "Montserrat Alternates","Segoe UI",sans-serif;outline:none}
.ntn-dg input:focus,.ntn-dg select:focus,.ntn-dg textarea:focus{border-color:#E0893F}
.ntn-dg textarea{min-height:300px;font:12px monospace}
.ntn-bt{height:28px;padding:0 12px;border-radius:6px;border:1px solid #444;background:#383838;color:#EAE5DC;font:700 12px "Montserrat Alternates","Segoe UI",sans-serif;cursor:pointer}
.ntn-bt:hover{background:#444}.ntn-bt.pr{background:#E0893F;border-color:#E0893F;color:#1A1A1D}.ntn-bt.pr:hover{background:#EE9A52}
.ntn-x{width:26px;height:26px;padding:0;border:0;background:transparent;color:#9A968D;cursor:pointer;font-size:14px}.ntn-x:hover{color:#fff}
.ntn-hint{color:#9A968D;font-size:11px}.ntn-er{color:#E0893F;font-size:12px}
`;
let dialog = null;
function openEditor(node) {
  const S = node.__ntn; if (dialog) dialog.remove();
  if (!document.getElementById("ntn-css")) { const st = document.createElement("style"); st.id = "ntn-css"; st.textContent = CSS; document.head.appendChild(st); }
  const el = (t, c, x) => { const e = document.createElement(t); if (c) e.className = c; if (x !== undefined) e.textContent = x; return e; };
  const ov = el("div", "ntn-ov"), dg = el("div", "ntn-dg"), hd = el("div", "ntn-h"), bd = el("div", "ntn-b"), ft = el("div", "ntn-f");
  hd.append(el("b", "", "Workflow Check")); const jbtn = el("button", "ntn-bt", "JSON"); jbtn.type = "button"; hd.append(jbtn);
  const err = el("span", "ntn-er"), cancel = el("button", "ntn-bt", "Cancel"), saveB = el("button", "ntn-bt pr", "Save");
  cancel.type = saveB.type = "button"; ft.append(err, el("span", "sp"), cancel, saveB);
  dg.append(hd, bd, ft); ov.append(dg);
  const inp = (v, ph) => { const i = el("input"); i.type = "text"; i.value = v || ""; if (ph) i.placeholder = ph; return i; };
  const table = (cls, heads, rows, make) => {
    const box = el("div", "ntn-t"), h = el("div", "ntn-r hd " + cls); heads.forEach((x) => h.append(el("span", "", x))); h.append(el("span")); box.append(h);
    const body = el("div", "ntn-t"); box.append(body); const list = [];
    const add = (row) => { const line = el("div", "ntn-r " + cls), cells = make(row || {}); cells.forEach((c) => line.append(c)); const x = el("button", "ntn-x", "✕"); x.type = "button"; x.title = "Remove row"; const ent = { line, cells }; x.onclick = () => { line.remove(); list.splice(list.indexOf(ent), 1); }; line.append(x); body.append(line); list.push(ent); };
    rows.forEach(add); return { box, add, list };
  };
  const dirSel = (v) => { const s = el("select"); const o0 = el("option", "", "(folder)"); o0.value = ""; s.append(o0); for (const d of DIRS) { const o = el("option", "", d); o.value = d; s.append(o); } s.value = kindOfDir(v) || ""; return s; };
  const D = JSON.parse(JSON.stringify(S.data));
  const models = table("m", ["File name", "Folder", "Size", "Download link (paste here)", "Note"], D.models, (r) => [inp(r.name, "model.safetensors"), dirSel(r.dir), inp(r.size, "13 GB"), inp(r.url, "https://huggingface.co/.../resolve/main/file.safetensors"), inp(r.note, "tip / credit")]);
  const packs = table("p", ["Pack", "GitHub link", "Probe node (any node class from the pack)"], D.packs, (r) => [inp(r.name, "ComfyUI-AusBoss"), inp(r.url, "https://github.com/..."), inp(r.node, "NodeClassName")]);
  const tools = (btns) => { const d = el("div"); d.style.cssText = "display:flex;gap:6px;flex-wrap:wrap"; btns.forEach(([t, f]) => { const b = el("button", "ntn-bt", t); b.type = "button"; b.onclick = f; d.append(b); }); return d; };
  const detect = () => {                                       // every loader file in the workflow becomes a row, links pre-filled when known
    const have = new Set(models.list.map((e) => base(e.cells[0].value)));
    for (const r of scanGraph(S).rows) { if (r.manual || have.has(base(r.file))) continue; models.add({ name: r.file, dir: r.kind, url: linkFor(S, r.file) }); }
  };
  const form = el("div", "ntn-b"); form.style.padding = "0";
  form.append(el("div", "ntn-hint", "Paste the download link next to each file. Get / Get everything on the card use these links. Bypassed loaders are skipped."), models.box, tools([["+ model", () => models.add({})], ["Detect from this workflow", detect]]), el("div", "ntn-hint", "Node packs: the probe node is checked against this install; missing = Install button (GitHub)."), packs.box, tools([["+ pack", () => packs.add({})]]));
  const read = () => parse(JSON.stringify({
    models: models.list.map((e) => ({ name: e.cells[0].value, dir: e.cells[1].value, size: e.cells[2].value, url: e.cells[3].value, note: e.cells[4].value })),
    packs: packs.list.map((e) => ({ name: e.cells[0].value, url: e.cells[1].value, node: e.cells[2].value })),
  }));
  let jsonMode = false; const ta = el("textarea");
  bd.append(form);
  jbtn.onclick = () => {
    if (!jsonMode) { ta.value = JSON.stringify(read(), null, 2); bd.textContent = ""; bd.append(ta); jbtn.textContent = "Form"; jsonMode = true; }
    else { try { S.data = parse(ta.value); } catch (e) { err.textContent = "That JSON does not parse."; return; } close(); openEditor(node); }
  };
  const close = () => { ov.remove(); dialog = null; };
  saveB.onclick = () => {
    let next; if (jsonMode) { try { JSON.parse(ta.value); } catch (e) { err.textContent = "That JSON does not parse."; return; } next = parse(ta.value); } else next = read();
    S.data = next; save(node); close(); check(node);
  };
  cancel.onclick = close;
  ov.addEventListener("keydown", (e) => { e.stopPropagation(); if (e.key === "Escape") close(); if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) saveB.onclick(); });
  ov.addEventListener("pointerdown", (e) => { e.stopPropagation(); if (e.target === ov) close(); });
  ov.addEventListener("wheel", (e) => e.stopPropagation());
  document.body.append(ov); dialog = ov;
}

// ---- layout + drawing -----------------------------------------------------------------------------
function packFor(S, type) {
  const p = PACKS.find((x) => x.re.test(type));
  const mine = S.data.packs.find((x) => x.node === type && x.url) || S.data.packs.find((x) => x.name === type && x.url);
  if (mine) return { name: mine.name, url: mine.url };
  return p ? { name: p.name, url: p.url } : { name: type, url: "" };
}

const rowH = (r) => (r.state === "missing" && r.matches && r.matches.length ? ROW + 14 : ROW);
function relayout(node) {
  const S = node.__ntn;
  const want = Math.max(S.h + 40, 160);                 // card height + title bar + margin
  if (Math.abs(node.size[1] - want) > 1 || node.size[0] < W) node.setSize([Math.max(W, node.size[0]), want]);
}

function rr(ctx, x, y, w, h, r) { ctx.beginPath(); ctx.roundRect ? ctx.roundRect(x, y, w, h, r) : ctx.rect(x, y, w, h); }
function txt(ctx, t, x, y, color, f, align) { ctx.save(); ctx.font = f; ctx.textAlign = align || "left"; ctx.shadowColor = "rgba(0,0,0,.55)"; ctx.shadowBlur = 3; ctx.shadowOffsetY = 1; ctx.fillStyle = color; ctx.fillText(t, x, y); ctx.restore(); }
function fit(ctx, t, maxW) { if (ctx.measureText(t).width <= maxW) return t; while (t.length > 4 && ctx.measureText(t + "…").width > maxW) t = t.slice(0, -1); return t + "…"; }

function btn(ctx, node, id, label, x, y, w, h, fn, primary) {
  const hov = node.__ntHover === id;
  rr(ctx, x, y, w, h, 6);
  ctx.fillStyle = primary ? (hov ? "#EE9A52" : COL.or) : (hov ? "#444" : "#383838"); ctx.fill();
  txt(ctx, label, x + w / 2, y + h / 2 + 4, primary ? "#1A1A1D" : COL.wh, font(700, 12), "center");
  hit(node, id, x, y, w, h, fn, "pointer", () => { if (node.__ntHover !== id) { node.__ntHover = id; node.setDirtyCanvas(true, true); } return "pointer"; });
}

function drawCard(node, ctx, y0, width) {
  const S = node.__ntn, w = Math.max(width, 300) - PAD * 2;
  node.__lcHits && node.__lcHits.clear();
  const x0 = PAD;
  const rows = S.rows || [], types = S.types || [];
  const need = rows.filter((r) => !r.off && r.state !== "found");
  const missing = need.length + types.filter((t) => !t.off).length;
  // header
  rr(ctx, x0, y0 + 4, w, 62, 10); ctx.fillStyle = COL.head; ctx.fill();
  txt(ctx, "Workflow Check", x0 + 16, y0 + 36, COL.or, font(400, 24, "Audiowide, serif"));
  const sub = S.busy ? "checking…" : S.err ? S.err : !rows.length ? "no model loaders found in this workflow" : missing ? `${missing} thing${missing > 1 ? "s" : ""} to sort out` : "everything is in place - press Run";
  txt(ctx, sub, x0 + 16, y0 + 56, missing || S.err ? COL.or : COL.mut, font(500, 12));
  let bx = x0 + w - 10;
  const bw = [60, 64, 64, 140]; const labels = ["Edit", "Keys", "Check", "Get everything"];
  const fns = [() => openEditor(node), () => setKeysPrompt(node), () => check(node), () => getAll(node)];
  for (let i = 0; i < 4; i++) { bx -= bw[i]; btn(ctx, node, "h" + i, labels[i], bx, y0 + 20, bw[i], 28, fns[i], i === 3); bx -= 8; }

  let y = y0 + 76;
  if (!rows.length) { txt(ctx, S.busy ? "…" : "Add this note to a workflow that has model loaders.", x0 + 16, y + 20, COL.mut, font(500, 13)); y += ROW; }
  for (const r of rows) {
    const rh = rowH(r), job = S.jobs[r.id], running = job && job.state === "running";
    const url0 = linkFor(S, r.file);
    const zone = running ? 330 : r.state === "found" ? 110 : (r.matches && r.matches.length ? 100 : 0) + (url0 ? 54 : 132) + 90;
    rr(ctx, x0, y, w, rh - 4, 7); ctx.fillStyle = COL.row; ctx.fill();
    ctx.save(); ctx.globalAlpha = r.off ? 0.5 : 1;
    txt(ctx, KIND_LABEL[r.kind] || r.kind, x0 + 12, y + 20, COL.mut, font(700, 10));
    ctx.font = font(500, 13); const name = fit(ctx, String(r.file).replace(/\\/g, "/"), w - 98 - zone);
    txt(ctx, name, x0 + 86, y + 21, COL.wh, font(500, 13));
    if (r.state === "missing" && r.matches && r.matches.length) { ctx.font = font(500, 11); txt(ctx, fit(ctx, "you have: " + r.matches[0].replace(/\\/g, "/"), w - 100), x0 + 86, y + 39, COL.mut, font(500, 11)); }
    ctx.restore();
    const bxr = x0 + w - 10, by = y + 3, bh = ROW - 10;
    if (job && job.state === "running") {
      const pw = 150, px = bxr - pw - 56, pct = job.total ? job.done / job.total : 0;
      rr(ctx, px, y + 12, pw, 8, 4); ctx.fillStyle = "#383838"; ctx.fill();
      rr(ctx, px, y + 12, Math.max(6, pw * pct), 8, 4); ctx.fillStyle = COL.or; ctx.fill();
      txt(ctx, job.total ? Math.round(pct * 100) + "%  " + (job.speed ? (job.speed / 1e6).toFixed(1) + " MB/s" : "") : "…", px - 8, y + 21, COL.mut, font(500, 11), "right");
      btn(ctx, node, "c" + r.id, "Stop", bxr - 50, by, 50, bh, async () => { await api.fetchApi("/nothing_check/cancel", { method: "POST", body: JSON.stringify({ id: job.id }) }); job.state = "cancelled"; }, false);
    } else if (r.state === "found") {
      txt(ctx, "✓ installed", bxr, y + 21, COL.mut, font(600, 12), "right");
    } else {
      const label = r.state === "broken" ? "BROKEN FILE" : job?.state === "error" ? "FAILED" : "MISSING";
      let rx = bxr;
      const url = linkFor(S, r.file);
      const act = [];
      if (r.matches && r.matches.length) act.push(["Use match", () => assign(node, r, r.matches[0]), false, 90]);
      if (url) act.push(["Get", () => getOne(node, r), true, 54]);
      else act.push(["Add link", () => addLink(node, r), false, 78], ["Find", () => window.open("https://huggingface.co/models?search=" + encodeURIComponent(base(r.file).replace(/\.[a-z]+$/, "")), "_blank"), false, 54]);
      for (const [lab, fn, prim, bw2] of act.reverse()) { rx -= bw2; btn(ctx, node, "a" + r.id + lab, lab, rx, by, bw2, bh, fn, prim); rx -= 6; }
      txt(ctx, job?.state === "error" ? "FAILED" : label, rx - 4, y + 21, COL.or, font(700, 11), "right");
      if (job?.state === "error") { ctx.font = font(500, 10); node.__ntErr = job.error; }
    }
    y += rh;
  }
  if (types.length) {
    y += 8; txt(ctx, "NODE PACKS", x0 + 4, y + 14, COL.mut, font(700, 11)); y += 22;
    for (const t of types) {
      const p = packFor(S, t.type), job = S.jobs["pack|" + t.type];
      rr(ctx, x0, y, w, ROW - 4, 7); ctx.fillStyle = COL.row; ctx.fill();
      txt(ctx, "NODE", x0 + 12, y + 20, COL.mut, font(700, 10));
      ctx.font = font(500, 13);
      txt(ctx, fit(ctx, t.type + (p.name !== t.type ? "  (" + p.name + ")" : ""), w - 300), x0 + 86, y + 21, COL.wh, font(500, 13));
      const by = y + 3, bh = ROW - 10, bxr = x0 + w - 10;
      if (job && job.state === "running") txt(ctx, job.note || "installing…", bxr, y + 21, COL.or, font(600, 12), "right");
      else if (job && job.state === "done") txt(ctx, job.note || "installed - restart ComfyUI", bxr, y + 21, COL.or, font(600, 12), "right");
      else if (p.url) { btn(ctx, node, "p" + t.type, job?.state === "error" ? "Retry" : "Install", bxr - 70, by, 70, bh, () => installPack(node, "pack|" + t.type, p.url), true); txt(ctx, job?.state === "error" ? "FAILED" : "MISSING", bxr - 82, y + 21, COL.or, font(700, 11), "right"); }
      else { btn(ctx, node, "p" + t.type, "Add repo link", bxr - 110, by, 110, bh, () => ask("GitHub link for the pack that has '" + t.type + "'", "https://github.com/", (v) => { v = String(v || "").trim(); if (v) { v = okUrl(v); if (!v) return; S.data.packs.push({ name: t.type, url: v, node: t.type }); save(node); node.setDirtyCanvas(true, true); } }), false); txt(ctx, "MISSING", bxr - 122, y + 21, COL.or, font(700, 11), "right"); }
      y += ROW;
    }
    txt(ctx, "After a node pack installs, restart ComfyUI once and reload the page.", x0 + 4, y + 12, COL.mut, font(500, 11)); y += 18;
  }
  const nh = y - y0 + 12;
  if (Math.abs(nh - S.h) > 1) { S.h = nh; setTimeout(() => relayout(node), 0); }
}

app.registerExtension({
  name: "NoThing.WorkflowCheck",
  beforeRegisterNodeDef(nodeType, nodeData) {
    if (nodeData.name !== "NoThingWorkflowCheck") return;
    const created = nodeType.prototype.onNodeCreated;
    nodeType.prototype.onNodeCreated = function () {
      created?.apply(this, arguments);
      try { build(this); } catch (e) { console.error("[No_Thing] Workflow Check card failed:", e); }
    };
    function build(node) {
      const w = node.widgets.find((x) => x.name === "note");
      const S = (node.__ntn = { w, data: parse(w.value), rows: [], types: [], jobs: {}, h: 200 });
      w.hidden = true; w.computeSize = () => [0, -4]; w.computeLayoutSize = () => ({ minHeight: 0, maxHeight: 0, minWidth: 0 }); w.draw = () => {};
      const card = {
        name: "card", type: "nt_card", value: "", options: { serialize: false }, serialize: false,
        computeSize: () => [W, S.h], computeLayoutSize: () => ({ minHeight: S.h, minWidth: 300 }),
        draw(ctx, n, width, y) { drawCard(n, ctx, y, width); },
      };
      if (node.addCustomWidget) node.addCustomWidget(card); else node.widgets.push(card);
      node.color = "#444444"; node.bgcolor = COL.bg;
      node.setSize([W, 260]);
      const onRes = node.onResize;
      node.onResize = function (size) { if (size && size[0] < 420) size[0] = 420; return onRes ? onRes.apply(this, arguments) : undefined; };
      node.__lcHoverOut = () => { node.__ntHover = null; node.setDirtyCanvas(true, true); };
      node.__ntnFocus = () => { if (Date.now() - (S.when || 0) > 4000) check(node); };
      setTimeout(() => check(node), 900);
    }
    const refresh = nodeType.prototype.refreshComboInNode;
    nodeType.prototype.refreshComboInNode = function () { refresh?.apply(this, arguments); if (this.__ntn) check(this); };   // ComfyUI's R key
    const cfg = nodeType.prototype.onConfigure;
    nodeType.prototype.onConfigure = function () {
      cfg?.apply(this, arguments);
      const S = this.__ntn; if (!S) return;
      S.data = parse(S.w.value);
      setTimeout(() => check(this), 1200);                // after the whole workflow has loaded
    };
  },
});

// coming back to the window re-checks the disk (a file may have been added meanwhile)
window.addEventListener("focus", () => { for (const n of (app.graph?._nodes || [])) n.__ntnFocus?.(); });
