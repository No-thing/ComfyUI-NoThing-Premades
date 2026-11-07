"""
Themes for the No_Thing Roulette Bar: ONE choice that steers the outfit, makeup and underwear dice together and gives them a matching
colour scheme (a main colour and a contrasting accent that every part shares). Everything else stays random.

Each theme: category, one line, the outfit style(s), makeup look(s) and underwear style(s) it may roll, and the colours.
"colours": (main colours, accent colours): one of each is picked per roll, so a new seed gives a new but still fitting palette.
Names must exist in outfit_data / makeup_data / underwear_data (checked by validate()).
"""
T = {}


def theme(name, cat, desc, outfit, makeup, underwear, main, accent):
    T[name] = dict(cat=cat, desc=desc, outfit=list(outfit), makeup=list(makeup), underwear=list(underwear), colours=(list(main), list(accent)))


# ---------------------------------------------------------------- dark
theme("Goth", "Dark", "black and grey with red or silver accents", ["Goth"], ["Goth & Dark"], ["Corsets", "Lace Classics"],
      ["black", "jet black", "charcoal grey"], ["blood red", "silver", "dark grey"])
theme("Goth Mommy", "Dark", "black leather and velvet, pentagram harnesses, blood red", ["Goth", "Dominant"], ["Goth & Dark"], ["Dominant", "Harness & Strappy"],
      ["black", "jet black"], ["blood red", "oxblood", "silver"])
theme("Mourning Veils", "Dark", "black lace, funeral veils, face veils and netting", ["Mourning Veils"], ["Masquerade & Veils", "Goth & Dark"], ["Masquerade & Veils", "Lace Classics"],
      ["black", "jet black"], ["charcoal grey", "deep burgundy", "dark plum"])
theme("Emo", "Dark", "black, grey and deep red, band tees, plaid micro skirts, strap harnesses, striped gloves and socks", ["Emo"], ["Emo & Scene"], ["Harness & Strappy", "Lace Classics"],
      ["black", "charcoal grey", "deep red"], ["dark purple", "white", "deep red"])
theme("Scene Kid", "Dark", "neon and black, tutus, stripes, big colourful hair", ["Scene"], ["Emo & Scene"], ["Kawaii & Sweet", "Harness & Strappy", "Lace Classics"],
      ["hot pink", "neon green", "electric blue"], ["black", "white", "purple"])
theme("Cyber Goth", "Dark", "black with neon green, UV purple and hot pink", ["Goth", "Latex"], ["Goth & Dark", "Neon Rave"], ["Latex & PVC", "Harness & Strappy"],
      ["black", "jet black"], ["neon green", "UV purple", "hot pink"])

# ---------------------------------------------------------------- neon and party
theme("Neon Raver", "Neon & Party", "contrasting neon colours, mesh, holographic, kandi", ["Neon Raver"], ["Neon Rave"], ["Sheer & Mesh", "Harness & Strappy"],
      ["neon pink", "neon green", "acid yellow", "neon orange"], ["electric blue", "UV purple", "neon pink"])
theme("Y2K Pop", "Neon & Party", "early 2000s pop: baby pink, silver, rhinestones", ["Y2K", "Y2K Brands"], ["Y2K & Retro-Futurism"], ["Branded Lounge", "Kawaii & Sweet"],
      ["baby pink", "hot pink", "baby blue"], ["silver", "white", "lilac"])
theme("Club Glam", "Neon & Party", "going-out glamour: fabric club dresses, black, gold and red", ["Dresses", "High Street Trend", "Luxury Houses"], ["American & Glam", "Overdone & Hyper-Stylized"], ["Luxury Couture", "Bodysuits & Teddies", "Designer"],
      ["black", "deep red", "gold metallic"], ["champagne", "gold metallic", "black"])
theme("Idol Stage", "Neon & Party", "J-pop stage costumes, sequins and ribbons", ["Idol Stage"], ["Japanese & East Asian", "Doll & Anime"], ["Babydolls & Slips", "Bodysuits & Teddies", "Lace Classics"],
      ["hot pink", "baby blue", "lavender"], ["white", "gold metallic", "pastel pink"])

