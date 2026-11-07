"""
No_Thing Underwear Roulette - rolls a random lingerie / underwear set from the dataset in underwear_data.py.
It is the sibling of the Outfit Roulette (which now only does clothes): use one, the other, or both.

Rows: Coverage (Soft ... Micro), Style (the 12 families: Designer, Lace Classics, Corsets, ...), Add-ons (which kinds of extras:
Legwear, Garter belt, Gloves & neck, Headwear, Layer), Add-on amount, Colour. Nothing picked in a row = anything goes for that row.
Random OFF = no dice: the texts of the buttons you picked are joined. The `seed` decides the roll.
"""
import json
import os
import re
import random

from . import underwear_data as D
from . import framing as FR
from .outfit_data import COLOURS
from .roulette_common import avoid, group, with_seed, scheme_pair, tier

HERE = os.path.dirname(os.path.abspath(__file__))
SEPS = {"newline": "\n", "space": " ", "comma": ", "}
NO_BOTTOMS, NO_TOPS = FR.NO_BOTTOMS, FR.NO_TOPS
OPTION_TEXTS = {
    NO_BOTTOMS: "For torso crops: On = only the bra / top half is mentioned (no panties, thongs, garters, stockings or legwear), so the model does not pull back to show them.",
    NO_TOPS: "For lower-body crops: On = only the bottom half is mentioned (panties, garters, stockings), no bras, corsets, gloves or chokers.",
}


def _parse_entry(s):
    head, _, text = s.partition("|")
    lo, _, hi = head.partition("-")
    lo = int(lo)
    return lo, int(hi) if hi else lo, text.strip()


def _load_custom():
    """Optional underwear_custom.json: {"Corsets": ["3|my line"], "extras": {"Legwear": ["2|my stockings"]}}"""
    path = os.path.join(HERE, "underwear_custom.json")
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def _build():
    custom = _load_custom()
    sets = {}
    for name, entries in D.SETS.items():
        extra = custom.get(name, [])
        sets[name] = [_parse_entry(e) for e in list(entries) + [e for e in (extra if isinstance(extra, list) else []) if isinstance(e, str) and "|" in e]]
    ex_custom = custom.get("extras", {}) if isinstance(custom.get("extras", {}), dict) else {}
    extras = {}
    for name, entries in D.EXTRAS.items():
        extra = ex_custom.get(name, [])
        extras[name] = [_parse_entry(e) for e in list(entries) + [e for e in (extra if isinstance(extra, list) else []) if isinstance(e, str) and "|" in e]]
    return sets, extras


SETS, EXTRAS = _build()


def default_bar():
    lvl_texts = dict(zip(D.LEVELS, [
        "soft everyday cotton and seamless underwear", "pretty classic lace and satin sets", "seductive plunge, sheer and garter pieces",
        "bold cut-out, cage and strappy lingerie", "minimal-fabric strap and string lingerie"]))
    amt_texts = {"None": "no add-ons", "Few": "with one add-on", "Some": "with a couple of add-ons", "Loaded": "loaded with add-ons"}
    style_texts = {n: D.DESC[n] for n in D.STYLE_NAMES}
    addon_texts = {"Legwear": "stockings, fishnets and tights", "Garter belt": "garter belts and thigh garters", "Gloves & neck": "gloves and chokers (leather, spiked and O-ring ones too)", "Soft gloves & neck": "lace, satin and pearl gloves and chokers",
                   "Headwear": "bunny ears, horns, masks and headbands", "Veils & masks": "face veils, mourning veils, mesh face covers and masquerade masks", "Layer": "robes, kimonos and open shirts"}
    col_texts = {k: "mainly " + v[0] for k, v in COLOURS.items()}
    return {"v": 1, "sep": "newline", "groups": [
        group("Coverage", D.LEVELS, lvl_texts),
        group("Style", D.STYLE_NAMES, style_texts),
        group("Add-ons", D.ADDON_NAMES, addon_texts),
        group("Add-on amount", D.AMOUNTS, amt_texts),
        group("Colour", list(COLOURS), col_texts),
        group("Options", [NO_BOTTOMS, NO_TOPS], OPTION_TEXTS, locked=True),
    ]}


def _parse(raw):
    try:
        data = json.loads(raw)
        if isinstance(data, dict) and isinstance(data.get("groups"), list):
            return data
    except (TypeError, ValueError):
        pass
    return {"sep": "newline", "groups": []}


def _on(data, name):
    for g in data.get("groups", []):
        if g.get("name") == name:
            return [b.get("label", "") for b in g.get("buttons", []) if b.get("on")]
    return []


