"""
No_Thing Roulette Bar: face, hair, body, makeup, outfit and underwear in ONE wide, flat node.

Each part is exactly one of the old roulettes (same buttons, same dataset, same rules), just driven from one bar:
  * one seed for the whole bar; every part gets its own sub-seed made from it,
  * a part can be switched off, locked (keeps its roll when the seed changes) or re-rolled on its own,
  * open a part to pick what its dice may choose from (the button rows of the old node).
Same seed + same buttons = same prompt. The six old nodes still exist, so saved workflows keep loading.
"""
import json
import re

from . import body_node, head_node, makeup_node, outfit_node, underwear_node
import copy
import random

from . import themes_data
from .roulette_common import SEPS, scheme, tier_ctx, frame_ctx, FRAMES, cover_ctx, cover_of, need_mask_ctx, MASK_THEMES, hair_ctx, shape_ctx, avoid_ctx, clash_pattern

PARTS = [  # key, title, class, default bar
    ("face", "Face", head_node.NoThingFaceRoulette, lambda: head_node.default_bar("face")),
    ("hair", "Hair", head_node.NoThingHairRoulette, lambda: head_node.default_bar("hair")),
    ("body", "Body", body_node.NoThingBodyRoulette, body_node.default_bar),
    ("makeup", "Makeup", makeup_node.NoThingMakeupRoulette, makeup_node.default_bar),
    ("outfit", "Outfit", outfit_node.NoThingOutfitRoulette, outfit_node.default_bar),
    ("underwear", "Underwear", underwear_node.NoThingUnderwearRoulette, underwear_node.default_bar),
]
NO_UNDERWEAR_THEMES = {"Beach Day", "Kigurumi Mix", "Cosplay"}
NO_HAIR_MAKEUP_THEMES = {"Cosplay"}                      # the character brings their own hair and makeup
MASK = 0xFFFFFFFFFFFFFFFF


# Framing square: which of the old option buttons each step switches on (outfit / underwear), and which parts are out of the picture
FRAME_OPTS = {2: {"outfit": ["No shoes"]}, 3: {"outfit": ["No shoes", "No bottoms"], "underwear": ["No bottoms"]},
              4: {"outfit": ["No tops", "No shoes"], "underwear": ["No tops"]}}
FRAME_OFF = {4: {"face", "hair", "makeup"}}                      # bottoms only: no face in the picture


def with_options(data, labels):
    data = copy.deepcopy(data)
    for g in data.get("groups", []):
        if g.get("name") == "Options":
            for b in g.get("buttons", []):
                if b.get("label") in labels:
                    b["on"] = True
    return data


def default_bar():
    return {"v": 1, "sep": "newline", "enabled": True, "frame": 1, "shape": 0, "open": None, "theme": "", "fine": False, "mode": "simple",
            "parts": [{"key": k, "name": n, "enabled": True, "locked": False, "salt": 0, "data": mk()} for k, n, _, mk in PARTS]}


def part_seed(seed, index, part):
    """A part's own seed. Locked: only its salt counts, so the main seed can change and this part stays put."""
    salt = int(part.get("salt") or 0)
    if part.get("locked"):
        return (salt * 104729 + index * 7919 + 12345) & MASK
    return (int(seed) * 1000003 + index * 7919 + salt * 104729) & MASK


# which row of each part a theme steers (the row that holds the style names)
THEME_ROWS = {"outfit": [("Style", "outfit", False)], "makeup": [("Look", "makeup", False)],
              "underwear": [("Style", "underwear", False), ("Add-ons", "addons", True)],
              "hair": [("Hairstyle", "hair", True), ("Hair colour", "haircol", True)]}       # True = only when the theme defines it (the style rows always follow the theme)


