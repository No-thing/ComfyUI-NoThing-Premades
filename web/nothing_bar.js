import { app } from "../../scripts/app.js";
import { api } from "../../scripts/api.js";
import { hit } from "./nt_interact.js";

// No_Thing Prompt Bar: rows of square buttons, each one a piece of prompt text.
// Click = on/off (orange glow = on). "Edit" lets you rename, rewrite, add, remove and reorder.
// Everything is stored as JSON in the node's one hidden text field ("bar_data"), so it is saved
// with the workflow and sent to the backend like any other setting.

const CLASSES = new Set(["NoThingPromptBar", "NoThingPromptBarDetail", "NoThingOutfitRoulette", "NoThingUnderwearRoulette", "NoThingMakeupRoulette", "NoThingHeadRoulette", "NoThingFaceRoulette", "NoThingHairRoulette", "NoThingBodyRoulette", "NoThingLighting"]);
// the fixed-button nodes: no Edit / Join, an ON/OFF switch. Roulettes roll anything left empty; Lighting is click-and-choose (empty = left out).
const WHAT = { NoThingOutfitRoulette: "outfit", NoThingUnderwearRoulette: "underwear", NoThingMakeupRoulette: "makeup", NoThingHeadRoulette: "face and hair", NoThingFaceRoulette: "face", NoThingHairRoulette: "hair", NoThingBodyRoulette: "body shape", NoThingLighting: "lighting" };
const isRoulette = (node) => (node.comfyClass || node.type) in WHAT;
const EDITABLE = new Set(["NoThingOutfitRoulette", "NoThingUnderwearRoulette", "NoThingMakeupRoulette", "NoThingHeadRoulette", "NoThingFaceRoulette", "NoThingHairRoulette", "NoThingFaceRoulette", "NoThingHairRoulette", "NoThingBodyRoulette", "NoThingLighting"]);      // these let you rewrite what a button says
const isEditable = (node) => EDITABLE.has(node.comfyClass || node.type);
const isDice = (node) => isRoulette(node) && !isChooser(node);                    // the nodes with a Random switch
const isRandom = (node) => isDice(node) && node.__nt.data.random !== false;
const isChooser = (node) => (node.comfyClass || node.type) === "NoThingLighting";
const isSimple = (node) => isRoulette(node) && !!node.__nt.data.simple;           // Simple mode: no button rows, just the quick switches and whatever is picked
const QUICK = new Set(["No shoes", "No bottoms", "No tops"]);                      // always visible in Simple mode
const ALIAS = { "No bottoms": "No pants" };                                         // what the button is called on screen
const dl = (label) => ALIAS[label] || label;
const SEPS = [["newline", "New line"], ["space", "Space"], ["comma", "Comma"]];
const FONT = "10.5px 'Montserrat Alternates', Inter, 'Segoe UI', sans-serif";
const COL = {
  panel: "#2B2B2B", head: "#EAE5DC", label: "#A8A39A", rule: "#444444", btn: "#383838", well: "#1D1D1D",
  onBg: "#3a2414", onEdge: "#ff8a2a", onGlow: "rgba(255,138,42,0.45)", onText: "#fff1e4",
  offBg: "#383838", offEdge: "#4a4a4a", offText: "#D8D8D8",
};
// compact metrics: four roulette nodes sit side by side under the Edit Page
const PAD = 8, HEAD_H = 26, LABEL_W = 68, BTN_H = 18, GAP = 3, GROUP_GAP = 6, FOOT_H = 36, MIN_W = 296, TOOL_H = 18;

// brand lettering: Montserrat Alternates ships in ./fonts (SIL Open Font License); on arrival every node re-measures its buttons
if (typeof FontFace !== "undefined") {
  try {
    const f = new FontFace("Montserrat Alternates", `url(${new URL("./fonts/MontserratAlternates-Light.ttf", import.meta.url).href})`, { weight: "300 700" });
    f.load().then(() => {
      document.fonts.add(f);
      for (const n of ((app.graph && (app.graph._nodes || app.graph.nodes)) || [])) if (n.__nt) { n.__nt.key = ""; if (n.computeSize) n.setSize([n.size[0], n.computeSize()[1]]); n.setDirtyCanvas(true, true); }
    }).catch(() => { /* cosmetic */ });
  } catch (e) { /* cosmetic */ }
}

const mctx = document.createElement("canvas").getContext("2d");
if (mctx) mctx.font = FONT;

