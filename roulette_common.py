"""Shared helpers for the No_Thing roulette / chooser nodes (the buttons are a JSON string, same as the Prompt Bar)."""
import json

SEPS = {"newline": "\n", "space": " ", "comma": ", "}


def group(name, labels, texts=None, exclusive=False, locked=False):
    """`text` is what the button says (the user can edit it); `def` remembers the original so the node can tell what was edited."""
    btns = []
    for l in labels:
        t = (texts or {}).get(l, "")
        b = {"label": l, "text": t, "def": t, "on": False}
        if locked:
            b["locked"] = True                     # the panel does not offer editing for this button
        btns.append(b)
    return {"name": name, "exclusive": exclusive, "buttons": btns}


def parse(raw):
    try:
        data = json.loads(raw)
        if isinstance(data, dict) and isinstance(data.get("groups"), list):
            return data
    except (TypeError, ValueError):
        pass
    return {"sep": "newline", "groups": []}


def chosen(data, group_name):
    """Labels switched on in a row (an exclusive row only counts its first one)."""
    for g in data.get("groups", []):
        if g.get("name") == group_name:
            on = [b.get("label", "") for b in g.get("buttons", []) if b.get("on")]
            return on[:1] if g.get("exclusive") else on
    return []


def join(data, prefix, middle, suffix):
    parts = [p.strip() for p in (prefix, middle, suffix) if p and p.strip()]
    return SEPS.get(data.get("sep"), "\n").join(parts)


def weighted(rng, items, vibes, tag_of):
    """Pick from items; ones whose tags match a chosen vibe are 6x as likely."""
    if not items:
        return None
    w = [1 + (5 if vibes and set(tag_of(i)) & set(vibes) else 0) for i in items]
    return rng.choices(items, w)[0]


def defaults_of(bar):
    """{row: {label: default text}} of a default_bar()."""
    return {g["name"]: {b["label"]: b.get("text", "") for b in g["buttons"]} for g in bar["groups"]}


def edited(data, group_name, defaults=None, legacy=()):
    """{label: text} for the buttons whose text the user changed in the panel.
    A button remembers its original in `def`. Nodes saved by older versions have no `def`: for those the text is compared with this
    version's default (and with `legacy`, the wording of earlier versions) so an untouched old node does not count as edited."""
    out = {}
    for g in data.get("groups", []):
        if g.get("name") != group_name:
            continue
        for b in g.get("buttons", []):
            t, d = str(b.get("text", "")).strip(), b.get("def")
            if not t:
                continue
            if d is not None:
                if t != str(d).strip():
                    out[b.get("label", "")] = t
            else:
                base = str(((defaults or {}).get(group_name) or {}).get(b.get("label", ""), "")).strip()
                if t != base and t not in legacy:
                    out[b.get("label", "")] = t
    return out


def with_seed(fn):
    """Wrap a roulette's run(): also report the seed it used (ui "nt_seed"), so the Edit Page can lock the exact roll that made a picture."""
    def run(self, bar_data, seed, prefix="", suffix=""):
        res = fn(self, bar_data, seed, prefix, suffix)
        ui = {"nt_seed": [int(seed)]}
        if isinstance(res, tuple) and len(res) > 1 and isinstance(res[1], str):
            ui["nt_text"] = [res[1]]                       # what the dice rolled, shown inside the node in Simple mode
        return {"ui": ui, "result": res}
    run.__name__ = fn.__name__
    run.raw = fn                                      # the plain function (no ui dict), for the Roulette Bar that runs six of them
    return run


# ---- a shared colour scheme: the Roulette Bar's Style (theme) hands every part the same main colour and accent
import threading

_SC = threading.local()


class scheme:
    """with scheme((primary, accent)): ...  the outfit, makeup and underwear rolls use exactly these two colours."""
    def __init__(self, pair):
        self.pair = pair

    def __enter__(self):
        _SC.pair = self.pair

    def __exit__(self, *a):
        _SC.pair = None


def scheme_pair():
    return getattr(_SC, "pair", None)


# ---- the "tier": how skimpy the outfit rolled (1 Covered .. 5 Micro). The Roulette Bar hands it to every other part so they match.
_TIER = threading.local()


class tier_ctx:
    """with tier_ctx(1): ...  body, face, makeup and underwear rolls stay as covered as the outfit (1 = PG)."""
    def __init__(self, n):
        self.n = n

    def __enter__(self):
        _TIER.n = self.n

    def __exit__(self, *a):
        _TIER.n = None


def tier():
    return getattr(_TIER, "n", None)


import re as _re
# words that contradict a Covered (1) outfit / a Cute (2) outfit; entries that contain them are never picked at that level
PG_BLOCK = {
    1: _re.compile(r"sheer|see-through|transparent|\bmesh\b|harness|garter|corset|bodice|bralette|\bbra\b|bikini|bandeau|lingerie|belly|"
                   r"waist (chain|cincher|tie)|beaded waist|leash|\bcrop\b|crop(ped)? (top|tee|sweater|sweatshirt|hoodie|baby)|"
                   r"slipping off|cleavage|midriff|cut-out|plunge|backless|strapless|thigh|slit|bondage|padlock|leather cuff|buckled|nude|"
                   r"collar with a chain|chain collar|riding|thong|waistband|g-string", _re.I),
    2: _re.compile(r"sheer|harness|garter|corset|bralette|lingerie|leash|\bcrop\b|bondage|see-through|transparent|plunge|padlock|chain collar|thong|waistband", _re.I),
}
# styles that are only about bondage / fetish: skipped at Covered
PG_STYLES_OFF = {1: set(), 2: set()}
# soft wording for face and makeup at Covered / Cute
PG_FACE_BLOCK = _re.compile(r"plump|overlin|seduc|sultr|bedroom|hooded|siren|heavy lid|predatory|aroused|wet-look|sheer|veil", _re.I)


