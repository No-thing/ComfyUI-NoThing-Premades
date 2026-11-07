import { app } from "../../scripts/app.js";
import { api } from "../../scripts/api.js";
import { hit } from "./nt_interact.js";
import { pickTheme } from "./nt_picker.js";

// No_Thing Roulette Bar: one wide, flat node for face, hair, body, makeup, outfit and underwear.
//   top row    : name, ON/OFF, Roll all (new seed), join, clear all
//   card row   : six equal cards (name, what was rolled, lock, dice). Click a card to open its buttons underneath.
//   open panel : the button rows of that part ("what may be rolled"); nothing picked = anything goes
// Everything lives in the node's one hidden text field (bar_data), like the other No_Thing nodes.

const CLS = "NoThingRouletteBar";
const UIF = "'Montserrat Alternates', Inter, 'Segoe UI', sans-serif";
const F = (w, px) => `${w} ${px}px ${UIF}`;
const COL = { panel: "#2B2B2B", well: "#1D1D1D", rule: "#444444", btn: "#383838", head: "#EAE5DC", label: "#A8A39A",
  orange: "#ff8a2a", onBg: "#3a2414", onText: "#fff1e4", offEdge: "#4a4a4a", offText: "#D8D8D8", glow: "rgba(255,138,42,0.55)" };
const STYLE_H = 40, SQ = 150, SIMPLE_H = 18 + SQ + 50, TAB_W = 118, TAB_H = 30;
const PAD = 10, HEAD_H = 46, CARD_H = 64, CGAP = 6, BTN_H = 18, GAP = 3, LABEL_W = 78, FOOT_H = 30, MIN_W = 900, PANEL_HEAD = 28;
const SEPS = [["newline", "New line"], ["space", "Space"], ["comma", "Comma"]];
const ALIAS = { "No bottoms": "No pants" };
const dl = (l) => ALIAS[l] || l;
const modeOf = (D) => (D.mode === "advanced" || D.mode === "simple" ? D.mode : D.fine === false ? "simple" : "advanced");   // Simple = big style + amount squares and the prompt; Advanced = the six parts

const mctx = document.createElement("canvas").getContext("2d");
const measure = (t, font) => { if (!mctx) return String(t).length * 6.5; mctx.font = font; return mctx.measureText(t).width; };

// brand fonts (ship in ./fonts, SIL Open Font License); every bar re-measures when they arrive
if (typeof FontFace !== "undefined") {
  [["Montserrat Alternates", "./fonts/MontserratAlternates-Light.ttf", "300 700"], ["Audiowide", "./fonts/Audiowide-Regular.ttf", "400"], ["Montserrat Alternates Bold", "./fonts/MontserratAlternates-Light.ttf", "700"]].forEach(([fam, rel, wt]) => {   // "Montserrat Alternates Bold": the bold weight under its own name, for workflow labels (they cannot pick a weight)
    try {
      const f = new FontFace(fam, `url(${new URL(rel, import.meta.url).href})`, { weight: wt });
      f.load().then(() => {
        document.fonts.add(f);
        for (const n of ((app.graph && (app.graph._nodes || app.graph.nodes)) || [])) if (n.__rk) { n.__rk.key = ""; fit(n); n.setDirtyCanvas(true, true); }
        if (app.graph) app.graph.setDirtyCanvas(true, true);                    // workflow labels that use these fonts repaint
      }).catch(() => {});
    } catch (e) { /* cosmetic */ }
  });
}

// ---------------------------------------------------------------- themes (web/themes.json, written by the node pack) and motion
let THEMES = [];
fetch(new URL("./themes.json", import.meta.url)).then((r) => r.json()).then((j) => {
  THEMES = Array.isArray(j) ? j : [];
  for (const n of ((app.graph && (app.graph._nodes || app.graph.nodes)) || [])) if (n.__rk) n.setDirtyCanvas(true, true);
}).catch(() => {});
const easeOutExpo = (t) => (t >= 1 ? 1 : 1 - Math.pow(2, -10 * Math.max(0, t)));
const jiggle = (t) => (t >= 1 ? 0 : Math.exp(-7 * t) * Math.sin(t * 30));        // a quick wobble that settles (like the cursor in the brand motion)
const now = () => (typeof performance !== "undefined" ? performance.now() : Date.now());
function bump(node, ms) {                                                          // keep redrawing for `ms` so animations can play
  const S = node.__rk; if (!S) return;
  S.animEnd = Math.max(S.animEnd || 0, now() + ms);
  if (S.raf) return;
  const step = () => { S.raf = 0; node.setDirtyCanvas(true, true); if (now() < S.animEnd) S.raf = requestAnimationFrame(step); };
  S.raf = requestAnimationFrame(step);
}
function wobble(ctx, cx, cy, t, amp, fn) {                                          // draw fn() rotated / squashed around (cx, cy) while t < 1
  if (t >= 1) { fn(); return; }
  ctx.save(); ctx.translate(cx, cy); ctx.rotate(jiggle(t) * amp); const k = 1 + 0.07 * Math.exp(-9 * t); ctx.scale(k, k); ctx.translate(-cx, -cy); fn(); ctx.restore();
}

// ---- style icons: web/icons/<style name>.png (square). Missing ones get a brand-orange placeholder tile.
const ICONS = {};
let ICON_SET = null;                                                   // web/icons/index.json lists the pictures that exist, so nothing 404s
const slug = (s) => String(s).toLowerCase().replace(/&/g, "").replace(/[^a-z0-9]+/g, "_").replace(/^_|_$/g, "");
const redrawAll = () => { for (const n of ((app.graph && (app.graph._nodes || app.graph.nodes)) || [])) if (n.__rk) n.setDirtyCanvas(true, true); };
fetch(new URL("./icons/index.json", import.meta.url)).then((r) => r.json()).then((j) => { ICON_SET = new Set(Array.isArray(j) ? j : []); redrawAll(); }).catch(() => { ICON_SET = new Set(); });

// ---- the Framing square's silhouette: web/frame_figure.png (your silhouette, transparent PNG) and its animated cut lines (fractions of its height)
const FRAME_CUTS = [[0, 1], [0, 0.915], [0, 0.38], [0.36, 0.915]];
let FIGURE = null;
{ const im = new Image(); im.onload = () => { FIGURE = im; redrawAll(); }; im.src = new URL("./frame_figure.png", import.meta.url).href; }
function frameNow(S) {                                   // [top, bottom] of the filled part, easing from the last step to the current one
  const to = FRAME_CUTS[Math.min(4, Math.max(1, parseInt(S.data && S.data.frame) || 1)) - 1], from = S.frFrom || to, e = easeOutExpo((now() - (S.frT || -1e9)) / 600);
  return [from[0] + (to[0] - from[0]) * e, from[1] + (to[1] - from[1]) * e];
}