// ---------------------------------------------------------------- data
function parse(raw) {
  try {
    const d = JSON.parse(raw);
    if (d && Array.isArray(d.groups)) {
      d.sep = d.sep || "newline";
      d.groups.forEach((g) => {
        g.name = String(g.name || "Group");
        g.exclusive = !!g.exclusive;
        g.buttons = Array.isArray(g.buttons) ? g.buttons : [];
        g.buttons.forEach((b) => { b.label = String(b.label ?? ""); b.text = String(b.text ?? ""); b.on = !!b.on; });
      });
      const opt = d.groups.find((g) => g.name === "Options" && g.buttons.some((b) => b.label === "One style per outfit"));
      if (opt && !opt.buttons.some((b) => b.label === "No shoes")) {                  // nodes saved before this button existed get it added
        opt.buttons.push({ label: "No shoes", text: "Off = shoes, boots and heels appear as the style rolls them. On = no shoes, socks, ankle pieces or feet anywhere in the prompt.", def: "", on: false, locked: true });
      }
      if (opt && !opt.buttons.some((b) => b.label === "Mixed brands")) {               // nodes saved before this button existed get it
        opt.buttons.push({ label: "Mixed brands", text: "Off = a brand style (Nike, Chanel...) sticks to ONE brand per roll, picked by the seed. On = pieces from every brand in the style are mixed.", def: "", on: false, locked: true });
      }
      const FRAME = [
        ["No bottoms", "For torso crops: On = only the top half is mentioned (no panties, skirts, legwear, shoes), so the model does not pull back to show them."],
        ["No tops", "For lower-body crops: On = only the bottom half is mentioned (no bras, tops, gloves, necklaces), so the model does not pull back to show them."],
      ];
      if (opt) {                                                                       // outfit bars saved before the framing buttons existed
        FRAME.forEach(([label, text]) => { if (!opt.buttons.some((b) => b.label === label)) opt.buttons.push({ label, text, def: "", on: false, locked: true }); });
      }
      const cov = d.groups.find((g) => g.name === "Coverage");
      const hasAdd = d.groups.some((g) => g.name === "Add-ons");
      if (cov && hasAdd && !d.groups.some((g) => g.name === "Options")) {             // underwear bars saved before the framing buttons existed
        d.groups.push({ name: "Options", exclusive: false, locked: true, buttons: FRAME.map(([label, text]) => ({ label, text, def: "", on: false, locked: true })) });
      }
      const sty = d.groups.find((g) => g.name === "Style" && g.buttons.some((b) => b.label === "Preppy Uniform"));
      if (sty && !sty.buttons.some((b) => b.label === "Baggy Comfy")) {                 // outfit nodes saved before this style existed get it
        const t = "baggy, oversized comfy clothes: big hoodies, loose sweatpants, hiding in soft layers (modest levels only)";
        sty.buttons.push({ label: "Baggy Comfy", text: t, def: t, on: false });
      }
      const ec = d.groups.find((g) => g.name === "Eye colour");
      if (ec) ec.buttons = ec.buttons.filter((b) => b.label !== "Violet");                   // violet eyes were taken out of the dataset
      const uw = d.groups.find((g) => g.name === "Style" && g.buttons.some((b) => b.label === "Lace Classics"));
      if (uw && !uw.buttons.some((b) => b.label === "Luxury Couture")) {                // underwear nodes saved before this style existed get it
        const t = "high-end designer lingerie: sheer silk robes, couture lace, gold-hardware straps, thigh straps and patterned harnesses (stars, pentagrams, art deco)";
        uw.buttons.push({ label: "Luxury Couture", text: t, def: t, on: false });
      }
      return d;
    }
  } catch (e) { /* fall through */ }
  return { v: 1, sep: "newline", groups: [] };
}

function sync(S) {
  if (S.w.value !== S.raw) { S.raw = S.w.value; S.data = parse(S.raw); S.key = ""; }
}

function commit(node, relayout) {
  const S = node.__nt;
  S.raw = JSON.stringify(S.data);
  S.w.value = S.raw;
  if (S.w.callback) { try { S.w.callback(S.raw); } catch (e) { /* ignore */ } }
  S.key = "";
  if (relayout) fit(node);
  if (app.graph && app.graph.change) app.graph.change();
  node.setDirtyCanvas(true, true);
}

function rollSeed(node) {                                              // a new seed for this node: same seed = same result, new seed = new variation
  const w = node.widgets && node.widgets.find((x) => x.name === "seed");
  if (!w) return;
  w.value = Math.floor(Math.random() * 4294967295);
  if (w.callback) { try { w.callback(w.value); } catch (e) { /* ignore */ } }
  if (app.graph && app.graph.change) app.graph.change();
  node.setDirtyCanvas(true, true);
}

function fit(node) {
  node.setSize([node.size[0], node.computeSize()[1]]);
}

