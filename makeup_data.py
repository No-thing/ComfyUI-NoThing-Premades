"""
The makeup dataset for the No_Thing Makeup Roulette node.
Every entry is  "levels|text"  where levels is one number or a range:
    1 Natural   barely there      2 Soft   pretty, light colour      3 Glam   defined, polished
    4 Bold      strong statement  5 Extreme  editorial, costume, full-on
{c} = the colour you picked in the Colour row (or a colour from the look's own palette), {c2} = a second colour.
Add your own lines in makeup_custom.json (see README) - they are picked up after a ComfyUI restart.
"""
LEVELS = ["Natural", "Soft", "Glam", "Bold", "Extreme"]
AMOUNTS = ["None", "Few", "Some", "Loaded"]
AMOUNT_RANGE = {"None": (0, 0), "Few": (1, 1), "Some": (2, 3), "Loaded": (4, 5)}

COLOURS = {
    "Nude": ["warm nude", "soft beige", "taupe", "peach", "rosy nude", "caramel"],
    "Pink": ["baby pink", "rose pink", "hot pink", "bubblegum pink", "petal pink"],
    "Red": ["classic red", "cherry red", "crimson", "blood red", "scarlet", "oxblood"],
    "Berry": ["berry", "deep plum", "wine", "burgundy", "mulberry", "raspberry"],
    "Black": ["jet black", "matte black", "glossy black", "charcoal"],
    "Purple": ["lavender", "lilac", "violet", "deep purple", "amethyst"],
    "Blue": ["ice blue", "baby blue", "cobalt blue", "electric blue", "teal", "navy"],
    "Green": ["mint green", "emerald", "olive", "sage", "lime green"],
    "Metallic": ["silver", "gold", "chrome", "bronze", "copper", "holographic"],
    "Neon": ["neon pink", "neon green", "neon orange", "UV purple", "acid yellow", "electric blue"],
}

FAMILIES = {}
DESC = {}

DESC["Japanese & East Asian"] = "Igari, gyaru, jirai kei, douyin and minimalist Japanese beauty"
FAMILIES["Japanese & East Asian"] = [
    "2-3|Igari hangover makeup: soft pink blush swept across the high cheekbones and bridge of the nose, gradient bitten lips, glossy eyelids",
    "2-3|Gyaru makeup: heavy drooping lower eyeliner, prominent artificial aegyo sal undertail highlight, long false eyelashes, pale nude lipstick",
    "3-4|Jirai kei makeup: soft burgundy eyeshadow, a pink-red eyeshadow halo, soft flushed under-eye blush, downturned puppy eyeliner, deep berry glossy lips",
    "2-3|Douyin makeup: hyper-glimmering liquid glitter across the lids, delicate individual spiky false lashes, soft blurred petal-pink lips, nose-tip blush",
    "1-2|minimalist Japanese beauty: porcelain dewy skin, sheer coral lip tint, soft feathered eyebrows, lengthening brown mascara",
    "2|Korean glass-skin makeup: luminous skin, straight soft brows, gradient peach lip tint, a little shimmer on the centre of the lids",
    "2-3|aegyo-sal makeup: soft pink under-eye shimmer, puppy-eye brown liner, juicy peach lips, a dusting of freckles",
    "4|full gyaru makeup: a thick, matte plaster-smooth base over the whole face, heavy white concealer highlights under the eyes, thick black upper eyeliner with a long wing, drawn-on lower lashes, huge double false lashes, a dark brown lip liner overlined with pale nude lipstick",
    "4-5|over-the-top gyaru makeup: a flawless layered matte base like plaster, bright concealer under the eyes and on the nose bridge, very heavy black eyeliner top and bottom, thick winged liner, stacked false lashes top and bottom, pale glossy lips with a dark liner",
    "5|extreme gyaru makeup: a heavy, ultra-matte plaster base covering the whole face, pale white concealer under the eyes, enormous layered false lashes, thick graphic black eyeliner all around the eye, drawn-on lower lashes, bold overlined lips outlined in dark brown liner",
    "5|full ganguro makeup: a deep tan base, a thick pale concealer under the eyes, bold white eyeliner on the lower lids, thick black upper liner, huge false lashes, white-pink pale lips outlined with a dark liner",
    "3-4|Gyaru 'ganguro-lite' makeup: bronzed tan base, thick white eyeliner on the lower lids, huge false lashes, glossy pale pink lips",
    "2|Chinese 'peach blossom' makeup: pink-peach blush across the cheeks and eyelids, soft brown liner flicked outward, rosy lip stain",
    "4|Japanese visual-kei makeup: sharp black winged liner, dark smoky lids fading to the temples, pale skin, deep red lips",
    "2|Japanese 'idol' makeup: shimmery pink lids, thick lower lash line, glossy peach lips, sparkly highlight on the inner corners of the eyes",
]

