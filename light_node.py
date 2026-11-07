"""
No_Thing Lighting - click and choose (no randomness): a lighting setup, one or two light colours (or a ready palette), a mood and extras.
Rows you leave empty are simply left out. Colour only (no setup) = "lit by <colour> light".
"""
import json

from . import light_data as D
from .roulette_common import chosen, defaults_of, edited, group, join, parse


def default_bar():
    return {"v": 1, "sep": "newline", "enabled": True, "groups": [
        group("Setup", list(D.SETUPS), D.SETUPS, exclusive=True),
        group("Palette", list(D.PALETTES), {k: f"Key: {a}, rim: {b}" for k, (a, b) in D.PALETTES.items()}, exclusive=True, locked=True),
        group("Key colour", list(D.COLOURS), D.COLOURS, exclusive=True),
        group("Rim colour", list(D.COLOURS), D.COLOURS, exclusive=True),
        group("Mood", list(D.MOODS), D.MOODS, exclusive=True),
        group("Extras", list(D.EXTRAS), D.EXTRAS),
    ]}


def build(data):
    dfl = defaults_of(default_bar())
    ov = {k: edited(data, k, dfl) for k in ("Setup", "Key colour", "Rim colour", "Mood", "Extras")}
    setup = next(iter(chosen(data, "Setup")), None)
    pal = next(iter(chosen(data, "Palette")), None)
    key = next(iter(chosen(data, "Key colour")), None)
    rim = next(iter(chosen(data, "Rim colour")), None)
    if pal in D.PALETTES:
        key, rim = D.PALETTES[pal]                          # a palette wins over single colours

    def word(label, row):
        return ov[row].get(label) or ov["Key colour" if row == "Rim colour" else "Rim colour"].get(label) or D.COLOURS.get(label)

    kw = (word(key, "Key colour") if key else None) or (word(rim, "Rim colour") if rim else None) or "warm white"
    rw = (word(rim, "Rim colour") if rim else None) or (word(key, "Key colour") if key else None) or "warm white"
    parts = []
    if setup in D.SETUPS:
        parts.append(ov["Setup"].get(setup, D.SETUPS[setup]).replace("{key}", kw).replace("{rim}", rw))
    elif key or rim:
        parts.append(f"lit by {kw} light" if kw == rw else f"lit by {kw} and {rw} light")
    mood = next(iter(chosen(data, "Mood")), None)
    if mood in D.MOODS:
        parts.append(f"the light is {ov['Mood'].get(mood, D.MOODS[mood])}")
    parts += [ov["Extras"].get(e, D.EXTRAS[e]) for e in chosen(data, "Extras") if e in D.EXTRAS]
    return (", ".join(parts) + ".") if parts else ""


class NoThingLighting:
    CATEGORY = "No_Thing"
    FUNCTION = "run"
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("prompt", "lighting")

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"bar_data": ("STRING", {"default": json.dumps(default_bar(), ensure_ascii=False)})},
            "optional": {"prefix": ("STRING", {"forceInput": True}), "suffix": ("STRING", {"forceInput": True})},
        }

    def run(self, bar_data, prefix="", suffix=""):
        data = parse(bar_data)
        text = "" if data.get("enabled") is False else build(data)
        return (join(data, prefix, text, suffix), text)