// ---------------------------------------------------------------- layout
function layoutFor(node, width) {
  const S = node.__nt;
  sync(S);
  const last = (node.properties && node.properties.nt_last) || "";
  const key = S.raw + "|" + width + "|" + S.edit + "|" + last;
  if (S.key === key && S.lay) return S.lay;
  if (mctx) mctx.font = FONT;
  const items = [];
  let y = HEAD_H;
  const x0 = PAD + LABEL_W, x1 = width - PAD;
  if (isSimple(node)) {                                                    // Simple: quick switches first, then only the buttons that are on
    let sx = PAD, sy = y;
    const sadd = (it) => {
      it.w = Math.min(it.w, x1 - PAD);
      if (sx + it.w > x1 && sx > PAD) { sx = PAD; sy += BTN_H + GAP; }
      it.x = sx; it.y = sy; it.h = BTN_H; sx += it.w + GAP;
      items.push(it);
    };
    const quick = [], chosen = [];
    S.data.groups.forEach((g, gi) => g.buttons.forEach((b, bi) => {
      if (g.name === "Options" && QUICK.has(b.label)) quick.push({ gi, bi }); else if (b.on) chosen.push({ gi, bi });
    }));
    quick.concat(chosen).forEach(({ gi, bi }) =>
      sadd({ k: "btn", gi, bi, w: Math.max(32, Math.ceil(mctx ? mctx.measureText(dl(S.data.groups[gi].buttons[bi].label) || "…").width : 36) + 12) }));
    y = (quick.length || chosen.length ? sy + BTN_H : y) + GROUP_GAP;
    const lines = last ? wrapLines(last, width - 2 * PAD - 16, 4) : [];       // what the dice rolled last time
    if (lines.length) { const h = lines.length * 14 + 12; items.push({ k: "rolled", x: PAD, y, w: width - 2 * PAD, h, lines }); y += h + GROUP_GAP; }
    S.lay = { items, height: y + FOOT_H - 8 };
    S.key = key;
    return S.lay;
  }
  S.data.groups.forEach((g, gi) => {
    let x = x0, ry = y;
    items.push({ k: "glabel", gi, x: PAD, y: ry, w: LABEL_W - 8, h: BTN_H });
    const add = (it) => {
      it.w = Math.min(it.w, x1 - x0);
      if (x + it.w > x1 && x > x0) { x = x0; ry += BTN_H + GAP; }
      it.x = x; it.y = ry; it.h = BTN_H; x += it.w + GAP;
      items.push(it);
    };
    g.buttons.forEach((b, bi) =>
      add({ k: "btn", gi, bi, w: Math.max(32, Math.ceil(mctx ? mctx.measureText(dl(b.label) || "…").width : 36) + 12) }));
    if (S.edit && !isRoulette(node)) add({ k: "add", gi, w: 36 });
    y = ry + BTN_H + GROUP_GAP;
  });
  if (S.edit && !isRoulette(node)) { items.push({ k: "addgroup", x: PAD, y, w: 120, h: BTN_H }); y += BTN_H + GROUP_GAP; }
  if (!S.data.groups.length && !S.edit) y += 30;
  S.lay = { items, height: y + FOOT_H - 8 };
  S.key = key;
  return S.lay;
}

// ---------------------------------------------------------------- drawing
function rr(ctx, x, y, w, h, r) {
  ctx.beginPath();
  ctx.moveTo(x + r, y);
  ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r);
  ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r);
  ctx.closePath();
}

function wrapLines(text, maxW, maxLines) {                              // greedy word wrap with the layout font; the last line ends in … if the text is longer
  if (mctx) mctx.font = FONT;
  const words = String(text).replace(/\s+/g, " ").trim().split(" "), lines = [];
  let cur = "";
  for (let i = 0; i < words.length; i++) {
    const t = cur ? cur + " " + words[i] : words[i];
    if (!mctx || mctx.measureText(t).width <= maxW || !cur) cur = t;
    else { lines.push(cur); cur = words[i]; }
    if (lines.length === maxLines) break;
  }
  if (lines.length < maxLines && cur) lines.push(cur);
  else if (lines.length === maxLines) lines[maxLines - 1] = lines[maxLines - 1].replace(/[ ,.]*$/, "") + "…";
  return lines;
}

function fitText(ctx, text, maxW) {
  let t = String(text);
  if (ctx.measureText(t).width <= maxW) return t;
  while (t.length > 2 && ctx.measureText(t + "…").width > maxW) t = t.slice(0, -1);
  return t + "…";
}

function drawToggle(ctx, x, y, w, h, label, on, edit) {
  ctx.save();
  rr(ctx, x, y, w, h, 5);
  ctx.fillStyle = on ? COL.onBg : COL.offBg;
  if (on) { ctx.shadowColor = COL.onGlow; ctx.shadowBlur = 8; }       // glow only when on
  ctx.fill();
  ctx.lineWidth = on ? 1.5 : 1;
  ctx.strokeStyle = on ? COL.onEdge : COL.offEdge;
  if (edit) ctx.setLineDash([4, 3]);
  ctx.stroke();
  ctx.restore();
  ctx.save();
  ctx.font = FONT; ctx.textAlign = "center"; ctx.textBaseline = "middle";
  ctx.fillStyle = on ? COL.onText : COL.offText;
  ctx.fillText(fitText(ctx, label || "…", w - 7), x + w / 2, y + h / 2 + 0.5);
  ctx.restore();
}