# ---------------------------------------------------------------- cute
theme("Kawaii Pastel", "Cute", "pastel pink, mint and lavender, bows and charms", ["Harajuku Kawaii", "Sanrio Cute", "Pastel Pop"], ["Pastel Kawaii"], ["Kawaii & Sweet"],
      ["pastel pink", "lavender", "mint green"], ["white", "baby blue", "butter yellow"])
theme("Coquette", "Cute", "bows, lace, ribbons and pearls in soft pinks", ["Coquette"], ["Doll & Anime", "Modest & Understated"], ["Babydolls & Slips", "Bridal & Romantic"],
      ["blush pink", "ivory", "baby pink"], ["white", "dusty rose", "champagne"])
theme("Doll Style", "Cute", "frilly doll dresses and lace", ["Doll Style"], ["Doll & Anime"], ["Babydolls & Slips", "Kawaii & Sweet"],
      ["pastel pink", "ivory", "lavender"], ["white", "baby blue", "black"])
theme("Jirai Kei", "Cute", "black and pink ruffles and ribbons", ["Jirai Kei"], ["Japanese & East Asian", "Doll & Anime"], ["Kawaii & Sweet", "Lace Classics"],
      ["black", "black"], ["hot pink", "baby pink", "white"])
theme("Gyaru", "Cute", "tanned glam, mini skirts and platforms", ["Gyaru"], ["Gyaru", "Japanese & East Asian"], ["Designer", "Lace Classics"],
      ["white", "baby pink", "baby blue"], ["gold metallic", "black", "hot pink"])

# Gyaru: huge voluminous hair is the baseline, in the milk-tea / blonde / brown range
T["Gyaru"].update(hair=["Gyaru volume"], haircol=["Blonde", "Brown"], addons=["Legwear", "Garter belt", "Soft gloves & neck"])

# ---------------------------------------------------------------- edgy
theme("Punk", "Edgy", "tartan, studs and leather, black and red", ["Punk"], ["Punk & Grunge"], ["Harness & Strappy", "Lace Classics"],
      ["black", "red"], ["white", "silver", "red"])
theme("Grunge", "Edgy", "flannel, torn tees, washed-out and moody", ["Grunge"], ["Punk & Grunge"], ["Lace Classics", "Harness & Strappy", "Bodysuits & Teddies"],
      ["charcoal grey", "faded black", "forest green", "dark red"], ["cream", "mustard yellow", "washed denim blue"])
theme("Alt Brands", "Edgy", "Dolls Kill, Killstar, Disturbia and friends", ["Alt Brands"], ["Goth & Dark", "Punk & Grunge"], ["Harness & Strappy", "Latex & PVC"],
      ["black", "black"], ["hot pink", "silver", "blood red"])

# ---------------------------------------------------------------- glam and classic
theme("Luxury Editorial", "Glam", "luxury houses, editorial makeup, black, ivory and gold", ["Luxury Houses"], ["American & Glam", "Overdone & Hyper-Stylized"], ["Designer"],
      ["black", "ivory", "champagne"], ["gold metallic", "black", "deep red"])
theme("Luxury Couture", "Glam", "couture lingerie: sheer silk robes, black lace, pearls, gold-hardware harnesses", ["Luxury Houses"], ["American & Glam", "Modest & Understated"], ["Luxury Couture"],
      ["black", "ivory", "champagne", "nude"], ["gold metallic", "pearl white", "deep burgundy"])
theme("Old Money", "Glam", "preppy and heritage, navy and cream", ["Preppy Uniform", "Heritage Brands"], ["Modest & Understated"], ["Lace Classics", "Bridal & Romantic"],
      ["navy blue", "cream", "white"], ["forest green", "camel", "red"])
theme("Boudoir Romantic", "Glam", "soft lace, silk, ivory and blush", ["Dresses"], ["American & Glam", "Modest & Understated"], ["Luxury Couture", "Lace Classics", "Babydolls & Slips"],
      ["ivory", "blush pink", "champagne"], ["burgundy", "dusty rose", "gold metallic"])