// ---- the Shape square: a simple figure whose widths ease between five body shapes (very slim ... hourglass); web/icons/shape_1..5.png replace it when they exist
const SHAPES = [["Very slim", "very slim, narrow frame"], ["Slim", "slender with soft curves"], ["Balanced", "natural proportions"], ["Curvy", "full bust, defined waist, wide hips"], ["Hourglass", "exaggerated hourglass"]];
const SHAPE_W = [[.100, .075, .062, .078, .060], [.105, .090, .068, .092, .070], [.110, .105, .078, .110, .082], [.115, .130, .072, .135, .105], [.118, .155, .060, .160, .125]];   // half-widths (of the tile) at shoulders, bust, waist, hips, thigh
function shapeNow(S, n) {
  const to = SHAPE_W[Math.min(5, Math.max(1, n)) - 1], from = S.shFrom || to, e = easeOutExpo((now() - (S.shT || -1e9)) / 600);
  return to.map((v, i) => from[i] + (v - from[i]) * e);
}
function drawFigure(ctx, cx, top, h, w, color) {                       // w: half-widths [shoulder, bust, waist, hip, thigh] as fractions of the tile
  const U = h / 0.8;                                                  // the tile size the widths refer to
  const ys = [0.20, 0.30, 0.41, 0.52], xs = [w[0], w[1], w[2], w[3]];
  const side = (sg, list) => list.map(([x, y]) => [cx + sg * x * U, top + y * h]);
  const smooth = (pts) => { for (let i = 1; i < pts.length; i++) { const a = pts[i - 1], b = pts[i], my = (a[1] + b[1]) / 2; ctx.bezierCurveTo(a[0], my, b[0], my, b[0], b[1]); } };
  ctx.save(); ctx.fillStyle = color;
  ctx.beginPath(); ctx.arc(cx, top + 0.075 * h, 0.062 * h, 0, Math.PI * 2); ctx.fill();                              // head
  const torsoR = side(1, [[xs[0] * 0.55, 0.15], ...xs.map((x, i) => [x, ys[i]]), [xs[3] * 0.9, 0.60]]), torsoL = side(-1, [[xs[0] * 0.55, 0.15], ...xs.map((x, i) => [x, ys[i]]), [xs[3] * 0.9, 0.60]]);
  ctx.beginPath(); ctx.moveTo(torsoL[0][0], torsoL[0][1]); ctx.lineTo(torsoR[0][0], torsoR[0][1]); smooth(torsoR);
  ctx.lineTo(torsoL[torsoL.length - 1][0], torsoL[torsoL.length - 1][1]); smooth(torsoL.slice().reverse().reverse().length ? torsoL.slice().reverse() : torsoL);
  ctx.closePath(); ctx.fill();                                                                                       // torso: neck-to-hip
  for (const sg of [-1, 1]) {                                                                                       // legs, with a small gap between them
    const outer = side(sg, [[xs[3] * 0.92, 0.50], [w[4], 0.66], [w[4] * 0.62, 0.86], [w[4] * 0.40, 1.0]]), inner = side(sg, [[0.010, 0.62], [0.012, 0.72], [w[4] * 0.12, 0.90], [w[4] * 0.10, 1.0]]);
    ctx.beginPath(); ctx.moveTo(outer[0][0], outer[0][1]); smooth(outer); ctx.lineTo(inner[3][0], inner[3][1]); smooth(inner.slice().reverse());
    ctx.lineTo(cx + sg * 0.004 * U, top + 0.56 * h); ctx.closePath(); ctx.fill();
  }
  ctx.restore();
}

// shape keys: web/shape_morph.png is 31 pre-rendered frames of the body morphing from your skinny (t = 0) to your thick (t = 1) silhouette and on to thicker (t = 1.5); the steps sit at these t values
const SHAPE_T = [0, 0.3, 0.65, 1.0, 1.5], SHAPE_FRAMES = 31, SHAPE_DT = 0.05;
let MORPH = null;
{ const im = new Image(); im.onload = () => { MORPH = im; redrawAll(); }; im.src = new URL("./shape_morph.png", import.meta.url).href; }


// ---- tips shown in the Simple page's panel: [label, text]
const TIPS = [
  ["ROULETTE", "Roll all gives a new seed. The same seed always gives the same prompt, so a great roll can be made again."],
  ["ROULETTE", "Lock a card to keep its roll while everything else re-rolls. The dice on a card re-rolls only that part."],
  ["ROULETTE", "A style picks outfit, makeup and underwear together and gives them a matching main and accent colour."],
  ["ROULETTE", "Covered and Cute leave underwear out of the prompt completely and keep the body wording vague."],
  ["ROULETTE", "In frame: Top only leaves bottoms, shoes and legwear out, so the model does not pull the camera back."],
  ["ROULETTE", "Shape sets the general body from Very slim to Hourglass. Your own Bust, Waist and Hips picks still win."],
  ["ROULETTE", "Click a bar under HOW MUCH to jump to a level. Click the last level again to roll any amount."],
  ["ROULETTE", "Advanced shows every part and button. Simple is for rolling, Advanced is for steering."],
  ["ROULETTE", "Cosplay rolls one famous character per roll: hair, outfit and props arrive together, so nothing clashes."],
  ["ROULETTE", "When a mask or veil rolls, makeup and face details step aside: the mask is the focus."],
  ["ROULETTE", "At Micro the accessories shrink to necklaces, piercings, earrings, bracelets and maybe a bag. Skin first, props last."],
  ["ROULETTE", "Coats and jackets are written as properly worn, which avoids the half-draped cape look."],
  ["ROULETTE", "Join sets how the six parts are glued together: new line, space or comma."],
  ["EDIT PAGE", "Hover the Edit Page and press 1 2 3 4 to flip between Compare, Color, Face and Crop."],
  ["EDIT PAGE", "Double-click any slider to reset it. Alt-click lets you type an exact value."],
  ["EDIT PAGE", "Nothing is graded until Apply Grade runs, at the very end, so crop and outpaint never see the colour."],
  ["EDIT PAGE", "Clipping warnings: blue is crushed shadows, red is blown highlights. Blown whites cannot be brought back."],
  ["EDIT PAGE", "Face tab: every slider is a soft round region around a landmark, so nothing outside it moves."],
  ["EDIT PAGE", "On the Crop tab the grey canvas is exactly what the outpaint model will paint."],
  ["EDIT PAGE", "Zoom the ComfyUI canvas too far out and nodes go quiet on purpose. Zoom back in and they wake up."],
  ["HISTORY", "Every run adds its finished picture to History. Click a step and it becomes the picture every tab works on."],
  ["HISTORY", "Leaving Face or Crop with changes bakes them into a History step, so you can sculpt, crop, sculpt again and keep every step."],
  ["HISTORY", "Source stays pinned at the bottom of History and is never removed. History keeps the newest 12 steps and clears when ComfyUI closes."],
  ["SNAPSHOT", "Snapshot bakes your LUT, FX, Grain and Lens as a layer and clears the sliders, so the next effect stacks on top. Up to 12 layers."],
  ["SNAPSHOT", "Every Snapshot layer gets its own grain, light leak and dust pattern. Switch a layer off or delete it on the Start tab."],
  ["LOCK", "Color, Face and Crop all lock the roulette dice on the seed that made your picture. Only Compare lets them roll again."],
  ["LOCK", "Click the Roll locked chip to give the dice back. Keep your main sampler seed on fixed, or the picture can still change upstream."],
  ["COLOR", "FX goes from VHS tape, scanlines and halation to Spider-Verse, Anime Halftone, Manga Screentone and Pop Art Dots."],
  ["COLOR", "Halation is the warm glow film puts around bright edges. Try the Halation Film look in FX for the real stock feel."],
  ["COLOR", "Grain looks follow real film: Fine Portrait keeps skin clean, Classic Film 400 gives the full filmic texture."],
  ["COLOR", "Pick a look, then set its strength right under the picker. Looks are slider recipes, so you can keep tuning after."],
  ["OUTPAINT", "Pad the canvas in Crop: the grey is what the model paints, and AusBoss Stitch Inpaint pastes your original pixels back."],
  ["OUTPAINT", "Big pads can invent extra faces or hands near the edge. Extend in two smaller steps instead of one big one."],
  ["AUSBOSS", "Visit AusBoss on Civitai and YouTube (@ausbossdev): super great tools and workflows. Thank you! <3"],
  ["COMFYUI", "Start ComfyUI with --preview-method latent2rgb (or taesd, auto, none) to watch the KSampler preview while it samples."],
  ["COMFYUI", "latent2rgb is a fast colour estimate of the latent, so you see noise turning into a picture. Default is none (no preview)."],
  ["COMFYUI", "taesd previews are sharper but need the TAESD decoder files in models/vae_approx. auto uses taesd when found, else latent2rgb."],
  ["COMFYUI", "--preview-size sets the largest preview the sampler shows (default 512)."],
  ["SKIN PASS", "Qwen skin pass: more LoRA strength gives cleaner, smoother skin. Less strength keeps more detail but can look rough."],
  ["STUDIO", "Every strange roll you screenshotted became a fix. Hundreds of rolls here were looked at one by one."],
  ["STUDIO", "Not a coder, a director: each feature started as 'that looks wrong' or 'what if', and got tested until it held."],
  ["STUDIO", "Vibe coding gets a bad name when nobody checks. Rolling it, breaking it and asking why is the part that counts."],
  ["STUDIO", "Slop is what you get when nobody looks. This pack was looked at, roll after roll."],
  ["STUDIO", "The Skimpy ladder, themes, masks, shapes and cosplay were all built one 'wait, that is not right' at a time."],
];

