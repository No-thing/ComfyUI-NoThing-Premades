"""
The underwear / lingerie dataset for the No_Thing Underwear Roulette node.

Every entry is  "levels|text"  where levels is one number or a range (1-5):
    1 Soft       everyday comfort: cotton, seamless, full coverage
    2 Classic    pretty lace and satin sets, balconette / demi / high-waist
    3 Seductive  plunge, sheer, strappy, garters
    4 Bold       cut-outs, cages, open-back, strap-heavy
    5 Micro      minimal-fabric strap / string sets (still clothing descriptions only)
{c} = the set's main colour, {c2} = its accent colour.

Add your own lines anywhere - they are picked up after a ComfyUI restart (or put them in underwear_custom.json:
{"Corsets": ["3|my line"], "extras": {"Legwear": ["2|my stockings"]}} ).
Everything here describes what is WORN, never what is shown.
"""

LEVELS = ["Soft", "Classic", "Seductive", "Bold", "Micro"]
AMOUNTS = ["None", "Few", "Some", "Loaded"]            # add-ons: 0 / 1 / 2 / 3-4
AMOUNT_RANGE = {"None": (0, 0), "Few": (1, 1), "Some": (2, 2), "Loaded": (3, 4)}

SETS = {}
PALETTE = {}
DESC = {}

# ------------------------------------------------------------------------------------------------ designer styles
DESC["Designer"] = "famous lingerie house styles"
PALETTE["Designer"] = ["black", "ivory", "champagne", "blush pink", "deep red", "midnight navy", "emerald green", "nude"]
SETS["Designer"] = [
    "2-4|Agent Provocateur style luxury {c} lace corsetry set with contrasting {c2} boning channels and silk ribbon accents",
    "2-3|La Perla style exquisite Italian {c} Chantilly lace bralette and silk satin high-cut knickers set",
    "3-4|Honey Birdette style provocative strappy {c} cage bra with gold hardware, push-up cups and a matching suspender belt",
    "4-5|Bordelle style intricate adjustable elastic strap bondage-inspired {c} body harness dress",
    "3-4|Savage X Fenty style unlined {c} floral lace plunge bralette with high-waisted sheer mesh cheeky panties",
    "3|Fleur du Mal style {c} satin bullet bra and sheer embroidered tulle high-waisted garter panty set",
    "3-4|Maison Close style seductive sheer {c} mesh bodysuit with delicate satin piping and open-back cutouts",
    "2-3|Chantal Thomass style playful retro-glamour {c} corseted bustier with pom-pom accents and sheer lace trim",
    "2-3|Aubade style French embroidered {c} lace demi-cup bra with delicate satin bows and a matching lace garter belt",
    "3|Coco de Mer style opulent {c} silk velvet and metallic lace plunge bra with matching garter straps",
    "1-2|Intimissimi style minimalist Italian {c} silk satin slip dress with delicate sheer lace trim along the neckline",
    "2-3|For Love & Lemons style romantic {c} floral embroidered sheer tulle bra set with scalloped edge ruffles",
    "3-4|Bluebella style geometric {c} mesh and strappy harness bra with delicate gold hardware accents",
    "3-4|Thistle & Spire style architectural embroidered sheer {c} mesh bodysuit with dramatic cutouts",
    "2-3|Victoria's Secret style {c} satin push-up bra with rhinestone shine straps and a matching cheeky panty",
    "2|Hunkemoller style {c} floral lace balconette bra with a matching high-leg brief and scalloped edges",
    "1-2|Wacoal style smooth {c} contour t-shirt bra with a seamless high-waisted brief and subtle lace trim",
    "1-2|Triumph style {c} minimiser bra with soft floral lace overlay and a matching full-coverage brief",
    "2|Fantasie style full-cup {c} embroidered lace bra with a matching Brazilian brief",
    "2-3|Cosabella style stretchy {c} Italian lace racerback bralette and low-rise thong set",
    "2|Hanky Panky style signature {c} stretch lace low-rise thong with a matching unlined lace bralette",
    "1-2|Skims style seamless {c} second-skin bralette and high-waisted brief in sculpting stretch fabric",
    "1-2|Aerie style soft {c} lace-trimmed bralette with a matching cotton high-cut brief",
    "2-3|Journelle style sophisticated {c} silk and lace bra with matching tap pant shorts",
    "3-4|Oh La La Cheri style flirty {c} halter bustier with garter straps and a matching lace thong",
    "2-3|Lonely Label style vintage-inspired {c} crochet-lace bralette with a matching high-waisted brief",
    "3-4|Kiki de Montparnasse style daring {c} silk and lace bra with sheer cutout panties and satin ties",
    "3|Myla style contemporary British {c} embroidered tulle bra with matching ribbon-tie knickers",
    "2-3|Rigby & Peller style bespoke {c} silk satin bra with delicate lace overlay and matching high-waisted knickers",
    "3-4|Ann Summers style playful {c} lace-up front bra with a matching open-side thong and satin bows",
    "3|Dita Von Teese style 1940s-glamour {c} satin corset-bra with lace appliqué and a matching garter belt",
    "2-3|Natori style luxurious {c} embroidered silk charmeuse chemise with a plunging lace bodice",
    "1-2|Eres style minimalist French {c} triangle bra with a matching high-leg brief in sleek microfibre",
    "1-2|Stella McCartney style ethereal {c} satin bralette with a delicate scalloped lace edge and a matching brief",
    "1-2|Negative Underwear style sleek {c} ribbed cotton scoop bralette and high-cut brief",
    "2-3|Adore Me style romantic {c} lace-trimmed plunge bra with matching bow-front panties",
    "2-3|Gilda & Pearl style vintage-glamour {c} velvet and lace set with satin ribbon ties",
    "3|Fleur of England style playful {c} silk satin balconette bra with contrast piping and a matching high-waisted brief",
    "2|Elle Macpherson Intimates style relaxed {c} cotton-modal bralette and high-cut brief",
]

