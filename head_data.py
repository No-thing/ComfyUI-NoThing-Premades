"""
Dataset for the No_Thing Head Roulette (face shape, eyes, lips, hair).  Everything describes an adult woman's features.
Tags (cute / sultry / fierce / soft) are used by the Vibe row: picking a vibe makes matching options much more likely.
Add your own lines in head_custom.json (see the README).
"""

FACES = {   # name: (text, tags)
    "Oval": ("an oval face with balanced, harmonious proportions", "soft"),
    "Heart": ("a heart-shaped face with a wide forehead, high cheekbones and a delicate pointed chin", "cute soft"),
    "Round": ("a soft round face with full cheeks", "cute soft"),
    "Square": ("a strong square jawline with defined cheekbones", "fierce"),
    "Diamond": ("a diamond-shaped face with sharp high cheekbones and a narrow chin", "sultry fierce"),
    "Long": ("a long, elegant face with a high forehead and a slim jaw", "soft sultry"),
    "V-line": ("a slim V-line face with a sharply tapered chin and sculpted cheekbones", "sultry"),
    "Angular": ("a chiselled angular face with hollow cheeks and a defined jaw", "fierce"),
    "Soft full": ("a soft, full-cheeked face with a gentle jaw", "cute soft"),
}

EYE_SHAPES = {   # name: (adjectives, tail, tags)
    "Almond canted (predatory)": ("almond-shaped, upturned canted", "with an elongated outer corner and a sharp, predatory gaze", "fierce sultry"),
    "Cat eye / fox": ("narrow, upswept fox-like cat", "with a lifted outer corner and a sly look", "sultry fierce"),
    "Siren": ("long, languid siren", "with a slightly upturned almond shape and a heavy lid", "sultry"),
    "Hooded": ("heavy-lidded hooded", "with a sleepy, seductive look", "sultry"),
    "Doe": ("big, round doe", "with a wide-open, wondering look", "cute"),
    "Downturned": ("soft downturned puppy", "with a gentle, melting look", "cute soft"),
    "Monolid": ("slim monolid", "with a smooth lid and a calm, cool look", "soft fierce"),
    "Wide-set": ("wide-set", "with an airy, dreamy look", "cute soft"),
    "Deep-set": ("deep-set", "shadowed by a strong brow bone", "fierce"),
    "Narrow slanted": ("slanted", "with a cold, intense stare", "fierce"),
}
EYE_SIZES = {"Small": "small", "Medium": "medium-sized", "Large": "large", "Very large": "very large"}
EYE_COLOURS = {"Dark brown": "dark brown", "Amber": "amber", "Hazel": "hazel", "Green": "green", "Blue": "blue",
               "Icy grey": "icy grey", "Golden": "golden"}      # no violet: it kept turning up on ordinary models (cosplay characters bring their own eyes)

LIP_SHAPES = {   # name: (adjectives, tail, tags)
    "Cupid's bow": ("neat", "with a sharp cupid's bow", "sultry"),
    "Heart": ("heart-shaped", "with a pronounced top lip", "cute soft"),
    "Pouty": ("pouty", "with a fuller lower lip", "sultry cute"),
    "Wide": ("wide", "with a generous smile line", "soft"),
    "Bow": ("small bow-shaped", "with a neat, delicate outline", "cute"),
    "Overlined": ("glossy overlined", "with a lifted, sculpted edge", "sultry"),
    "Thin": ("thin, refined", "with a clean outline", "fierce"),
    "Smirk": ("softly asymmetrical", "curling into a subtle smirk", "fierce sultry"),
}
LIP_SIZES = {"Thin": "thin", "Medium": "medium", "Full": "full", "Plump": "plump", "Very plump": "very plump"}

LENGTHS = ["Pixie", "Chin", "Shoulder", "Mid-back", "Waist", "Hip"]
LENGTH_WORD = ["very short", "chin-length", "shoulder-length", "mid-back-length", "waist-length", "hip-length"]

