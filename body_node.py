"""
No_Thing Body Roulette - body type, bust, waist, hips, legs and height. Pick what you care about, everything left empty is rolled.
Random OFF = no dice: only what you picked is used. With random on, leave a row empty and it is chosen to fit the body type that was rolled (a Bimbo gets a tiny waist and a very large bust, an Athletic
body gets toned legs ...). Pick a row yourself and your choice wins. The `seed` decides the roll.
"""
import json
import os
import random

from . import body_data as D
from .roulette_common import tier, frame, shape, chosen, defaults_of, edited, group, join, parse, weighted, with_seed

HERE = os.path.dirname(os.path.abspath(__file__))


def _types():
    out = dict(D.TYPES)
    try:
        with open(os.path.join(HERE, "body_custom.json"), encoding="utf-8") as f:
            extra = json.load(f)
        for name, v in (extra.items() if isinstance(extra, dict) else []):
            if isinstance(v, dict) and isinstance(v.get("text"), str):
                p = v.get("pools") if isinstance(v.get("pools"), dict) else {}
                out[name] = (v["text"], v.get("tags", ""), {k: [x for x in p.get(k, []) if isinstance(x, str)] for k in ("bust", "waist", "hips", "legs", "height")})
    except (OSError, ValueError):
        pass
    return out


def _ov(data):
    dfl = defaults_of(default_bar())
    return {k: edited(data, k, dfl, D.LEGACY) for k in ("Body type", "Bust", "Waist", "Hips & butt", "Legs", "Height")}


def default_bar():
    types = _types()
    return {"v": 1, "sep": "newline", "groups": [
        group("Body type", list(types), {k: v[0] for k, v in types.items()}),
        group("Bust", list(D.BUST), D.BUST), group("Waist", list(D.WAIST), D.WAIST), group("Hips & butt", list(D.HIPS), D.HIPS),
        group("Legs", list(D.LEGS), D.LEGS), group("Height", list(D.HEIGHT), D.HEIGHT),
    ]}


PG_FRAMES = ["an extremely slim, petite frame", "a slender, delicate frame", "a delicate, narrow build", "a very slim, petite build",
             "a lean, slim figure", "a slim, graceful frame"]
PG_FRAMES_CUTE = PG_FRAMES + ["a slim, toned figure", "a slim, graceful figure"]


PG_HEIGHT = {"Short": "a short stature", "Average": "an average height", "Tall": "a tall stature", "Very tall": "a very tall stature"}


def pg_body(rng, data):
    """Covered / Cute outfits: a vague build and a height, nothing anatomical (no bust, stomach, waist, hips, butt or thigh words)."""
    frames = PG_FRAMES if tier() == 1 else PG_FRAMES_CUTE
    if shape():
        frames = D.PG_SHAPE_WORDS[shape() - 1]                 # the Shape dial still shapes the body in PG mode: waist, hips and curves, never breasts or cleavage
    hs = [x for x in chosen(data, "Height") if x in D.HEIGHT] or list(D.HEIGHT)
    h = rng.choice(hs)
    return f"with {rng.choice(frames)} and {PG_HEIGHT[h]}.", f"Body: PG ({'Covered' if tier() == 1 else 'Cute'}) | Height: {h}"