# ------------------------------------------------------------------------------------------------ lace classics
DESC["Lace Classics"] = "bra-and-panty sets in lace and satin"
PALETTE["Lace Classics"] = ["black", "ivory", "white", "blush pink", "burgundy", "nude", "dusty rose", "navy blue", "champagne"]
SETS["Lace Classics"] = [
    "1-2|{c} cotton bralette with a scalloped lace trim and matching high-waisted briefs",
    "1|{c} soft jersey bralette and full-coverage briefs with a thin elastic lace edge",
    "2|{c} balconette bra with embroidered floral lace cups and matching high-leg briefs",
    "2|{c} demi-cup bra with satin bow detailing and matching hipster briefs",
    "2|{c} full-cup lace bra with wide side support and matching Brazilian briefs",
    "2-3|{c} Chantilly lace triangle bralette and matching low-rise thong",
    "2-3|{c} lace plunge bra with a satin underband and matching tanga briefs",
    "2-3|{c} longline lace bralette with a scalloped hem and matching high-waisted panty",
    "2|{c} racerback lace bralette with adjustable straps and matching boyshorts",
    "2-3|{c} halter-neck lace bra with a deep V and matching string-side bikini briefs",
    "3|{c} strapless lace bandeau bra and matching high-cut knickers with sheer side panels",
    "3|{c} unlined sheer lace bralette with a deep scoop neckline and matching cheeky briefs",
    "3|{c} lace balconette bra with contrast {c2} satin trim and a matching lace garter belt",
    "3|{c} floral-embroidered plunge bra with a matching thong and sheer lace tie sides",
    "3-4|{c} lace-up front bralette with satin ribbon lacing and matching low-rise string panties",
    "3-4|{c} open-cup lace bra with decorative scalloped edging and matching split-gusset lace knickers",
    "2-3|{c} velvet bralette with satin piping and matching high-leg velvet briefs",
    "2|{c} embroidered tulle bra with matching high-waisted knickers and tiny satin bows",
    "3|{c} lace bralette with bow-tied shoulder straps and matching ruffle-trim cheeky panties",
    "3-4|{c} crochet lace triangle bikini-style bra and matching tie-side briefs",
    "4|{c} lace micro-cup bra with thin criss-cross straps and matching micro thong",
    "4-5|{c} sheer lace scalloped micro-bralette with matching string thong",
    "2|{c} satin bralette with a lace-trimmed neckline and matching tap shorts",
    "2-3|{c} lace boudoir set: soft-cup bra, high-waisted briefs and matching mesh garter straps",
    "1-2|{c} wireless lace bralette with a stretch-lace back and matching seamless thong",
    "3|{c} plunge push-up bra with delicate eyelash lace edges and matching lace-front thong",
    "3-4|{c} lace bra with side-boned corset styling and matching high-cut thong",
    "2-3|{c} two-tone lace bra and panty set in {c} and {c2} with contrast satin ribbon ties",
    "3|{c} bandeau lace bra with a front tie and matching sheer-back high-waisted panty",
    "4|{c} sheer lace plunge bra with a lace-trimmed keyhole centre and matching cheeky thong",
]

# ------------------------------------------------------------------------------------------------ corsets, cinchers, bustiers
DESC["Corsets"] = "corsets, bustiers and waist cinchers"
PALETTE["Corsets"] = ["black", "ivory", "burgundy", "deep red", "champagne", "midnight navy", "emerald green", "blush pink"]
SETS["Corsets"] = [
    "3-4|underbust steel-boned hourglass corset in heavy {c} satin with back satin ribbon lacing",
    "3-4|overbust corseted bustier in {c} with sheer mesh side panels and a traditional front steel busk closure",
    "3|victorian-style tight-lacing waist cincher corset in high-gloss {c} brocade fabric",
    "4|gothic {c} leather underbust harness corset with heavy silver buckle closures and D-rings",
    "4-5|cupless {c} leather waist-training corset with a riveted lace-up front and reinforced steel boning",
    "3-4|sheer boned {c} mesh underbust corset with visible contrast casing channels and garter loops",
    "3|romantic floral tapestried {c} overbust corset with a lace-up back and sweetheart neckline",
    "3-4|sheer {c} tulle corseted girdle belt with integrated adjustable garter straps and steel boning",
    "4|{c} latex waist-cincher corset with front hook-and-eye closure and a matte smooth finish",
    "3|vintage {c} satin bullet-bra corset with high-waisted shaping panels and suspender clips",
    "2-3|soft {c} lace-trimmed corset-style bustier top with a zip back and flexible plastic boning",
    "3|{c} satin corset with contrast {c2} lacing, a sweetheart neckline and attached suspender straps",
    "3-4|{c} lace-overlay corset with a plunging neckline and shimmering silver boning",
    "3|{c} velvet overbust corset with satin ribbon shoulder ties and a gold-tone busk",
    "2-3|{c} embroidered waspie belt corset with lace-up back and a floral appliqué panel",
    "3-4|{c} brocade steel-boned corset dress in a mini length with a fully laced back",
    "4|{c} PVC lace-up front underbust corset with silver eyelets and adjustable straps",
    "3|{c} satin longline bustier with underwire cups and six detachable garter straps",
    "3-4|{c} leather-look corset belt with triple buckle front closure and a ruched side",
    "2-3|{c} mesh and satin waist trainer corset with a front hook closure and back laces",
    "3|{c} jacquard overbust corset with a scalloped neckline and contrast piping",
    "4|{c} cutout corset top with a keyhole front, crisscross lacing and fine chain trim",
    "3-4|{c} rose-embroidered tulle corset with a pointed bodice and a satin bow at the back",
    "3|{c} halter-neck corset bustier with a deep V front and a boned satin back",
    "4-5|{c} cupless shelf bustier with a satin waist band, garter straps and a back-lacing finish",
]

# ------------------------------------------------------------------------------------------------ bodysuits and teddies
DESC["Bodysuits & Teddies"] = "teddies, bodysuits and one-piece lingerie"
PALETTE["Bodysuits & Teddies"] = ["black", "ivory", "red", "nude", "burgundy", "navy blue", "blush pink", "forest green"]
SETS["Bodysuits & Teddies"] = [
    "1-2|{c} soft ribbed cotton bodysuit with a scoop neck and thin straps",
    "2|{c} satin teddy with lace-trimmed cups, thin straps and a high-cut leg",
    "2-3|{c} lace plunge teddy with an open back, scalloped edges and snap closure",
    "3|high-cut satin teddy bodysuit in {c} with a deep plunging neckline, underwire cups and detachable satin ribbon garter straps",
    "3|{c} halter lace bodysuit with a keyhole front and a thong-cut back",
    "3-4|sheer {c} mesh bodysuit with delicate embroidered flowers and a plunging neckline",
    "3-4|{c} lace long-sleeve bodysuit with a plunging V and sheer panelled sides",
    "4|{c} strappy cutout bodysuit with a criss-cross waist and a high-cut leg",
    "3|{c} velvet bodysuit with a sweetheart neckline, satin trim and snap crotch",
    "3-4|{c} sheer tulle teddy with satin piping, an open back and a ribbon tie at the neck",
    "4|{c} open-back lace teddy with side cutouts and a plunging neckline down to the waist",
    "4|{c} caged bodysuit with ring-linked straps over a sheer mesh base",
    "3|{c} off-the-shoulder ruffled lace bodysuit with a sweetheart bust and high-cut legs",
    "3|{c} balconette teddy in embroidered tulle with scalloped leg openings",
    "4-5|{c} micro teddy with thin ribbon straps, lace cups and a thong cut",
    "3-4|{c} satin bodysuit with a lace-up front, a plunging neck and bow-tied straps",
    "4|{c} metallic lamé bodysuit with a deep plunge, thin straps and a thong back",
    "3|{c} turtleneck sheer mesh bodysuit with lace appliqué at the bust and hip",
    "4|{c} halter harness bodysuit with a choker collar, ring accents and a backless design",
    "3|{c} polka-dot tulle bodysuit with a satin bow at the bust and a cheeky back",
    "2-3|{c} stretch lace bodysuit with a square neckline, wide straps and a snap closure",
    "4-5|{c} ultra-sheer mesh bodysuit with strategic lace patches and thin ribbon ties",
]

