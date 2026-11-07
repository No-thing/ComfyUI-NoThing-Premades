"""
No_Thing Head Roulette - face shape, eyes, lips and hair. Pick what you care about, everything left empty is rolled at random.
Random OFF = no dice: the first button you picked in each row is used, rows with nothing picked are left out.
The `seed` decides the roll: same seed = same face, "randomize" = a new one every run.
"""
import json
import os
import random
import re

from . import head_data as D
from .roulette_common import cover, tier, PG_FACE_BLOCK, chosen, defaults_of, edited, group, join, parse, weighted, with_seed

HERE = os.path.dirname(os.path.abspath(__file__))


def _custom():
    """Optional head_custom.json: {"hair": ["3-6|cute|Buns & braids|{c} {len} hair in a side braid"], "face": {"Name": ["text", "tags"]}}"""
    p = os.path.join(HERE, "head_custom.json")
    try:
        with open(p, encoding="utf-8") as f:
            d = json.load(f)
        return d if isinstance(d, dict) else {}
    except (OSError, ValueError):
        return {}


def _styles():
    out = []
    for line in D.STYLES + [x for x in _custom().get("hair", []) if isinstance(x, str) and x.count("|") >= 3]:
        head, tags, cat, text = line.split("|", 3)
        lo, _, hi = head.partition("-")
        out.append((int(lo), int(hi or lo), tags.split(), cat.strip(), text.strip()))
    return out


def _ov(data):
    dfl = defaults_of(default_bar())
    legacy = {", ".join(v[:3]) for v in D.HAIR_COLOURS.values()}          # earlier versions showed the first three colour words
    return {k: edited(data, k, dfl, legacy) for k in ("Face", "Eye shape", "Eye size", "Eye colour", "Lip shape", "Lip size", "Hair length", "Hair colour")}


def face_groups():
    return [
        group("Face", list(D.FACES), {k: v[0] for k, v in D.FACES.items()}),
        group("Eye shape", list(D.EYE_SHAPES), {k: f"{v[0]} eyes {v[1]}" for k, v in D.EYE_SHAPES.items()}),
        group("Eye size", list(D.EYE_SIZES), D.EYE_SIZES),
        group("Eye colour", list(D.EYE_COLOURS), D.EYE_COLOURS),
        group("Lip shape", list(D.LIP_SHAPES), {k: f"{v[0]} lips {v[1]}" for k, v in D.LIP_SHAPES.items()}),
        group("Lip size", list(D.LIP_SIZES), D.LIP_SIZES),
    ]


def hair_groups():
    return [
        group("Hair length", D.LENGTHS, dict(zip(D.LENGTHS, D.LENGTH_WORD))),
        group("Hairstyle", D.STYLE_CATS, {c: "Random style from this group." for c in D.STYLE_CATS}, locked=True),
        group("Hair colour", list(D.HAIR_COLOURS), {k: ", ".join(v) for k, v in D.HAIR_COLOURS.items()}),
    ]


def default_bar(which="head"):
    g = (face_groups() if which in ("head", "face") else []) + (hair_groups() if which in ("head", "hair") else [])
    return {"v": 1, "sep": "newline", "groups": g}