def apply_theme(key, data, theme):
    """A copy of the part's buttons where the theme's picks are the only ones switched on in each row it steers."""
    rows = THEME_ROWS.get(key)
    if not rows or not theme:
        return data
    data = copy.deepcopy(data)
    for rname, tkey, optional in rows:
        want = set(theme.get(tkey, []))
        if optional and not want:
            continue
        for g in data.get("groups", []):
            if g.get("name") == rname:
                have = {b.get("label") for b in g.get("buttons", [])}
                for lab in want - have:                                   # a bar saved before a style existed has no button for it: add one, so the theme still steers
                    g.setdefault("buttons", []).append({"label": lab, "text": "", "def": "", "on": False})
                for b in g.get("buttons", []):
                    b["on"] = b.get("label") in want
    return data


def theme_pair(theme, seed):
    """One main colour and one accent for the whole roll; a new seed gives a new but still fitting pair."""
    main, accent = theme["colours"]
    rng = random.Random(f"{int(seed)}:scheme")
    primary = rng.choice(main)
    rest = [a for a in accent if a != primary] or accent
    return primary, rng.choice(rest)


def export_themes():
    """web/themes.json lists the themes for the node's dropdown (name, category, one-line description)."""
    try:
        import os
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "web", "themes.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(themes_data.listing(), f, indent=1, ensure_ascii=False)
    except Exception:
        pass


def export_icons():
    """web/icons/index.json lists the style / amount pictures that exist (<style name>.png, level_1..5.png)."""
    try:
        import os
        d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "web", "icons")
        os.makedirs(d, exist_ok=True)
        names = sorted(f[:-4] for f in os.listdir(d) if f.lower().endswith(".png"))
        with open(os.path.join(d, "index.json"), "w", encoding="utf-8") as f:
            json.dump(names, f)
    except Exception:
        pass


export_themes()
export_icons()


def _parse(raw):
    try:
        d = json.loads(raw)
        if isinstance(d, dict) and isinstance(d.get("parts"), list):
            return d
    except (TypeError, ValueError):
        pass
    return default_bar()