# ------------------------------------------------------------------------------------------------ babydolls, slips, chemises, robes
DESC["Babydolls & Slips"] = "babydolls, chemises, slips and negligees"
PALETTE["Babydolls & Slips"] = ["black", "ivory", "champagne", "blush pink", "lavender", "dusty rose", "midnight navy", "sage green"]
SETS["Babydolls & Slips"] = [
    "1|{c} cotton nightgown with a lace-trimmed neckline and thin straps",
    "1-2|{c} silk bias-cut slip dress with a delicate lace neckline",
    "2|{c} satin chemise with an eyelash-lace bodice and adjustable spaghetti straps",
    "2-3|vintage silk bias-cut slip dress in {c} with delicate scalloped eyelash lace trimming along the plunging neckline and a thigh slit",
    "2-3|sheer floral tulle babydoll nightgown in {c} with satin shoulder ties, an empire waist gather and a matching micro lace thong",
    "3|{c} chiffon babydoll with a lace bust, a ribbon tie at the front and matching briefs",
    "3|{c} sheer open-front babydoll with ruffled trim and a satin ribbon tie",
    "3|{c} satin slip with a deep V neckline, a side slit and lace-trimmed hem",
    "3|{c} lace-trimmed satin negligee with a plunging neckline and a matching tie-front robe",
    "3|{c} velvet chemise with a lace bodice and thin straps",
    "3-4|{c} sheer mesh nightie with embroidered flowers over the bust and a thong",
    "3-4|{c} backless satin slip dress with a cowl neckline and a thigh-high slit",
    "2-3|{c} kimono-style satin robe with a tie waist, worn over a matching lace chemise",
    "3|{c} flowing sheer chiffon robe with marabou trim, open at the front over a matching set",
    "3|{c} embroidered organza gown with a sweetheart neckline, a long sheer skirt and matching knickers",
    "3-4|{c} lace-up front chemise in satin with a plunging neck and a mini hem",
    "2|{c} modal pyjama set with lace-trimmed camisole and shorts",
    "2-3|{c} satin camisole and tap shorts set with contrast {c2} piping",
    "3|{c} cross-back satin slip with adjustable straps and a lace-edged slit",
    "3-4|{c} sheer babydoll with a keyhole bust, bow ties and a ruffled micro-skirt hem",
    "2|{c} floral eyelet cotton chemise with a gathered bust and ribbon shoulder straps",
    "3-4|{c} long sheer lace gown with a deep plunge, long sleeves and a high thigh slit over a matching thong",
]

# ------------------------------------------------------------------------------------------------ harnesses and strappy architecture
DESC["Harness & Strappy"] = "bra harnesses, cage sets and strap-based lingerie"
PALETTE["Harness & Strappy"] = ["black", "red", "deep burgundy", "silver", "midnight navy", "blush pink", "gunmetal"]
SETS["Harness & Strappy"] = [
    "4|elastic multi-strap {c} pentagram chest harness overlaid over the collarbone and bust",
    "4|webbed spider-ring strap {c} harness framing the front torso and shoulders",
    "4|geometric caged {c} chest strap harness with central metallic ring joinery",
    "4-5|cross-body double pentagram {c} elastic body harness extending down to the waist",
    "4|gothic star-pattern neck-to-bust {c} strap harness with delicate chain dangles",
    "4|multi-tiered {c} elastic strap cage harness layered over the torso",
    "4|choker-to-bust {c} elastic harness with a metallic centre O-ring",
    "4|delicate {c} velvet-strap pentagram chest harness with miniature skull stud accents",
    "4|heavy-duty {c} vegan leather O-ring chest harness with silver rivet hardware",
    "4|studded {c} leather waist cincher harness with adjustable buckled side straps",
    "4|riveted gothic {c} leather cage harness wrapping across the ribcage and bust",
    "4|thick matte {c} leather body harness with dual brass D-rings and buckle closures",
    "4-5|cupless {c} leather cup harness with reinforced stitching and metallic O-ring joints",
    "4|double-wrapped {c} leather underbust harness with heavy metal buckle straps",
    "4|gothic spiked {c} leather chest strap harness with dangling silver chain links",
    "4|padded {c} leather chest harness with polished chrome ring hardware",
    "4-5|{c} leather garter harness with a rear-framing strap loop and polished buckles",
    "4|dual thigh-strap {c} leather harnesses with adjustable silver buckles",
    "4|crossed {c} elastic leg garters with central metallic O-ring joints",
    "4-5|waist-to-boot full-leg {c} cage harness with vertical connecting straps",
    "4|waist-cinching {c} leather garter belt with four reinforced metal suspender clips",
    "4|double-strap thigh-high {c} leg garters with studded leather accents",
    "4|cross-body {c} elastic hip harness with delicate silver chain accents",
    "4-5|gothic {c} leather waist-to-thigh harness with heavy-duty O-rings and leg cuffs",
    "4|{c} elastic bra harness with satin-covered cups and ring-linked straps over the shoulders",
    "4-5|{c} strappy cage bralette with a halter neck and matching string thong linked by gold rings",
    "3-4|{c} lace bralette with an attached elastic body harness and a matching high-waisted brief",
    "4|{c} sheer mesh bra set with an over-the-shoulder strap harness and a ring-front thong",
    "4|{c} velvet ribbon harness top with a heart-shaped centre ring and matching velvet briefs",
    "4-5|{c} multi-strap lingerie harness dress with an open front and a ring-linked waist",
    "4|{c} chain-detail strappy body harness worn over a lace bralette and thong set",
    "3-4|{c} bullet-bra cage top with criss-cross back straps and matching strappy briefs",
    "4|{c} elastic strappy hip belt with chain swags worn over a lace thong",
    "5|{c} minimal thin-strap micro harness set with gold ring joints and a matching string thong",
]