function iconFor(key) {
  if (ICONS[key] !== undefined) return ICONS[key] || null;
  if (ICON_SET === null) return null;
  if (!ICON_SET.has(key)) { ICONS[key] = false; return null; }
  ICONS[key] = null;
  const im = new Image();
  im.onload = () => { ICONS[key] = im; redrawAll(); };
  im.onerror = () => { ICONS[key] = false; };
  im.src = new URL(`./icons/${key}.png`, import.meta.url).href;
  return null;
}

// ---- page animation. Leaving is quick (blocks shrink back toward their top-left corner one by one), arriving is slower:
// every block grows from nothing at its upper-left corner while sliding into place, one after another, easing out (expo).
const OUT_MS = 200, OUT_STEP = 28, IN_MS = 640, IN_STEP = 85, MAX_BLOCKS = 9;
function animP(S, order) {
  const A = S.anim; if (!A) return 1;
  const t = now() - A.t0;
  if (A.phase === "out") { const r = Math.min(1, Math.max(0, (t - order * OUT_STEP) / OUT_MS)); return 1 - r * r * r; }
  return easeOutExpo(Math.min(1, Math.max(0, (t - order * IN_STEP) / IN_MS)));
}
function withAnim(ctx, S, order, x, y, fn) {
  const p = animP(S, order);
  if (p >= 0.999) { fn(); return; }
  if (p <= 0.004) return;
  ctx.save();
  ctx.globalAlpha *= Math.min(1, p * 1.4);
  const sc = 0.3 + 0.7 * p;
  ctx.translate(x - (1 - p) * 26, y - (1 - p) * 16); ctx.scale(sc, sc); ctx.translate(-x, -y);
  fn(); ctx.restore();
}
function setMode(node, target) {
  const S = node.__rk;
  if (!S || modeOf(S.data) === target || (S.anim && S.anim.phase === "out")) return;
  S.anim = { phase: "out", t0: now(), target }; bump(node, 1700);
}

// ---------------------------------------------------------------- data
function parse(raw) {
  try {
    const d = JSON.parse(raw);
    if (d && Array.isArray(d.parts)) {
      d.sep = d.sep || "newline";
      d.parts.forEach((p) => {
        p.data = p.data && Array.isArray(p.data.groups) ? p.data : { groups: [] };
        p.data.groups.forEach((g) => { g.buttons = Array.isArray(g.buttons) ? g.buttons : []; g.buttons.forEach((b) => { b.label = String(b.label ?? ""); b.on = !!b.on; }); });
        const ec = p.data.groups.find((g) => g.name === "Eye colour");
        if (ec) ec.buttons = ec.buttons.filter((b) => b.label !== "Violet");                 // violet eyes were taken out of the dataset
        const uw = p.key === "underwear" && p.data.groups.find((g) => g.name === "Style" && g.buttons.some((b) => b.label === "Lace Classics"));
        if (uw && !uw.buttons.some((b) => b.label === "Luxury Couture")) {                // bars saved before this style existed get it
          const t = "high-end designer lingerie: sheer silk robes, couture lace, gold-hardware straps, thigh straps and patterned harnesses (stars, pentagrams, art deco)";
          uw.buttons.push({ label: "Luxury Couture", text: t, def: t, on: false });
        }
      });
      return d;
    }
  } catch (e) { /* fall through */ }
  return { v: 1, sep: "newline", enabled: true, open: null, parts: [] };
}
function sync(S) { if (S.w.value !== S.raw) { S.raw = S.w.value; S.data = parse(S.raw); S.key = ""; } }
function commit(node, relayout) {
  const S = node.__rk;
  S.raw = JSON.stringify(S.data); S.w.value = S.raw;
  if (S.w.callback) { try { S.w.callback(S.raw); } catch (e) { /* ignore */ } }
  S.key = "";
  if (relayout) fit(node);
  if (app.graph && app.graph.change) app.graph.change();
  node.setDirtyCanvas(true, true);
}
function fit(node) { node.setSize([node.size[0], node.computeSize()[1]]); }
function rollSeed(node) {
  const w = node.widgets && node.widgets.find((x) => x.name === "seed");
  if (!w) return;
  w.value = Math.floor(Math.random() * 4294967295);
  if (w.callback) { try { w.callback(w.value); } catch (e) { /* ignore */ } }
  if (app.graph && app.graph.change) app.graph.change();
  node.setDirtyCanvas(true, true);
}
const rolled = (node) => { try { return JSON.parse((node.properties && node.properties.nt_parts) || "{}"); } catch (e) { return {}; } };

function wrapLines(text, maxW, maxLines, font) {
  const words = String(text).replace(/\s+/g, " ").trim().split(" ").filter(Boolean), lines = [];
  let cur = "";
  for (let i = 0; i < words.length; i++) {
    const t = cur ? cur + " " + words[i] : words[i];
    if (measure(t, font) <= maxW || !cur) cur = t; else { lines.push(cur); cur = words[i]; }
    if (lines.length === maxLines) break;
  }
  if (lines.length < maxLines && cur) lines.push(cur);
  else if (lines.length === maxLines) lines[maxLines - 1] = lines[maxLines - 1].replace(/[ ,.]*$/, "") + "…";
  return lines;
}

// ---------------------------------------------------------------- layout
function layoutFor(node, width) {
  const S = node.__rk; sync(S);
  const key = S.raw + "|" + width + "|" + ((node.properties && node.properties.nt_parts) || "");
  if (S.key === key && S.lay) return S.lay;
  const n = Math.max(1, S.data.parts.length);
  const cw = (width - 2 * PAD - (n - 1) * CGAP) / n;
  const fine = modeOf(S.data) === "advanced", TOP = HEAD_H + STYLE_H;
  const cards = fine ? S.data.parts.map((p, i) => ({ i, x: PAD + i * (cw + CGAP), y: TOP, w: cw, h: CARD_H })) : [];
  let y = fine ? TOP + CARD_H + 8 : HEAD_H + SIMPLE_H;
  const items = [];
  const open = S.data.open, part = fine && Number.isInteger(open) ? S.data.parts[open] : null;
  let panelTop = null;
  if (part) {
    panelTop = y; y += PANEL_HEAD;
    const x0 = PAD + LABEL_W, x1 = width - PAD;
    part.data.groups.forEach((g, gi) => {
      let x = x0, ry = y;
      items.push({ k: "glabel", gi, x: PAD, y: ry, w: LABEL_W - 8, h: BTN_H });
      g.buttons.forEach((b, bi) => {
        let w = Math.max(32, Math.ceil(measure(dl(b.label) || "…", F(500, 11))) + 14);
        w = Math.min(w, x1 - x0);
        if (x + w > x1 && x > x0) { x = x0; ry += BTN_H + GAP; }
        items.push({ k: "btn", gi, bi, x, y: ry, w, h: BTN_H }); x += w + GAP;
      });
      y = ry + BTN_H + 6;
    });
    y += 2;
  }
  S.lay = { cards, items, panelTop, part, fine, height: y + FOOT_H };
  S.key = key;
  return S.lay;
}

