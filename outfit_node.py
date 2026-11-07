"""
No_Thing Outfit Roulette - pick how skimpy, how many accessories and which styles; the node rolls a
random outfit from the dataset in outfit_data.py. Nothing picked in a row = anything goes for that row.

The buttons live in one hidden JSON field (same bar engine as the Prompt Bar). Only the button NAMES
matter here, the node looks them up in the dataset. The `seed` decides the roll: same seed = same outfit,
"randomize" (the default) = a new outfit every run.
"""
import json
import re
import os
import random

from . import outfit_data as D
from . import framing as FR
from .roulette_common import hair_on, need_mask, cover_of, pg_ok, PG_STYLES_OFF, group, with_seed, scheme_pair

HERE = os.path.dirname(os.path.abspath(__file__))
SEPS = {"newline": "\n", "space": " ", "comma": ", "}
ONE_STYLE = "One style per outfit"
NO_SHOES = "No shoes"
NO_OUTER = "No jackets"
_OUTER_WORDS = re.compile(r"\b(jackets?|coats?|puffers?|bombers?|parkas?|blazers?|windbreakers?|anoraks?|cardigans?|capes?|vests?|robes?|shrugs?)\b", re.I)
MIXED = "Mixed brands"
NO_BOTTOMS, NO_TOPS = FR.NO_BOTTOMS, FR.NO_TOPS
OPTION_TEXTS = {
    ONE_STYLE: "Off = pieces from your selected styles are mixed. On = the whole outfit stays in one style.",
    MIXED: "Off = a brand style (Nike, Chanel...) sticks to ONE brand per roll, picked by the seed. On = pieces from every brand in the style are mixed.",
    NO_OUTER: "On = no jackets, coats or puffers anywhere in the prompt (cropped bombers, leather jackets, puffers...), so the outfit stays easy to isolate.",
    NO_SHOES: "Off = shoes, boots and heels appear as the style rolls them. On = no shoes, socks, ankle pieces or feet anywhere in the prompt.",
    NO_BOTTOMS: "For torso crops: On = nothing below the waist is mentioned (no skirts, trousers, tights, shoes, thigh or ankle pieces), so the model does not pull back to show them.",
    NO_TOPS: "For lower-body crops: On = nothing above the waist is mentioned (no tops, jackets, dresses, necklaces, earrings, hats), only skirts, trousers, legwear and shoes.",
}
SHOE_WORDS = re.compile(r"\b(boots?|shoes?|heels?|stilettos?|pumps?|sneakers?|sandals?|mules?|loafers?|oxfords?|flats|high-tops|creepers?|rollerblades|stay-ups|mary[- ]janes?|platforms?|ankles?|anklets?|foot|feet|toes?|barefoot|socks?|leg ?warmers?)\b", re.I)


# ---------------------------------------------------------------- dataset
def _parse_entry(s):
    head, _, text = s.partition("|")
    lo, _, hi = head.partition("-")
    lo = int(lo)
    return lo, int(hi) if hi else lo, text.strip()


def _load_custom():
    """Optional outfit_custom.json: {"Goth": {"top": ["3|my line"], "acc": {"neck": ["a bat choker"]}}}"""
    path = os.path.join(HERE, "outfit_custom.json")
    if not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def _build_db():
    custom = _load_custom()
    db = {}
    for name, st in D.STYLES.items():
        extra = custom.get(name, {}) if isinstance(custom.get(name, {}), dict) else {}
        slots = {}
        for slot in D.SLOT_ORDER:
            entries = list(st.get(slot, [])) + [e for e in extra.get(slot, []) if isinstance(e, str) and "|" in e]
            slots[slot] = [_parse_entry(e) for e in entries]
        for slot, entries2 in D.STYLE_SKIMPY.get(name, {}).items():             # Skimpy / Micro pieces written for this style
            slots[slot] += [_parse_entry(e) for e in entries2]
        acc = {k: list(v) for k, v in st.get("acc", {}).items()}
        for k, v in D.STYLE_ACC_EXTRA.get(name, {}).items():
            acc.setdefault(k, []).extend(x for x in v if x not in acc.get(k, []))
        if name == "Beach":
            for k, v in D.BEACH_EXTRA.items():
                acc.setdefault(k, []).extend(x for x in v if x not in acc.get(k, []))
        for k, v in (extra.get("acc") or {}).items():
            acc.setdefault(k, []).extend(x for x in v if isinstance(x, str))
        db[name] = dict(slots=slots, acc=acc, palette=list(st["palette"]), desc=st["desc"])
    return db


