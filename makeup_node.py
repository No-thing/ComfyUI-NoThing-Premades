"""
No_Thing Makeup Roulette - rolls a random makeup look from the dataset in makeup_data.py.

Rows: Intensity (Natural ... Extreme), Look (8 families: Japanese & East Asian, American & Glam, Doll & Anime, Goth & Dark,
Punk & Grunge, Y2K & Retro-Futurism, Modest & Understated, Overdone & Hyper-Stylized), Add-ons (Lips, Cheeks, Eyes, Details),
Add-on amount, Colour. Nothing picked in a row = anything goes for that row.
Random OFF = no dice: the texts of the buttons you picked are joined. The `seed` decides the roll.
"""
import json
import re
import os
import random

from . import makeup_data as D
from .roulette_common import group, with_seed, scheme_pair, tier, PG_FACE_BLOCK

HERE = os.path.dirname(os.path.abspath(__file__))
SEPS = {"newline": "\n", "space": " ", "comma": ", "}


def _parse_entry(s):
    head, _, text = s.partition("|")
    lo, _, hi = head.partition("-")
    lo = int(lo)
    return lo, int(hi) if hi else lo, text.strip()


def _load_custom():
    """Optional makeup_custom.json: {"Goth & Dark": ["4|my look"], "extras": {"Lips": ["3|a plum lip"]}}"""
    try:
        with open(os.path.join(HERE, "makeup_custom.json"), encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def _lines(base, extra):
    return list(base) + [e for e in (extra if isinstance(extra, list) else []) if isinstance(e, str) and "|" in e]


def _build():
    custom = _load_custom()
    looks = {n: [_parse_entry(e) for e in _lines(es, custom.get(n))] for n, es in D.FAMILIES.items()}
    ex_c = custom.get("extras", {}) if isinstance(custom.get("extras", {}), dict) else {}
    extras = {n: [_parse_entry(e) for e in _lines(es, ex_c.get(n))] for n, es in D.EXTRAS.items()}
    return looks, extras


LOOKS, EXTRAS = _build()


def default_bar():
    lvl_texts = dict(zip(D.LEVELS, ["barely-there natural makeup", "soft pretty makeup", "polished glam makeup", "bold statement makeup", "extreme editorial makeup"]))
    amt_texts = {"None": "no extra details", "Few": "with one extra detail", "Some": "with a few extra details", "Loaded": "with lots of extra details"}
    add_texts = {"Lips": "lip colour and finish", "Cheeks": "blush, bronzer and highlight", "Eyes": "liner, shadow and lashes", "Details": "freckles, gems, glitter and face art"}
    return {"v": 1, "sep": "newline", "groups": [
        group("Intensity", D.LEVELS, lvl_texts),
        group("Look", D.STYLE_NAMES, {n: D.DESC[n] for n in D.STYLE_NAMES}),
        group("Add-ons", D.ADDON_NAMES, add_texts),
        group("Add-on amount", D.AMOUNTS, amt_texts),
        group("Colour", list(D.COLOURS), {k: "mainly " + v[0] for k, v in D.COLOURS.items()}),
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
    """Random off: the texts of the picked buttons."""
    parts = []
    for row in ("Look", "Intensity", "Add-ons", "Colour"):
        for g in data.get("groups", []):
            if g.get("name") == row:
                on = [str(b.get("text", "")).strip() for b in g.get("buttons", []) if b.get("on")]
                parts.append(" and ".join(t for t in on if t) if row in ("Look", "Add-ons") else ", ".join(t for t in on if t))
    parts = [p for p in parts if p]
    return ("makeup: " + ", ".join(parts) + ".") if parts else ""


_AREAS = {"lip": r"\blips?\b|lipstick|lip ?(gloss|oil|tint|liner)|lip-", "lid": r"\blids?\b|eyeshadow|eye shadow|shadow|eyeliner|\bliner\b|crease", "lash": r"lash|mascara",
          "brow": r"brow", "cheek": r"blush|cheek|contour", "glow": r"highlight|strobe|shimmer on the (cheek|nose)|glow", "skin": r"foundation|skin|base|complexion"}


def _areas(t):
    return {k for k, rx in _AREAS.items() if re.search(rx, t, re.I)}


def roll(seed, levels=(), looks=(), addons=(), amounts=(), colours=()):
    """Returns (text, summary, details)."""
    rng = random.Random(seed)
    lvl_idx = [D.LEVELS.index(l) + 1 for l in levels if l in D.LEVELS] or list(range(1, 6))
    sel = [s for s in looks if s in LOOKS]
    if not sel:                                                 # nothing picked: one or two families, not all eight
        sel = rng.sample(D.STYLE_NAMES, rng.choices([1, 2], [65, 35])[0])
    want = rng.choice(lvl_idx)
    level, pool, notes = want, [], []
    soft = tier() in (1, 2)                                     # Covered / Cute outfit: no sheer veils, plumped or overlined lips, seductive looks
    for strict in ((True, False) if soft else (False,)):
        for cand in sorted(range(1, 6), key=lambda x: (abs(x - want), x > want)):      # nothing at this level: nearest one (softer first)
            pool = [(s, t) for s in sel for lo, hi, t in LOOKS[s] if lo <= cand <= hi and not (strict and PG_FACE_BLOCK.search(t))]
            if pool:
                level = cand
                break
        if pool:
            break
    if level != want:
        notes.append(f"nothing at {D.LEVELS[want - 1]}, used {D.LEVELS[level - 1]}")
    family = rng.choice(sorted({s for s, _ in pool}, key=sel.index))
    main = rng.choice([t for s, t in pool if s == family])

    words = [w for c in colours if c in D.COLOURS for w in D.COLOURS[c]] if colours else list(D.PALETTE[family])
    primary = rng.choice(words)
    rest = [w for w in words if w != primary]
    accent = rng.choice(rest) if rest else primary
    if scheme_pair():
        primary, accent = scheme_pair()                       # the Bar's Style hands every part the same colours

    def fill(t):
        return t.replace("{c2}", accent).replace("{c}", primary)

    text = fill(main)
    if (colours or scheme_pair()) and "{c}" not in main:                           # a picked colour always shows up, even in looks with fixed colours
        text += f", with {primary} touches in the eyeshadow and liner"            # eyes only: a colour on the lips fought the look's own lip and made blotches
    n = rng.randint(*D.AMOUNT_RANGE[rng.choice([a for a in amounts if a in D.AMOUNT_RANGE] or D.AMOUNTS)])
    kinds = [g for g in addons if g in EXTRAS] or list(EXTRAS)
    rng.shuffle(kinds)
    extras = []
    for g in kinds:
        if len(extras) >= n:
            break
        opts = [t for lo, hi, t in EXTRAS[g] if lo <= level <= hi]
        if tier() in (1, 2):
            opts = [t for t in opts if not PG_FACE_BLOCK.search(t)]
        taken = _areas(text)                                                       # an add-on never repeats a part of the face the look already styles
        opts = [t for t in opts if not (_areas(t) & taken)]
        if opts:
            extras.append(fill(rng.choice(opts)))
            text += ", " + extras[-1]                                              # counted, so the next add-on cannot repeat it either
    text += "."
    summary = f"Intensity: {D.LEVELS[level - 1]} | Look: {family} | Add-ons: {len(extras)} | Colour: {primary}"
    if notes:
        summary += " | " + "; ".join(notes)
    return text, summary, dict(level=level, family=family, extras=extras, primary=primary)


class NoThingMakeupRoulette:
    CATEGORY = "No_Thing"
    FUNCTION = "run"
    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("prompt", "makeup", "active")

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
        text, summary, _ = roll(seed, _on(data, "Intensity"), _on(data, "Look"), _on(data, "Add-ons"), _on(data, "Add-on amount"), _on(data, "Colour"))
        return (join(text), text, summary)