// ---------------------------------------------------------------- drawing
function rr(ctx, x, y, w, h, r) {
  ctx.beginPath(); ctx.moveTo(x + r, y);
  ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r);
  ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath();
}
function fitText(ctx, text, maxW) {
  let t = String(text);
  if (ctx.measureText(t).width <= maxW) return t;
  while (t.length > 2 && ctx.measureText(t + "…").width > maxW) t = t.slice(0, -1);
  return t + "…";
}
function pill(ctx, x, y, w, h, label, on, accent) {
  ctx.save();
  rr(ctx, x, y, w, h, 6);
  if (accent) { ctx.fillStyle = COL.orange; ctx.shadowColor = COL.glow; ctx.shadowBlur = 12; }
  else ctx.fillStyle = on ? COL.onBg : COL.btn;
  ctx.fill(); ctx.shadowBlur = 0;
  if (!accent) { ctx.lineWidth = on ? 1.5 : 1; ctx.strokeStyle = on ? COL.orange : COL.offEdge; ctx.stroke(); }
  ctx.font = F(700, 11.5); ctx.textAlign = "center"; ctx.textBaseline = "middle";
  ctx.fillStyle = accent ? "#1E1E1E" : on ? COL.onText : COL.offText;
  ctx.fillText(label, x + w / 2, y + h / 2 + 0.5);
  ctx.restore();
}
function lockGlyph(ctx, cx, cy, on) {
  ctx.save(); ctx.strokeStyle = on ? "#1E1E1E" : "#9a9a9a"; ctx.fillStyle = ctx.strokeStyle; ctx.lineWidth = 1.5; ctx.lineCap = "round";
  ctx.beginPath(); ctx.arc(cx, cy - 1.5, 3, Math.PI, 0); ctx.stroke();
  ctx.fillRect(cx - 4.5, cy - 1.5, 9, 6.5); ctx.restore();
}
function diceGlyph(ctx, cx, cy) {
  ctx.save(); ctx.strokeStyle = COL.orange; ctx.fillStyle = COL.orange; ctx.lineWidth = 1.5;
  rr(ctx, cx - 6, cy - 6, 12, 12, 3); ctx.stroke();
  [[-2.5, -2.5], [2.5, 2.5], [0, 0], [-2.5, 2.5], [2.5, -2.5]].forEach(([dx, dy]) => { ctx.beginPath(); ctx.arc(cx + dx, cy + dy, 0.9, 0, Math.PI * 2); ctx.fill(); });
  ctx.restore();
}
function setHover(node, h) {
  const S = node.__rk;
  const same = S.hover && h && S.hover.tip === h.tip && S.hover.pi === h.pi && S.hover.gi === h.gi && S.hover.bi === h.bi;
  if (!same) { S.hover = h; node.setDirtyCanvas(true, true); }
}