DB = _build_db()


def default_bar():
    lvl_texts = dict(zip(D.LEVELS, [
        "fully dressed in everyday clothes", "cute and playful with a little skin showing", "low-cut with thigh slits and sheer panels",
        "micro skirts, crop tops, cut-outs and sheer panels", "minimal-fabric strap and cut-out outfits"]))
    amt_texts = {"None": "no accessories", "Few": "with a couple of accessories", "Some": "with a few accessories", "Loaded": "loaded with accessories"}
    style_texts = {n: DB[n]["desc"] for n in D.STYLE_NAMES}                    # note: Preppy Uniform only exists at Covered / Cute when rolling
    col_texts = {k: "mainly " + v[0] for k, v in D.COLOURS.items()}
    return {"v": 1, "sep": "newline", "groups": [
        group("Skimpy", D.LEVELS, lvl_texts),
        group("Style", D.STYLE_NAMES, style_texts),
        group("Accessories", D.AMOUNTS, amt_texts),
        group("Colour", list(D.COLOURS), col_texts),
        group("Options", [ONE_STYLE, MIXED, NO_SHOES, NO_BOTTOMS, NO_TOPS, NO_OUTER], OPTION_TEXTS, locked=True),
    ]}


def fixed(data):
    """Random off: no dice. The texts of the buttons you picked are joined, e.g. 'wearing dark gothic clothes, low-cut with thigh slits, mainly black'."""
    parts = []
    for row in ("Style", "Skimpy", "Colour", "Accessories"):
        for g in data.get("groups", []):
            if g.get("name") == row:
                on = [str(b.get("text", "")).strip() for b in g.get("buttons", []) if b.get("on")]
                parts.append(" and ".join(t for t in on if t) if row == "Style" else ", ".join(t for t in on if t))
    parts = [p for p in parts if p]
    return ("wearing " + ", ".join(parts) + ".") if parts else ""


def _on(data, group_name):
    for g in data.get("groups", []):
        if g.get("name") == group_name:
            return [b.get("label", "") for b in g.get("buttons", []) if b.get("on")]
    return []


def _parse(raw):
    try:
        data = json.loads(raw)
        if isinstance(data, dict) and isinstance(data.get("groups"), list):
            return data
    except (TypeError, ValueError):
        pass
    return {"sep": "newline", "groups": []}


# ---------------------------------------------------------------- the roll
def _has_set(style, level):
    s = DB[style]["slots"]
    has = lambda sl: any(lo <= level <= hi and pg_ok(t, level) for lo, hi, t in s[sl])
    return has("one") or (has("top") and has("bottom"))


_GENERIC = {k: [_parse_entry(e) for e in v] for k, v in D.GENERIC_SKIMPY.items()}


def _eligible(style, slot, level):
    if slot in ("one", "top", "bottom") and style not in D.PG_NO_GENERIC and not _has_set(style, level):   # the style has nothing at this level: borrow the generic cut
        g = [t for lo, hi, t in _GENERIC[slot] if lo <= level <= hi]
        if g:
            return g
    return [t for lo, hi, t in DB[style]["slots"][slot] if lo <= level <= hi and pg_ok(t, level)]


def _nosho(options):
    """Entries without footwear; a footwear phrase inside a longer entry ('dress with combat boots') is cut off."""
    out = []
    for t in options:
        if SHOE_WORDS.search(t):
            t2 = re.sub(r"\s+(with|and|over)\s+[^,]*?" + SHOE_WORDS.pattern + r"[^,]*", "", t, flags=re.I)
            if SHOE_WORDS.search(t2):
                continue
            t = t2
        out.append(t)
    return out


