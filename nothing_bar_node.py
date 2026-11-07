"""
No_Thing Prompt Bar - a row of buttons, each one a piece of prompt text.

The buttons, their names and their texts live in one hidden text field ("bar_data", a small JSON
document) that the on-canvas bar edits. The node simply joins the texts of the buttons that are
switched on. Nothing else to wire: feed your base prompt into `prefix`, take `prompt` out.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SEPS = {"newline": "\n", "space": " ", "comma": ", "}


def _load(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return json.load(f)


def _parse(raw):
    try:
        data = json.loads(raw)
        if isinstance(data, dict) and isinstance(data.get("groups"), list):
            return data
    except (TypeError, ValueError):
        pass
    return {"sep": "newline", "groups": []}


class NoThingPromptBar:
    CATEGORY = "No_Thing"
    FUNCTION = "run"
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("prompt", "active")
    DEFAULT_FILE = "defaults_look.json"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"bar_data": ("STRING", {"default": json.dumps(_load(cls.DEFAULT_FILE), ensure_ascii=False)})},
            "optional": {"prefix": ("STRING", {"forceInput": True}), "suffix": ("STRING", {"forceInput": True})},
        }

    def run(self, bar_data, prefix="", suffix=""):
        data = _parse(bar_data)
        parts = [prefix.strip()] if prefix and prefix.strip() else []
        active = []
        for g in data["groups"]:
            taken = False
            for b in g.get("buttons", []):
                if not b.get("on"):
                    continue
                if g.get("exclusive") and taken:      # one-at-a-time group: first one wins
                    continue
                taken = True
                text = str(b.get("text", "")).strip()
                if text:
                    parts.append(text)
                active.append(f'{g.get("name", "")}: {b.get("label", "")}')
        if suffix and suffix.strip():
            parts.append(suffix.strip())
        return (SEPS.get(data.get("sep"), "\n").join(parts), ", ".join(active))


class NoThingPromptBarDetail(NoThingPromptBar):
    DEFAULT_FILE = "defaults_detail.json"