function drawBar(ctx, node, y0) {
  const S = node.__rk, width = node.size[0];
  sync(S);
  const A = S.anim;
  if (A && A.phase === "out" && now() - A.t0 > OUT_MS + (MAX_BLOCKS - 1) * OUT_STEP) {          // the old page has left: switch, then the new page arrives
    S.data.mode = A.target; S.data.fine = A.target === "advanced"; S.anim = { phase: "in", t0: now() };
    commit(node, true); bump(node, 1700);
  } else if (A && A.phase === "in" && now() - A.t0 > IN_MS + MAX_BLOCKS * IN_STEP + 40) S.anim = null;
  const lay = layoutFor(node, width);
  const reg = node.__lcHits;
  if (reg) for (const k of Array.from(reg.keys())) if (k.startsWith("rk:")) reg.delete(k);
  hit(node, "rk:bg", 0, y0, width, lay.height, () => {});
  const need = node.computeSize()[1];
  if (Math.abs(node.size[1] - need) > 1) node.size[1] = need;
  ctx.save();
  ctx.beginPath(); ctx.rect(0, y0, width, lay.height); ctx.clip();
  const D = S.data, on = D.enabled !== false, roll = rolled(node);
  const tip = (t) => () => { setHover(node, { tip: t }); return "pointer"; };

  // ---- top row: name, ON/OFF, Simple | Advanced tabs, and Clear all + Roll all in the upper right
  ctx.textBaseline = "middle"; ctx.textAlign = "left";
  const mid = y0 + (HEAD_H - 4) / 2, mode = lay.fine ? "advanced" : "simple";
  ctx.font = "400 17px Audiowide, 'Roboto Slab', Georgia, serif"; ctx.fillStyle = COL.orange;
  ctx.fillText("No_Thing", PAD, mid);
  let x = PAD + measure("No_Thing", "400 17px Audiowide, 'Roboto Slab', Georgia, serif") + 8;
  ctx.font = F(600, 12.5); ctx.fillStyle = COL.head; ctx.fillText("Roulette", x, mid + 0.5);
  x += measure("Roulette", F(600, 12.5)) + 14;
  pill(ctx, x, mid - 10, 40, 20, on ? "ON" : "OFF", on);
  hit(node, "rk:enable", x, mid - 10, 40, 20, () => { D.enabled = !on; commit(node, false); }, "pointer", tip("Switch the whole bar on / off. Off = only the prefix / suffix text passes through."));
  x += 58;
  const shownMode = S.anim && S.anim.phase === "out" ? S.anim.target : mode;                 // the tab lights up at once, the page follows with its animation
  [["simple", "Simple"], ["advanced", "Advanced"]].forEach(([id, label]) => {
    const act = shownMode === id, ty = mid - TAB_H / 2;
    ctx.save(); rr(ctx, x, ty, TAB_W, TAB_H, 9);
    if (act) { ctx.fillStyle = COL.orange; ctx.shadowColor = COL.glow; ctx.shadowBlur = 12; } else ctx.fillStyle = COL.btn;
    ctx.fill(); ctx.shadowBlur = 0;
    ctx.font = F(700, 14); ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillStyle = act ? "#1E1E1E" : COL.offText;
    ctx.fillText(label, x + TAB_W / 2, ty + TAB_H / 2 + 0.5); ctx.restore();
    hit(node, "rk:tab:" + id, x, ty, TAB_W, TAB_H, () => setMode(node, id), "pointer", tip(id === "simple" ? "Simple: pick a style and how much, read the prompt." : "Advanced: the six parts, locks, dice and every button."));
    x += TAB_W + 6;
  });
  {
    const rx = width - PAD - 96, ry = mid - 14;
    wobble(ctx, rx + 48, mid, (now() - (S.rollT || -1e9)) / 650, 0.1, () => pill(ctx, rx, ry, 96, 28, "Roll all", true, true));
    hit(node, "rk:rollall", rx, ry, 96, 28, () => { S.rollT = now(); bump(node, 700); rollSeed(node); }, "pointer", tip("Roll all: a new seed, so every unlocked part gets a new variation. Same seed = same prompt."));
    const cx = rx - 6 - 74;
    pill(ctx, cx, ry + 2, 74, 24, "Clear all", false);
    hit(node, "rk:tool:clear", cx, ry + 2, 74, 24, () => { D.parts.forEach((p) => p.data.groups.forEach((g) => g.buttons.forEach((b) => { b.on = false; }))); D.theme = ""; commit(node, false); }, "pointer", tip("Clear all: switch every button off in every part and drop the style (everything is rolled)."));
  }
  ctx.strokeStyle = COL.rule; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(PAD, y0 + HEAD_H - 3.5); ctx.lineTo(width - PAD, y0 + HEAD_H - 3.5); ctx.stroke();

  const th = THEMES.find((t) => t.name === D.theme);
  const setTheme = (name) => { D.theme = name; S.themeT = now(); bump(node, 700); commit(node, false); };
  const stepTheme = (dir) => { const i = THEMES.findIndex((t) => t.name === D.theme); setTheme(dir < 0 ? (i <= 0 ? (i === 0 ? "" : THEMES.length ? THEMES[THEMES.length - 1].name : "") : THEMES[i - 1].name) : (i + 1 >= THEMES.length ? "" : THEMES[i + 1].name)); };

  // ---- ADVANCED: style row (one choice that steers outfit, makeup and underwear and gives them matching colours) + Join
  if (lay.fine) withAnim(ctx, S, 0, PAD, y0 + HEAD_H, () => {
    const sy = y0 + HEAD_H, joinW = 118, wx = PAD + 50, ww = width - PAD - joinW - 8 - wx;
    ctx.font = F(700, 10); ctx.fillStyle = COL.orange; ctx.textAlign = "left"; ctx.textBaseline = "middle";
    ctx.fillText("STYLE", PAD + 2, sy + 20);
    rr(ctx, wx, sy + 6, ww, 28, 7); ctx.fillStyle = COL.well; ctx.fill(); ctx.strokeStyle = th ? COL.orange : COL.rule; ctx.lineWidth = th ? 1.4 : 1; ctx.stroke();
    ctx.fillStyle = "#8a8a8a"; ctx.font = F(600, 14); ctx.textAlign = "center"; ctx.fillText("‹", wx + 13, sy + 19.5); ctx.fillText("›", wx + ww - 13, sy + 19.5);
    const te = easeOutExpo((now() - (S.themeT || -1e9)) / 520);
    ctx.save(); ctx.beginPath(); ctx.rect(wx + 24, sy + 6, ww - 48, 28); ctx.clip(); ctx.globalAlpha *= on ? 0.4 + 0.6 * te : 0.45; ctx.textAlign = "left";
    const label = th ? th.name : "Any style: everything random", off = (1 - te) * 18;
    ctx.font = F(700, 13.5); ctx.fillStyle = th ? COL.head : COL.label; ctx.fillText(label, wx + 28 + off, sy + 20);
    if (th) { const lw = measure(label, F(700, 13.5)); ctx.font = F(500, 11); ctx.fillStyle = COL.label; ctx.fillText(fitText(ctx, th.desc, Math.max(0, ww - 60 - lw)), wx + 28 + lw + 12 + off, sy + 20.5); }
    ctx.restore();
    hit(node, "rk:theme", wx, sy + 6, ww, 28, ({ ev, pos }) => {
      if (pos && pos[0] < wx + 26) stepTheme(-1);
      else if (pos && pos[0] > wx + ww - 26) stepTheme(1);
      else pickTheme({ event: ev, items: THEMES, current: D.theme || "", noneLabel: "Any style", onPick: setTheme });
    }, "pointer", tip("Style: one choice that steers outfit, makeup and underwear together and gives them matching colours (a main colour plus a contrasting accent). Pick Any style to roll everything freely."));
    const jx = width - PAD - joinW, sepName = (SEPS.find((q) => q[0] === D.sep) || SEPS[0])[1];
    pill(ctx, jx, sy + 8, joinW, 24, "Join: " + sepName, false);
    hit(node, "rk:tool:sep", jx, sy + 8, joinW, 24, () => { const i = SEPS.findIndex((q) => q[0] === D.sep); D.sep = SEPS[(i + 1) % SEPS.length][0]; commit(node, false); }, "pointer", tip("How the six parts are joined in the prompt: new line, space or comma."));
  });

  // ---- SIMPLE: a style square, an amount square and the prompt beside them
  if (!lay.fine) {
    const by = y0 + HEAD_H + 2, sqy = by + 18, gap = 18, x2 = PAD + SQ + gap, xf = PAD + 2 * (SQ + gap), xs = PAD + 3 * (SQ + gap), x3 = PAD + 4 * (SQ + gap), w3 = width - PAD - x3;
    const cap = (t, cx) => { ctx.font = F(700, 10); ctx.fillStyle = COL.orange; ctx.textAlign = "left"; ctx.textBaseline = "middle"; ctx.fillText(t, cx + 2, by + 8); };
    const tile = (tx, fillA, fillB, radius) => {
      ctx.save(); ctx.shadowColor = "rgba(0,0,0,0.55)"; ctx.shadowBlur = 16; ctx.shadowOffsetY = 7;
      rr(ctx, tx, sqy, SQ, SQ, radius); const g = ctx.createLinearGradient(tx, sqy, tx + SQ, sqy + SQ); g.addColorStop(0, fillA); g.addColorStop(1, fillB); ctx.fillStyle = g; ctx.fill(); ctx.restore();
    };
    const under = (tx, name, sub, accent) => {
      ctx.font = F(700, 14.5); ctx.fillStyle = COL.head; ctx.textAlign = "left"; ctx.textBaseline = "middle";
      const nm = fitText(ctx, name, SQ - 44); ctx.fillText(nm, tx + 4, sqy + SQ + 15);
      ctx.font = F(700, 12); ctx.fillStyle = COL.orange; ctx.textAlign = "right"; ctx.fillText(accent, tx + SQ - 4, sqy + SQ + 15);
      ctx.font = F(500, 10.5); ctx.fillStyle = COL.label; ctx.textAlign = "left"; ctx.fillText(fitText(ctx, sub, SQ - 6), tx + 4, sqy + SQ + 32);
    };
    // style square
    withAnim(ctx, S, 0, PAD, by, () => {
      cap("STYLE", PAD);
      tile(PAD, "#ff9a3e", "#ff7f1f", 22);
      ctx.save(); rr(ctx, PAD, sqy, SQ, SQ, 22); ctx.clip();
      const ic = th ? iconFor(slug(th.name)) : null, te = easeOutExpo((now() - (S.themeT || -1e9)) / 520);
      ctx.globalAlpha *= on ? 1 : 0.45;
      if (ic) { const k = 1 + 0.06 * (1 - te); ctx.drawImage(ic, PAD - SQ * (k - 1) / 2, sqy - SQ * (k - 1) / 2, SQ * k, SQ * k); }
      else {                                                                                  // placeholder until the style's picture exists
        ctx.fillStyle = "rgba(18,17,20,0.16)"; ctx.beginPath(); ctx.arc(PAD + SQ / 2, sqy + SQ + 30, SQ * 0.7, 0, Math.PI * 2); ctx.fill();
        if (th) { const ini = th.name.split(/\s+/).map((w) => w[0]).join("").slice(0, 3).toUpperCase(); ctx.font = "400 54px Audiowide, Georgia, serif"; ctx.fillStyle = "#121114"; ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillText(ini, PAD + SQ / 2, sqy + SQ / 2 - 4); }
        else diceGlyph(ctx, PAD + SQ / 2, sqy + SQ / 2 - 4);
        if (!th) { ctx.font = F(700, 11); ctx.fillStyle = "#121114"; ctx.textAlign = "center"; ctx.fillText("ANY STYLE", PAD + SQ / 2, sqy + SQ / 2 + 28); }
      }
      ctx.restore();
      ctx.font = F(600, 18); ctx.textBaseline = "middle"; ctx.textAlign = "center";                                     // step arrows on the sides
      [["‹", PAD + 15], ["›", PAD + SQ - 15]].forEach(([g, ax]) => { ctx.fillStyle = "rgba(18,17,20,0.32)"; ctx.beginPath(); ctx.arc(ax, sqy + SQ / 2, 10, 0, Math.PI * 2); ctx.fill(); ctx.fillStyle = "rgba(234,229,220,0.8)"; ctx.fillText(g, ax, sqy + SQ / 2 - 1); });
      under(PAD, th ? th.name : "Any style", th ? th.desc : "everything is rolled freely", "▾");
      hit(node, "rk:sq:style", PAD, sqy, SQ, SQ + 36, ({ ev, pos }) => {
        if (pos && pos[0] < PAD + 30 && pos[1] < sqy + SQ) stepTheme(-1);
        else if (pos && pos[0] > PAD + SQ - 30 && pos[1] < sqy + SQ) stepTheme(1);
        else pickTheme({ event: ev, items: THEMES, current: D.theme || "", noneLabel: "Any style", onPick: setTheme });
      }, "pointer", tip("Style: click to search and pick; the arrows step through. It steers outfit, makeup and underwear together and gives them matching colours."));
    });
    // amount square (Covered ... Micro: the outfit's Skimpy row, one level at a time)
    withAnim(ctx, S, 1, x2, by, () => {
      cap("HOW MUCH", x2);
      const og = D.parts.find((q) => q.key === "outfit"), lg = og && og.data.groups.find((g) => /skimp/i.test(g.name));
      const names = lg ? lg.buttons.map((b) => b.label) : ["Covered", "Cute", "Revealing", "Skimpy", "Micro"], cur = lg ? lg.buttons.findIndex((b) => b.on) : -1;
      const setLevel = (i) => { if (!lg) return; const was = lg.buttons[i] && lg.buttons[i].on; lg.buttons.forEach((b) => { b.on = false; }); if (!was && lg.buttons[i]) lg.buttons[i].on = true; S.lvlT = now(); bump(node, 600); commit(node, false); };
      tile(x2, "#2b2b2e", "#1d1d1f", 22);
      ctx.save(); rr(ctx, x2, sqy, SQ, SQ, 22); ctx.strokeStyle = "rgba(255,255,255,0.07)"; ctx.lineWidth = 1.5; ctx.stroke(); ctx.clip();
      ctx.globalAlpha *= on ? 1 : 0.45;
      const lk = cur >= 0 ? iconFor("level_" + (cur + 1)) : null, le = easeOutExpo((now() - (S.lvlT || -1e9)) / 450);
      if (lk) ctx.drawImage(lk, x2, sqy, SQ, SQ);
      else {                                                                                  // placeholder: five bars that fill up to the level
        const n = names.length, bw = 16, bg = 8, bx0 = x2 + (SQ - (n * bw + (n - 1) * bg)) / 2, base = sqy + SQ - 44;
        for (let i = 0; i < n; i++) {
          const h = 18 + i * 14, filled = cur >= 0 && i <= cur, hh = filled ? h * (0.55 + 0.45 * le) : h;
          rr(ctx, bx0 + i * (bw + bg), base - hh, bw, hh, 5); ctx.fillStyle = filled ? COL.orange : "#3a3a3e"; ctx.fill();
        }
        if (cur < 0) { ctx.font = F(700, 11); ctx.fillStyle = COL.label; ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillText("ANY AMOUNT", x2 + SQ / 2, sqy + 24); }
      }
      ctx.restore();
      under(x2, cur >= 0 ? names[cur] : "Any amount", cur >= 0 ? "click to step, click a bar to jump" : "nothing picked: any amount is rolled", cur >= 0 ? (cur + 1) + " / " + names.length : "");
      hit(node, "rk:sq:lvl", x2, sqy, SQ, SQ + 36, () => setLevel(cur + 1 >= names.length ? (cur < 0 ? 0 : cur) : cur + 1), "pointer", tip("How much: Covered to Micro. Click to step up (click the last level again to clear it, so any amount is rolled)."));
      const n = names.length, sw = (SQ - 20 - (n - 1) * 4) / n;
      for (let i = 0; i < n; i++) {
        const sx = x2 + 10 + i * (sw + 4), act = cur >= 0 && i <= cur;
        rr(ctx, sx, sqy + SQ - 22, sw, 7, 3.5); ctx.fillStyle = act ? COL.head : "#3a3a3e"; ctx.fill();
        hit(node, "rk:sq:lvl" + i, sx - 1, sqy + SQ - 28, sw + 2, 20, () => setLevel(i), "pointer", tip(names[i] + ": " + (lg && lg.buttons[i] ? (lg.buttons[i].text || "").replace(/\s+/g, " ").trim() : "")));
      }
    });
    // framing square: what is in the picture. A silhouette fills the part that is in frame (full body / no feet / top only / bottoms only)
    withAnim(ctx, S, 2, xf, by, () => {
      cap("IN FRAME", xf);
      const FR = [["Full body", "top, bottoms and shoes", 0, 215], ["No feet", "no shoes or socks", 0, 186], ["Top only", "no bottoms or legwear", 0, 92], ["Bottoms only", "no top, face or shoes", 92, 186]];
      const cf = Math.min(4, Math.max(1, parseInt(D.frame) || 1)) - 1;
      const setFrame = (i) => { S.frFrom = frameNow(S); S.frT = now(); D.frame = i + 1; bump(node, 700); commit(node, false); };
      tile(xf, "#ff9a3e", "#ff7f1f", 22);
      ctx.save(); rr(ctx, xf, sqy, SQ, SQ, 22); ctx.clip();
      ctx.globalAlpha *= on ? 1 : 0.45;
      const cur = frameNow(S);
      if (FIGURE) {
        const fh = SQ * 0.78, fw = fh * FIGURE.width / FIGURE.height, fx = xf + (SQ - fw) / 2, fy = sqy + 9;
        ctx.save(); ctx.globalAlpha *= 0.17; ctx.drawImage(FIGURE, fx, fy, fw, fh); ctx.restore();                // the whole figure, faint
        ctx.save(); ctx.beginPath(); ctx.rect(fx - 4, fy + cur[0] * fh, fw + 8, (cur[1] - cur[0]) * fh); ctx.clip(); ctx.drawImage(FIGURE, fx, fy, fw, fh); ctx.restore();   // the part in frame, solid
        ctx.strokeStyle = "rgba(234,229,220,0.85)"; ctx.lineWidth = 1.2; ctx.setLineDash([4, 4]);
        [cur[0], cur[1]].forEach((f) => { if (f > 0.01 && f < 0.99) { const yy = fy + f * fh; ctx.beginPath(); ctx.moveTo(xf + 10, yy); ctx.lineTo(xf + SQ - 10, yy); ctx.stroke(); } });
        ctx.setLineDash([]);
      }
      ctx.restore();
      under(xf, FR[cf][0], FR[cf][1], (cf + 1) + " / 4");
      hit(node, "rk:sq:frame", xf, sqy, SQ, SQ + 36, () => setFrame((cf + 1) % 4), "pointer", tip("In frame: click to step Full body, No feet, Top only, Bottoms only. Whatever is out of the picture is left out of the prompt (shoes, bottoms, top and face), so the model does not pull the camera back."));
      const sw = (SQ - 20 - 3 * 4) / 4;
      for (let i = 0; i < 4; i++) {
        const sx = xf + 10 + i * (sw + 4);
        rr(ctx, sx, sqy + SQ - 22, sw, 7, 3.5); ctx.fillStyle = i === cf ? "#3a1c08" : "rgba(58,28,8,0.28)"; ctx.fill();
        hit(node, "rk:sq:frame" + i, sx - 1, sqy + SQ - 28, sw + 2, 20, () => setFrame(i), "pointer", tip(FR[i][0] + ": " + FR[i][1]));
      }
    });
    // shape square: general body shape from very slim to hourglass (the figure's widths ease between the steps; 0 = not chosen, any shape is rolled)
    withAnim(ctx, S, 3, xs, by, () => {
      cap("SHAPE", xs);
      const cs = Math.min(5, Math.max(0, parseInt(D.shape) || 0));
      const setShape = (i) => { { const se0 = easeOutExpo((now() - (S.shT || -1e9)) / 650), tt = SHAPE_T[(cs || 3) - 1], tf = S.shFromT !== undefined ? S.shFromT : tt; S.shFromT = tf + (tt - tf) * se0; } S.shFrom = shapeNow(S, cs || 3); S.shT = now(); D.shape = i; bump(node, 700); commit(node, false); };
      tile(xs, "#ff9a3e", "#ff7f1f", 22);
      ctx.save(); rr(ctx, xs, sqy, SQ, SQ, 22); ctx.clip();
      ctx.globalAlpha *= on ? 1 : 0.45;
      if (MORPH) {                                                                                // shape keys: the body morphs from the previous step to this one with expo easing
        const tTo = SHAPE_T[(cs || 3) - 1], tFrom = S.shFromT !== undefined ? S.shFromT : tTo, se = easeOutExpo((now() - (S.shT || -1e9)) / 650);
        const t = tFrom + (tTo - tFrom) * se, fi = Math.min(SHAPE_FRAMES - 1, Math.max(0, Math.round(t / SHAPE_DT))), fw = MORPH.width / SHAPE_FRAMES;
        ctx.save(); ctx.globalAlpha *= cs ? 1 : 0.3; ctx.drawImage(MORPH, fi * fw, 0, fw, MORPH.height, xs, sqy, SQ, SQ); ctx.restore();
        if (!cs) { ctx.font = F(700, 11); ctx.fillStyle = "#3a1c08"; ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillText("ANY SHAPE", xs + SQ / 2, sqy + SQ - 36); }
      } else {
        const w = shapeNow(S, cs || 3), fh = SQ * 0.8;
        drawFigure(ctx, xs + SQ / 2, sqy + 8, fh, w.map((v) => v * 1.0), cs ? "#3a1c08" : "rgba(58,28,8,0.28)");
        if (!cs) { ctx.font = F(700, 11); ctx.fillStyle = "#3a1c08"; ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillText("ANY SHAPE", xs + SQ / 2, sqy + SQ - 36); }
      }
      ctx.restore();
      under(xs, cs ? SHAPES[cs - 1][0] : "Any shape", cs ? SHAPES[cs - 1][1] : "any body shape is rolled", cs ? cs + " / 5" : "");
      hit(node, "rk:sq:shape", xs, sqy, SQ, SQ + 36, () => setShape(cs >= 5 ? 0 : cs + 1), "pointer", tip("Shape: click to step from Very slim to Hourglass (click again after Hourglass to clear it, so any shape is rolled). It sets the general body shape; your own Bust, Waist and Hips picks still win."));
      const sw = (SQ - 20 - 4 * 4) / 5;
      for (let i = 0; i < 5; i++) {
        const sx = xs + 10 + i * (sw + 4);
        rr(ctx, sx, sqy + SQ - 22, sw, 7, 3.5); ctx.fillStyle = (cs && i + 1 <= cs) ? "#3a1c08" : "rgba(58,28,8,0.28)"; ctx.fill();
        hit(node, "rk:sq:shape" + i, sx - 1, sqy + SQ - 28, sw + 2, 20, () => setShape(i + 1), "pointer", tip(SHAPES[i][0] + ": " + SHAPES[i][1]));
      }
    });
    // tips panel (the finished prompt lives next to the Saver in your workflow): a new tip for every seed, cheap to draw (text is wrapped once per tip and width)
    withAnim(ctx, S, 4, x3, by, () => {
      cap("DID YOU KNOW", x3);
      const bh = SQ + 36, sw = node.widgets && node.widgets.find((x) => x.name === "seed"), sv = sw ? Number(sw.value) || 0 : 0;
      if (S.tipSeed !== sv) { S.tipSeed = sv; S.tipT = now(); S.tipIdx = Math.abs(Math.imul(sv ^ (sv >>> 15), 2246822519) >>> 0) % TIPS.length; }
      const tp = TIPS[S.tipIdx || 0], re = easeOutExpo((now() - (S.tipT || -1e9)) / 600), tf = F(500, 12.5), key = S.tipIdx + ":" + Math.round(w3);
      if (S.tipKey !== key) { S.tipKey = key; S.tipLines = wrapLines(tp[1], w3 - 32, Math.max(3, Math.floor((bh - 74) / 17.5)), tf); }
      ctx.save(); rr(ctx, x3, sqy, w3, bh, 18); ctx.fillStyle = "#171719"; ctx.fill(); ctx.strokeStyle = COL.rule; ctx.lineWidth = 1; ctx.stroke(); ctx.clip();
      ctx.globalAlpha *= (on ? 1 : 0.45) * (0.3 + 0.7 * re);
      ctx.font = F(700, 10); ctx.fillStyle = COL.orange; ctx.textAlign = "left"; ctx.textBaseline = "middle"; ctx.fillText(tp[0], x3 + 16, sqy + 20 + (1 - re) * 6);
      ctx.font = tf; ctx.fillStyle = "#e6e1d8"; ctx.textBaseline = "top";
      (S.tipLines || []).forEach((ln, k) => ctx.fillText(ln, x3 + 16, sqy + 38 + k * 17.5 + (1 - re) * 6));
      ctx.font = F(500, 10); ctx.fillStyle = COL.label; ctx.textBaseline = "middle"; ctx.textAlign = "right"; ctx.fillText(((S.tipIdx || 0) + 1) + " / " + TIPS.length, x3 + w3 - 14, sqy + bh - 16);
      ctx.restore();
      hit(node, "rk:sq:tips", x3, sqy, w3, bh, () => { S.tipIdx = ((S.tipIdx || 0) + 1) % TIPS.length; S.tipT = now(); S.tipKey = ""; bump(node, 700); }, "pointer", tip("A new tip appears with every seed. Click to see the next one."));
    });
  }

  // ---- the six cards
  if (!on) ctx.globalAlpha = 0.45;
  lay.cards.forEach((c) => {
    const p = D.parts[c.i], isOpen = D.open === c.i, pOn = p.enabled !== false, cy = y0 + c.y;
    const lx = c.x + c.w - 52, dx = c.x + c.w - 24;
    withAnim(ctx, S, 1 + c.i, c.x, cy, () => {
    ctx.save();
    rr(ctx, c.x, cy, c.w, c.h, 8); ctx.fillStyle = COL.well; ctx.fill();
    ctx.lineWidth = isOpen ? 1.6 : 1; ctx.strokeStyle = isOpen ? COL.orange : COL.rule;
    if (isOpen) { ctx.shadowColor = COL.glow; ctx.shadowBlur = 8; }
    ctx.stroke(); ctx.restore();
    // on/off dot + name
    ctx.beginPath(); ctx.arc(c.x + 13, cy + 14, 4.5, 0, Math.PI * 2); ctx.fillStyle = pOn ? COL.orange : "#555"; ctx.fill();
    ctx.font = F(700, 13.5); ctx.fillStyle = pOn ? COL.head : COL.label; ctx.textAlign = "left"; ctx.textBaseline = "middle";
    ctx.fillText(fitText(ctx, p.name, c.w - 78), c.x + 24, cy + 14.5);
    // lock + dice
    rr(ctx, lx, cy + 5, 22, 18, 5); ctx.fillStyle = p.locked ? COL.orange : COL.btn; ctx.fill(); lockGlyph(ctx, lx + 11, cy + 14, p.locked);
    wobble(ctx, dx + 11, cy + 14, (now() - ((S.diceT && S.diceT[c.i]) || -1e9)) / 650, 0.35, () => { rr(ctx, dx, cy + 5, 22, 18, 5); ctx.fillStyle = COL.btn; ctx.fill(); diceGlyph(ctx, dx + 11, cy + 14); });
    // what was rolled
    const txt = !pOn ? "off: adds nothing" : roll[p.key] ? roll[p.key].replace(/^(wearing|with|in)\s+/i, "") : "rolls anything";
    ctx.font = F(500, 10.5); ctx.fillStyle = pOn && roll[p.key] ? "#d9d4cb" : COL.label;
    const rv = easeOutExpo((now() - (S.revealT || -1e9) - c.i * 70) / 600);                  // new roll: each card's text eases in, one after another
    ctx.save(); ctx.globalAlpha = (on ? 1 : 0.45) * (0.25 + 0.75 * rv);
    wrapLines(txt, c.w - 16, 2, F(500, 10.5)).forEach((ln, k) => ctx.fillText(ln, c.x + 8, cy + 36 + k * 13 + (1 - rv) * 7));
    ctx.restore();
    });
    hit(node, `rk:card${c.i}`, c.x, cy, c.w, c.h, () => { D.open = isOpen ? null : c.i; commit(node, true); }, "pointer", tip(`${p.name}: click to ${isOpen ? "close" : "open"} the buttons that decide what may be rolled.`));
    hit(node, `rk:dot${c.i}`, c.x + 4, cy + 4, 22, 20, () => { p.enabled = !pOn; commit(node, false); }, "pointer", tip(`${p.name} ${pOn ? "ON: click to switch it off (adds nothing)." : "OFF: click to switch it on."}`));
    hit(node, `rk:lock${c.i}`, lx, cy + 5, 22, 18, () => { p.locked = !p.locked; if (p.locked && !p.salt) p.salt = 1 + Math.floor(Math.random() * 1e9); commit(node, false); }, "pointer", tip(p.locked ? `${p.name} is LOCKED: it keeps its roll when the seed changes. Click to unlock.` : `Lock ${p.name}: keep this roll when the seed changes.`));
    hit(node, `rk:dice${c.i}`, dx, cy + 5, 22, 18, () => { p.salt = 1 + Math.floor(Math.random() * 1e9); (S.diceT = S.diceT || {})[c.i] = now(); bump(node, 700); commit(node, false); }, "pointer", tip(`Re-roll only ${p.name}: a new variation of this part, the others stay.`));
  });
  ctx.globalAlpha = 1;

  // ---- open panel
  if (lay.part) {
    const p = lay.part, py = y0 + lay.panelTop;
    withAnim(ctx, S, 7, PAD, py, () => {
    ctx.save(); rr(ctx, PAD - 2, py - 2, width - 2 * PAD + 4, lay.height - lay.panelTop - FOOT_H + 2, 8); ctx.fillStyle = "rgba(0,0,0,0.18)"; ctx.fill(); ctx.restore();
    ctx.font = F(700, 12.5); ctx.fillStyle = COL.orange; ctx.textAlign = "left"; ctx.textBaseline = "middle";
    ctx.fillText(p.name + ": what may be rolled", PAD + 2, py + 12);
    let rx = width - PAD - 2;
    const dr = p.data.random !== false;
    [{ id: "rnd", label: "Random", w: 60, on: dr, fn: () => { p.data.random = !dr; commit(node, false); }, t: dr ? "Random is ON: anything you leave empty is rolled. Click to switch it off and use only what you pick, as written." : "Random is OFF: only what you pick is used, nothing is rolled. Click to roll again." },
     { id: "clr", label: "Clear", w: 46, on: false, fn: () => { p.data.groups.forEach((g) => g.buttons.forEach((b) => { b.on = false; })); commit(node, false); }, t: "Switch every button of this part off (everything is rolled)." }]
      .forEach((t) => { rx -= t.w; pill(ctx, rx, py + 3, t.w, 18, t.label, t.on); hit(node, "rk:p" + t.id, rx, py + 3, t.w, 18, t.fn, "pointer", tip(t.t)); rx -= 5; });
    lay.items.forEach((it) => {
      const g = p.data.groups[it.gi], iy = y0 + it.y;
      if (it.k === "glabel") {
        const any = g.buttons.some((b) => b.on);
        ctx.font = F(700, 10); ctx.textAlign = "left"; ctx.textBaseline = "middle"; ctx.fillStyle = any ? COL.orange : COL.label;
        ctx.fillText(fitText(ctx, g.name.toUpperCase(), it.w), it.x, iy + BTN_H / 2 + 0.5);
        hit(node, `rk:g${it.gi}`, it.x, iy, it.w, BTN_H, () => { g.buttons.forEach((b) => { b.on = false; }); commit(node, false); }, "pointer", tip("Click a row name to switch that row off."));
      } else {
        const b = g.buttons[it.bi];
        ctx.save(); rr(ctx, it.x, iy, it.w, it.h, 5); ctx.fillStyle = b.on ? COL.onBg : COL.btn;
        if (b.on) { ctx.shadowColor = COL.glow; ctx.shadowBlur = 8; }
        ctx.fill(); ctx.shadowBlur = 0; ctx.lineWidth = b.on ? 1.5 : 1; ctx.strokeStyle = b.on ? COL.orange : COL.offEdge; ctx.stroke();
        ctx.font = F(500, 11); ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillStyle = b.on ? COL.onText : COL.offText;
        ctx.fillText(fitText(ctx, dl(b.label) || "…", it.w - 8), it.x + it.w / 2, iy + it.h / 2 + 0.5); ctx.restore();
        hit(node, `rk:b${it.gi}:${it.bi}`, it.x, iy, it.w, it.h, () => {
          const was = b.on; if (g.exclusive) g.buttons.forEach((o) => { o.on = false; }); b.on = !was; commit(node, false);
        }, "pointer", () => { setHover(node, { gi: it.gi, bi: it.bi }); return "pointer"; });
      }
    });
    });
  }

  // ---- footer
  const fy = y0 + lay.height - FOOT_H + 4;
  rr(ctx, PAD, fy, width - 2 * PAD, 22, 6); ctx.fillStyle = COL.well; ctx.fill(); ctx.strokeStyle = COL.rule; ctx.lineWidth = 1; ctx.stroke();
  ctx.font = F(500, 11); ctx.textAlign = "left"; ctx.textBaseline = "middle";
  const hv = S.hover; let line, tone = COL.label;
  if (hv && hv.tip) line = hv.tip;
  else if (hv && lay.part && lay.part.data.groups[hv.gi] && lay.part.data.groups[hv.gi].buttons[hv.bi]) { line = (lay.part.data.groups[hv.gi].buttons[hv.bi].text || "").replace(/\s+/g, " ").trim() || "(no text)"; tone = "#d9d4cb"; }
  else if (!on) { line = "Switched OFF: the bar adds nothing to the prompt."; tone = COL.orange; }
  else line = lay.fine ? "Click a card to choose what it may roll. Lock keeps a part's roll, the dice re-roll just that part. Roll all gives a new seed." : "Pick a style and how much, then Roll all. Advanced shows every part and button.";
  ctx.fillStyle = tone; ctx.fillText(fitText(ctx, line, width - 2 * PAD - 20), PAD + 9, fy + 11.5);
  ctx.restore();
}

