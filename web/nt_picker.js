// Searchable, categorised dropdown for the Roulette Bar's Style (theme) chooser.
// Type to filter, arrow keys + Enter to pick, Esc or any click outside closes it. Opens with an expo ease-out like the brand motion.

const ORANGE = "#ff8a2a";
const EXPO = "cubic-bezier(0.16, 1, 0.3, 1)";
const EVENTS = ["pointerdown", "mousedown", "wheel", "contextmenu"];
let open = null;

function close(fast) {
  const el = open;
  if (!el) return;
  open = null;
  EVENTS.forEach((n) => document.removeEventListener(n, onDoc, true));
  window.removeEventListener("blur", onBlur); window.removeEventListener("resize", onBlur);
  document.removeEventListener("keydown", onKey, true);
  el.style.transition = "opacity 140ms ease-out, transform 140ms ease-out";
  el.style.opacity = "0"; el.style.transform = "translateY(-4px) scale(.98)";
  setTimeout(() => el.remove(), fast ? 0 : 150);
}
function onDoc(e) { if (open && !open.contains(e.target)) close(); }   // pointerdown too: the canvas cancels the compatibility mouse events
function onBlur() { close(true); }
function onKey(e) { if (e.key === "Escape") close(); }

// items: [{ name, cat, desc }], current: name or "", noneLabel: text of the first row
export function pickTheme({ event, items, current, noneLabel, onPick }) {
  close(true);
  const el = document.createElement("div");
  Object.assign(el.style, {
    position: "fixed", zIndex: 100000, width: "320px", maxHeight: "min(72vh, 560px)", display: "flex", flexDirection: "column",
    background: "#232323", border: "1px solid #3a3a3a", borderRadius: "8px", boxShadow: "0 10px 30px rgba(0,0,0,.55)",
    font: "12px 'Montserrat Alternates', system-ui, sans-serif", color: "#d8d8d8", overflow: "hidden",
    opacity: "0", transform: "translateY(-10px) scale(.94)", transformOrigin: "top left", willChange: "transform, opacity",
  });
  const input = document.createElement("input");
  input.placeholder = "Search styles…  (" + items.length + ")";
  Object.assign(input.style, { margin: "8px", padding: "7px 9px", background: "#161616", border: "1px solid #3a3a3a", borderRadius: "6px", color: "#eee", font: "inherit", outline: "none" });
  const list = document.createElement("div");
  Object.assign(list.style, { overflowY: "auto", padding: "0 6px 8px" });
  el.append(input, list);

  let flat = [], sel = 0;
  const choose = (v) => { close(); onPick(v); };
  const render = () => {
    const q = input.value.trim().toLowerCase();
    list.textContent = ""; flat = [];
    const add = (name, desc, v, dim) => {
      const row = document.createElement("div");
      Object.assign(row.style, { padding: "5px 8px", borderRadius: "5px", cursor: "pointer" });
      const a = document.createElement("div"); a.textContent = name;
      a.style.color = dim ? "#8a8a8a" : (v === current ? ORANGE : "#e6e6e6");
      row.append(a);
      if (desc) { const b = document.createElement("div"); b.textContent = desc; Object.assign(b.style, { fontSize: "10.5px", color: "#8f8a82", marginTop: "1px" }); row.append(b); }
      const i = flat.length; flat.push({ v, row });
      row.onmouseenter = () => { sel = i; paint(); };
      row.onclick = () => choose(v);
      list.append(row);
    };
    if (!q) add(noneLabel, "no theme: every part rolls anything", "", true);
    const cats = [...new Set(items.map((t) => t.cat))];
    for (const cat of cats) {
      const shown = items.filter((t) => t.cat === cat && (!q || (t.name + " " + t.desc + " " + cat).toLowerCase().includes(q)));
      if (!shown.length) continue;
      const h = document.createElement("div");
      h.textContent = cat.toUpperCase();
      Object.assign(h.style, { padding: "9px 8px 3px", fontSize: "10px", letterSpacing: ".08em", color: ORANGE, opacity: ".85" });
      list.append(h);
      shown.forEach((t) => add(t.name, t.desc, t.name));
    }
    if (!flat.length) { const e = document.createElement("div"); e.textContent = "No style matches"; e.style.cssText = "padding:10px 8px;color:#777"; list.append(e); }
    sel = q ? 0 : Math.max(0, flat.findIndex((f) => f.v === current));
    paint(true);
  };
  const paint = (scroll) => {
    flat.forEach((f, i) => { f.row.style.background = i === sel ? "#3a3a3a" : "transparent"; });
    if (scroll && flat[sel]) flat[sel].row.scrollIntoView({ block: "center" });
  };
  input.addEventListener("input", render);
  input.addEventListener("keydown", (e) => {
    if (e.key === "ArrowDown") { sel = Math.min(flat.length - 1, sel + 1); paint(); flat[sel] && flat[sel].row.scrollIntoView({ block: "nearest" }); e.preventDefault(); }
    else if (e.key === "ArrowUp") { sel = Math.max(0, sel - 1); paint(); flat[sel] && flat[sel].row.scrollIntoView({ block: "nearest" }); e.preventDefault(); }
    else if (e.key === "Enter") { if (flat[sel]) choose(flat[sel].v); }
    e.stopPropagation();
  });

  document.body.append(el);
  const ev = event || {}, vw = window.innerWidth, vh = window.innerHeight, r = el.getBoundingClientRect();
  el.style.left = Math.max(8, Math.min((ev.clientX ?? 100) - 20, vw - r.width - 8)) + "px";
  el.style.top = Math.max(8, Math.min((ev.clientY ?? 100) - 10, vh - r.height - 8)) + "px";
  open = el;
  EVENTS.forEach((n) => document.addEventListener(n, onDoc, true));
  window.addEventListener("blur", onBlur); window.addEventListener("resize", onBlur);
  document.addEventListener("keydown", onKey, true);
  render();
  input.focus();
  requestAnimationFrame(() => {
    el.style.transition = "opacity 260ms " + EXPO + ", transform 520ms " + EXPO;
    el.style.opacity = "1"; el.style.transform = "none";
    flat.slice(0, 14).forEach((f, i) => {
      f.row.style.opacity = "0"; f.row.style.transform = "translateY(8px)";
      f.row.style.transition = "opacity 300ms " + EXPO + " " + (i * 14) + "ms, transform 560ms " + EXPO + " " + (i * 14) + "ms";
      requestAnimationFrame(() => { f.row.style.opacity = "1"; f.row.style.transform = "none"; });
    });
  });
}