theme("Bridal", "Glam", "white and ivory lace, veils", ["Dresses"], ["Modest & Understated", "American & Glam"], ["Bridal & Romantic"],
      ["white", "ivory"], ["champagne", "pale gold", "blush pink"])
theme("Pin-up", "Glam", "1950s pin-up: cherry red, black and white", ["Dresses"], ["American & Glam"], ["Pin-up Vintage"],
      ["cherry red", "black", "ivory"], ["white", "black", "powder blue"])
theme("Masquerade Ball", "Glam", "gowns, feathered masks, gold and deep red", ["Masquerade"], ["Masquerade & Veils"], ["Masquerade & Veils", "Luxury Couture", "Corsets"],
      ["black", "deep burgundy", "emerald green", "midnight blue"], ["gold metallic", "silver", "ivory"])

# ---------------------------------------------------------------- everyday
theme("Streetwear", "Everyday", "sneakers, logos, oversized and sporty", ["Streetwear Brands", "Athleisure Brands"], ["Modest & Understated", "American & Glam"], ["Branded Lounge"],
      ["black", "white", "grey"], ["neon orange", "electric blue", "red"])
theme("Cosy Baggy", "Everyday", "oversized, soft and comfortable", ["Baggy Comfy"], ["Modest & Understated"], ["Babydolls & Slips", "Lace Classics"],
      ["oatmeal beige", "grey", "dusty pink"], ["cream", "sage green", "lavender"])
theme("Cottage Mori", "Everyday", "linen, earthy tones, forest girl", ["Mori Girl"], ["Modest & Understated"], ["Lace Classics", "Bridal & Romantic"],
      ["cream", "sage green", "oatmeal beige"], ["terracotta", "dusty pink", "mustard yellow"])

# ---------------------------------------------------------------- kink fashion
theme("Dominant", "Kink", "leather, latex, harnesses, thigh boots", ["Dominant"], ["Goth & Dark", "Overdone & Hyper-Stylized"], ["Dominant", "Latex & PVC"],
      ["black", "jet black"], ["blood red", "silver", "gunmetal"])
theme("Submissive", "Kink", "satin, ribbons, ring collars, soft pastels", ["Submissive"], ["Doll & Anime", "Modest & Understated"], ["Submissive"],
      ["blush pink", "ivory", "white"], ["powder blue", "lavender", "soft red"])
theme("Latex Fetish", "Kink", "glossy latex and PVC", ["Latex"], ["Overdone & Hyper-Stylized", "Goth & Dark"], ["Latex & PVC"],
      ["jet black", "red", "hot pink"], ["silver", "black", "electric blue"])
theme("Kigurumi Mix", "Kink", "animal onesies mixed with harnesses", ["Kigurumi"], ["Doll & Anime"], ["Dominant", "Submissive"],
      ["pastel pink", "black", "lavender"], ["white", "blood red", "baby blue"])

# ---------------------------------------------------------------- beach, sport, techwear, jackets
theme("Beach Day", "Everyday", "huge sun hats, sheer white dresses, bikini strings, sand and sea colours", ["Beach"], ["American & Glam"], ["Sheer & Mesh", "Bridal & Romantic"],
      ["white", "sand beige", "turquoise", "coral"], ["sunny yellow", "seafoam green", "white"])
theme("Sporty Girl", "Everyday", "cropped hoodies over sports bras, low-waist sweatpants with a high-rise thong", ["Sporty Girl", "Athleisure Brands"], ["American & Glam"], ["Branded Lounge"],
      ["black", "grey", "baby pink", "white"], ["neon pink", "white", "lilac"])
theme("Boxing Gym", "Everyday", "Lonsdale, Everlast, Gymshark and Venum, red and black", ["Boxing & Gym Brands"], ["American & Glam"], ["Branded Lounge"],
      ["black", "red", "white"], ["red", "royal blue", "white"])