def fixed(data):
    """Random off: the texts of the picked buttons, e.g. 'wearing famous lingerie house styles, seductive plunge ..., mainly black'."""
    parts = []
    for row in ("Style", "Coverage", "Add-ons", "Colour"):
        for g in data.get("groups", []):
            if g.get("name") == row:
                on = [str(b.get("text", "")).strip() for b in g.get("buttons", []) if b.get("on")]
                parts.append(" and ".join(t for t in on if t) if row in ("Style", "Add-ons") else ", ".join(t for t in on if t))
    parts = [p for p in parts if p]
    text = ("wearing " + ", ".join(parts) + ".") if parts else ""
    opts = [b.get("label") for g in data.get("groups", []) if g.get("name") == "Options" for b in g.get("buttons", []) if b.get("on")]
    if text and (NO_BOTTOMS in opts or NO_TOPS in opts):
        bits = FR.strip_bits(text, NO_TOPS in opts, NO_BOTTOMS in opts)
        text = ("wearing " + bits.replace("wearing ", "", 1) + ".") if bits.strip() else ""
    return text


def roll(seed, levels=(), styles=(), addons=(), amounts=(), colours=(), no_bottoms=False, no_tops=False):
    """Returns (text, summary, details)."""
    rng = random.Random(seed)
    lvl_idx = [D.LEVELS.index(l) + 1 for l in levels if l in D.LEVELS] or list(range(1, 6))
    t_ = tier()
    if t_ and t_ >= 3:                                         # inside the Bar the underwear follows the outfit: Revealing = thongs, Skimpy = lingerie model, Micro = erotic
        lvl_idx = [t_] if t_ in lvl_idx or not [l for l in lvl_idx if l >= t_ - 1] else [l for l in lvl_idx if l >= t_ - 1][:1]
    elif t_ == 2:
        lvl_idx = [l for l in lvl_idx if l <= 2] or [2]
    sel = [s for s in styles if s in SETS]
    free = not sel
    if free:                                                   # nothing picked: one or two families, not all twelve
        sel = rng.sample(D.STYLE_NAMES, rng.choices([1, 2], [65, 35])[0])
    want = rng.choice(lvl_idx)

    def lines(s_):                                             # a family's lines cut down to what is in frame (tops / bottoms)
        out = []
        for lo, hi, t in SETS[s_]:
            if no_bottoms or no_tops:
                t = FR.visible_text(t, no_tops=no_tops, no_bottoms=no_bottoms)
                if not t:
                    continue
            out.append((lo, hi, t))
        return out

    def find(sel_):
        cache = {s_: lines(s_) for s_ in sel_}
        for cand in sorted(range(1, 6), key=lambda x: (abs(x - want), x > want)):          # nothing at this level: the nearest one (softer first)
            pl = [(s_, t) for s_ in sel_ for lo, hi, t in cache[s_] if lo <= cand <= hi]
            if pl:
                return cand, pl
        return want, []

    level, pool = find(sel)
    notes = []
    if not pool and (no_bottoms or no_tops):                   # the picked families have nothing for this framing: any family will do
        notes.append("nothing for this framing in the picked styles, used any style")
        sel = list(D.STYLE_NAMES)
        level, pool = find(sel)
    if level != want and pool:
        notes.append(f"nothing at {D.LEVELS[want - 1]}, used {D.LEVELS[level - 1]}")
    if not pool:
        return "", "nothing to show for this framing", dict(level=level, style="", extras=[], primary="")
    styles_here = sorted({s_ for s_, _ in pool}, key=sel.index)
    style = rng.choice(styles_here)
    cands = [t for s_, t in pool if s_ == style]
    if style == "Branded Lounge":                              # sporty look: the sports sets, not the Playboy / Victoria's Secret lingerie lines
        cands = [t for t in cands if not re.search(r"^(Playboy|Victoria)", t)] or cands
    cands = [t for t in cands if not avoid(t)] or cands          # the outfit already has a hat or sunglasses: no ears, mask or veil on top
    main = rng.choice(cands)

    words = [w for c in colours if c in COLOURS for w in COLOURS[c]] if colours else list(D.PALETTE[style])
    primary = rng.choice(words)
    rest = [w for w in words if w != primary]
    accent = rng.choice(rest) if rest else primary
    if scheme_pair():
        primary, accent = scheme_pair()                       # the Bar's Style hands every part the same colours

    def fill(text, accent_ok=False):
        c = accent if (accent_ok and rng.random() < 0.5) else primary
        out = text.replace("{c}", c).replace("{c2}", accent)
        return re.sub(r"\ba (?=(emerald|ivory|aqua|amber|olive|orange|ash|apricot|azure|indigo)\b)", "an ", out)

    amount = rng.choice([a for a in amounts if a in D.AMOUNT_RANGE] or D.AMOUNTS)
    n = rng.randint(*D.AMOUNT_RANGE[amount])
    groups = [g for g in addons if g in EXTRAS] or list(EXTRAS)
    if no_bottoms:                                             # torso crop: no legwear or garters
        groups = [g for g in groups if g not in ("Legwear", "Garter belt")]
    if no_tops:                                                # lower-body crop: no gloves, chokers, headwear or robes
        groups = [g for g in groups if g not in ("Gloves & neck", "Soft gloves & neck", "Headwear", "Veils & masks", "Layer")]
    if level >= 5:                                             # Micro: no robe, kimono or open shirt over the lingerie (Skimpy may keep one)
        if style != "Latex & PVC":                                  # (a latex robe or an open sheer robe fits the latex look at any level)
            groups = [g for g in groups if g != "Layer"] or groups
    if style == "Luxury Couture":                              # high-end look: no bunny ears or headbands, and no second robe when the set already has one
        groups = [g for g in groups if g != "Headwear" and not (g == "Layer" and "robe" in main)] or groups
    rng.shuffle(groups)
    extras = []
    if style == "Branded Lounge":                              # sporty set: sport gear (sleeves, one phone strap on an arm OR a leg), no lace, garters or robes
        opts = [_parse_entry(e) for e in D.SPORT_EXTRAS]
        pool_s = [t for lo, hi, t in opts if lo <= level <= hi]
        if no_bottoms:
            pool_s = [t for t in pool_s if not re.search("leg|thigh|knee", t)]
        if no_tops:
            pool_s = [t for t in pool_s if not re.search("arm|wrist", t)]
        rng.shuffle(pool_s)
        phone = False
        for t in pool_s:
            if len(extras) >= min(n, 2):
                break
            if D.SPORT_PHONE in t:
                if phone:
                    continue
                phone = True
            if "compression sleeve" in t and phone and "arm" in t and any("armband" in e for e in extras):
                continue
            extras.append(fill(t, True))
        groups = []
    for g in groups:
        if len(extras) >= n:
            break
        opts = [t for lo, hi, t in EXTRAS[g] if lo <= level <= hi]                   # none at this level: skip that kind of add-on
        if style == "Luxury Couture":                                                # no coarse fishnets, cat / bunny or neon pieces on a couture set
            opts = [t for t in opts if not re.search(r"fishnet|bunny|cat |kitten|neon|spiked|studded|gothic|face|veil|mask", t)]
        if style == "Boho Crochet":                                                  # only beads, shells, chains and charms: no lace gloves, mesh tights or bows
            opts = [t for t in opts if re.search(r"chain|bead|shell|anklet|charm|pendant|cuff|bracelet|choker", t) and not re.search(r"lace|mesh|fishnet|bow|stocking|thigh|sheer|latex|spiked|studded|veil|mask", t)]
        if g == "Layer" and style == "Latex & PVC":
            opts += [t for lo, hi, t in (_parse_entry(e) for e in D.LATEX_LAYER) if lo <= level <= hi]
        if no_bottoms:
            opts = [t for t in opts if not FR.LOW.search(t)]
        if no_tops:
            opts = [t for t in opts if not FR.TOP.search(t)]
        opts = [t for t in opts if not avoid(t)]
        if opts:
            extras.append(fill(rng.choice(opts), True))
    text = "wearing " + fill(main)
    if extras:
        text += ", with " + ", ".join(extras)
    text += "."
    summary = f"Coverage: {D.LEVELS[level - 1]} | Style: {style} | Add-ons: {len(extras)} | Colour: {primary}"
    if notes:
        summary += " | " + "; ".join(notes)
    return text, summary, dict(level=level, style=style, extras=extras, primary=primary)


class NoThingUnderwearRoulette:
    CATEGORY = "No_Thing"
    FUNCTION = "run"
    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("prompt", "underwear", "active")

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "bar_data": ("STRING", {"default": json.dumps(default_bar(), ensure_ascii=False)}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
            },
            "optional": {"prefix": ("STRING", {"forceInput": True}), "suffix": ("STRING", {"forceInput": True})},
        }

    @with_seed
    def run(self, bar_data, seed, prefix="", suffix=""):
        data = _parse(bar_data)
        sep = SEPS.get(data.get("sep"), "\n")
        join = lambda mid: sep.join(p.strip() for p in (prefix, mid, suffix) if p and p.strip())
        if data.get("enabled") is False:
            return (join(""), "", "Off")
        if data.get("random") is False:
            text = fixed(data)
            return (join(text), text, "Random off")
        opts = _on(data, "Options")
        text, summary, _ = roll(seed, _on(data, "Coverage"), _on(data, "Style"), _on(data, "Add-ons"), _on(data, "Add-on amount"), _on(data, "Colour"),
                                NO_BOTTOMS in opts, NO_TOPS in opts)
        return (join(text), text, summary)