DESC["American & Glam"] = "Instagram glam, clean girl, Hollywood glamour and studio contour"
FAMILIES["American & Glam"] = [
    "3-4|2016 Instagram glam: razor-sharp carved pomade eyebrows, heavy cut-crease eyeshadow, matte liquid lipstick, dramatic winged eyeliner",
    "1-2|modern clean-girl makeup: ultra-dewy glass skin, brushed-up soap brows, glossy clear lip oil, sun-kissed bronzer, subtle cream blush",
    "3|classic Hollywood vintage glamour: classic matte crimson red lip, crisp liquid winged eyeliner, soft warm eyeshadow contouring",
    "3-4|studio contour makeup: deeply sculpted cheekbones, brightened under-eye baking, sharp nose contour, lined nude lip gloss",
    "2|soft-glam makeup: soft brown smoky lids, defined brows, fluttery lashes, glowing highlight and a rosy nude lip",
    "3|'old money' makeup: sleek groomed brows, neutral satin lids, a slight peach blush, a muted rose lip",
    "2-3|Latte makeup: warm brown tones on the lids, caramel blush, glossy brown lip, bronzed skin",
    "3|'Euphoria' makeup: shimmering coloured eyeshadow, rhinestones under the eyes, glossy lips, glittery liner",
    "2|strawberry-girl makeup: pink-red blush across the nose and cheeks, glossy red-pink lips, dewy skin, soft pink shimmer lids",
    "3|siren-eye makeup: elongated dark winged liner, smoky outer corners, defined brows, a nude glossy lip",
    "1|red-carpet-natural makeup: flawless skin, soft brown eyeshadow wash, groomed brows, neutral satin lips",
]

DESC["Doll & Anime"] = "porcelain doll, anime eyes and creepy-cute doll looks"
FAMILIES["Doll & Anime"] = [
    "3-4|ball-jointed porcelain doll makeup: stark matte porcelain foundation, rounded circular pink cheek blush, oversized top and bottom dolly false lashes, small heart-shaped rosebud lips",
    "3-4|anime eye enlargement makeup: white waterline pencil to artificially enlarge the eyes, exaggerated drawn-on lower lashes, soft pink gradient lip stain",
    "3|creepy-cute doll makeup: translucent skin, dramatic wide-eyed lower lash extensions, subtle freckles, dark berry stained lips",
    "2-3|kewpie-doll makeup: round pink blush apples, bright wide eyes with white inner-corner liner, glossy cherry lips, light freckles",
    "4|living-doll glam: flawless matte skin, huge spidery lashes, heavy round blush, tiny bright red bow lips",
    "2-3|manga-heroine makeup: big bright eyes with sparkly highlights painted in the iris area, soft pink lids, rosy cheeks, glossy pink lips",
    "4|anime-cosplay makeup: contoured round eyes, coloured lower lashes drawn on, bold coloured eyeshadow, glossy lips",
]

DESC["Goth & Dark"] = "trad-goth, nu-goth and cyber-goth"
FAMILIES["Goth & Dark"] = [
    "4-5|trad-goth makeup: stark white foundation, heavy solid black eyeshadow swept to the temples, razor-thin drawn-on arched eyebrows, sharp black matte lipstick",
    "3-4|nu-goth makeup: deep plum vampy lipstick, smoky burgundy eyeshadow, sharp cat-eye eyeliner, sculpted pale skin",
    "4-5|cyber-goth makeup: high-contrast graphic black eyeliner, neon lip color, metallic silver eyebrow accents, holographic skin highlighter",
    "3-4|vampire makeup: deathly pale skin, dark red-black smoky eyes, deep crimson lips with a faint bite stain, shadowy hollow cheeks",
    "3|soft-goth makeup: defined black kohl, dusty mauve lids, pale flawless foundation, a berry-stained lip",
    "4|witchy makeup: deep green-black smoky eyes, a dark purple lip, subtle silver stars at the temples, matte pale skin",
    "4-5|gothic doll makeup: powder-white skin, black winged liner, dark rosy blush, a small black glossy lip with red centre",
    "5|deathly-pale ghost makeup: grey-white skin, dark sunken eyes with a blue tint, faint blue lips, painted stitch lines at the mouth corners",
]