# ------------------------------------------------------------------------------------------------ sheer and mesh
DESC["Sheer & Mesh"] = "sheer mesh, tulle and see-through sets"
PALETTE["Sheer & Mesh"] = ["black", "nude", "ivory", "red", "pastel pink", "lavender", "smoke grey", "navy blue"]
SETS["Sheer & Mesh"] = [
    "3|translucent monochromatic sheer {c} mesh bralette and high-leg thong lingerie set",
    "3|sheer {c} chiffon open-front babydoll with ruffled trim and a sheer satin ribbon tie",
    "3-4|see-through {c} tulle corseted bodysuit with delicate sheer paneling",
    "3|{c} fine-mesh triangle bralette with picot-edged trim and a matching mesh thong",
    "3|{c} sheer tulle bra with embroidered vines and a matching high-waisted mesh brief",
    "3-4|{c} polka-dot Swiss dot mesh bodysuit with a plunging V and cheeky back",
    "3|{c} mesh balconette bra with scalloped lace edges and a matching sheer brief",
    "4|{c} sheer net bra with thin satin straps and a matching low-slung mesh brief",
    "3|{c} powder mesh long-sleeve crop top with a plunge neckline over a matching high-cut brief",
    "3-4|{c} sheer pleated chiffon bralette with a halter tie and matching bikini briefs",
    "4|{c} diamond-grid mesh bralette and matching high-leg thong",
    "3|{c} translucent tulle slip dress with satin straps and sheer tiered skirt",
    "3-4|{c} mesh bodystocking with strategically placed satin panels",
    "3|{c} sheer organza bralette with ruffle trim and a matching tie-side thong",
    "4|{c} fishnet bodysuit with a halter neck and a high-cut lace-edged leg",
    "4|{c} semi-sheer cut-out mesh teddy with a plunging neckline and lattice side panels",
    "3|{c} embroidered sheer mesh bra and garter belt set with floral appliqué",
    "3-4|{c} black-edged sheer ombre mesh bra and briefs fading from {c} to nude",
    "3|{c} glitter-flecked tulle bralette with silver trim and matching high-waisted briefs",
    "4|{c} dotted tulle plunge bodysuit with open sides and lace-up back",
    "3|{c} sheer lace-trimmed mesh bandeau bra with a matching brief and mesh garter straps",
    "4-5|{c} sheer micro mesh triangle top with ribbon ties and matching string bottoms",
    "3|{c} sheer mesh camisole set with scalloped lace trim and a matching mesh thong",
    "4|{c} sheer harness-style mesh crop with crossover straps and a matching high-waisted panty",
]

# ------------------------------------------------------------------------------------------------ latex, PVC, vinyl
DESC["Latex & PVC"] = "latex, PVC and vinyl lingerie"
PALETTE["Latex & PVC"] = ["jet black", "red", "smoke grey", "baby pink", "electric blue", "white", "hot pink", "violet"]
SETS["Latex & PVC"] = [
    "3-4|high-gloss {c} molded latex bikini lingerie set with a shiny reflective finish",
    "4|wet-look shiny {c} PVC waist-cincher corset with a front steel busk and back lacing",
    "3-4|translucent tinted {c} latex bodysuit with high-cut legs and a deep plunge neck",
    "3-4|high-shine liquid {c} vinyl push-up bra and a high-waisted strap-detailed panty set",
    "4-5|glossy {c} latex micro-bikini with silver ring connections and thin tie straps",
    "4|zip-up skin-tight {c} latex catsuit-style lingerie top with integrated garter straps",
    "3-4|molded {c} latex underwire bra with a matching lace-up latex garter belt",
    "4|wet-look {c} PVC cup-less corset top with a heavy metallic front zipper",
    "3-4|translucent smoky-grey rubberized latex bralette set with contrast trim",
    "4|slick reflective {c} patent leather lingerie set with riveted ring accents",
    "3|{c} latex bralette and high-waisted latex briefs with contrast {c2} piping",
    "4|{c} latex halter bodysuit with a deep plunge and a zip front",
    "3-4|{c} vinyl bustier with a front zip and matching high-cut vinyl shorts",
    "4|{c} latex lace-up front corset with matching latex thong and sleeves",
    "3|{c} shiny liquid-latex slip dress with thin straps and a thigh-high slit over matching briefs",
    "4|{c} PVC strappy cage bra and matching strap-side briefs with chrome buckles",
    "4-5|{c} latex micro-triangle top with chain ties and matching string bottoms",
    "3-4|{c} semi-translucent latex babydoll with a plunging front and matching briefs",
    "4|{c} latex garter belt with six metallic clips worn over a high-gloss thong",
    "3|{c} patent-leather-look bralette with gold zip detail and matching high-waisted briefs",
    "4|{c} wet-look vinyl teddy with a halter neck, a front zipper and a high-cut leg",
    "4-5|{c} PVC micro bikini with transparent straps and silver ring hardware",
]

# ------------------------------------------------------------------------------------------------ kawaii and sweet
DESC["Kawaii & Sweet"] = "cute pastel sets, maid, cat and bunny styles"
PALETTE["Kawaii & Sweet"] = ["pastel pink", "baby blue", "lavender", "mint green", "white", "peach", "lilac", "butter yellow", "cherry red"]
SETS["Kawaii & Sweet"] = [
    "2-3|{c} frilly maid-inspired lingerie set with a white lace apron, a sheer maid bra and ruffled bloomers",
    "3-4|cat-girl keyhole cutout lingerie set in {c} with a bell choker, a cat-ear headband and a velvet tail attachment",
    "2|{c} lace-trimmed satin ruffle bra and matching frilled panty set with satin bow accents",
    "2|{c} ribbon-tied silk panty set with adjustable side-tie satin ribbons and a ruffled elastic waistband",
    "2-3|sweet strawberry-print sheer mesh bralette and high-waist panty set with lettuce-trim edges in {c}",
    "3-4|fluffy plush faux-fur trimmed {c} micro-bikini with attached plush cat ears and tail",
    "2-3|{c} chiffon babydoll nightgown with sheer frilly shoulder ruffles and white bow accents",
    "3-4|soft plush velvet {c} bunny girl lingerie set with a fluffy white pom-pom tail and a lace-up front",
    "2|sheer organza {c} heart-patterned lingerie set with delicate scalloped elastic trim",
    "2|{c} gingham bralette with ruffled straps and matching frilly high-waisted briefs",
    "2|{c} cherry-print cotton bralette and high-waisted briefs with white lace edging",
    "2-3|{c} bow-front satin bra and panty set with puffy ribbon straps and tiny pearl buttons",
    "2|{c} cloud-print cotton bralette with a ruffle hem and matching boyshorts",
    "3|{c} lace heart-cutout bralette with satin bows and matching heart-front panties",
    "3-4|{c} kitten-ear lace bralette with a ribbon choker and matching cheeky briefs",
    "2-3|{c} teddy-bear print pyjama cami set with lace-trimmed shorts",
    "3|{c} sheer polka-dot tulle babydoll with a heart-shaped bust cutout and a ruffled hem",
    "2-3|{c} strawberry-print lace bustier with ruffled straps and a matching frilly skirt-panty",
    "3-4|{c} bunny-ears-and-tail lingerie set: lace bralette, thong with a fluffy pom-pom tail and a satin bow tie collar",
    "3|{c} kimono-style short satin robe with sheer sleeves, a bow sash and a matching tie-side panty",
    "2-3|{c} french-maid-style satin corset with a frilled white apron front and ruffled garter straps",
    "3|{c} nurse-inspired lingerie set: white-trimmed bra and panties with a cross emblem and a tiny matching apron",
    "2|{c} rainbow-ruffle cotton bralette and matching bloomer shorts",
    "3|{c} sheer pastel star-print mesh bralette with matching high-waist panty and satin ties",
]