def pg_ok(text, t=None):
    t = t if t is not None else tier()
    rx = PG_BLOCK.get(t) if t else None
    return not (rx and rx.search(text))


# ---- the "frame": what is in the picture (1 full body, 2 no feet, 3 top only, 4 bottoms only). The Roulette Bar's Framing square sets it.
_FRAME = threading.local()
FRAMES = ["Full body", "No feet", "Top only", "Bottoms only"]


class frame_ctx:
    def __init__(self, n):
        self.n = n

    def __enter__(self):
        _FRAME.n = self.n

    def __exit__(self, *a):
        _FRAME.n = None


def frame():
    return getattr(_FRAME, "n", None) or 1


# ---- a mask or veil in the outfit / underwear: the mask is the focus, so the face and makeup say little or nothing
_COVER = threading.local()
COVER_FULL = _re.compile(r"veil|face cover|covering the (whole|entire|eyes)|whole face|entire face|half-face|lower face|visor|balaclava|face mask|net over|mesh face", _re.I)
COVER_EYES = _re.compile(r"\bmasks?\b|masquerade|nose cover|domino|blindfold", _re.I)


def cover_of(*texts):
    t = " ".join(x for x in texts if x)
    if COVER_FULL.search(t):
        return "full"
    if COVER_EYES.search(t):
        return "eyes"
    return None


class cover_ctx:
    def __init__(self, kind):
        self.kind = kind

    def __enter__(self):
        _COVER.kind = self.kind

    def __exit__(self, *a):
        _COVER.kind = None


def cover():
    return getattr(_COVER, "kind", None)


# themes where a mask / veil is the whole point: the outfit always gets one
_NEED = threading.local()
MASK_THEMES = {"Masquerade Ball", "Mourning Veils"}


class need_mask_ctx:
    def __init__(self, on):
        self.on = on

    def __enter__(self):
        _NEED.on = self.on

    def __exit__(self, *a):
        _NEED.on = False


def need_mask():
    return bool(getattr(_NEED, "on", False))


# the Bar's hair part is on: the outfit does not add its own hair accessories ("a high gym ponytail") on top of it
_HAIR = threading.local()


class hair_ctx:
    def __init__(self, on):
        self.on = on

    def __enter__(self):
        _HAIR.on = self.on

    def __exit__(self, *a):
        _HAIR.on = False


def hair_on():
    return bool(getattr(_HAIR, "on", False))


# ---- the "shape": general body shape from very slim (1) to hourglass (5), 0 = not chosen. The Roulette Bar's Shape square sets it.
_SHAPE = threading.local()


class shape_ctx:
    def __init__(self, n):
        self.n = n

    def __enter__(self):
        _SHAPE.n = self.n

    def __exit__(self, *a):
        _SHAPE.n = None


def shape():
    n = getattr(_SHAPE, "n", None) or 0
    return n if 1 <= n <= 5 else 0


# ---- parts that must not contradict each other: the Bar hands the underwear a pattern for what the outfit already uses (a hat, sunglasses ...)
_AVOID = threading.local()


class avoid_ctx:
    def __init__(self, rx):
        self.rx = rx

    def __enter__(self):
        _AVOID.rx = self.rx

    def __exit__(self, *a):
        _AVOID.rx = None


def avoid(text):
    """True when `text` would clash with what the outfit already wears."""
    rx = getattr(_AVOID, "rx", None)
    return bool(rx and rx.search(text))


_HEAD_CLASH = _re.compile(r"\b(hat|cap|beret|beanie|visor|bandana|headband|tiara|crown|headpiece|hair bow|hair bows|ribbon hair bow|ears?)\b", _re.I)
_EYES_CLASH = _re.compile(r"sunglasses|glasses|goggles|\bshades\b", _re.I)
_AVOID_HEAD = _re.compile(r"(?<![a-z])ears?\b|headband|\bhorns?\b|crown|fascinator|headpiece|\bhats?\b|beret|bandana|\bmask\b|veil|tiara|\bhood\b", _re.I)
_AVOID_EYES = _re.compile(r"\bmask\b|veil|face covering|blindfold|\beye\b.*\bties\b", _re.I)


def clash_pattern(outfit_text):
    """What the underwear / add-ons may not bring, given the outfit: no second hat or ears on top of a hat, no mask over sunglasses."""
    parts = []
    if outfit_text and _HEAD_CLASH.search(outfit_text):
        parts.append(_AVOID_HEAD.pattern)
    if outfit_text and _EYES_CLASH.search(outfit_text):
        parts.append(_AVOID_EYES.pattern)
    return _re.compile("|".join(parts), _re.I) if parts else None