DESC["Punk & Grunge"] = "90s grunge, 70s punk and riot grrrl"
FAMILIES["Punk & Grunge"] = [
    "3|90s grunge makeup: dark brown smoky eyeshadow, defined black kohl liner, brushed brows, a muted brownish-red matte lipstick",
    "4|70s punk makeup: graphic black block eyeliner, bold blended blush, sharp contrast, deep oxblood lips",
    "3-4|riot grrrl makeup: bold black ring eyes, crisp red lipstick, graphic eyeliner marks, clean glowing skin",
    "4|pop-punk makeup: bold black wing, dark purple-pink lids, red-black lips, a little under-eye glitter",
    "3-4|e-girl makeup: tiny drawn hearts under the eyes, pink blush across the nose, winged liner, glossy pink lips",
    "4|scene-kid makeup: heavy black raccoon-eye liner, bright blue shadow, thin brows, black-pink lip",
]

DESC["Y2K & Retro-Futurism"] = "Y2K pop-star, frosted 90s and retro-futurism"
FAMILIES["Y2K & Retro-Futurism"] = [
    "3|Y2K pop-star makeup: frosty ice-blue shimmer eyeshadow, dark brown lip liner filled with ultra-glossy clear lip gloss, soft body glitter, thin plucked eyebrows",
    "3|late 90s frosted makeup: metallic silver eyeshadow, heavy frosted pink lipstick, glitter accents on the lids, soft rosy cheeks",
    "4|retro-futurism makeup: metallic chrome liquid eyeliner, holographic lip gloss, iridescent cheekbone highlight, pastel lilac eyeshadow",
    "3|Bratz-doll makeup: bright frosty eyeshadow, thick lined glossy lips, heavy highlighter, rhinestone accents",
    "3|90s supermodel makeup: brown-lined plum lips, warm bronze lids, thin groomed brows, matte tan skin",
    "3-4|space-age mod makeup: bold graphic white-and-black lashes drawn under the eyes, pale lips, 60s block-colour lids",
    "4|cyber-Y2K makeup: glossy blue lids with silver dots, metallic pink lips, tiny rhinestones along the brow",
]

DESC["Modest & Understated"] = "no-makeup makeup, soft nude wash, monochromatic nude"
FAMILIES["Modest & Understated"] = [
    "1|no-makeup makeup: sheer tinted moisturizer, subtle spot concealing, soft tinted lip balm, natural groomed brows, clear lash mascara",
    "1-2|soft nude wash makeup: warm nude eyeshadow wash, natural peach lip tint, soft brown pencil eyeliner, natural skin finish",
    "1-2|monochromatic nude makeup: muted taupe and warm beige tones across eyelids, cheeks, and satin nude lips",
    "1|fresh-faced makeup: bare skin with a light glow, curled lashes, a touch of cream blush",
    "1-2|bare-minimum makeup: just groomed brows, mascara and a rosy lip balm",
    "2|sunlit makeup: bronzed lids, a sprinkle of freckles, golden highlight, peachy-pink lips",
    "1|natural skin-first makeup: even skin tone with visible pores and freckles, soft brows, hydrated lips",
]

DESC["Overdone & Hyper-Stylized"] = "theatrical avant-garde, drag-inspired glam, maximalist festival"
FAMILIES["Overdone & Hyper-Stylized"] = [
    "5|theatrical avant-garde makeup: extreme graphic geometric eyeliner, crystal rhinestones encrusted around the eyes, metallic gold foil accents, dramatic exaggerated lip shaping",
    "4-5|drag-inspired overdone glam: heavy cut-crease block eyeshadow, dramatic layered triple-stacked false eyelashes, intense baking highlight, overlined two-tone ombre lips",
    "4-5|maximalist festival makeup: chunky face glitter, iridescent face gems, bold neon graphic face paint, intense metallic lip color",
    "5|high-fashion editorial makeup: sculptural coloured eyeshadow reaching the brows, bleached eyebrows, glossy metallic lips, pearls on the skin",
    "5|fantasy fairy makeup: iridescent scales along the cheekbones, pastel gradient lids, glitter stars, dewy glossy lips",
    "4-5|runway colour-block makeup: a single saturated colour on the lids and brow bone, a matching block of colour on the lips, bare skin",
]

DESC["Emo & Scene"] = "emo guyliner and bold kohl, scene-kid raccoon eyes with neon shadow"
FAMILIES["Emo & Scene"] = [
    "3|emo makeup: heavy defined black kohl eyeliner, pale flawless foundation, dark side-swept brows, a dark-berry lip",
    "3-4|emo makeup: thick black wing blended into smoky grey shadow, chipped black nail polish, pale skin, a muted plum lip",
    "4|scene-kid makeup: heavy black raccoon-eye liner, bright neon blue and pink shadow, thin brows, black-pink lip",
    "4|scene-kid makeup: rainbow-gradient lids, thick lashes, glitter under the eyes, glossy hot-pink lips",
    "4|alt-scene makeup: thick black liner with stars at the corners, purple lids, a tiny heart drawn on the cheek",
]