# ------------------------------------------------------------------------------------------------ branded lounge and sporty
DESC["Branded Lounge"] = "logo-band cotton, sporty and lounge sets"
PALETTE["Branded Lounge"] = ["white", "heather grey", "black", "navy blue", "baby pink", "sage green", "red", "beige"]
SETS["Branded Lounge"] = [
    "1-2|Calvin Klein style iconic elastic logo waistband unlined triangle bralette and a matching high-cut waist cotton thong set in crisp {c}",
    "1-2|Calvin Klein style {c} heathered cotton racerback bralette with a wide white branded elastic chest band and matching boyshorts",
    "1-2|Calvin Klein style {c} ribbed cotton scoop-neck cropped tank top with a soft branded waistband and matching cheeky hiphugger underwear",
    "3|Playboy style {c} satin push-up bustier corset with plush faux-fur trim along the sweetheart neckline and satin bow accents",
    "3-4|Playboy style high-cut {c} satin teddy bodysuit with a deep plunging neckline, underwire cups and detachable satin ribbon garter straps",
    "3|Playboy style sheer {c} mesh bustier with satin bone piping, plush white marabou fur trim and satin bow-tied side cutouts",
    "2-3|Victoria's Secret style plush {c} velvet demi-cup bra with rhinestone-embellished shine straps and a matching lace-waist cheeky panty",
    "1|{c} ribbed cotton tank-style bralette with a soft elastic underband and matching high-rise briefs",
    "1|{c} seamless sports bralette with a wide band and matching seamless high-cut briefs",
    "1-2|{c} microfibre racerback sports bra with mesh panels and matching high-waisted briefs",
    "1|{c} soft terry lounge bralette and matching boyleg shorts",
    "1-2|{c} cotton triangle bralette and matching hipster briefs with a branded waistband",
    "1-2|{c} jersey crop camisole with a lettuce-edge hem and matching high-leg briefs",
    "1|{c} basic cotton bralette and boy shorts set with a stitched logo band",
    "2|{c} logo-jacquard bralette with a wide elastic band and matching thong",
    "2|{c} satin-trim sports bra with a keyhole back and matching bike shorts",
    "1-2|{c} thermal ribbed long-sleeve top with a scoop neck and matching ribbed briefs",
    "2|{c} velour lounge set: a cropped cami with a lace trim and matching soft shorts",
    "2-3|{c} cut-out sports bralette with strappy racerback and matching high-cut thong",
    "1-2|{c} seamless ribbed longline bralette and matching mid-rise briefs",
    "2|{c} mesh-panel sports bra and matching high-waisted briefs with contrast {c2} side stripes",
    "1-2|{c} organic-cotton bralette with a scoop neck and matching full-coverage briefs",
]

# ------------------------------------------------------------------------------------------------ pin-up vintage
DESC["Pin-up Vintage"] = "1940s-1960s pin-up and retro lingerie"
PALETTE["Pin-up Vintage"] = ["black", "ivory", "cherry red", "powder blue", "soft pink", "emerald green", "polka-dot white", "peach"]
SETS["Pin-up Vintage"] = [
    "3|vintage steel-boned {c} satin corset bustier with a traditional front busk closure, tight back ribbon lacing and attached adjustable garter straps",
    "2-3|1950s-style {c} satin bullet bra with matching high-waisted girdle briefs",
    "2-3|{c} pin-up satin high-waisted brief and underwire bra set with a bow at the bust",
    "3|{c} retro waspie with ribbon-trimmed edges, six suspender clips and matching tap pants",
    "2-3|{c} polka-dot halter bra and ruffled high-waisted bikini-style briefs",
    "3|{c} lace-trimmed long-line bra and matching suspender belt with seam-stockings",
    "3|1940s-style {c} satin and lace corset-bra with matching French knickers",
    "2|{c} gingham pin-up bralette with a front bow and high-waisted briefs",
    "2-3|{c} vintage girdle with lace panels, side zip and attached garter clips",
    "3|{c} burlesque-style bustier with satin bows, feather trim and a matching high-cut brief",
    "3|{c} cap-sleeve lace teddy with a sweetheart neckline and satin ribbon ties",
    "2-3|{c} 1960s-style babydoll set with a ruffled hem and matching bloomer briefs",
    "3|{c} bombshell bustier with a pointed cup, a boned waist and a lace-up back",
    "2-3|{c} cherry-print satin bra and matching button-front high-waisted briefs with a ribbon bow",
    "3|{c} retro garter-belt set in satin with a matching bralette and seamed stockings",
    "3-4|{c} pin-up cutout swim-style teddy with a plunging neckline and a high-cut leg",
]

# ------------------------------------------------------------------------------------------------ bridal and romantic
DESC["Bridal & Romantic"] = "white lace, bridal and boudoir sets"
PALETTE["Bridal & Romantic"] = ["ivory", "white", "champagne", "blush pink", "pale gold", "powder blue", "soft lilac"]
SETS["Bridal & Romantic"] = [
    "2-3|{c} bridal lace bra and matching high-waisted briefs with satin ribbon bows",
    "3|{c} bridal garter belt set with a lace balconette bra, a matching thong and a blue ribbon garter",
    "3|{c} bridal lace bodysuit with a plunging neck, an open back and scalloped edges",
    "2-3|{c} silk bridal chemise with a lace bodice and a matching robe",
    "3|{c} bridal corset with lace-up back, pearl buttons and sheer tulle trim",
    "3|{c} sheer floral lace bridal babydoll with a satin bow and a matching thong",
    "2-3|{c} embroidered tulle bridal bra and matching brief with pearl-detail straps",
    "3|{c} boudoir set: lace bralette, high-waisted knickers, garter belt and satin gloves",
    "2|{c} satin bridal tap-short set with a lace-trimmed camisole",
    "3|{c} long lace bridal negligee with a plunging neckline, a thigh slit and a satin sash",
    "3|{c} bridal teddy with embroidered lace cups, a sheer waist and a ribbon-tied back",
    "2-3|{c} romantic lace-up bralette set with scalloped trim and matching high-cut briefs",
]

