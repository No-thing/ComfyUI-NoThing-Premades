"""
Dataset for the No_Thing Body Roulette. Every entry describes an adult woman's figure.
TYPES: name -> (text, vibe tags, pools) where pools say which Bust / Waist / Hips / Legs options fit that type when you did not pick them yourself.
Add your own types in body_custom.json (see the README).
"""

LEGACY = {                                    # wording of earlier versions, so an untouched old node is not mistaken for an edited one
    "a small bust", "a medium bust", "a large bust", "a very large bust", "a huge, oversized bust", "a tiny cinched waist", "a slim waist",
    "a natural waist", "a soft, rounded waist", "narrow hips", "average hips", "wide hips", "very wide, flared hips", "a big, round butt",
    "a huge, full butt", "long slim legs", "thick, full thighs", "toned, strong legs", "average legs", "a short frame", "an average height",
    "a tall frame", "a very tall, statuesque frame", "an exaggerated bimbo hourglass figure", "a slim stacked figure with a slender frame",
    "a bottom-heavy pear-shaped figure with a narrow upper body", "a skinny, very slim narrow frame with long thin limbs and a flat stomach",
    "an athletic, toned body with defined abs and strong shoulders",
    "an exaggerated bimbo hourglass figure with a tiny cinched waist, a very large bust and wide, curvy hips",
    "a slim stacked figure: a slender frame and small waist with a large bust and full, round hips",
    "a bottom-heavy pear-shaped figure with a narrow upper body, wide hips, full thighs and a big round butt",
    "an athletic, toned body with defined abs, strong shoulders and powerful legs",
}

BUST = {"Small": "small perky breasts", "Medium": "medium round breasts", "Large": "large full round breasts",
        "Very large": "very large heavy breasts with deep cleavage", "Huge": "huge, massive breasts with deep cleavage"}
WAIST = {"Tiny": "a tiny wasp waist cinched in tight", "Slim": "a slim narrow waist", "Natural": "a natural waist", "Soft": "a soft rounded waist with a little belly"}
HIPS = {"Narrow": "narrow hips", "Average": "balanced hips", "Wide": "wide curvy hips", "Very wide": "very wide flared hips",
        "Big round butt": "a big round firm butt", "Huge butt": "a huge, massive round butt"}
LEGS = {"Long and slim": "long slim legs", "Thick thighs": "thick, heavy thighs", "Toned": "toned muscular legs", "Average": "average legs"}
HEIGHT = {"Short": "a short frame", "Average": "an average height", "Tall": "a tall frame", "Very tall": "a very tall, statuesque frame"}

TYPES = {
    "Bimbo": ("an extreme bimbo body with a massively exaggerated hourglass figure: an enormous bust, a wasp waist, huge round hips and a big firm butt, all plump glossy curves",
              "sultry", dict(bust=["Very large", "Huge"], waist=["Tiny"], hips=["Wide", "Very wide", "Big round butt"], legs=["Long and slim", "Thick thighs"])),
    "Slim stack": ("a slim stacked body: a slender frame with a flat toned stomach, a tiny waist, narrow hips and slim thighs, paired with large round full breasts, everything else slim",
                   "sultry", dict(bust=["Large", "Very large"], waist=["Tiny"], hips=["Narrow"], legs=["Long and slim"])),
    "Bottom heavy": ("a bottom-heavy pear body: a small narrow upper body with a slim waist, very wide flared hips, thick heavy thighs and a huge round butt",
                     "sultry soft", dict(bust=["Small", "Medium"], waist=["Slim", "Natural"], hips=["Very wide", "Big round butt", "Huge butt"], legs=["Thick thighs"])),
    "Skinny": ("a very skinny lean body with a narrow frame, thin arms and legs, visible collarbones, a flat stomach and a small bust",
               "soft fierce", dict(bust=["Small"], waist=["Slim", "Tiny"], hips=["Narrow"], legs=["Long and slim"])),
    "Athletic": ("an athletic toned body with defined abs, strong shoulders, firm toned glutes and muscular thighs, low body fat, a fit sporty figure",
                 "fierce", dict(bust=["Small", "Medium"], waist=["Slim", "Natural"], hips=["Narrow", "Average"], legs=["Toned"])),
}
VIBES = ["Sultry", "Soft", "Fierce"]


# General shape ladder for the Bar's Shape square: (name, short description, existing types it picks from or a custom (text, tags, pools), vague wording for Covered / Cute)
SHAPES = [
    ("Very slim", "very slim, narrow frame", ["Skinny"], None, "an extremely slim, petite frame"),
    ("Slim", "slender with soft curves", [], ("a slim, slender body with a narrow frame, a flat stomach and long limbs", "soft",
        dict(bust=["Small", "Medium"], waist=["Slim"], hips=["Narrow", "Average"], legs=["Long and slim"])), "a slender, graceful frame"),
    ("Balanced", "natural proportions", [], ("a balanced body with natural, softly feminine proportions", "soft sultry",
        dict(bust=["Medium"], waist=["Natural", "Slim"], hips=["Average", "Wide"], legs=["Average", "Toned"])), "a balanced, natural build"),
    ("Curvy", "full bust, defined waist, wide hips", ["Slim stack", "Bottom heavy"], None, "a soft, graceful figure"),
    ("Hourglass", "exaggerated hourglass bimbo", ["Bimbo"], None, "a graceful, softly curved figure"),
]


# PG mode (Covered / Cute outfits): the Shape dial still works, in words that name the figure (waist, hips, curves) but never the bust
PG_SHAPE_WORDS = [
    ["an extremely slim, petite frame", "a very slim, delicate build"],
    ["a slender, graceful frame with a narrow waist", "a slim, elegant build with long limbs"],
    ["a balanced, naturally feminine figure with a defined waist", "a softly curved, feminine build"],
    ["a curvy, voluptuous hourglass figure with a defined waist and full hips", "a voluptuous, curvy build with a narrow waist and wide hips"],
    ["an exaggerated voluptuous hourglass figure with a tiny waist and very wide, full hips and soft plump curves", "a dramatic hourglass build, a cinched tiny waist, full round hips and thick curvy thighs"],
]


# Toned-down wording, used when the Shape dial is on "any" or the outfit is still mostly covered (Covered .. Revealing): a voluptuous hourglass build,
# no breast or cleavage detail, no "bimbo". Your own Bust / Waist / Hips picks and edited texts still win.
TONED_TYPES = {
    "Bimbo": "a voluptuous hourglass figure with a tiny waist and wide, full hips",
    "Slim stack": "a slim stacked figure: a tiny waist, narrow hips and slim thighs with a full, generous bust, everything else slim",
    "Bottom heavy": "a pear-shaped figure with a slim waist, wide full hips and full thighs",
    "Skinny": "a very skinny lean body with a narrow frame, thin arms and legs, visible collarbones and a flat stomach",
}
TONED_WAIST = {"Tiny": "a tiny cinched waist"}
TONED_HIPS = {"Very wide": "very wide, full hips", "Big round butt": "full, round hips", "Huge butt": "very full, round hips"}
TONED_LEGS = {"Thick thighs": "full, shapely thighs"}