DESC["Masquerade & Veils"] = "painted masks, jewelled eyes and veiled glamour"
FAMILIES["Masquerade & Veils"] = [
    "4|masquerade makeup: a painted gold filigree mask around the eyes, crystal gems at the temples, deep burgundy lips",
    "4-5|jewelled masquerade makeup: rhinestone-edged eye mask in black and gold, shimmering lids, glossy dark red lips",
    "3-4|veiled gothic makeup: a smoky black eye with a sheer black veil over the face, pale skin, a deep wine lip",
    "4|mourning-glam makeup: dark smoky lids, a single small black gem on the cheekbone, black rose lip stain",
    "4-5|venetian carnival makeup: half the face in glitter and gold paint with a feather-lined eyebrow, ruby lips",
]

DESC["Neon Rave"] = "UV face paint, holographic gems, neon liner and festival glitter"
FAMILIES["Neon Rave"] = [
    "4|neon rave makeup: UV-reactive graphic liner in neon pink and electric blue, holographic face gems, chrome lips",
    "4-5|festival makeup: chunky iridescent glitter on the cheekbones, neon green wing, a holographic highlight",
    "4|cyber-rave makeup: sharp neon geometric lines on the temples, white liner, a glossy UV purple lip",
    "3-4|glow makeup: pastel neon gradient lids, glitter freckles, sparkling inner-corner highlights, a clear glossy lip",
]

STYLE_NAMES = list(FAMILIES)

# optional add-ons: kinds of extras that get rolled on top of a look (lo-hi levels)
EXTRAS = {
    "Lips": [
        "1|a tinted lip balm", "1-2|a juicy peach lip gloss", "2|a rosy lip stain", "2-3|a glossy {c} lip", "3|a satin {c} lipstick", "3-4|a matte {c} liquid lipstick",
        "3|a lined and overlined {c} lip", "2-3|a deep brown lip liner with a soft gloss", "3|a dark brown overlined lip liner with a nude gloss", "3-4|a dark lip liner with a lighter {c} centre", "4|a sharply lined {c} lip with dark liner", "4|a high-shine plumped {c} lip", "4-5|a glossy black cherry lip", "5|a metallic {c} lip", "5|a two-tone ombre {c} and {c2} lip",
    ],
    "Cheeks": [
        "1|a touch of cream blush", "1-2|a soft sun-kissed bronzer", "2|a rosy blush across the cheeks and nose", "2-3|a glowing champagne highlighter", "3|sculpted contour and a peach blush",
        "3-4|a strong {c} blush swept up to the temples", "4|a heavy baked highlighter", "4-5|bold sculpted cheeks with a strobe highlight", "5|a metallic {c} cheek wash",
    ],
    "Eyes": [
        "1|clear mascara", "1-2|a soft brown mascara", "2|a wash of {c} shimmer on the lids", "2|curled lashes with a little brown liner", "2-3|a soft winged {c} liner", "3|a smoky {c} eyeshadow",
        "3|a classic black wing", "3-4|full false lashes", "4|a graphic coloured liner in {c}", "3|a sharp black graphic wing", "3|a thin cat-eye wing in black liner", "3-4|thick defined black kohl liner", "4|dramatic double wing eyeliner",
        "4|heavy drawn-on lower lashes with thick black liner", "4-5|thick white lower liner and a black upper wing", "5|an extreme elongated black wing with drawn-on lower lashes", "4|a bold cut-crease in {c}", "4-5|a metallic {c} eyeshadow", "5|glitter-covered lids",
        "5|a graphic {c} shape painted around the eye", "4-5|a white graphic liner",
    ],
    "Details": [
        "1|a few natural freckles", "1-2|groomed natural brows", "2|a few tiny face gems at the temple", "2|a heart painted under one eye", "2-3|faux freckles drawn across the nose",
        "3|a glittery inner-corner highlight", "3|bleached brows", "3-4|small rhinestones under the eyes", "4|a metallic star sticker on the cheekbone", "4|a dark brow slit", "4-5|chunky face glitter along the cheekbones",
        "5|a row of crystal gems along the brow", "5|neon graphic face paint", "5|painted sparkling constellations across the face",
    ],
}
ADDON_NAMES = list(EXTRAS)