def _face_roll(rng, data, ov, vibes):
    pick = lambda name, table, tagi: (lambda sel: weighted(rng, sel or list(table), vibes, lambda k: table[k][tagi].split() if tagi is not None else []))([x for x in chosen(data, name) if x in table])
    soft = tier() in (1, 2)                                   # Covered / Cute outfit: no seductive eyes, no plump or pouty lips
    eye_shapes = {k: v for k, v in D.EYE_SHAPES.items() if not (soft and PG_FACE_BLOCK.search(k + " " + v[0] + " " + v[1]))} or D.EYE_SHAPES
    lip_shapes = {k: v for k, v in D.LIP_SHAPES.items() if not (soft and (k == "Pouty" or PG_FACE_BLOCK.search(k + " " + v[0] + " " + v[1])))} or D.LIP_SHAPES
    lip_sizes = {k: v for k, v in D.LIP_SIZES.items() if not (soft and PG_FACE_BLOCK.search(k + " " + v))} or D.LIP_SIZES
    face = pick("Face", D.FACES, 1)
    shape = pick("Eye shape", eye_shapes, 2)
    esize = rng.choice([x for x in chosen(data, "Eye size") if x in D.EYE_SIZES] or list(D.EYE_SIZES))
    ecol = rng.choice([x for x in chosen(data, "Eye colour") if x in D.EYE_COLOURS] or list(D.EYE_COLOURS))
    lshape = pick("Lip shape", lip_shapes, 2)
    lsize = rng.choice([x for x in chosen(data, "Lip size") if x in lip_sizes] or list(lip_sizes))
    eye_phrase = ov["Eye shape"].get(shape) or f"{D.EYE_SHAPES[shape][0]} eyes {D.EYE_SHAPES[shape][1]}"
    lip_phrase = ov["Lip shape"].get(lshape) or f"{D.LIP_SHAPES[lshape][0]} lips {D.LIP_SHAPES[lshape][1]}"
    eyes = f"{ov['Eye size'].get(esize, D.EYE_SIZES[esize])} {eye_phrase}, {ov['Eye colour'].get(ecol, D.EYE_COLOURS[ecol])} irises"
    lips = f"{ov['Lip size'].get(lsize, D.LIP_SIZES[lsize])} {lip_phrase}"
    text = f"{ov['Face'].get(face, D.FACES[face][0])}, {eyes}, {lips}"
    if cover() == "eyes":                                     # a mask on the eyes: face shape and lips only, the mask is the focus
        text = f"{ov['Face'].get(face, D.FACES[face][0])}, {lips}"
    return text, f"Face: {face} | Eyes: {shape}, {esize}, {ecol} | Lips: {lshape}, {lsize}"


BRAID_BOOST = 2                                                       # extra copies of every braid style in the pool (0 = no boost)


def _hair_roll(rng, data, ov, vibes):
    lens = [D.LENGTHS.index(x) + 1 for x in chosen(data, "Hair length") if x in D.LENGTHS] or list(range(1, 7))
    cats = [c for c in chosen(data, "Hairstyle") if c in D.STYLE_CATS]
    styles = _styles()
    length = rng.choice(lens)
    fits = lambda s, L: s[0] <= L <= s[1]
    in_cat = [s for s in styles if not cats or s[3] in cats]
    cand = [s for s in in_cat if fits(s, length)]
    if not cand:                                               # nothing in those hairstyle groups at this length: keep the groups, change the length
        ok = [L for L in lens if any(fits(s, L) for s in in_cat)] or [L for L in range(1, 7) if any(fits(s, L) for s in in_cat)]
        if ok:
            length = rng.choice(ok)
            cand = [s for s in in_cat if fits(s, length)]
        else:
            cand = [s for s in styles if fits(s, length)]
    cand = cand + [s for s in cand if "braid" in s[4].lower()] * BRAID_BOOST           # braids are the favourite: they come up about 3x as often as their share of the list
    style = weighted(rng, cand, vibes, lambda s: s[2])
    cols = [c for c in chosen(data, "Hair colour") if c in D.HAIR_COLOURS] or list(D.HAIR_COLOURS)
    fam = rng.choice(cols)
    words = [w.strip() for w in ov["Hair colour"].get(fam, "").split(",") if w.strip()] or D.HAIR_COLOURS[fam]
    colour = rng.choice(words)
    lword = ov["Hair length"].get(D.LENGTHS[length - 1], D.LENGTH_WORD[length - 1])
    hair = style[4].replace("{c}", colour).replace("{len}", lword)
    return hair, f"Hair: {D.LENGTHS[length - 1]}, {style[3]}, {colour}"


def roll(seed, data, which="head"):
    rng = random.Random(seed)
    vibes = chosen(data, "Vibe")
    ov = _ov(data)
    parts, notes = [], []
    if which in ("head", "face"):
        t, s = _face_roll(rng, data, ov, vibes)
        parts.append(t); notes.append(s)
    if which in ("head", "hair"):
        t, s = _hair_roll(rng, data, ov, vibes)
        parts.append(t); notes.append(s)
    text = "with " + (", and ".join([", ".join(parts[:-1]), parts[-1]]) if len(parts) > 1 and which == "head" else parts[0]) + "."
    summary = " | ".join(notes)
    if vibes:
        summary = "Vibe: " + "/".join(vibes) + " | " + summary
    return text, summary