function drawSmall(ctx, x, y, w, h, label, on) {
  ctx.save();
  rr(ctx, x, y, w, h, 5);
  ctx.fillStyle = on ? COL.onBg : COL.btn; ctx.fill();
  ctx.lineWidth = 1; ctx.strokeStyle = on ? COL.onEdge : "#4a4a4a"; ctx.stroke();
  ctx.font = FONT; ctx.textAlign = "center"; ctx.textBaseline = "middle";
  ctx.fillStyle = on ? COL.onText : "#cfcfd6";
  ctx.fillText(label, x + w / 2, y + h / 2 + 0.5);
  ctx.restore();
}

function summary(S) {
  const names = [];
  S.data.groups.forEach((g) => {
    let taken = false;
    g.buttons.forEach((b) => { if (b.on && !(g.exclusive && taken)) { taken = true; names.push(b.label); } });
  });
  return names;
}

function roulette_label(node, active) {
  const what = WHAT[node.comfyClass || node.type];
  if (isDice(node) && node.__nt.data.enabled !== false && node.__nt.data.random === false) return active.length ? `${active.length} picked · used as written` : "Random off · pick what you want";
  if (isRoulette(node) && node.__nt.data.enabled === false) return `Off · no ${what} is added`;
  if (isChooser(node)) return active.length ? `${active.length} chosen` : "Nothing chosen · no lighting is added";
  return isRoulette(node) ? (active.length ? `${active.length} chosen · the rest is random` : "Nothing chosen · everything is random") : `${active.length} on`;
}