// ---------------------------------------------------------------- node setup
function setupNode(node) {
  if (node.__rk) return;
  const w = node.widgets && node.widgets.find((x) => x.name === "bar_data");
  if (!w) return;
  const S = node.__rk = { w, raw: null, data: parse(w.value), hover: null, key: "", lay: null };
  S.raw = w.value;
  w.computeSize = (width) => { const ww = Math.max(MIN_W, node.size ? node.size[0] : width || MIN_W); return [ww, layoutFor(node, ww).height]; };
  w.computeLayoutSize = () => { const h = layoutFor(node, Math.max(MIN_W, node.size[0])).height; return { minHeight: h, maxHeight: h, minWidth: MIN_W }; };
  w.draw = (ctx, n, _w, y) => drawBar(ctx, n, y);
  w.serializeValue = undefined;
  node.__lcHoverOut = () => setHover(node, null);
  node.color = "#444444"; node.bgcolor = COL.panel;
  node.size[0] = Math.max(980, node.size[0]);
  node.setSize([node.size[0], node.computeSize()[1]]);
  const origSet = node.setSize;
  node.setSize = function (s) { this.size[0] = Math.max(MIN_W, s[0]); return origSet.call(this, [this.size[0], this.computeSize()[1]]); };
  const prevResize = node.onResize;
  node.onResize = function () { if (prevResize) prevResize.apply(this, arguments); const need = node.computeSize()[1]; if (Math.abs(node.size[1] - need) > 0.5) node.size[1] = need; };
  const prevCfg = node.onConfigure;
  node.onConfigure = function () { if (prevCfg) prevCfg.apply(this, arguments); S.key = ""; fit(node); };
}

api.addEventListener("executed", (ev) => {                              // the bar reports what each part rolled
  const d = ev && ev.detail, t = d && d.output && d.output.nt_parts;
  if (!t || !t.length) return;
  const n = app.graph && app.graph.getNodeById ? app.graph.getNodeById(Number(d.node)) : null;
  if (!n || !n.__rk) return;
  n.properties = n.properties || {};
  n.properties.nt_parts = String(t[0]);
  n.__rk.key = ""; n.__rk.revealT = now(); bump(n, 1000); n.setDirtyCanvas(true, true);
});

app.registerExtension({
  name: "NoThing.RouletteBar",
  nodeCreated(node) {
    if ((node.comfyClass || node.type) !== CLS) return;
    try { setupNode(node); } catch (e) { console.error("[No_Thing] Roulette Bar setup failed", e); }
  },
});