# ------------------------------------------------------------------------------------------------ add-ons
# ------------------------------------------------------------------------------------------------ dominant, submissive, masquerade
DESC["Dominant"] = "dominant lingerie: leather and latex harness sets, pentagram harnesses, goth mommy and kigurumi mix-ups"
PALETTE["Dominant"] = ["black", "deep red", "oxblood", "gunmetal", "silver"]
SETS["Dominant"] = [
    "4|{c} leather underbust corset with a matching ring-linked chest harness and thong",
    "4-5|{c} pentagram chest harness over a sheer mesh bralette with a leather waist belt and briefs",
    "4|goth-mommy {c} velvet corset with a pentagram strap harness, a spiked choker and long lace gloves",
    "4-5|{c} latex bra top with a leather body harness, a high-cut latex brief and thigh cuffs",
    "4|{c} PVC bustier with silver buckles, a garter harness and matching string briefs",
    "4-5|{c} caged leather bralette with a collar-linked harness and a ring-front thong",
    "4|{c} sheer bodysuit under a heavy leather chest harness with silver rivets",
    "5|{c} minimal strap harness set with O-rings, a chain collar and a matching string thong",
    "4|{c} kigurumi onesie with fox ears unzipped to the waist, a leather chest harness over a bralette",
    "4|{c} cat kigurumi hoodie worn open over a strappy cage bra harness and high-waisted briefs",
    "4-5|{c} wolf kigurumi top pulled down at the shoulders with a pentagram harness and matching briefs",
    "4|{c} latex corset dress with a front zip, a ring collar and long latex gloves",
    "3-4|{c} leather bralette and high-waisted leather briefs with a garter belt and thigh-high stockings",
    "4-5|{c} wet-look cut-out teddy with a lace-up front, a studded collar and matching armbands",
]

DESC["Submissive"] = "soft submissive lingerie: satin ribbons, ring collars, delicate harnesses and sheer sets"
PALETTE["Submissive"] = ["blush pink", "ivory", "white", "powder blue", "lavender", "soft red"]
SETS["Submissive"] = [
    "3|{c} satin ribbon-collar lace bralette set with matching high-waisted briefs",
    "3-4|{c} sheer babydoll with a ring-front satin collar and a matching thong",
    "4|{c} delicate elastic ribbon harness over a lace bralette with ruffled briefs",
    "3-4|{c} satin teddy with a ribbon-tie collar and thigh-high stockings with bows",
    "4|{c} velvet ribbon heart-ring harness top with matching velvet briefs and satin wrist cuffs",
    "4-5|{c} sheer mesh bodysuit with a satin choker and ribbon ties at the hips",
    "3|{c} pastel kigurumi onesie unzipped at the chest over a lace bralette and briefs",
    "4|{c} bunny kigurumi hoodie worn open over a satin bralette with a ribbon harness and ruffled briefs",
    "3-4|{c} lace slip set with a bell collar and satin ankle ribbons",
    "4|{c} garter belt set with satin bows, a ring choker and lace-top stockings",
    "4-5|{c} minimal sheer ribbon set with a pearl choker and satin ties",
]

DESC["Masquerade & Veils"] = "masquerade lingerie with lace eye masks, veils, long gloves and feathers"
PALETTE["Masquerade & Veils"] = ["black", "burgundy", "ivory", "gold", "midnight navy", "emerald green", "deep red"]
SETS["Masquerade & Veils"] = [
    "3-4|{c} corset bustier with gold embroidery, a matching thong and a lace masquerade eye mask",
    "4|{c} sheer lace bodysuit with feather trim and a jewelled venetian eye mask",
    "4|{c} velvet corset with a ribbon-tie bralette, garter belt and a veil of black lace over the face",
    "3-4|{c} lace bra set with a long sheer train, opera gloves and a feathered half mask",
    "4-5|{c} mesh teddy with gold appliqué, thigh-high stockings and a beaded masquerade mask",
    "3-4|{c} mourning-lace bralette set with a long black veil and a jet-bead choker",
    "4|{c} gothic bridal-style sheer bodysuit with a birdcage veil and long lace gloves",
]