def fixed(data, which="head"):
    """Random off: build the phrase from exactly what is picked (first pick per row), nothing is rolled."""
    ov = _ov(data)
    first = lambda row, table: next((x for x in chosen(data, row) if x in table), None)
    parts = []
    face = first("Face", D.FACES) if which != "hair" else None
    if face:
        parts.append(ov["Face"].get(face, D.FACES[face][0]))
    f = which != "hair"
    shape, esize, ecol = (first("Eye shape", D.EYE_SHAPES), first("Eye size", D.EYE_SIZES), first("Eye colour", D.EYE_COLOURS)) if f else (None, None, None)
    if shape or esize:
        phrase = (ov["Eye shape"].get(shape) or f"{D.EYE_SHAPES[shape][0]} eyes {D.EYE_SHAPES[shape][1]}") if shape else "eyes"
        sz = ov["Eye size"].get(esize, D.EYE_SIZES[esize]) if esize else ""
        parts.append(f"{sz} {phrase}".strip())
    if ecol:
        parts.append(f"{ov['Eye colour'].get(ecol, D.EYE_COLOURS[ecol])} irises")
    lshape, lsize = (first("Lip shape", D.LIP_SHAPES), first("Lip size", D.LIP_SIZES)) if f else (None, None)
    if lshape or lsize:
        phrase = (ov["Lip shape"].get(lshape) or f"{D.LIP_SHAPES[lshape][0]} lips {D.LIP_SHAPES[lshape][1]}") if lshape else "lips"
        sz = ov["Lip size"].get(lsize, D.LIP_SIZES[lsize]) if lsize else ""
        parts.append(f"{sz} {phrase}".strip())
    h_on = which != "face"
    length = first("Hair length", D.LENGTHS) if h_on else None
    cat = next((c for c in chosen(data, "Hairstyle") if c in D.STYLE_CATS), None) if h_on else None
    fam = first("Hair colour", D.HAIR_COLOURS) if h_on else None
    colour = ""
    if fam:
        words = [w.strip() for w in ov["Hair colour"].get(fam, "").split(",") if w.strip()] or D.HAIR_COLOURS[fam]
        colour = words[0]
    lword = ov["Hair length"].get(length, D.LENGTH_WORD[D.LENGTHS.index(length)]) if length else ""
    if cat:
        L = D.LENGTHS.index(length) + 1 if length else None
        st = [s for s in _styles() if s[3] == cat and (L is None or s[0] <= L <= s[1])] or [s for s in _styles() if s[3] == cat]
        text = st[0][4]
        for ph, val in (("{c} ", colour + " " if colour else ""), ("{c}", colour), ("{len} ", lword + " " if lword else ""), ("{len}", lword)):
            text = text.replace(ph, val)
        parts.append(re.sub(r"\s+", " ", text).strip())
    elif colour or lword:
        parts.append(re.sub(r"\s+", " ", f"{colour} {lword} hair").strip())
    return ("with " + ", ".join(parts) + ".") if parts else ""


class NoThingHeadRoulette:
    """The first, combined node. Kept so saved workflows still load; new ones should use Face + Hair."""
    CATEGORY = "No_Thing"
    FUNCTION = "run"
    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("prompt", "head", "active")
    WHICH = "head"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "bar_data": ("STRING", {"default": json.dumps(default_bar(cls.WHICH), ensure_ascii=False)}),
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
            text = fixed(data, self.WHICH)
            return (join(data, prefix, text, suffix), text, "Random off")
        text, summary = roll(seed, data, self.WHICH)
        return (join(data, prefix, text, suffix), text, summary)


class NoThingFaceRoulette(NoThingHeadRoulette):
    """Face shape, eyes and lips only (no hair)."""
    RETURN_NAMES = ("prompt", "face", "active")
    WHICH = "face"


class NoThingHairRoulette(NoThingHeadRoulette):
    """Hair length, hairstyle and colour only (no face)."""
    RETURN_NAMES = ("prompt", "hair", "active")
    WHICH = "hair"