# "levels|tags|category|text"  levels = hair lengths it works with (1 pixie .. 6 hip); {len} = length word, {c} = hair colour
STYLES = [
    "3-6|soft sultry|Straight|{c} {len} sleek, glossy straight hair",
    "3-6|soft|Waves & curls|{c} {len} soft beach waves",
    "3-6|sultry|Waves & curls|{c} {len} loose Hollywood curls",
    "3-6|cute|Waves & curls|{c} {len} bouncy ringlet curls",
    "2-6|fierce soft|Waves & curls|{c} {len} voluminous natural curls",
    "1-2|sultry fierce|Bob & short|a sharp, blunt {c} bob",
    "2|cute soft|Bob & short|a {c} chin-length bob with wispy ends",
    "2-3|sultry|Bob & short|a sleek {c} lob with a deep side part",
    "1|fierce|Bob & short|a cropped {c} pixie cut with a textured top",
    "1-2|cute|Bob & short|a short, layered {c} cut with side-swept bangs",
    "3-6|cute|Bangs|{c} {len} hair in a hime cut with straight cheek-length side locks and blunt bangs",
    "2-6|cute fierce|Bangs|{c} {len} hair with full blunt bangs",
    "4-6|fierce soft|Bangs|{c} {len} straight hair with full blunt bangs and long, thick sidelocks framing the face",
    "4-6|soft sultry|Bangs|{c} {len} sleek straight hair with heavy straight-cut bangs and long, thick, face-framing sidelocks falling past the chest",
    "5-6|fierce|Bangs|{c} {len} very long straight hair with thick, even bangs and two long, thick sidelocks, the rest falling smooth down the back",
    "3-6|soft sultry|Bangs|{c} {len} hair with face-framing curtain bangs",
    "3-6|cute|Ponytails & twin tails|{c} {len} hair in high twin tails",
    "3-6|sultry fierce|Ponytails & twin tails|{c} {len} hair in a high, swishing ponytail",
    "3-6|soft|Ponytails & twin tails|{c} {len} hair in a low ponytail with loose strands",
    "3-6|cute soft|Buns & braids|{c} hair in a messy bun with loose strands",
    "3-6|cute|Buns & braids|{c} hair in two space buns",
    "4-6|soft|Buns & braids|{c} {len} hair in a long fishtail braid over one shoulder",
    "4-6|cute|Buns & braids|{c} {len} hair in twin braids",
    "3-6|sultry|Half-up & retro|{c} {len} hair half up and half down",
    "3-5|sultry|Half-up & retro|{c} {len} retro pin-up hair with victory rolls and curled ends",
    "3-4|fierce|Edgy cuts|a {c} {len} shaggy wolf cut with heavy layers",
    "2-4|fierce|Edgy cuts|a {c} {len} shag with choppy layers",
    "1-3|fierce|Edgy cuts|a {c} undercut with the longer top swept to one side",
    "3-6|fierce|Buns & braids|{c} {len} box braids",
    "4-6|soft fierce|Buns & braids|{c} {len} hair in one long, thick, majestic braid falling over one shoulder",
    "5-6|soft fierce|Buns & braids|{c} {len} hair in one very long, thick braid down the back with small metallic gold hair ties spaced along its length",
    "5-6|fierce|Buns & braids|{c} {len} hair in one very long, thick braid down the back with silver ring hair ties along it",
    "5-6|soft|Buns & braids|{c} {len} hair in one very long, thick, loose braid down the back, tied at the end with a metallic cuff",
    "4-6|soft|Buns & braids|{c} {len} hair in a thick, regal side braid with loose face-framing strands",
    "5-6|fierce soft|Buns & braids|{c} {len} hair in a thick braid crown around the head with the rest in one majestic long braid down the back",
    "5-6|soft sultry|Buns & braids|{c} {len} hair in a very long, thick, loose fishtail braid over one shoulder, tied with a thin gold ribbon",
    "5-6|fierce|Buns & braids|{c} {len} hair in two very long, thick braids tied with metallic gold hair ties",
    "5-6|soft|Buns & braids|{c} {len} hair in a long, thick Dutch braid running down the back into a single heavy braid",
    "4-6|sultry soft|Straight|{c} {len} wet-look hair slicked back",
    "3-6|sultry|Waves & curls|{c} {len} voluminous bouncy blowout",
    "4-6|soft sultry|Waves & curls|{c} {len} layered, elegant, majestic and voluminous hair; extremely thick, full-bodied and heavily layered, with deep volume from the roots to the ends",
    "5-6|sultry fierce|Waves & curls|{c} {len} layered, elegant, majestic and voluminous waves, extremely thick and full, falling past the shoulders",
    "5-6|soft|Straight|{c} {len} layered, elegant, majestic and voluminous straight hair, very long and extremely thick",
    "6|soft sultry|Straight|{c} {len} very long, heavy, silky hair, extremely thick, smooth and full from the roots to the ends",
    "3-6|soft sultry|Half-up & retro|{c} {len} hair centre-parted and falling over the shoulders",
    "3-6|cute|Ponytails & twin tails|{c} {len} high ponytail with wispy face-framing strands",
    "2-6|fierce|Edgy cuts|{c} {len} razor-cut layers with sharp face-framing pieces",
    "2-6|fierce|Edgy cuts|{c} {len} wild teased layers with a heavy choppy fringe",
    "2-5|fierce|Edgy cuts|{c} {len} spiky punk shag with uneven layers and a long side fringe",
    "2-6|fierce|Edgy cuts|{c} {len} razor-cut emo layers with a long swept fringe and thinned ends",
    "3-6|soft sultry|Waves & curls|{c} {len} tousled bedhead waves",
]