class NoThingRouletteBar:
    CATEGORY = "No_Thing"
    FUNCTION = "run"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)                           # ONE output: prefix in, prompt out (what was rolled is shown on the cards)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "bar_data": ("STRING", {"default": json.dumps(default_bar(), ensure_ascii=False)}),
                "seed": ("INT", {"default": 0, "min": 0, "max": MASK}),
            },
            "optional": {"prefix": ("STRING", {"forceInput": True}), "suffix": ("STRING", {"forceInput": True})},
        }

    def run(self, bar_data, seed, prefix="", suffix=""):
        data = _parse(bar_data)
        sep = SEPS.get(data.get("sep"), "\n")
        by_key = {p.get("key"): p for p in data["parts"]}
        texts, summaries, prompts = {}, [], []
        theme = themes_data.T.get(data.get("theme") or "")
        pair = theme_pair(theme, seed) if theme else None
        results = {}
        tier_n = None
        try:
            fr = min(4, max(1, int(data.get("frame") or 1)))
        except (TypeError, ValueError):
            fr = 1
        try:
            sh = min(5, max(0, int(data.get("shape") or 0)))
        except (TypeError, ValueError):
            sh = 0
        o_idx = [i for i, p in enumerate(PARTS) if p[0] == "outfit"][0]
        o_part = by_key.get("outfit")
        if data.get("enabled") is not False and o_part and o_part.get("enabled") is not False:
            # the outfit goes first: how skimpy it rolled (1 Covered .. 5 Micro) decides how the body, face, makeup and underwear are worded
            pdata = with_options(apply_theme("outfit", o_part.get("data") or {}, theme), FRAME_OPTS.get(fr, {}).get("outfit", []))
            with scheme(pair), frame_ctx(fr), need_mask_ctx(data.get("theme") in MASK_THEMES and fr != 4), hair_ctx(bool(by_key.get("hair")) and by_key["hair"].get("enabled") is not False and fr != 4 and data.get("theme") not in NO_HAIR_MAKEUP_THEMES):
                res = PARTS[o_idx][2].run.raw(PARTS[o_idx][2](), json.dumps(pdata), part_seed(seed, o_idx, o_part), "", "")
            results["outfit"] = res
            for n, lab in enumerate(outfit_node.D.LEVELS, 1):
                if f"Skimpy: {lab}" in str(res[2]):
                    tier_n = n
        else:                                                    # outfit off: only a lone Covered / Cute pick on the Skimpy row counts
            for g in (o_part or {}).get("data", {}).get("groups", []):
                if g.get("name") == "Skimpy":
                    on = [b.get("label") for b in g.get("buttons", []) if b.get("on")]
                    if len(on) == 1 and on[0] in outfit_node.D.LEVELS:
                        tier_n = outfit_node.D.LEVELS.index(on[0]) + 1
        u_idx = [i for i, p in enumerate(PARTS) if p[0] == "underwear"][0]
        u_part = by_key.get("underwear")
        if data.get("enabled") is not False and u_part and u_part.get("enabled") is not False and tier_n not in (1, 2) and "underwear" not in FRAME_OFF.get(fr, ()):
            pdata = with_options(apply_theme("underwear", u_part.get("data") or {}, theme), FRAME_OPTS.get(fr, {}).get("underwear", []))
            clash = clash_pattern(str(results["outfit"][1]) if "outfit" in results and isinstance(results["outfit"][1], str) else "")
            with scheme(pair), tier_ctx(tier_n), frame_ctx(fr), avoid_ctx(clash):
                results["underwear"] = PARTS[u_idx][2].run.raw(PARTS[u_idx][2](), json.dumps(pdata), part_seed(seed, u_idx, u_part), "", "")
        if data.get("theme") in NO_UNDERWEAR_THEMES:               # a beach look is the bikini itself: no lingerie, harness or garters on top
            results.pop("underwear", None)
        cov = cover_of(*(str(results[k][1]) for k in ("outfit", "underwear") if k in results and isinstance(results[k][1], str)))
        for i, (key, title, cls, _mk) in enumerate(PARTS):
            part = by_key.get(key)
            if data.get("enabled") is False or not part or part.get("enabled") is False:
                texts[key] = ""
                continue
            if key in ("hair", "makeup") and data.get("theme") in NO_HAIR_MAKEUP_THEMES:
                texts[key] = ""
                continue
            if key == "underwear" and data.get("theme") in NO_UNDERWEAR_THEMES:
                texts[key] = ""
                continue
            if key == "underwear" and tier_n in (1, 2):         # Covered and Cute: no underwear in the prompt
                texts[key] = ""
                continue
            if key in FRAME_OFF.get(fr, ()):
                texts[key] = ""
                continue
            if cov and key == "makeup":                          # a mask or veil is the focus: no makeup next to it
                texts[key] = ""
                continue
            if cov == "full" and key == "face":                  # the face is covered
                texts[key] = ""
                continue
            if key in results:
                res = results[key]
            else:
                pdata = with_options(apply_theme(key, part.get("data") or {}, theme), FRAME_OPTS.get(fr, {}).get(key, []))
                with scheme(pair if key in ("outfit", "makeup", "underwear") else None), tier_ctx(tier_n), frame_ctx(fr), cover_ctx(cov), shape_ctx(sh):
                    res = cls.run.raw(cls(), json.dumps(pdata), part_seed(seed, i, part), "", "")
            texts[key] = res[1] if isinstance(res[1], str) else ""
            if res[0] and res[0].strip():
                prompts.append(res[0].strip())
            summaries.append(str(res[2]) if len(res) > 2 and res[2] else title)
        if (tier_n or 0) >= 3 and not re.search(r"\\b(adult|mature|woman in her|[2-4]\\d[- ]year)", " ".join([prefix or "", suffix or "", " ".join(prompts)]), re.I):
            prompts.insert(0, "an adult woman")                      # Revealing and up: the prompt always says she is an adult
        parts = [p.strip() for p in (prefix, sep.join(prompts), suffix) if p and p.strip()]
        prompt = sep.join(parts)
        out = (prompt,)
        return {"ui": {"nt_seed": [int(seed)], "nt_parts": [json.dumps(texts, ensure_ascii=False)]}, "result": out}
