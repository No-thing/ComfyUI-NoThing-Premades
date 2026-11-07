from .nothing_bar_node import NoThingPromptBar, NoThingPromptBarDetail
from .outfit_node import NoThingOutfitRoulette
from .underwear_node import NoThingUnderwearRoulette
from .makeup_node import NoThingMakeupRoulette
from .head_node import NoThingFaceRoulette, NoThingHairRoulette, NoThingHeadRoulette
from .body_node import NoThingBodyRoulette
from .light_node import NoThingLighting
from .rack_node import NoThingRouletteBar
from .banner_node import NoThingBanner

try:                                    # the checker can never take the other nodes down with it
    from .note_node import NoThingWorkflowCheck
except Exception:
    import traceback
    print("[No_Thing] Workflow Check failed to load:")
    traceback.print_exc()
    NoThingWorkflowCheck = None

WEB_DIRECTORY = "./web"
NODE_CLASS_MAPPINGS = {
    "NoThingPromptBar": NoThingPromptBar,
    "NoThingPromptBarDetail": NoThingPromptBarDetail,
    "NoThingOutfitRoulette": NoThingOutfitRoulette,
    "NoThingUnderwearRoulette": NoThingUnderwearRoulette,
    "NoThingMakeupRoulette": NoThingMakeupRoulette,
    "NoThingFaceRoulette": NoThingFaceRoulette,
    "NoThingHairRoulette": NoThingHairRoulette,
    "NoThingHeadRoulette": NoThingHeadRoulette,
    "NoThingBodyRoulette": NoThingBodyRoulette,
    "NoThingLighting": NoThingLighting,
    "NoThingRouletteBar": NoThingRouletteBar,
    "NoThingBanner": NoThingBanner,
}
if NoThingWorkflowCheck is not None:
    NODE_CLASS_MAPPINGS["NoThingWorkflowCheck"] = NoThingWorkflowCheck
NODE_DISPLAY_NAME_MAPPINGS = {
    "NoThingPromptBar": "No_Thing Prompt Bar (Look)",
    "NoThingPromptBarDetail": "No_Thing Prompt Bar (Detail)",
    "NoThingOutfitRoulette": "No_Thing Outfit Roulette (clothes)",
    "NoThingUnderwearRoulette": "No_Thing Underwear Roulette (lingerie)",
    "NoThingMakeupRoulette": "No_Thing Makeup Roulette (looks)",
    "NoThingFaceRoulette": "No_Thing Face Roulette (face, eyes, lips)",
    "NoThingHairRoulette": "No_Thing Hair Roulette (length, style, colour)",
    "NoThingHeadRoulette": "No_Thing Head Roulette (old: face + hair in one)",
    "NoThingBodyRoulette": "No_Thing Body Roulette (figure)",
    "NoThingLighting": "No_Thing Lighting (click and choose)",
    "NoThingRouletteBar": "No_Thing Roulette Bar (face, hair, body, makeup, outfit, underwear in one wide bar)",
    "NoThingBanner": "No_Thing Banner (picture only)",
}
if NoThingWorkflowCheck is not None:
    NODE_DISPLAY_NAME_MAPPINGS["NoThingWorkflowCheck"] = "No_Thing Workflow Check (models + packs)"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