# ------------------------------------------------------------------------------------------------ luxury couture
DESC["Luxury Couture"] = "high-end designer lingerie: sheer silk robes, couture lace, gold-hardware straps, thigh straps and patterned harnesses (stars, pentagrams, art deco)"
PALETTE["Luxury Couture"] = ["black", "ivory", "champagne", "gold", "nude", "deep burgundy", "midnight navy", "pearl white", "emerald green", "blush pink"]
SETS["Luxury Couture"] = [
    # sheer robes and silks
    "2-3|a floor-length sheer {c} silk organza robe worn open over a matching {c2} lace bralette and high-waisted briefs",
    "3|a gossamer {c} chiffon robe with marabou feather cuffs and hem, worn open over a delicate {c2} lace balconette set",
    "3-4|a long sheer {c} tulle robe with hand-embroidered gold floral appliqué, worn off the shoulders over a fine lace bodysuit",
    "2-3|a liquid {c} silk charmeuse kimono robe with a satin sash left untied, over a matching lace-trimmed bra and thong set",
    "3-4|a cathedral-length sheer {c} cape-sleeve robe edged in Chantilly lace over a plunging {c2} lace teddy",
    "3|a sheer {c} velvet-devoré robe with a trailing hem, worn open over a silk satin bralette and French knickers",
    # couture lace
    "2-3|a hand-finished {c} Leavers lace bralette with scalloped edges and silk ribbon straps and matching high-cut briefs",
    "3|an ultra-fine {c} Chantilly lace plunge bra with a gold-plated centre ring and a matching lace suspender belt",
    "3-4|a bespoke {c} corded lace and sheer tulle bodysuit with a sculpted plunging neckline and an open lace-up back",
    "3|a couture {c} guipure lace longline bra with satin underbust boning and a matching lace thong with gold clasps",
    "2-3|a {c} silk satin and French lace bullet-bra set with a high-waisted garter panty and fine silk garters",
    "3-4|a {c} lace-covered underwire corset with crystal-beaded trim, hand-sewn pearls at the neckline and a matching sheer panty",
    "3|a haute couture {c} gold-threaded metallic lace bralette set with a silk satin ribbon bow at the centre",
    # strap and harness designs
    "4|an elegant {c} leather and gold-chain bra harness with fine straps crossing the chest and a matching strappy brief",
    "4|a delicate {c} satin-ribbon body harness with gold O-rings, thin straps framing the chest, waist and hips over a sheer bodysuit",
    "4-5|a luxury {c} fine-strap cage bra with gold hardware and a matching hip and backside strap harness with gold buckles",
    "4|a {c} sheer mesh bodysuit with a high-end pentagram strap harness in {c2} satin elastic and gold rings across the chest",
    "4-5|a {c} five-point star strap harness bra with gold rings at each point and a matching star-pattern strappy thong",
    "4|a {c} geometric art-deco strap harness bralette with gold-plated buckles and a matching low-slung strappy brief",
    "4-5|a {c} constellation pattern chain harness with tiny crystal stars at every joint, worn over a sheer lace bralette and briefs",
    "4|a {c} sacred-geometry strap harness with hexagon links and gold hardware worn over a fine mesh bodysuit",
    "4-5|a {c} butterfly-wing strap harness bra in satin elastic with gold rings and a matching butterfly-back hip harness",
    "4|a {c} diamond-lattice strap harness across the torso with a plunging neckline, gold ring accents and silk satin briefs",
    "4-5|a {c} filigree gold-chain bra harness with draped chains falling to the waist and a matching delicate waist chain and thong",
    "4|a {c} crystal-studded strap harness bralette with swan-neck straps and a matching high-cut brief with side straps",
    # thigh straps, garters, hip pieces
    "3-4|a {c} lace-trimmed satin bralette set with fine adjustable thigh straps with gold buckles and a matching suspender belt",
    "3-4|a {c} silk and lace corset-belt with long suspender straps, gold clips and matching thigh garters in {c2} lace",
    "4|a {c} delicate leather thigh-strap garter set with gold rings, worn over sheer silk stockings and a lace thong",
    "4-5|a {c} luxury strap-only set: fine gold-ringed bra straps, a waist strap, double thigh straps and a matching backside strap harness",
    "3-4|a {c} sheer lace bodysuit with a built-in strap harness at the hips and fine adjustable thigh straps with gold hardware",
    # embellished and statement
    "3-4|a {c} silk-velvet balconette set encrusted with crystals in a baroque pattern and a matching beaded garter belt",
    "3|a {c} corset-style bustier in jacquard silk with gold thread embroidery, a plunging sweetheart neckline and matching silk briefs",
    "3-4|a {c} pearl-strand bralette with draped pearl straps and a matching pearl-trimmed lace thong, under a sheer robe",
    "4|a {c} crystal-fringe bralette with cascading crystal strands and a matching sheer skirt of beads over a thong",
    "3-4|a {c} feathered silk and tulle balconette set with ostrich feather trim at the cups, a sheer gown-length robe and delicate straps",
    "5|a barely-there {c} gold-chain and sheer silk-thread lingerie set, a jewelled micro bra and a fine-chain waist and hip harness",
    "4-5|a {c} sheer second-skin bodysuit with a strategic gold-embroidered pattern and a built-in strap harness at the chest",
]

DESC["Boho Crochet"] = "boho festival lingerie: crochet and macramé sets, shell and bead body chains, fringe, sheer kimonos and hand-dyed fabrics"
PALETTE["Boho Crochet"] = ["cream", "rust orange", "mustard yellow", "sage green", "emerald green", "terracotta", "faded indigo", "dusty rose"]
SETS["Boho Crochet"] = [
    "2|a hand-crocheted {c} triangle bralette with long ties and matching crochet briefs",
    "2-3|a yellow-and-orange striped crochet bralette with a {c2} flower motif and matching high-cut briefs",
    "3|a macramé {c} bralette with knotted cord straps and a matching macramé string thong",
    "3|an open-weave {c} crochet bodysuit with a plunging neckline, worn over nothing but a thin {c2} thong",
    "3-4|a {c} crochet halter bikini-style set with wooden bead ties and a layered gold belly chain",
    "3-4|a sheer {c} embroidered voile kimono robe worn open over a {c2} crochet bralette and briefs",
    "4|a tiny {c} crochet triangle top and string bottoms with seashell charms, worn with layered shell and bead body chains",
    "4|a fringed {c} suede-look bralette and low-slung fringe micro skirt over a beaded thong",
    "4-5|a hand-beaded {c} fishnet mini dress worn over a strappy crochet {c2} bikini set",
    "4-5|a delicate chain-and-bead body harness in gold and {c} wooden beads over a minimal {c2} crochet set",
    "2-3|a tie-dye {c} cotton bralette and matching boyshorts",
    "3|a loose open-knit {c} cardigan worn off the shoulders over a crochet bralette and briefs",
    "3-4|a sheer {c} printed sarong tied low on the hips over a crochet {c2} bikini set with a belly chain",
    "4|a {c} macramé bodysuit with open-lace panels and bead-tipped ties",
    "3|a sheer {c} embroidered floral cage-strap bustier with delicate lace trim and a matching sheer {c2} thong",
    "3-4|an olive-and-gold open-weave crochet bralette with long fringe ties and a matching crochet string bottom with leopard-print cord ties",
]