theme("Cyber Techwear", "Edgy", "cropped tech jackets, tactical harnesses, straps, masks and visors", ["Cyber Techwear"], ["Goth & Dark", "Neon Rave"], ["Harness & Strappy", "Sheer & Mesh"],
      ["black", "charcoal grey", "gunmetal"], ["neon green", "electric blue", "hot pink"])
theme("Y2K Techwear", "Neon & Party", "silver nylon cropped jackets, parachute pants, chrome and reflective straps", ["Y2K Techwear"], ["Y2K & Retro-Futurism"], ["Sheer & Mesh", "Branded Lounge"],
      ["silver metallic", "chrome", "black"], ["ice blue", "baby pink", "white"])
theme("Jacket Season", "Edgy", "cropped pilot, leather and puffer jackets over very little", ["Puffer & Cropped Jackets"], ["American & Glam"], ["Lace Classics", "Harness & Strappy"],
      ["black", "white", "baby pink", "silver metallic"], ["red", "ice blue", "chocolate brown"])

theme("Boho Hippie", "Everyday", "modern festival hippie: dreadlocks, beads and shells in the hair, patchwork skirts, crochet, layered crystal jewellery, hand-poked tattoos", ["Boho Hippie"], ["Modest & Understated", "American & Glam"], ["Boho Crochet"],
      ["rust orange", "cream", "forest green", "mustard yellow", "terracotta"], ["emerald green", "faded indigo", "gold metallic", "dusty rose"])

theme("Cosplay", "Neon & Party", "27 famous characters, each a complete fixed look (hair, outfit, props)", ["Cosplay"], [], [], ["black"], ["white"])
CATEGORY_ORDER = ["Dark", "Neon & Party", "Cute", "Edgy", "Glam", "Everyday", "Kink"]


def validate():
    """Names that do not exist anywhere (typos): returns a list of strings."""
    from . import makeup_data, outfit_data, underwear_data
    bad = []
    for n, t in T.items():
        bad += [f"{n}: outfit {s}" for s in t["outfit"] if s not in outfit_data.STYLES]
        bad += [f"{n}: makeup {s}" for s in t["makeup"] if s not in makeup_data.FAMILIES]
        bad += [f"{n}: underwear {s}" for s in t["underwear"] if s not in underwear_data.SETS]
    return bad


def listing():
    return [dict(name=n, cat=t["cat"], desc=t["desc"]) for n, t in sorted(T.items(), key=lambda kv: (CATEGORY_ORDER.index(kv[1]["cat"]), 0))]


# parts a theme can steer besides outfit / makeup / underwear style: hair categories and colours, and which underwear add-ons make sense
T["Emo"].update(hair=["Edgy cuts", "Bob & short", "Bangs"], haircol=["Black", "Two-tone", "Pink", "Blue", "Purple", "Red"], addons=["Legwear", "Garter belt", "Gloves & neck"])
T["Scene Kid"].update(hair=["Edgy cuts", "Waves & curls", "Ponytails & twin tails", "Bangs"], haircol=["Pink", "Pastel", "Blue", "Purple", "Two-tone"], addons=["Legwear", "Garter belt", "Gloves & neck"])

# Cyber Goth: no animal ears / tails or masquerade masks from the generic Headwear and Veils add-on pools
T["Cyber Goth"].update(addons=["Legwear", "Garter belt", "Gloves & neck", "Layer"])

# Idol Stage: sweet stage-wear underneath, no animal ears / tails from the headwear pool
T["Idol Stage"].update(addons=["Legwear", "Garter belt", "Soft gloves & neck"])

# basic goth: long straight hair, bangs and sidelocks, braids
T["Goth"].update(hair=["Straight", "Bangs"], haircol=["Black", "Brown", "Red", "Purple", "Silver / White"])

# the favourite hair (long thick braids, bangs with sidelocks) stays in every dark theme's pool
T["Goth"].update(hair=["Straight", "Bangs", "Buns & braids", "Waves & curls"])
T["Emo"].update(hair=["Edgy cuts", "Bob & short", "Bangs", "Straight", "Buns & braids"])
T["Scene Kid"].update(hair=["Edgy cuts", "Waves & curls", "Ponytails & twin tails", "Bangs", "Buns & braids"])