function drawBar(ctx, node, y0) {
  const S = node.__nt, width = node.size[0];
  const lay = layoutFor(node, width);
  const reg = node.__lcHits;
  if (reg) for (const k of Array.from(reg.keys())) if (k.startsWith("nt:")) reg.delete(k);
  hit(node, "nt:bg", 0, y0, width, lay.height, () => {});               // swallow stray clicks
  const need = node.computeSize()[1];                                   // the height is always exactly what the buttons need,
  if (Math.abs(node.size[1] - need) > 1) node.size[1] = need;          // however the node was dragged
  ctx.save();
  ctx.beginPath(); ctx.rect(0, y0, width, lay.height); ctx.clip();     // nothing is ever drawn outside the frame

  // header: count on the left, tools on the right
  const active = summary(S);
  ctx.font = "600 10.5px 'Montserrat Alternates', Inter, 'Segoe UI', sans-serif"; ctx.textAlign = "left"; ctx.textBaseline = "middle";
  ctx.fillStyle = active.length ? COL.onEdge : COL.label;
  let lx = PAD;
  if (isRoulette(node)) {                                             // on/off switch: off = prefix / suffix pass through, no outfit
    const en = S.data.enabled !== false;
    drawSmall(ctx, PAD, y0 + 4, 38, TOOL_H, en ? "ON" : "OFF", en);
    hit(node, "nt:enable", PAD, y0 + 4, 38, TOOL_H, () => { S.data.enabled = !en; commit(node, false); }, "pointer",
      () => { setHover(node, { tip: `Switch this node on / off. Off = the prompt passes through without the ${WHAT[node.comfyClass || node.type]}.` }); return "pointer"; });
    lx = PAD + 44;
    if (isDice(node)) {                                               // Random: glowing orange = the dice roll, off = only what you picked is used
      const rnd = isRandom(node);
      drawSmall(ctx, lx, y0 + 4, 54, TOOL_H, "Random", rnd);
      hit(node, "nt:random", lx, y0 + 4, 54, TOOL_H, () => { S.data.random = !rnd; commit(node, true); }, "pointer",
        () => { setHover(node, { tip: rnd ? "Random is ON: anything you leave empty is rolled. Click to switch it off and use only what you pick." : "Random is OFF: the prompt is built from exactly what you picked, nothing is rolled. Click to roll again." }); return "pointer"; });
      lx += 60;
    }
  }
  ctx.fillStyle = isRoulette(node) && S.data.enabled === false ? COL.label : ctx.fillStyle;
  const sepLabel = (SEPS.find((s) => s[0] === S.data.sep) || SEPS[0])[1];
  const roulette = isRoulette(node);
  const simple = isSimple(node);
  const tools = roulette ? [
    ...(isDice(node) ? [{ id: "roll", label: "Roll", w: 34, fn: () => rollSeed(node), tip: "Roll: a new seed for this node, so a new variation of what is picked. Same seed = same result." }] : []),
    { id: "mode", label: simple ? "Full" : "Simple", w: 46, fn: () => { S.data.simple = !simple; commit(node, true); },
      tip: simple ? "Full: show every button row so you can pick exactly what may be rolled." : "Simple: hide the button rows, keep only the quick switches and what you picked." },
    ...(!simple && isEditable(node) ? [{ id: "edit", label: S.edit ? "Done" : "Edit", w: 38, on: S.edit, fn: () => { S.edit = !S.edit; fit(node); node.setDirtyCanvas(true, true); } }] : []),
    ...(!simple ? [{ id: "off", label: "Clear", w: 40, fn: () => {
        S.data.groups.forEach((g) => g.buttons.forEach((b) => { b.on = false; })); commit(node, false);
      }, tip: "Clear: switch every button off (everything is rolled)." }] : []),
  ] : [
    { id: "edit", label: S.edit ? "Done" : "Edit", w: 48, on: S.edit, fn: () => { S.edit = !S.edit; fit(node); node.setDirtyCanvas(true, true); } },
    { id: "sep", label: "Join: " + sepLabel, w: 92, fn: () => {
        const i = SEPS.findIndex((s) => s[0] === S.data.sep);
        S.data.sep = SEPS[(i + 1) % SEPS.length][0]; commit(node, false);
      } },
    { id: "off", label: "All off", w: 54, fn: () => {
        S.data.groups.forEach((g) => g.buttons.forEach((b) => { b.on = false; })); commit(node, false);
      } },
  ];
  let tx = width - PAD;
  tools.forEach((t) => {
    tx -= t.w;
    drawSmall(ctx, tx, y0 + 4, t.w, TOOL_H, t.label, t.on);
    hit(node, "nt:tool:" + t.id, tx, y0 + 4, t.w, TOOL_H, t.fn, "pointer", t.tip ? () => { setHover(node, { tip: t.tip }); return "pointer"; } : undefined);
    tx -= 5;
  });
  ctx.font = "600 10.5px 'Montserrat Alternates', Inter, 'Segoe UI', sans-serif"; ctx.textAlign = "left"; ctx.textBaseline = "middle";
  if (tx - lx - 4 >= 34) ctx.fillText(fitText(ctx, roulette_label(node, active), tx - lx - 4), lx, y0 + 13);     // no room = no label (the footer says it)
  ctx.strokeStyle = COL.rule; ctx.lineWidth = 1;
  ctx.beginPath(); ctx.moveTo(PAD, y0 + HEAD_H - 2.5); ctx.lineTo(width - PAD, y0 + HEAD_H - 2.5); ctx.stroke();

  // groups and buttons (dimmed while the node is switched OFF, so it is obvious it adds nothing)
  const hv = S.hover;
  const isOff = isRoulette(node) && S.data.enabled === false;
  if (isOff) ctx.globalAlpha = 0.4;
  lay.items.forEach((it) => {
    const x = it.x, y = y0 + it.y;
    if (it.k === "rolled") {                                           // Simple mode: the text the dice rolled last time
      ctx.save(); rr(ctx, x, y, it.w, it.h, 6); ctx.fillStyle = COL.well; ctx.fill(); ctx.strokeStyle = COL.rule; ctx.stroke();
      ctx.font = FONT; ctx.textAlign = "left"; ctx.textBaseline = "middle"; ctx.fillStyle = COL.head;
      it.lines.forEach((ln, i) => ctx.fillText(ln, x + 8, y + 6 + 7 + i * 14));
      ctx.restore(); return;
    }
    if (it.k === "glabel") {
      const g = S.data.groups[it.gi], any = g.buttons.some((b) => b.on);
      ctx.font = "600 9.5px 'Montserrat Alternates', Inter, 'Segoe UI', sans-serif"; ctx.textAlign = "left"; ctx.textBaseline = "middle";
      ctx.fillStyle = any ? COL.onEdge : COL.label;
      ctx.fillText(fitText(ctx, (g.name + (S.edit && !isRoulette(node) ? " ✎" : "")).toUpperCase(), it.w), x, y + BTN_H / 2 + 0.5);
      hit(node, `nt:g${it.gi}`, x, y, it.w, BTN_H, () => {
        if (S.edit && !isRoulette(node)) editGroup(node, it.gi);
        else { g.buttons.forEach((b) => { b.on = false; }); commit(node, false); }       // click a group name = clear that row
      }, "pointer", () => { setHover(node, { tip: S.edit && !isRoulette(node) ? "Edit this row" : "Click to switch this row off" }); return "pointer"; });
    } else if (it.k === "btn") {
      const g = S.data.groups[it.gi], b = g.buttons[it.bi];
      drawToggle(ctx, x, y, it.w, it.h, dl(b.label), b.on, S.edit && (!isRoulette(node) || (isEditable(node) && !b.locked)));
      if (b.def !== undefined && String(b.text).trim() !== String(b.def).trim()) {                // a small dot: this button's text was edited
        ctx.save(); ctx.fillStyle = COL.onEdge; ctx.beginPath(); ctx.arc(x + it.w - 6, y + 6, 2.6, 0, Math.PI * 2); ctx.fill(); ctx.restore();
      }
      hit(node, `nt:b${it.gi}:${it.bi}`, x, y, it.w, it.h, ({ ev }) => {
        if (!isRoulette(node) && (S.edit || (ev && ev.shiftKey))) { editButton(node, it.gi, it.bi, false); return; }
        if (isEditable(node) && !b.locked && (S.edit || (ev && ev.shiftKey))) { editText(node, it.gi, it.bi); return; }
        const was = b.on;
        if (g.exclusive) g.buttons.forEach((o) => { o.on = false; });
        b.on = !was;
        commit(node, false);
      }, "pointer", () => { setHover(node, { gi: it.gi, bi: it.bi }); return "pointer"; });
    } else if (it.k === "add") {
      ctx.save();
      rr(ctx, x, y, it.w, it.h, 5); ctx.setLineDash([4, 3]); ctx.strokeStyle = "#4a4a4a"; ctx.lineWidth = 1; ctx.stroke();
      ctx.setLineDash([]); ctx.fillStyle = "#A8A39A"; ctx.font = "16px 'Montserrat Alternates', Inter, 'Segoe UI', sans-serif";
      ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillText("+", x + it.w / 2, y + it.h / 2);
      ctx.restore();
      hit(node, `nt:add${it.gi}`, x, y, it.w, it.h, () => {
        const g = S.data.groups[it.gi];
        g.buttons.push({ label: "New", text: "", on: false });
        commit(node, true);
        editButton(node, it.gi, g.buttons.length - 1, true);
      }, "pointer", () => { setHover(node, { tip: "Add a button to this row" }); return "pointer"; });
    } else if (it.k === "addgroup") {
      ctx.save();
      rr(ctx, x, y, it.w, it.h, 5); ctx.setLineDash([4, 3]); ctx.strokeStyle = "#4a4a4a"; ctx.lineWidth = 1; ctx.stroke();
      ctx.setLineDash([]); ctx.fillStyle = "#A8A39A"; ctx.font = FONT;
      ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillText("+ Add row", x + it.w / 2, y + it.h / 2 + 0.5);
      ctx.restore();
      hit(node, "nt:addgroup", x, y, it.w, it.h, () => {
        S.data.groups.push({ name: "New row", exclusive: false, buttons: [] });
        commit(node, true);
        editGroup(node, S.data.groups.length - 1, true);
      }, "pointer", () => { setHover(node, { tip: "Add a new row of buttons" }); return "pointer"; });
    }
  });

  ctx.globalAlpha = 1;
  if (!S.data.groups.length && !S.edit) {
    ctx.font = FONT; ctx.fillStyle = COL.label; ctx.textAlign = "center"; ctx.textBaseline = "middle";
    ctx.fillText("No buttons yet. Press Edit, then + Add row.", width / 2, y0 + HEAD_H + 14);
  }

  // footer: what the hovered button says, else what is switched on
  const fy = y0 + lay.height - FOOT_H + 8 + 3;
  rr(ctx, PAD, fy, width - 2 * PAD, 22, 5); ctx.fillStyle = COL.well; ctx.fill();
  ctx.strokeStyle = COL.rule; ctx.stroke();
  ctx.font = FONT; ctx.textAlign = "left"; ctx.textBaseline = "middle";
  let line, tone = "#A8A39A";
  if (hv && hv.tip) line = hv.tip;
  else if (hv && S.data.groups[hv.gi] && S.data.groups[hv.gi].buttons[hv.bi]) {
    const b = S.data.groups[hv.gi].buttons[hv.bi];
    line = (b.text || "(empty – press Edit to write a prompt)").replace(/\s+/g, " ").trim(); tone = "#b8b8c2";
    if (isEditable(node) && !b.locked && S.edit) line = "Click to edit:  " + line;
  } else if (isOff) { line = "Switched OFF: this node adds nothing to the prompt. Click OFF (top left) to turn it on."; tone = "#ff9a5a";
  } else if (active.length) { line = active.join("  ·  "); tone = "#d4b79c"; }
  else line = isDice(node) && !isRandom(node) ? "Random is off: only the buttons you pick are used, as written. Shift+click a button to edit its text." : isChooser(node) ? "Click what you want. Shift+click or Edit text changes what a button says." : isEditable(node) ? "Pick what you care about, the rest is rolled. Shift+click or Edit text changes what a button says." : isRoulette(node) ? "Pick skimpiness, styles, accessories or colours. Anything left empty is rolled at random." : "Nothing on – the prompt passes through unchanged.";
  ctx.fillStyle = tone;
  ctx.fillText(fitText(ctx, line, width - 2 * PAD - 20), PAD + 9, fy + 11.5);
  ctx.restore();
}