# Brand styles: each roll sticks to ONE brand (picked from the seed) so the outfit does not turn into logo soup.
# "pick" = brands the seed chooses between; "also" = other brands that clash with the pick, so they are filtered out too.
BRANDS = {
    "Streetwear Brands": dict(pick=["Supreme", "Stussy", "Off-White", "Palace", "BAPE", "Carhartt", "Fear of God"], also=["Nike", "Adidas", "Air Jordan", "New Balance", "Timberland", "North Face", "G-Shock"]),
    "Athleisure Brands": dict(pick=["Nike", "Adidas", "Lululemon", "Gymshark", "Alo Yoga", "Puma", "Fila", "Champion"], also=["New Balance"]),
    "Luxury Houses": dict(pick=["Chanel", "Dior", "Gucci", "Versace", "Prada", "Saint Laurent", "Balenciaga", "Burberry", "Miu Miu"], also=[]),
    "High Street Trend": dict(pick=["Zara", "H&M", "Shein", "Fashion Nova", "Princess Polly", "Brandy Melville", "Urban Outfitters", "Pretty Little Thing", "Free People"], also=[]),
    "Alt Brands": dict(pick=["Dolls Kill", "Killstar", "Disturbia", "Demonia", "Hot Topic", "Current Mood", "Punk Rave"], also=[]),
    "Heritage Brands": dict(pick=["Levi's", "Wrangler", "Carhartt", "Ralph Lauren", "Tommy Hilfiger", "Lacoste", "Fred Perry", "Dickies"], also=[]),
    "Boxing & Gym Brands": dict(pick=["Lonsdale", "Everlast", "Gymshark", "Venum"], also=["Hayabusa", "Title Boxing"]),
    "Y2K Brands": dict(pick=["Juicy", "Baby Phat", "Von Dutch", "Ed Hardy", "Bebe", "Sean John"], also=[]),
}
_BRAND_RE = {n: re.compile("|".join(re.escape(b) for b in sorted(v["pick"] + v["also"], key=len, reverse=True)), re.I) for n, v in BRANDS.items()}


def _brand_filter(style, brand, options, fallback=False):
    """Keep entries of the chosen brand and entries with no brand at all. fallback=True (shoes): nothing left = keep every brand."""
    if not brand or style not in BRANDS:
        return options
    keep = []
    for t in options:
        found = {m.group(0).lower() for m in _BRAND_RE[style].finditer(t)}
        if not found or brand.lower() in found:
            keep.append(t)
    return keep or (options if fallback else [])


