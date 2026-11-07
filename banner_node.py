"""
No_Thing Banner - a picture node. It has no inputs and no outputs and does nothing when you press Run.
It only paints the brand banner (web/banners/workflow_banner.png) on the canvas, so the banner lives
inside the workflow and moves, resizes and copies like any other node.
"""


class NoThingBanner:
    CATEGORY = "No_Thing"
    FUNCTION = "run"
    RETURN_TYPES = ()
    OUTPUT_NODE = False

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {}}

    def run(self):
        return ()