# the palette each family picks its extra colours from when you did not pick a Colour
PALETTE = {
    "Japanese & East Asian": ["petal pink", "coral", "burgundy", "peach", "rose pink"],
    "American & Glam": ["classic red", "rosy nude", "bronze", "mauve", "champagne"],
    "Doll & Anime": ["baby pink", "rose pink", "cherry red", "lilac", "soft berry"],
    "Goth & Dark": ["deep plum", "jet black", "blood red", "burgundy", "midnight blue"],
    "Punk & Grunge": ["oxblood", "charcoal", "dark brown", "muted red", "black"],
    "Y2K & Retro-Futurism": ["ice blue", "frosted pink", "silver", "lilac", "holographic"],
    "Modest & Understated": ["warm nude", "soft beige", "taupe", "peach", "rosy nude"],
    "Overdone & Hyper-Stylized": ["neon pink", "gold", "electric blue", "magenta", "emerald"],
    "Emo & Scene": ["black", "charcoal", "dark berry", "neon pink", "electric blue"],
    "Masquerade & Veils": ["gold", "deep burgundy", "jet black", "wine red", "silver"],
    "Neon Rave": ["neon pink", "electric blue", "neon green", "UV purple", "holographic silver"],
}


DESC["Pastel Kawaii"] = "soft pastel eyes, rosy blush, glossy pink lips, sparkle and tiny hearts"
FAMILIES["Pastel Kawaii"] = [
    "1-2|soft pastel makeup: sheer pink wash on the lids, a light flush of rosy blush, tinted glossy pink lips, lightly curled lashes",
    "2|pastel kawaii makeup: pink and lavender gradient lids with fine shimmer, soft blush across the cheeks and nose, glossy peach-pink lips",
    "2-3|sweet pastel makeup: baby blue shimmer on the lids, a soft pink wing, strawberry blush, juicy glossy pink lips with a highlight",
    "2-3|heart-blush makeup: rosy blush drawn in a soft heart shape on the cheeks, pastel pink lids with sparkle, glossy lips",
    "3|pastel glam: lilac and pink blended shadow with glitter at the inner corners, defined soft lashes, rosy blush, mirror-gloss pink lips",
    "3-4|pastel sparkle makeup: iridescent pastel lids with tiny rhinestones at the outer corners, dewy skin, pink blush and glossy lips",
    "3-4|kawaii glam: pastel gradient wing, delicate individual lashes, cheek blush with a tiny heart highlight, glossy strawberry lips",
    "4|bold pastel makeup: bright pink and baby blue graphic lids, glitter under the eyes, flushed cheeks, glossy hot-pink lips",
]
PALETTE["Pastel Kawaii"] = ["baby pink", "lavender", "baby blue", "peach", "mint green"]

DESC["Gyaru"] = "hime, agejo, onee and rokku gyaru: lenses, lashes, liner and glossy pink lips"
FAMILIES["Gyaru"] = [
    "1-2|onee gyaru makeup: neat soft winged liner, natural thick curled lashes, peach shadow, defined brows, satin pale skin, nude pink glossy lips",
    "2|soft gyaru makeup: brown circle lenses, curled false upper lashes, soft feathery lower lashes, pink shimmer on the lids, blended pink blush, glossy pink lips",
    "2-3|hime gyaru makeup: natural eye shape made to look bigger with brown circle lenses, thick curled false upper lashes, soft feathery lower lashes, winged liner extending the outer corner, soft pink shimmer shadow, pale smooth satin skin with a matte finish, blush blended high on the cheeks, a bright nose highlight, glossy plump pink lips",
    "3|agejo makeup: thick false upper lashes with extra clumps, brown gradient shadow with gold glitter on the lids, light brown circle lenses, peach blush, soft contoured cheeks, glossy coral-pink lips",
    "3-4|gyaru makeup: thick white eyeliner with thick false upper lashes, drawn-on spiky lower lashes, soft pink shimmer shadow, pale matte skin, a bright nose highlight, pink blush across the cheeks, glossy plump pink lips, a small silver stud piercing below the lower lip",
    "3-4|rokku gyaru makeup: smoky black-brown shadow, thick winged liner, long false lashes, pale matte skin, deep red berry lips",
    "4|hime doll gyaru makeup: brown circle lenses, very thick curled false upper lashes, drawn-on lower lashes with each lash a separate sharp stroke, thick winged liner, pink shimmer shadow, pale matte skin with high pink blush, nose highlight, glossy pink lips with a pale lip edge, a tiny lip piercing",
    "4-5|ganguro gyaru makeup: golden-tan skin, white concealer around the eyes, white lower lash line, pale pastel lips, dark brown liner, rhinestones and stickers at the outer corners of the eyes",
]
PALETTE["Gyaru"] = ["baby pink", "peach", "gold", "brown", "black"]