# Kawaii Pastel: garters and gloves only (the outfit brings its own pastel stockings, so no fishnets) (no masks, veils or horns from the generic add-on pools)
T["Kawaii Pastel"].update(addons=["Garter belt", "Soft gloves & neck"])
T["Kawaii Pastel"].update(hair=["Ponytails & twin tails", "Buns & braids", "Waves & curls", "Bangs", "Straight", "Half-up & retro"], haircol=["Pink", "Pastel", "Blue", "Purple", "Blonde", "Silver / White", "Two-tone"])

# Punk and Grunge: no veils, masks, bunny ears or horns from the generic add-on pools, at any skimpiness level
T["Punk"].update(addons=["Legwear", "Garter belt", "Gloves & neck"])
T["Grunge"].update(addons=["Legwear", "Garter belt", "Gloves & neck"])

# Alt Brands: no masks, veils, bunny / fox ears, tails, maid headpieces or bridal veils from the generic Headwear and Veils add-on pools
T["Alt Brands"].update(addons=["Legwear", "Garter belt", "Gloves & neck", "Layer"])

# Jacket Season: no bunny ears, masks or veils from the generic add-on pools
T["Jacket Season"].update(addons=["Legwear", "Garter belt", "Gloves & neck"])

# Luxury Editorial: polished and elegant (high-end office / red carpet), so natural hair colours, groomed styles, glam makeup and no bunny ears or masks
T["Luxury Editorial"].update(hair=["Straight", "Waves & curls", "Bob & short", "Half-up & retro", "Buns & braids"], haircol=["Black", "Brown", "Blonde"],
                             addons=["Legwear", "Garter belt", "Soft gloves & neck"], makeup=["American & Glam", "Modest & Understated"])

# Elegant themes: natural hair colours and groomed styles, glam makeup (no festival / avant-garde looks), no bunny ears, masks or horns
_ELEGANT_ADDONS = ["Legwear", "Garter belt", "Soft gloves & neck"]
_ELEGANT_COLS = ["Black", "Brown", "Blonde"]
T["Luxury Couture"].update(hair=["Straight", "Waves & curls", "Half-up & retro", "Buns & braids"], haircol=_ELEGANT_COLS, addons=_ELEGANT_ADDONS, makeup=["American & Glam", "Modest & Understated"])
T["Boho Hippie"].update(hair=["Dreads & Boho"], haircol=["Blonde", "Red", "Silver / White", "Brown", "Black"], addons=["Legwear", "Garter belt", "Soft gloves & neck"], makeup=["Modest & Understated", "American & Glam"])
T["Old Money"].update(hair=["Straight", "Waves & curls", "Bob & short", "Half-up & retro", "Buns & braids"], haircol=_ELEGANT_COLS, addons=_ELEGANT_ADDONS)
T["Boudoir Romantic"].update(hair=["Waves & curls", "Straight", "Half-up & retro", "Buns & braids", "Bangs"], haircol=_ELEGANT_COLS, addons=_ELEGANT_ADDONS)
T["Bridal"].update(hair=["Waves & curls", "Straight", "Half-up & retro", "Buns & braids"], haircol=_ELEGANT_COLS, addons=_ELEGANT_ADDONS)
T["Pin-up"].update(hair=["Half-up & retro", "Waves & curls", "Bob & short", "Ponytails & twin tails"], haircol=_ELEGANT_COLS + ["Red"], addons=_ELEGANT_ADDONS)
T["Club Glam"].update(hair=["Waves & curls", "Straight", "Ponytails & twin tails", "Half-up & retro", "Buns & braids"], haircol=_ELEGANT_COLS + ["Red"],
                      addons=_ELEGANT_ADDONS, makeup=["American & Glam"])

# Cosy Baggy: soft lingerie only (no sport gear such as phone straps) and no masks, veils or ears
T["Cosy Baggy"].update(addons=["Legwear", "Soft gloves & neck"])