HAIR_COLOURS = {
    "Black": ["jet black", "blue-black", "soft black"],
    "Brown": ["dark brunette", "chestnut brown", "chocolate brown", "caramel brown"],
    "Blonde": ["honey blonde", "golden blonde", "ash blonde", "platinum blonde", "strawberry blonde", "milk-tea blonde", "light golden-brown with blonde highlights"],
    "Red": ["copper red", "fiery red", "auburn", "burgundy", "cherry red"],
    "Pink": ["bubblegum pink", "hot pink", "rose pink", "magenta"],
    "Pastel": ["pastel pink", "lavender", "mint", "baby blue", "peach"],
    "Blue": ["electric blue", "midnight blue", "teal", "cyan"],
    "Purple": ["deep violet", "plum", "ultraviolet purple"],
    "Silver / White": ["silver", "icy white", "silver-grey"],
    "Two-tone": ["black with pink streaks", "blonde with pink tips", "split-dye black and white", "dark roots fading to pastel pink", "peekaboo blue under black", "black with neon blue and pink underlayers", "split-dye black and red", "rainbow streaks through black", "black with bright purple chunks"],
}

# Gyaru: the hair is the selling point, so every style here is big (descriptive wording: thickness, layers, teased crown, no metaphors)
STYLES += [
    "4-6|cute|Gyaru volume|{c} {len} hair in two thick spiral drill curls hanging in front of the shoulders, a full blunt fringe and a teased, voluminous crown",
    "5-6|cute soft|Gyaru volume|{c} {len} hair in two very thick, bouncy ringlet curls falling over the chest, with blunt bangs and side locks, big and full from the roots",
    "4-6|soft sultry|Gyaru volume|{c} {len} hair teased high at the crown into a big rounded volume, with long, thick, tousled curls falling down the back and thick face-framing side locks",
    "4-6|sultry|Gyaru volume|{c} {len} layered, extremely voluminous curled hair with a teased crown, heavy side-swept bangs and thick curls falling past the shoulders",
    "5-6|cute fierce|Gyaru volume|{c} {len} hair in a big half-up style with a teased, rounded crown, a curled fringe and thick curls falling down the back",
    "4-6|cute|Gyaru volume|{c} {len} hair in high twin tails of thick, bouncy curls with a teased crown and long face-framing side locks",
    "4-6|soft|Gyaru volume|{c} {len} very long, thick, layered wavy hair with long full bangs and thick side locks framing the face, big and full-bodied",
    "5-6|fierce soft|Gyaru volume|{c} {len} very long, straight, thick layered hair with long side-parted bangs hanging over the cheeks, a teased crown and a slightly wavy finish",
    "4-6|cute soft|Gyaru volume|{c} {len} hair in a high, voluminous updo with a big teased crown, curled strands falling around the face and the back hair left long in thick curls",
    "5-6|soft sultry|Gyaru volume|{c} {len} hair in thick, full, layered waves with a voluminous teased crown and a curtain of thick side locks",
    "5-6|cute soft|Gyaru volume|{c} {len} hair in two very thick, voluminous braids with a teased crown, curled ends and long face-framing side locks",
    "5-6|soft|Gyaru volume|{c} {len} hair with a teased, voluminous crown and one very long, thick braid falling over the shoulder, with curled strands around the face",
]

from .boho_data import STYLES_HAIR as _BOHO_HAIR   # dreadlocks, beads and wraps
STYLES += _BOHO_HAIR

VIBES = ["Cute", "Sultry", "Fierce", "Soft"]

STYLE_CATS = ["Straight", "Waves & curls", "Bob & short", "Bangs", "Ponytails & twin tails", "Buns & braids", "Half-up & retro", "Edgy cuts", "Gyaru volume", "Dreads & Boho"]