function setHover(node, h) {
  const S = node.__nt;
  const same = S.hover && h && S.hover.gi === h.gi && S.hover.bi === h.bi && S.hover.tip === h.tip;
  if (!same) { S.hover = h; node.setDirtyCanvas(true, true); }
}

// ---------------------------------------------------------------- the editor dialog
function openDialog(spec) {
  const el = (tag, css, text) => { const e = document.createElement(tag); if (css) e.style.cssText = css; if (text != null) e.textContent = text; return e; };
  const ov = el("div", "position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:10000;display:flex;align-items:center;justify-content:center;font:13px Inter,'Segoe UI',sans-serif");
  const panel = el("div", "width:min(520px,92vw);background:#1b1b1d;border:1px solid #34343a;border-radius:10px;padding:18px;color:#e8e8ea;box-shadow:0 24px 70px rgba(0,0,0,.7)");
  panel.appendChild(el("div", "font-weight:600;font-size:14px;margin-bottom:14px", spec.title));
  const inputs = {};
  spec.fields.forEach((f) => {
    const wrap = el("div", "margin-bottom:12px");
    if (f.type === "check") {
      const lab = el("label", "display:flex;align-items:center;gap:8px;color:#cfcfd6;cursor:pointer");
      const cb = el("input"); cb.type = "checkbox"; cb.checked = !!f.value; cb.style.cssText = "accent-color:#ff8a2a;width:15px;height:15px";
      lab.appendChild(cb); lab.appendChild(el("span", "", f.label));
      wrap.appendChild(lab); inputs[f.key] = cb;
    } else {
      wrap.appendChild(el("div", "color:#8d8d96;font-size:11px;letter-spacing:.06em;text-transform:uppercase;margin-bottom:5px", f.label));
      const inp = el(f.type === "area" ? "textarea" : "input",
        "width:100%;box-sizing:border-box;background:#101012;color:#ececf0;border:1px solid #34343a;border-radius:6px;padding:8px 10px;font:13px Inter,'Segoe UI',sans-serif;outline:none;" + (f.type === "area" ? "min-height:170px;resize:vertical;line-height:1.45" : ""));
      inp.value = f.value; if (f.type === "area") inp.rows = 8;
      inp.addEventListener("focus", () => { inp.style.borderColor = "#ff8a2a"; });
      inp.addEventListener("blur", () => { inp.style.borderColor = "#34343a"; });
      wrap.appendChild(inp); inputs[f.key] = inp;
    }
    panel.appendChild(wrap);
  });
  const row = el("div", "display:flex;align-items:center;gap:8px;margin-top:6px");
  const btn = (text, css, fn) => { const b = el("button", "border-radius:6px;padding:7px 13px;font:13px Inter,'Segoe UI',sans-serif;cursor:pointer;border:1px solid #3a3a40;background:#2a2a2e;color:#e0e0e6;" + (css || ""), text); b.addEventListener("click", fn); return b; };
  const close = () => { ov.remove(); };
  const save = () => {
    const v = {}; spec.fields.forEach((f) => { v[f.key] = f.type === "check" ? inputs[f.key].checked : inputs[f.key].value; });
    spec.onSave(v); close();
  };
  const cancel = () => { if (spec.onCancel) spec.onCancel(); close(); };
  (spec.moves || []).forEach((m) => row.appendChild(btn(m.label, m.disabled ? "opacity:.35;pointer-events:none" : "", () => { close(); m.fn(); })));
  if (spec.onDelete) row.appendChild(btn("Delete", "color:#ff8f8f;border-color:#5a3434", () => { close(); spec.onDelete(); }));
  row.appendChild(el("div", "flex:1"));
  row.appendChild(btn("Cancel", "", cancel));
  row.appendChild(btn("Save", "background:#3a2414;border-color:#ff8a2a;color:#fff1e4;box-shadow:0 0 12px rgba(255,138,42,.45)", save));
  panel.appendChild(row);
  panel.appendChild(el("div", "margin-top:10px;color:#6f6f78;font-size:11px", "Ctrl+Enter saves · Esc cancels"));
  ov.appendChild(panel);
  ["keydown", "keyup", "keypress"].forEach((t) => ov.addEventListener(t, (e) => {
    e.stopPropagation();
    if (t === "keydown" && e.key === "Escape") cancel();
    if (t === "keydown" && e.key === "Enter" && (e.ctrlKey || e.metaKey)) { e.preventDefault(); save(); }
  }));
  document.body.appendChild(ov);
  const first = inputs[spec.fields[0].key];
  if (first && first.focus) { first.focus(); if (first.select && spec.fields[0].type !== "check") first.select(); }
  return { close, inputs };
}