EXTRAS = {
    "Legwear": [
        "2-5|coarse wide-gap large-net fishnet pantyhose extending up to a high waist",
        "2-5|micro-mesh delicate fine fishnet tights with a seamless toe and a smooth waistband",
        "3-5|whale-net large diamond-patterned fishnet stockings with thick lace top bands",
        "2-5|classic vertical back-seam sheer thigh-high stockings with wide lace tops",
        "1-4|polka-dot Swiss dot sheer pantyhose with a delicate elastic waistband",
        "2-5|gothic floral lace patterned tights with intricate botanical lace weaves",
        "2-4|opaque gradient ombre nylon stockings transitioning from dark black to a sheer tone",
        "2-5|sheer ultra-thin 10-denier thigh-high stockings held up by double silicone grip bands",
        "3-5|distressed shredded fishnet tights with laddered run-stop holes and ripped mesh texture",
        "2-5|geometric diamond-grid mesh tights with a reinforced high-waist band",
        "1-3|opaque {c} knee-high socks with a lace cuff",
        "1-3|sheer {c} thigh-high stockings with a bow at the top",
        "2-4|{c} lace-top hold-up stockings with a delicate back seam",
        "2-4|{c} over-the-knee socks with a ribbon bow and a lace trim",
        "3-5|{c} sheer stockings attached to the garter belt with satin clips",
        "2-4|{c} sheer tights with an embroidered floral ankle motif",
        "2-4|{c} crystal-studded sheer stockings with a back seam",
        "1-3|{c} ribbed knit over-the-knee leg warmers",
        "3-5|{c} patterned lace thigh-highs with a wide scalloped top",
        "2-4|{c} glossy sheer thigh-high stockings with a contrasting {c2} heel panel",
    ],
    "Garter belt": [
        "3-5|a wide {c} satin garter belt with six metal clips",
        "3-5|a {c} lace garter belt with adjustable suspenders",
        "3-5|a {c} velvet suspender belt with a bow at the front",
        "4-5|a thin {c} elastic garter belt with ring-linked straps",
        "3-5|a {c} leather suspender belt with polished buckle details",
        "3-5|a {c} embroidered tulle garter belt with satin ribbons",
        "2-4|a pair of {c} lace thigh garters with satin bows",
        "2-4|a {c} lace leg garter with a small charm",
    ],
    "Gloves & neck": [
        "3-5|opera-length sheer {c} mesh stretch gloves extending past the elbows",
        "2-5|wrist-length scalloped floral lace gloves with delicate thumb loops",
        "3-5|elbow-length fingerless fishnet gloves with elastic thumb-ring loops",
        "3-5|fingerless matte leather gloves with silver wrist buckle straps and knuckle cutouts",
        "2-5|sheer embroidered tulle gloves with delicate floral threadwork accents",
        "3-5|gothic black leather choker with a central polished steel O-ring and a rear buckle",
        "2-5|scalloped black lace ribbon choker with a hanging teardrop crystal pendant",
        "3-5|spiked gothic leather collar with a heavy D-ring leash attachment point",
        "2-5|minimalist thin elastic strap choker with a tiny centre metallic ring",
        "2-4|a {c} velvet ribbon choker with a small cameo",
        "2-4|{c} satin opera gloves with a bow at the wrist",
        "3-5|a {c} pearl-strand choker with a satin ribbon tie",
        "3-5|a {c} lace-up neck corset collar with a front ring",
        "2-4|a {c} lace choker with a heart-shaped charm",
    ],
    "Headwear": [
        "2-5|a wired lace bunny ears headband with flexible shaping and sheer lace mesh fill",
        "3-5|a pleather high-gloss bunny mask headband with tall pointed ears and a nose cover",
        "2-5|a plush velvet bunny ears headband with satin inner ear lining",
        "2-5|a lace cat-ear headband with delicate hanging silver jingle bells and satin bows",
        "3-5|a gothic devil horn headband made of polished black acrylic with chain dangles",
        "3-5|a sheer lace eye mask with delicate ribbon ties for a masquerade aesthetic",
        "2-5|a soft faux-fur fox ears headband with a clip-on matching plush tail",
        "2-4|a gothic maid lace headpiece band with scalloped edges and dual side satin ribbons",
        "3-5|a leather harness headpiece with thin face-framing straps and silver ring hardware",
        "2-4|a {c} satin bow headband",
        "2-4|a {c} lace veil-style headpiece with a small bow",
        "3-5|a {c} feather fascinator clipped in the hair",
        "2-4|a {c} velvet cat-ear headband with a bow",
    ],
    "Veils & masks": [
        "3-5|a black birdcage veil covering the eyes and nose",
        "3-5|a long black mourning veil falling over the face",
        "3-5|a sheer black mesh face covering with only the lips visible",
        "3-5|a lace face veil with a beaded edge, hooked behind the ears",
        "3-5|a gothic lace mantilla veil draped over the head and shoulders",
        "3-5|a venetian masquerade half mask with gold filigree and ribbon ties",
        "3-5|a feathered masquerade eye mask with crystal accents",
        "3-5|a black lace masquerade mask with a delicate crystal gem",
        "4-5|a sheer {c} tulle face veil gathered at the chin",
        "3-5|a jewelled {c} half mask with tall feathers on one side",
        "3-5|a {c} bridal-style fingertip veil over the hair",
        "3-5|a {c} lace face veil with a satin ribbon at the nape",
    ],
    "Layer": [
        "2-4|an open sheer {c} robe with feather trim at the cuffs",
        "2-4|a flowing {c} satin kimono robe tied loosely at the waist",
        "1-3|an oversized white button-up shirt hanging open",
        "2-4|a fluffy {c} marabou-trimmed robe falling off the shoulders",
        "1-3|a soft {c} knit cardigan left open",
        "2-4|a sheer lace {c} duster robe with a satin tie",
        "2-4|a silky {c} dressing gown with embroidered flowers on the back",
        "3-5|a see-through {c} organza robe with satin ribbon ties",
        "1-3|a cosy {c} oversized sweater slipping off one shoulder",
        "2-4|a velvet {c} smoking jacket worn open over the set",
    ],
}

# the soft half of "Gloves & neck": lace, tulle, satin and pearl pieces for sweet, cosy, elegant and glam themes (no leather collars, spikes or leash rings)
EXTRAS["Soft gloves & neck"] = [
    "3-5|opera-length sheer {c} mesh stretch gloves extending past the elbows",
    "2-5|wrist-length scalloped floral lace gloves with delicate thumb loops",
    "2-5|sheer embroidered tulle gloves with delicate floral threadwork accents",
    "2-5|scalloped black lace ribbon choker with a hanging teardrop crystal pendant",
    "2-5|minimalist thin elastic strap choker with a tiny centre metallic ring",
    "2-4|a {c} velvet ribbon choker with a small cameo",
    "2-4|{c} satin opera gloves with a bow at the wrist",
    "3-5|a {c} pearl-strand choker with a satin ribbon tie",
    "2-4|a {c} lace choker with a heart-shaped charm",
]

ADDON_NAMES = list(EXTRAS)
STYLE_NAMES = list(SETS)


# Sporty sets (Branded Lounge) get sport gear instead of lace gloves, garters or robes. Never two phone straps (arm AND leg).
SPORT_EXTRAS = [
    "1-5|a {c} compression sleeve on one arm", "1-5|{c} compression sleeves on both arms", "1-5|a {c} compression sleeve on one leg",
    "1-5|{c} compression leg sleeves on both legs", "2-5|a {c} phone strap worn like an armband on the upper arm",
    "2-5|a {c} phone-case strap wrapped around one thigh", "1-5|{c} knee-high sports socks", "1-5|a {c} sweatband on one wrist",
]
SPORT_PHONE = "phone"
SETS["Branded Lounge"] += [
    "3|{c} longline sports bra with a plunging neckline and matching high-rise logo-band thong",
    "3|{c} cropped low-zip sports bra and matching cheeky bike shorts",
    "4|{c} strappy cross-back sports bralette with ring details and matching micro bike shorts",
    "4|{c} racerback cut-out sports bra, barely covering, with a matching high-cut logo-band thong",
    "5|{c} tiny strap sports bra top and matching string-side micro bike shorts",
    "5|{c} micro cross-strap sports bralette and low-slung micro thong with a logo waistband",
]

LATEX_LAYER = ["3-5|a long glossy {c} latex robe worn open", "3-5|a glossy {c} latex kimono robe tied loosely", "3-5|a short {c} latex robe hanging off the shoulders", "3-5|an open sheer {c} robe over the latex"]