def roll(seed, levels=(), styles=(), amounts=(), colours=(), one_style=False, no_shoes=False, no_bottoms=False, no_tops=False, mixed_brands=False, no_outer=False):
    """Returns (outfit_text, summary_text, details_dict)."""
    rng = random.Random(seed)
    brand_of = {}                                                       # own random stream: rolls of non-brand styles stay exactly as before

    def brand(style):
        if mixed_brands or style not in BRANDS:
            return None
        if style not in brand_of:
            r = random.Random(f"{seed}:{style}")
            picks = list(BRANDS[style]["pick"])
            good = [b for b in picks if viable(style, b)] or picks         # only brands that can dress a whole outfit in the chosen skimpy range
            brand_of[style] = r.choice(good)
        return brand_of[style]

    def elig(style, slot, level):
        return _brand_filter(style, brand(style), elig0(style, slot, level), fallback=(slot in ("feet", "one", "top", "bottom")))        # no piece of the chosen brand at this level: another brand beats a different style

    def viable(style, b):
        for lv in lvl_idx:
            has = [bool(_brand_filter(style, b, elig0(style, sl, lv))) for sl in ("one", "top", "bottom")]
            if ok(has[0], has[1], has[2]):
                return True
        return False

    def elig0(style, slot, level):
        if no_shoes and slot == "feet":
            return []
        if no_outer and slot == "outer":
            return []
        if no_bottoms and slot in ("bottom", "legs", "feet"):              # torso crop: nothing below the waist is mentioned
            return []
        if no_tops and slot in ("top", "outer", "one", "head"):            # lower-body crop: nothing above the waist
            return []
        opts = _nosho(_eligible(style, slot, level)) if no_shoes else _eligible(style, slot, level)
        if no_outer and slot in ("top", "one"):                              # a jacket worn over a bra top: gone
            opts = [t for t in opts if not _OUTER_WORDS.search(t)]
        if no_tops and slot in ("bottom", "legs"):                          # 'leggings under an oversized top' -> 'leggings'
            opts = [v for v in (FR.lower_only(t) for t in opts) if v]
        if no_bottoms and slot in ("top", "outer", "one"):                 # 'crop top with a tiny skirt' -> 'crop top'; a mini dress is dropped
            opts = [v for v in (FR.visible_text(t, no_bottoms=True) for t in opts) if v]
        return opts
    lvl_idx = [D.LEVELS.index(l) + 1 for l in levels if l in D.LEVELS] or list(range(1, 6))
    sel = [s for s in styles if s in DB] or list(D.STYLE_NAMES)
    off = PG_STYLES_OFF.get(max(lvl_idx), set()) if len(lvl_idx) == 1 else set()      # Covered only: no bondage / latex styles
    sel = [s for s in sel if s not in off] or sel
    free_styles = not [s for s in styles if s in DB]
    level = rng.choice(lvl_idx)
    if free_styles and not one_style:                          # nothing picked: a random handful of styles, not all twelve
        pool = rng.sample([x for x in sel if x != "Cosplay"] or sel, rng.choices([1, 2, 3], [50, 35, 15])[0])
    else:
        pool = [rng.choice(sel)] if one_style else list(sel)
    if level >= 3:                                                      # Revealing and up: no childlike styles (Sanrio, Kigurumi, Doll, Harajuku, school uniform)
        pool = [x for x in pool if x not in D.CHILDLIKE_STYLES] or [rng.choice([x for x in D.STYLE_NAMES if x not in D.CHILDLIKE_STYLES])]
    if "Cosplay" in pool:                                              # a cosplay look is one fixed character: never mixed with other styles
        pool = ["Cosplay"]
    notes = []

    def parts_at(lv, pl):
        return ([s for s in pl if elig(s, "one", lv)],
                [s for s in pl if elig(s, "top", lv)],
                [s for s in pl if elig(s, "bottom", lv)])

    def ok(o, t, b):
        if no_tops and no_bottoms:
            return True
        if no_tops:
            return bool(b)
        if no_bottoms:
            return bool(o or t)
        return bool(o or (t and b))

    def find(pl):
        for cand in sorted(range(1, 6), key=lambda x: (abs(x - level), x > level)):   # nothing at this level: nearest one (less skimpy first)
            o, t, b = parts_at(cand, pl)
            if ok(o, t, b):
                return cand, o, t, b
        return None

    found = None
    if len(lvl_idx) == 1 and level <= 2:                       # Covered / Cute only: never creep up a level; switch to a style that has something at this level
        for pl in (pool, [x for x in D.STYLE_NAMES if x not in PG_STYLES_OFF.get(level, set())]):
            o, t, b = parts_at(level, pl)
            if ok(o, t, b):
                found = (level, o, t, b)
                if pl is not pool:
                    notes.append(f"{'/'.join(pool)} has nothing at {D.LEVELS[level - 1]}, used any style")
                    pool = pl
                break
    if found is None:
        found = find(pool)
    if found is None and pool != list(D.STYLE_NAMES):                 # the picked styles have nothing for this framing: any style will do
        notes.append(f"{'/'.join(pool)} has nothing for this framing, used any style")
        pool = list(D.STYLE_NAMES)
        found = find(pool)
    lv, ones, tops, bots = found if found else (level, [], [], [])
    if lv != level and found:
        notes.append(f"{'/'.join(pool)} has nothing at {D.LEVELS[level - 1]}, used {D.LEVELS[lv - 1]}")
    level = lv
    use_one = bool(ones) and not no_tops and (not (tops and (bots or no_bottoms)) or rng.random() < 0.4)

    # colours
    if colours:
        words = [w for c in colours if c in D.COLOURS for w in D.COLOURS[c]]
    else:
        words = [w for s in pool for w in DB[s]["palette"]]
    primary = rng.choice(words)
    rest = [w for w in words if w != primary]
    accent = rng.choice(rest) if rest else primary
    if scheme_pair():
        primary, accent = scheme_pair()                       # the Bar's Style hands every part the same colours

    def fill(text, main=True):
        c = primary if (main or rng.random() < 0.5) else accent
        return text.replace("{c}", c).replace("{c2}", accent)

    picked = {}
    if use_one:
        picked["one"] = fill(rng.choice(elig(rng.choice(ones), "one", level)))
    else:
        if tops and not no_tops:
            picked["top"] = fill(rng.choice(elig(rng.choice(tops), "top", level)))
        if bots and not no_bottoms:
            picked["bottom"] = fill(rng.choice(elig(rng.choice(bots), "bottom", level)))
    chance = {"outer": [.55, .4, .3, .25, 0][level - 1], "legs": .6, "feet": .85, "head": .3 if level < 5 else 0}
    for s_ in pool:
        chance["head"] = max(chance["head"], D.HEAD_CHANCE.get(s_, 0))        # a beach style almost always has the big sun hat
    if level >= 5:
        chance["head"] = 0.5 if any(x in D.HEAD_OK_AT_MICRO for x in pool) else 0
        if any(x in D.LATEX_OUTER_AT_MICRO for x in pool):
            chance["outer"] = 0.45                                       # a latex robe over the latex is part of the look even at Micro           # Micro: no hats, even for beach styles (sporty keeps caps and headbands)
    if any(x in D.JACKET_FIRST for x in pool):
        chance["outer"] = 1.0                                            # jacket season: the jacket is always there
    for slot in ("outer", "legs", "feet", "head"):
        cands = [s for s in pool if elig(s, slot, level)]
        if cands and rng.random() < chance[slot]:
            picked[slot] = fill(rng.choice(elig(rng.choice(cands), slot, level)), main=False)

    # accessories
    amount = rng.choice([a for a in amounts if a in D.AMOUNT_RANGE] or D.AMOUNTS)
    n = rng.randint(*D.AMOUNT_RANGE[amount])
    if pool == ["Cosplay"]:
        n = 0                                                           # the character brings their own props
    skimpy = level >= 4
    if skimpy:
        n = min(n, D.MICRO_ACC_MAX[level])                                    # Skimpy / Micro: a few pieces, not a costume
    allowed = set(D.MICRO_SLOTS) | {x for s_ in pool for x in D.STYLE_MICRO_SLOTS.get(s_, ())}
    slots = [x for x in D.ACC_SLOT_ORDER if (x != "hair" or "head" not in picked) and (not skimpy or x in allowed) and not (no_bottoms and x == "ankle") and not (no_tops and x in ("neck", "ears", "face", "hair"))]
    rng.shuffle(slots)
    acc = []
    for slot in slots:
        if len(acc) >= n:
            break
        opts = [a for s in pool for a in _brand_filter(s, brand(s), DB[s]["acc"].get(slot, []))]
        if level <= 2:
            opts = [a for a in opts if pg_ok(a, level)]
        if hair_on() and slot == "hair":                                       # the Bar's hair part owns the hairstyle: only real accessories (flower, clip, bow ...)
            opts = [a for a in opts if re.search(D.HAIR_ACC_OK, a, re.I)]
        if skimpy and slot == "face":
            opts = [a for a in opts if re.search("sunglasses", a, re.I)]
        if skimpy and slot == "extra":
            opts = [a for a in opts if re.search(D.MICRO_EXTRA_OK, a, re.I)]
            opts = [a for a in opts if re.search("volleyball|drink|cocktail|towel", a, re.I)] or opts                 # beach: the volleyball is the prop
        if skimpy and slot == "ears":
            opts = opts + D.MICRO_PIERCINGS
        if D.GENERIC_ACC.get(slot) and not pool == ["Baggy Comfy"] and (not opts or rng.random() < 0.2):      # baggy comfy keeps to its own soft accessories
            opts = opts + [a for a in D.GENERIC_ACC[slot] if level > 2 or pg_ok(a, level)]
        if no_shoes:
            opts = [o for o in opts if not SHOE_WORDS.search(o)]
        if no_bottoms:
            opts = [o for o in opts if not FR.LOW.search(o)]
        if no_tops:
            opts = [o for o in opts if not FR.TOP.search(o)]
        if opts:
            acc.append(rng.choice(opts))

    if "Beach" in pool and not no_tops:                                         # a beach look always has sunglasses and a prop (volleyball, drink or towel)
        b_acc = DB["Beach"]["acc"]
        if not any("sunglasses" in a for a in acc):
            acc.append(rng.choice([a for a in b_acc.get("face", []) if "sunglasses" in a]))
        if not any(re.search("volleyball|drink|cocktail|towel", a) for a in acc):
            acc.append(rng.choice([a for a in b_acc.get("extra", []) if re.search("volleyball|drink|cocktail|towel", a)]))
    if "Dominant" in pool and not any(re.search(D.DOMINANT_PROPS, a) for a in acc):        # a Dominant look always carries a whip, crop or paddle
        acc.append(rng.choice([a for a in DB["Dominant"]["acc"].get("extra", []) if re.search(D.DOMINANT_PROPS, a)]))
    if need_mask() and not no_tops and not any(cover_of(a) for a in acc):       # Masquerade / Mourning Veils: the mask or veil is always there
        masks = [a for s in pool for a in DB[s]["acc"].get("face", []) if cover_of(a) and (level > 2 or pg_ok(a, level))]
        if masks:
            acc = [a for a in acc if a not in DB[pool[0]]["acc"].get("face", [])]
            acc.insert(0, rng.choice(masks))
    if "outer" in picked and not re.search(r"\b(open|worn|draped|hanging|off one|off the|over|cape|cloak|poncho|shawl|stole|wrap|scarf|boa|robe|kimono|vest|gilet|bolero|shrug|sleeveless|tied|unzipped|unbuttoned|slipping|sliding|falling)\b", picked["outer"], re.I):
        picked["outer"] += " worn properly with both arms in the sleeves"       # a bare 'long velvet coat' in the list gets drawn as a half-worn cape; say how it is worn
    order = [s for s in ("one", "top", "bottom", "outer", "legs", "feet", "head") if s in picked]
    outfit = ("wearing " + ", ".join(picked[s] for s in order)) if order else ""
    if acc:
        outfit += (", with " if order else "wearing ") + ", ".join(acc)
    outfit = (outfit + ".") if outfit else ""
    style_txt = "+".join(sel) if not free_styles else "any"
    bnames = [brand_of[s] for s in pool if s in brand_of]
    if bnames:
        style_txt += " (" + ", ".join(bnames) + ")"
    summary = f"Skimpy: {D.LEVELS[level - 1]} | Style: {style_txt} | Accessories: {len(acc)} | Colour: {primary}"
    if notes:
        summary += " | " + "; ".join(notes)
    return outfit, summary, dict(level=level, pool=pool, picked=picked, acc=acc, primary=primary, one=use_one)