function move(arr, i, d) { const j = i + d; if (j < 0 || j >= arr.length) return; const t = arr[i]; arr[i] = arr[j]; arr[j] = t; }

function editButton(node, gi, bi, isNew) {
  const S = node.__nt, g = S.data.groups[gi], b = g.buttons[bi];
  openDialog({
    title: `Button in "${g.name}"`,
    fields: [{ key: "label", label: "Button name", type: "text", value: b.label },
             { key: "text", label: "Prompt text (added to the prompt when this button is on)", type: "area", value: b.text }],
    onSave: (v) => { b.label = v.label.trim() || "Button"; b.text = v.text; commit(node, true); },
    onCancel: isNew ? () => { g.buttons.splice(bi, 1); commit(node, true); } : null,
    onDelete: () => { g.buttons.splice(bi, 1); commit(node, true); },
    moves: [{ label: "◀ Left", disabled: bi === 0, fn: () => { move(g.buttons, bi, -1); commit(node, true); } },
            { label: "Right ▶", disabled: bi === g.buttons.length - 1, fn: () => { move(g.buttons, bi, 1); commit(node, true); } }],
  });
}

function editText(node, gi, bi) {
  const S = node.__nt, g = S.data.groups[gi], b = g.buttons[bi];
  const hint = g.name === "Setup" ? "  ·  write {key} and {rim} where the light colours go" : g.name === "Hair colour" ? "  ·  separate colour words with commas" : "";
  openDialog({
    title: `${g.name}: ${b.label}`,
    fields: [{ key: "text", label: "What this button adds to the prompt" + hint, type: "area", value: b.text }],
    onSave: (v) => { b.text = v.text.trim() ? v.text : (b.def ?? ""); commit(node, true); },
    moves: b.def !== undefined ? [{ label: "Reset to default", disabled: String(b.text).trim() === String(b.def).trim(), fn: () => { b.text = b.def; commit(node, true); } }] : [],
  });
}