def roll(seed, data):
    rng = random.Random(seed)
    types = _types()
    vibes = chosen(data, "Vibe")
    sel = [t for t in chosen(data, "Body type") if t in types] or list(types)
    if shape():                                                # the Shape square decides the body type (your own Bust / Waist / Hips picks still win)
        nm, _desc, picks, custom, _pg = D.SHAPES[shape() - 1]
        if custom:
            t = nm
            types = dict(types)
            types[t] = custom
        else:
            t = rng.choice([x for x in picks if x in types] or sel)
    else:
        t = weighted(rng, sel, vibes, lambda k: types[k][1].split())
    text, _, pools = types[t]
    ov = _ov(data)
    text = ov["Body type"].get(t, text)

    def part(row, table, key):
        mine = [x for x in chosen(data, row) if x in table]
        opts = mine or [x for x in pools.get(key, []) if x in table] or list(table)
        return rng.choice(opts)

    bust, waist, hips, legs = part("Bust", D.BUST, "bust"), part("Waist", D.WAIST, "waist"), part("Hips & butt", D.HIPS, "hips"), part("Legs", D.LEGS, "legs")
    height = part("Height", D.HEIGHT, "height")
    toned = (not shape()) or tier() <= 3                       # dial on "any", or the outfit is still mostly covered: a voluptuous hourglass build, no breast / cleavage detail
    picked = lambda row, table: any(x in table for x in chosen(data, row))
    waist_t = ov["Waist"].get(waist) or (D.TONED_WAIST.get(waist) if toned and not picked("Waist", D.WAIST) else None) or D.WAIST[waist]
    hips_t = ov["Hips & butt"].get(hips) or (D.TONED_HIPS.get(hips) if toned and not picked("Hips & butt", D.HIPS) else None) or D.HIPS[hips]
    legs_t = ov["Legs"].get(legs) or (D.TONED_LEGS.get(legs) if toned and not picked("Legs", D.LEGS) else None) or D.LEGS[legs]
    height_t = ov["Height"].get(height, D.HEIGHT[height])
    skip_bust = toned and not picked("Bust", D.BUST) and not ov["Bust"].get(bust)
    bust_t = None if skip_bust else ov["Bust"].get(bust, D.BUST[bust])
    if toned and t not in ov["Body type"]:
        text = D.TONED_TYPES.get(t, text)
    if frame() == 3:                                           # top only: nothing below the waist is mentioned
        parts = [x for x in (bust_t, waist_t, height_t) if x]
        return "with " + ", ".join(parts[:-1]) + (", and " if len(parts) > 1 else "") + parts[-1] + ".", f"Body: {t} | Bust: {bust} | Waist: {waist} | Height: {height} | framing: top only"
    if frame() == 4:                                           # bottoms only: hips, butt, legs
        return f"with {hips_t}, {legs_t}, and {height_t}.", f"Body: {t} | Hips: {hips} | Legs: {legs} | Height: {height} | framing: bottoms only"
    covers = toned and t in ("Bimbo", "Slim stack", "Bottom heavy") and t not in ov["Body type"]      # the toned text already names waist and hips
    parts = [x for x in (text, bust_t, None if covers and not picked("Waist", D.WAIST) else waist_t,
                         None if covers and not picked("Hips & butt", D.HIPS) else hips_t, legs_t) if x]
    out = "with " + ", ".join(parts) + f", and {height_t}."
    summary = f"Body: {t} | Bust: {bust} | Waist: {waist} | Hips: {hips} | Legs: {legs} | Height: {height}"
    return out, summary


def fixed(data):
    """Random off: exactly what is picked (first pick per row), nothing is rolled."""
    types = _types()
    ov = _ov(data)
    first = lambda row, table: next((x for x in chosen(data, row) if x in table), None)
    parts = []
    t = first("Body type", types)
    if t:
        parts.append(ov["Body type"].get(t, types[t][0]))
    for row, table in (("Bust", D.BUST), ("Waist", D.WAIST), ("Hips & butt", D.HIPS), ("Legs", D.LEGS), ("Height", D.HEIGHT)):
        x = first(row, table)
        if x:
            parts.append(ov[row].get(x, table[x]))
    return ("with " + ", ".join(parts) + ".") if parts else ""


class NoThingBodyRoulette:
    CATEGORY = "No_Thing"
    FUNCTION = "run"
    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("prompt", "body", "active")

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
        data = parse(bar_data)
        if data.get("enabled") is False:
            return (join(data, prefix, "", suffix), "", "Off")
        if data.get("random") is False:                           # dice off: only what is picked
            text = fixed(data)
            return (join(data, prefix, text, suffix), text, "Random off")
        text, summary = roll(seed, data)
        return (join(data, prefix, text, suffix), text, summary)