class NoThingOutfitRoulette:
    CATEGORY = "No_Thing"
    FUNCTION = "run"
    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("prompt", "outfit", "active")

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
        if data.get("enabled") is False:                         # switched off: only the text around it passes through
            parts = [p.strip() for p in (prefix, suffix) if p and p.strip()]
            return (SEPS.get(data.get("sep"), "\n").join(parts), "", "Off")
        if data.get("random") is False:                          # dice off: just the picked buttons, as written
            outfit = fixed(data)
            opts = _on(data, "Options")
            if outfit and (NO_SHOES in opts or NO_BOTTOMS in opts or NO_TOPS in opts or NO_OUTER in opts):      # shoes, hidden half of the body: gone from whatever the picked texts say
                bits = [b for b in re.split(r",\s*", outfit.rstrip(".")) if b.strip()]
                if NO_SHOES in opts:
                    bits = [b for b in bits if not SHOE_WORDS.search(b)]
                if NO_OUTER in opts:
                    bits = [b for b in bits if not _OUTER_WORDS.search(b)]
                bits = [b for b in FR.strip_bits(", ".join(bits), NO_TOPS in opts, NO_BOTTOMS in opts).split(", ") if b]
                outfit = (", ".join(bits) + ".") if bits else ""
            parts = [p.strip() for p in (prefix, outfit, suffix) if p and p.strip()]
            return (SEPS.get(data.get("sep"), "\n").join(parts), outfit, "Random off")
        outfit, summary, _ = roll(
            seed, _on(data, "Skimpy"), _on(data, "Style"), _on(data, "Accessories"), _on(data, "Colour"),
            ONE_STYLE in _on(data, "Options"), NO_SHOES in _on(data, "Options"), NO_BOTTOMS in _on(data, "Options"), NO_TOPS in _on(data, "Options"), MIXED in _on(data, "Options"), NO_OUTER in _on(data, "Options"))
        parts = [p.strip() for p in (prefix, outfit, suffix) if p and p.strip()]
        return (SEPS.get(data.get("sep"), "\n").join(parts), outfit, summary)