function editGroup(node, gi, isNew) {
  const S = node.__nt, g = S.data.groups[gi];
  openDialog({
    title: "Row",
    fields: [{ key: "name", label: "Row name", type: "text", value: g.name },
             { key: "exclusive", label: "One at a time (pressing a button switches the others in this row off)", type: "check", value: g.exclusive }],
    onSave: (v) => {
      g.name = v.name.trim() || "Row"; g.exclusive = v.exclusive;
      if (g.exclusive) { let seen = false; g.buttons.forEach((b) => { if (b.on && seen) b.on = false; if (b.on) seen = true; }); }
      commit(node, true);
    },
    onCancel: isNew ? () => { S.data.groups.splice(gi, 1); commit(node, true); } : null,
    onDelete: () => { S.data.groups.splice(gi, 1); commit(node, true); },
    moves: [{ label: "▲ Up", disabled: gi === 0, fn: () => { move(S.data.groups, gi, -1); commit(node, true); } },
            { label: "Down ▼", disabled: gi === S.data.groups.length - 1, fn: () => { move(S.data.groups, gi, 1); commit(node, true); } }],
  });
}

// ---------------------------------------------------------------- node setup
function setupNode(node) {
  if (node.__nt) return;
  const w = node.widgets && node.widgets.find((x) => x.name === "bar_data");
  if (!w) return;
  const S = node.__nt = { w, raw: null, data: parse(w.value), edit: false, hover: null, key: "", lay: null };
  S.raw = w.value;

  w.computeSize = (width) => {
    const ww = Math.max(MIN_W, node.size ? node.size[0] : width || MIN_W);
    return [ww, layoutFor(node, ww).height];
  };
  w.computeLayoutSize = () => {
    const h = layoutFor(node, Math.max(MIN_W, node.size[0])).height;
    return { minHeight: h, maxHeight: h, minWidth: MIN_W };
  };
  w.draw = (ctx, n, _w, y) => drawBar(ctx, n, y);
  w.serializeValue = undefined;

  node.__lcHoverOut = () => { setHover(node, null); };
  node.color = "#444444";
  node.bgcolor = COL.panel;
  node.size[0] = Math.max(320, node.size[0]);          // width first: the height depends on it
  node.setSize([node.size[0], node.computeSize()[1]]);

  const origSet = node.setSize;
  node.setSize = function (s) {              // whatever size is asked for, the height stays exactly what the buttons need
    this.size[0] = Math.max(MIN_W, s[0]);
    return origSet.call(this, [this.size[0], this.computeSize()[1]]);
  };
  const prevResize = node.onResize;
  node.onResize = function (size) {          // height always follows the content
    if (prevResize) prevResize.apply(this, arguments);
    const need = node.computeSize()[1];
    if (Math.abs(node.size[1] - need) > 0.5) node.size[1] = need;
  };
  // a loaded workflow sets the value after the node exists
  const prevCfg = node.onConfigure;
  node.onConfigure = function () {
    if (prevCfg) prevCfg.apply(this, arguments);
    S.key = "";
    fit(node);
  };
}

api.addEventListener("executed", (ev) => {                              // a roulette reports what it rolled: remembered in the node, shown in Simple mode
  const d = ev && ev.detail, t = d && d.output && d.output.nt_text;
  if (!t || !t.length) return;
  const n = app.graph && app.graph.getNodeById ? app.graph.getNodeById(Number(d.node)) : null;
  if (!n || !n.__nt) return;
  n.properties = n.properties || {};
  n.properties.nt_last = String(t[0]);
  n.__nt.key = "";
  if (n.computeSize) n.setSize([n.size[0], n.computeSize()[1]]);
  n.setDirtyCanvas(true, true);
});

app.registerExtension({
  name: "NoThing.PromptBar",
  nodeCreated(node) {
    if (!CLASSES.has(node.comfyClass || node.type)) return;
    try { setupNode(node); }
    catch (e) { console.error("[No_Thing] Prompt Bar setup failed", e); }
  },
});
