"""
The outfit dataset for the No_Thing Outfit Roulette node.

Every entry is  "levels|text"  where levels is one number or a range (1-5):
    1 Covered    everyday, fully dressed
    2 Cute       playful, a little skin
    3 Revealing  low-cut, slits, sheer panels
    4 Skimpy     micro skirts, crop tops, cut-outs, sheer panels
    5 Micro      minimal-fabric strap and cut-out outfits (clothes you can wear out; underwear lives in the Underwear Roulette)
{c} = the outfit's main colour, {c2} = its accent colour.

Add your own lines anywhere - they are picked up after a ComfyUI restart.
Slots:  one (one-piece / full set)   top   bottom   outer   legs   feet   head
Accessory slots (acc): neck  ears  hands  wrists  waist  hair  face  ankle  extra
"""

LEVELS = ["Covered", "Cute", "Revealing", "Skimpy", "Micro"]
AMOUNTS = ["None", "Few", "Some", "Loaded"]          # accessory counts: 0 / 1-2 / 3-4 / 5-7
AMOUNT_RANGE = {"None": (0, 0), "Few": (1, 2), "Some": (3, 4), "Loaded": (5, 7)}

COLOURS = {
    "Black": ["black", "jet black", "glossy black", "matte black"],
    "White": ["white", "ivory", "pearl white", "cream"],
    "Red": ["red", "crimson", "blood red", "cherry red", "scarlet"],
    "Pink": ["pink", "hot pink", "baby pink", "rose pink", "bubblegum pink"],
    "Pastel": ["pastel pink", "pastel blue", "mint green", "lavender", "peach", "lilac", "butter yellow"],
    "Neon": ["neon pink", "neon green", "electric blue", "neon orange", "UV purple", "acid yellow"],
    "Purple": ["purple", "deep violet", "plum", "amethyst", "magenta"],
    "Blue": ["navy blue", "baby blue", "cobalt blue", "midnight blue", "ice blue", "teal"],
    "Metallic": ["silver metallic", "gold metallic", "chrome", "holographic", "rose gold", "gunmetal"],
}

# ---------------------------------------------------------------------------------------- styles
STYLES = {}

STYLES["Casual"] = dict(
    desc="normal everyday clothes",
    palette=["white", "black", "grey", "denim blue", "beige", "olive green", "baby pink", "navy blue", "cream"],
    one=["1|{c} knit sweater dress", "1|{c} shirt dress with a belt", "1-2|{c} summer sundress with thin straps",
         "1|{c} long-sleeve wrap dress", "2|{c} overall dress over a fitted tee", "2|{c} jersey skater dress",
         "2-3|{c} bodycon mini dress", "3|{c} backless halter mini dress", "3-4|{c} ribbed cut-out mini dress"],
    top=["1|{c} oversized hoodie", "1|{c} knit cardigan over a plain tee", "1|{c} fitted turtleneck", "1|{c} flannel shirt",
         "1|{c} button-up blouse", "1|{c} striped long-sleeve tee", "2|{c} cropped hoodie", "2|{c} cropped baby tee",
         "2|{c} off-shoulder sweater", "2-3|{c} ribbed tank top", "3|{c} tube top", "3|{c} knotted crop shirt showing midriff",
         "3-4|{c} halter crop top", "4|{c} bandeau top", "4-5|{c} tiny triangle bikini-style top", "5|{c} strapless bandeau with a plunging cut"],
    bottom=["1|{c} straight-leg jeans", "1|{c} high-waisted trousers", "1|{c} long pleated midi skirt", "1|{c} joggers",
            "1-2|{c} knee-length denim skirt", "2|{c} high-waisted shorts", "2|{c} cargo mini skirt", "2-3|{c} denim cut-off shorts",
            "3|{c} low-rise jeans", "3|{c} short tennis skirt", "3-4|{c} micro denim skirt", "4|{c} ultra-short micro shorts",
            "4-5|{c} low-slung string-side mini skirt", "5|{c} micro hot pants"],
    outer=["1|{c} oversized denim jacket", "1|{c} long wool coat", "1|{c} puffer jacket", "1-2|{c} varsity jacket",
           "2|{c} cropped bomber jacket", "2-3|{c} open cropped cardigan"],
    legs=["1|opaque {c} tights", "1-2|{c} knee-high socks", "2|white ankle socks", "2-3|{c} thigh-high socks", "3|sheer {c} stockings"],
    feet=["1|white sneakers", "1|ankle boots", "1-2|chunky platform sneakers", "2|ballet flats", "2-3|combat boots", "3|strappy block-heel sandals"],
    head=["1|knit beanie", "1-2|{c} baseball cap", "2|oversized sunglasses pushed up in the hair", "2|bucket hat"],
    acc=dict(
        neck=["thin gold chain necklace", "simple pendant necklace", "small pearl necklace", "heart locket"],
        ears=["small hoop earrings", "pearl stud earrings", "dainty gold huggies"],
        hands=["thin stackable rings", "a signet ring", "a simple silver band ring"],
        wrists=["a leather-strap watch", "a beaded friendship bracelet", "a thin gold bangle"],
        waist=["a plain leather belt"], hair=["a scrunchie on the wrist", "a claw clip in the hair"],
        face=["round glasses"], ankle=["a delicate anklet"], extra=["a small crossbody bag"]),
)

STYLES["Kigurumi"] = dict(
    desc="cute animal onesie pyjamas, hoods, paws and tails",
    palette=["pastel pink", "baby blue", "cream white", "lavender", "mint green", "yellow", "grey", "peach", "black"],
    one=["1|{c} bunny kigurumi onesie with long floppy ears on the hood", "1|{c} cat kigurumi onesie with ear hood and tail", "1|{c} panda kigurumi with a round-eared hood",
         "1|{c} fluffy bear kigurumi onesie", "1|{c} unicorn kigurumi with a rainbow mane and a horn", "1|{c} fluffy sheep kigurumi onesie",
         "1|{c} dinosaur kigurumi with a spiked tail and hood", "1|{c} shark kigurumi with a fin and teeth on the hood", "1|{c} fox kigurumi with a bushy tail",
         "1|{c} duck kigurumi onesie with a beak hood", "1|{c} frog kigurumi onesie with big eyes on the hood", "1|{c} penguin kigurumi onesie",
         "1|{c} strawberry-cow print kigurumi", "1|{c} axolotl kigurumi with gill fronds on the hood", "1|{c} wolf kigurumi with ears and a tail",
         "2|{c} short-leg kigurumi romper with an animal-ear hood", "2|{c} kigurumi hoodie dress with a tail", "2|{c} cat-ear hooded kigurumi shorts set",
         "2-3|{c} zip-front kigurumi unitard cut at the thigh, animal-ear hood", "3|{c} low-zip kigurumi romper with the hood down",
         "3|{c} kigurumi onesie unzipped to the waist, hood up", "3-4|{c} cropped kigurumi top with matching tail shorts and paw gloves",
         "4|{c} cropped animal-ear hoodie with micro shorts and fluffy paw mitts", "4|{c} kigurumi-style fuzzy bikini top with matching tail shorts",
         "5|{c} fluffy kigurumi-themed bikini set with a tail, ear headband and paw mitts"],
    top=[], bottom=[], outer=["1-2|{c} fluffy animal-ear hoodie with paw pockets", "2|{c} oversized cat-ear hoodie"],
    legs=["1|fluffy paw-print socks", "2|{c} striped knee-high socks", "2-3|{c} fluffy thigh-high leg warmers with paw prints"],
    feet=["1|fluffy paw slippers", "1|fuzzy animal-foot slippers", "2|plush bunny slippers"],
    head=["1|{c} animal-ear hood", "2|{c} animal-ear headband", "2|pom-pom beanie with ears"],
    acc=dict(
        neck=["a bell collar choker", "a heart-tag collar", "a fluffy neck scarf"],
        ears=["tiny star earrings", "cute animal-shaped studs"],
        hands=["candy-coloured rings", "a cute cat-face ring"],
        wrists=["pastel jelly bracelets", "fluffy wrist cuffs", "a beaded charm bracelet"],
        waist=["a clip-on plush tail", "a pastel charm belt"], hair=["pastel hair clips", "twin pigtails with bows", "a big satin bow in the hair"],
        face=["blush-heart makeup stickers"], ankle=["a bell anklet"], extra=["a small plush toy clipped on", "a carrot-shaped charm"]),
)

STYLES["Dresses"] = dict(
    desc="gowns, mini dresses, party dresses",
    palette=["red", "black", "emerald green", "navy blue", "champagne", "white", "blush pink", "royal purple", "gold"],
    one=["1|{c} floor-length chiffon gown with long sleeves", "1|{c} elegant A-line midi dress", "1-2|{c} cottagecore puff-sleeve midi dress", "1-2|{c} tea-length polka-dot swing dress",
         "2|{c} satin slip dress", "2|{c} fit-and-flare mini dress with a sweetheart neckline", "2|{c} babydoll dress with a bow", "2-3|{c} off-shoulder ruffled mini dress",
         "3|{c} halter evening gown with a high thigh slit", "3|{c} backless satin gown", "3|{c} plunging V-neck cocktail dress", "3|{c} one-shoulder cut-out midi dress",
         "3-4|{c} corset-bodice mini dress", "4|{c} sheer mesh gown with strategic embroidery", "4|{c} micro bodycon dress with a deep neckline",
         "4|{c} backless halter mini with a lace-up back", "4-5|{c} plunging sequin micro dress", "5|{c} string-strapped micro slip dress", "5|{c} gown with extreme cut-outs and a thigh-high slit",
         "2|{c} princess ball gown with a layered tulle skirt", "3|{c} velvet gown with a plunging neckline and long train", "4|{c} sheer-panelled evening dress with sequins"],
    top=[], bottom=[], outer=["1|{c} faux-fur stole", "2|{c} cropped satin jacket", "2-3|{c} open long evening coat", "3|{c} feather-trim shrug"],
    legs=["1|sheer nude tights", "3|sheer {c} stockings", "3|{c} lace-top stay-ups"],
    feet=["1|strappy heels", "2|{c} pointed pumps", "2|satin ankle-strap heels", "3|{c} platform sandals", "3|{c} stiletto heels"],
    head=["2|{c} satin hair bow", "2|a delicate tiara", "2-3|a pearl hair comb"],
    acc=dict(
        neck=["a crystal pendant necklace", "a pearl necklace", "a diamond choker", "a gold collar necklace", "a velvet ribbon choker with a brooch"],
        ears=["chandelier earrings", "pearl drop earrings", "crystal studs"],
        hands=["a cocktail ring", "an emerald ring", "stacked diamond rings"],
        wrists=["a tennis bracelet", "a gold cuff bracelet", "long satin opera gloves"],
        waist=["a jewelled belt"], hair=["a glittering hair pin"], face=["a lace fan covering the lower face"], ankle=["a jewelled anklet"], extra=["a small clutch bag", "a silk shawl"]),
)

STYLES["Y2K"] = dict(
    desc="2000s pop fashion: low-rise, rhinestones, baby tees, velour",
    palette=["hot pink", "baby blue", "silver", "lime green", "white", "orange", "purple", "black", "rose pink"],
    one=["2|{c} halter mini dress with butterfly print", "2|{c} cami slip mini dress with rhinestone straps", "3|{c} denim mini dress with a laced front",
         "3|{c} halter bandage dress with a bejewelled clasp", "4|{c} metallic micro dress with side cut-outs", "4-5|{c} rhinestone-strap micro halter dress",
         "2|{c} velour tracksuit set with rhinestone zip", "3-4|{c} cropped velour zip hoodie and matching micro shorts", "5|{c} rhinestone bikini set with butterfly clips"],
    top=["2|{c} baby tee with glittery lettering", "2|{c} butterfly-print crop tank", "2|{c} rhinestone halter top", "2-3|{c} cropped zip-up velour hoodie",
         "3|{c} tie-front bandeau", "3|{c} mesh long-sleeve", "3|{c} cropped fur-trim cardigan", "3-4|{c} lace-up corset crop top",
         "4|{c} triangle halter with chain straps", "4|{c} metallic tube top", "4-5|{c} tiny rhinestone bikini top", "5|{c} clear-strap micro bandeau"],
    bottom=["2|{c} low-rise flare jeans", "2|{c} cargo pants", "2|{c} velour low-rise sweatpants", "2-3|{c} pleated plaid mini skirt",
            "3|{c} low-rise denim mini skirt with studs", "3|{c} rhinestone-belted denim shorts", "3-4|{c} tiny micro skirt", "4|{c} low-slung micro skirt with a chain belt",
            "4|{c} hot pants with an exposed waistband", "4-5|{c} sequin micro shorts", "5|{c} string-side micro bikini bottom"],
    outer=["2|{c} faux-fur cropped jacket", "2|{c} cropped puffer jacket", "2-3|{c} cropped denim jacket with rhinestones", "3|{c} sheer jacket with sequins"],
    legs=["2|{c} striped leg warmers", "2-3|{c} fishnet stockings", "2|white knee socks", "3|{c} sparkly tights"],
    feet=["2|chunky platform sneakers", "2|{c} mary jane platforms", "3|{c} clear platform heels", "3|{c} rhinestone kitten heels", "2-3|{c} ugg-style mini boots"],
    head=["2|{c} trucker hat", "2|{c} velvet headband", "2|a butterfly clip crown in the hair", "2|{c} bucket hat"],
    acc=dict(
        neck=["a rhinestone butterfly choker", "a stack of beaded necklaces", "a heart pendant on a chain", "a puka shell necklace", "a charm choker"],
        ears=["big rhinestone hoops", "butterfly earrings", "heart studs"],
        hands=["glittery candy rings", "chunky butterfly ring", "stacked rhinestone rings"],
        wrists=["jelly bracelets", "stacked beaded bracelets", "a rhinestone watch", "a charm bracelet"],
        waist=["a rhinestone belly chain", "a chain belt slung low", "a studded belt"],
        hair=["butterfly clips", "claw clips", "tiny glitter hair clips", "chunky headband"], face=["rimless tinted glasses", "star-shaped sunglasses"],
        ankle=["a charm anklet"], extra=["a baguette shoulder bag", "a flip phone charm", "a mini shoulder purse"]),
)

STYLES["Goth"] = dict(
    desc="dark romantic: lace, velvet, corsets, crosses",
    palette=["black", "black", "deep burgundy", "dark purple", "blood red", "midnight blue", "silver-grey"],
    one=["1-2|{c} gothic Victorian lace-trim dress with a high collar", "2|{c} velvet corset mini dress", "2-3|{c} off-shoulder lace gothic gown",
         "3|{c} sheer lace gown with a plunging neckline", "3|{c} corseted dress with a long layered skirt", "3-4|{c} velvet slip dress with a front slit and lace-up sides",
         "4|{c} sheer mesh dress with gothic lace panels", "4|{c} corset mini dress with a laced-open back"],
    top=["1|{c} lace-sleeve blouse with a high collar", "1-2|{c} oversized band tee tied up", "2-3|{c} corset top with gothic lacing", "2|{c} mesh long-sleeve top",
         "3|{c} underbust corset over a sheer blouse", "3-4|{c} bat-wing sheer top"],
    bottom=["1|{c} tiered tulle maxi skirt", "1-2|{c} pleated tartan mini skirt", "2|{c} layered ruffle mini skirt", "2-3|{c} lace-trim mini skirt", "3|{c} velvet high-waisted mini skirt",
            "3|{c} lace-up side shorts", "3-4|{c} asymmetric slit skirt", "4|{c} sheer micro skirt over lace briefs", "4|{c} micro skirt with chain belt"],
    outer=["1|{c} long velvet coat", "1-2|{c} lace-trim cape with a hood", "2|{c} cropped moto jacket", "2-3|{c} sheer lace kimono robe", "3|{c} open gothic frock coat"],
    legs=["1-2|{c} opaque tights with lace tops", "2|{c} fishnet tights", "2-3|{c} striped thigh-highs"],
    feet=["1-2|{c} platform combat boots", "2|{c} buckled creeper shoes", "3|{c} lace-up knee-high boots", "3|{c} platform Mary Janes", "3-4|{c} thigh-high lace-up platform boots"],
    head=["2|a small black hat with a veil", "2-3|a black lace headpiece", "3|a spiked velvet headband"],
    acc=dict(
        neck=["a black velvet choker with a cross charm", "a crucifix necklace", "a layered chain choker", "a bat-wing pendant", "a lace choker with a cameo", "a spiderweb-lace collar"],
        ears=["silver cross earrings", "dangling bat earrings", "black gem drop earrings"],
        hands=["skull rings", "black lacquer fingertip rings", "a silver spider ring", "stacked silver rings"],
        wrists=["lace fingerless gloves", "spiked wristbands", "a rosary bracelet", "long lace opera gloves", "velvet wrist cuffs"],
        waist=["a studded belt"], hair=["black lace hair bows", "a cobweb hairpin"],
        face=["dark lipstick and dark winged liner", "a half lace veil"], ankle=["a chain anklet"], extra=["a coffin-shaped purse", "a lace parasol"]),
)

STYLES["Latex"] = dict(
    desc="glossy latex and PVC",
    palette=["glossy black", "glossy red", "glossy white", "pink", "transparent", "metallic silver", "neon purple", "royal blue"],
    one=["3|{c} latex bodysuit with a high neck and long sleeves", "3|{c} latex catsuit with a front zip", "3-4|{c} latex halter bodysuit with a plunging neckline", "3|{c} latex nurse-style mini dress",
         "4|{c} latex cut-out catsuit", "4|{c} latex corset dress with a mini hem", "4|{c} transparent PVC mini dress with a zip front", "5|{c} minimal latex strap set"],
    top=["2-3|{c} latex crop top with a high neck", "3|{c} latex long-sleeve crop top", "3-4|{c} latex corset", "4-5|{c} latex bandeau with chrome zip", "5|{c} latex triangle top with thin ties"],
    bottom=["2-3|{c} latex leggings", "3|{c} latex pencil skirt", "3|{c} latex hot pants", "3-4|{c} latex mini skirt with a rear zip", "4|{c} latex micro skirt", "4|{c} latex high-waist shorts with a front zip", "5|{c} latex micro bikini bottom"],
    outer=["2-3|{c} latex cropped jacket", "3|{c} latex trench coat", "3|{c} latex cape", "4|{c} sheer latex shrug"],
    legs=["3|{c} latex thigh-high stockings", "4|{c} PVC leg wraps"],
    feet=["3|{c} patent ankle boots", "3|{c} patent stiletto pumps", "3-4|{c} latex thigh-high boots", "4|{c} platform patent heels"],
    head=["3|{c} latex hood with open face", "3|{c} latex cap", "4|{c} latex cat-ear headpiece"],
    acc=dict(
        neck=["a latex collar", "a silver ring-pendant choker", "a chain-link choker"],
        ears=["chrome hoops", "metal stud earrings"],
        hands=["large chrome rings", "dark metal rings"],
        wrists=["long latex gloves", "latex opera gloves", "chrome cuffs"],
        waist=["a wide latex waist belt"], hair=["a sleek high ponytail"], face=["wraparound sunglasses", "a glossy lip colour"], ankle=["a chrome ankle chain"], extra=["a latex handbag"]),
)

STYLES["Grunge"] = dict(
    desc="90s grunge: flannel, ripped denim, band tees",
    palette=["black", "faded black", "red plaid", "grey", "olive green", "dark denim blue", "burgundy"],
    one=["1-2|{c} slip dress over a faded band tee", "2|{c} babydoll dress with combat boots", "2|{c} ripped floral grunge dress", "2-3|{c} lace-trim slip dress under a flannel", "3|{c} distressed mesh slip dress"],
    top=["1|{c} oversized flannel shirt", "1|{c} faded band tee with cut sleeves", "1-2|{c} oversized striped cardigan", "2|{c} cropped distressed tee", "2|{c} knotted flannel",
         "2-3|{c} torn tank top", "3|{c} mesh long-sleeve", "3|{c} safety-pin tank top", "4|{c} fishnet top", "4|{c} cut-up tee tied into a tiny crop"],
    bottom=["1|{c} ripped baggy jeans", "1|{c} skinny jeans", "1-2|{c} plaid midi skirt", "2|{c} ripped denim shorts", "2-3|{c} torn tartan mini skirt", "3|{c} distressed micro denim skirt", "3-4|{c} ripped micro shorts", "4|{c} frayed cutoff micro shorts"],
    outer=["1|{c} oversized flannel tied around the waist", "1|{c} leather biker jacket", "1|{c} baggy cardigan", "2|{c} distressed denim jacket"],
    legs=["1-2|{c} ripped tights", "2|{c} fishnet tights", "2|{c} striped knee socks", "2-3|{c} laddered tights"],
    feet=["1|worn-in combat boots", "1|scuffed canvas high-tops", "2|chunky platform boots"],
    head=["1|{c} beanie", "2|messy half-up hair with a clip", "2|a cap worn backwards"],
    acc=dict(
        neck=["a black choker", "a tattoo-style stretch choker", "a chain necklace with a small padlock", "a leather cord pendant"],
        ears=["multiple small hoops", "ear cuffs", "safety-pin earrings"],
        hands=["chunky silver rings", "chipped black nail polish and plain rings"],
        wrists=["studded wristbands", "friendship bracelets", "a wristband stack", "a worn leather cuff"],
        waist=["a studded belt", "a chain wallet"], hair=["messy bangs with pins"], face=["smudged eyeliner", "round sunglasses"], ankle=["a thin ankle chain"], extra=["a patched backpack", "pin badges on the jacket"]),
)

STYLES["Punk"] = dict(
    desc="spikes, tartan, chains, safety pins, studs",
    palette=["black", "red", "neon pink", "neon green", "grey", "black and red", "electric blue"],
    one=["2|{c} tartan pinafore dress with safety pins", "2-3|{c} studded leather mini dress", "3|{c} ripped tartan bodycon dress with chain straps", "4|{c} spiked halter mini with cut-outs",
         "4|{c} safety-pin-stitched micro dress"],
    top=["1-2|{c} studded leather vest", "2|{c} ripped band crop tee", "2|{c} patched sleeveless denim vest", "2-3|{c} torn mesh top", "3|{c} chain-strap tank top", "3|{c} tartan bandeau with safety pins",
         "4|{c} cut-out crop top with chain details", "4-5|{c} safety-pin tube top", "5|{c} strips of tartan held with safety pins"],
    bottom=["1-2|{c} tartan mini skirt with chains", "2|{c} ripped black skinny jeans", "2|{c} studded belt over cargo shorts", "2-3|{c} pleated tartan micro skirt", "3|{c} leather mini skirt with zippers",
            "3-4|{c} shredded micro shorts", "4|{c} micro tartan skirt with safety pins", "4|{c} low-rise leather hot pants", "4-5|{c} chain-slung micro skirt"],
    outer=["1|{c} studded leather biker jacket", "1-2|{c} patched denim battle jacket", "2|{c} cropped spiked jacket", "2-3|{c} torn oversized shirt", "3|{c} open leather jacket over a bare chest line"],
    legs=["2|{c} torn fishnets", "2|{c} striped knee socks", "3|{c} fishnet thigh-highs"],
    feet=["1-2|{c} tall lace-up combat boots", "2|{c} platform creepers", "2-3|{c} studded platform boots"],
    head=["2|a spiked leather headband", "2|a mohawk-style upright hair", "2-3|a studded cap"],
    acc=dict(
        neck=["a spiked collar", "a dog-tag chain", "a studded choker", "a heavy chain necklace", "a safety-pin necklace"],
        ears=["safety-pin earrings", "bar studs", "multiple ear piercings"],
        hands=["spiked rings", "skull rings", "bold chunky rings"],
        wrists=["spiked bracelets", "studded wrist cuffs", "chain bracelets", "fingerless studded gloves"],
        waist=["a bullet belt", "a studded belt with chains", "chains looped from the belt"], hair=["colourful spiked hair", "neon-dyed streaks"],
        face=["bold neon eyeliner", "a nose ring"], ankle=["chain anklets"], extra=["a patched shoulder bag"]),
)

STYLES["Barbie"] = dict(
    desc="Barbiecore: pink everything, glitter, retro glam",
    palette=["hot pink", "bubblegum pink", "baby pink", "magenta", "white", "pastel pink", "hot pink and white"],
    one=["1-2|{c} gingham sundress", "2|{c} puff-sleeve baby-doll dress with a big bow", "2|{c} retro 60s mini dress with a white collar", "2|{c} tulle party dress", "2-3|{c} glitter halter mini dress",
         "3|{c} sequin bodycon mini dress", "3|{c} satin cocktail dress with a sweetheart neckline", "3-4|{c} tiny corset dress with a heart neckline", "4|{c} rhinestone micro dress", "2|{c} matching tracksuit with rhinestone trim",
         "3|{c} cut-out swimsuit with heart detail", "5|{c} heart-shaped micro bikini with glitter ties"],
    top=["2|{c} cropped cardigan with pearl buttons", "2|{c} puff-sleeve crop top", "2|{c} heart-neck knit top", "2-3|{c} tie-front blouse", "3|{c} ruffled bandeau", "3|{c} heart-shaped corset top", "3-4|{c} glittery halter top", "4|{c} satin triangle top with heart ties"],
    bottom=["1-2|{c} pleated tennis skirt", "2|{c} high-waisted wide-leg trousers", "2|{c} ruffled mini skirt", "2-3|{c} glitter mini skirt", "3|{c} satin hot pants", "3|{c} sequin micro skirt", "3-4|{c} tiny pleated micro skirt", "4|{c} rhinestone micro shorts"],
    outer=["1-2|{c} faux-fur coat", "2|{c} cropped blazer with gold buttons", "2|{c} varsity jacket", "2-3|{c} marabou-trim bolero"],
    legs=["1-2|white knee-high socks", "2|{c} sheer tights", "2-3|{c} thigh-high socks with bows", "3|{c} glitter stockings"],
    feet=["1-2|{c} kitten heels", "2|{c} platform sandals", "2|{c} rollerblades", "2-3|{c} mary-jane platform shoes", "3|{c} glittery stiletto heels"],
    head=["2|a satin bow headband", "2|a pink cowboy hat", "2|{c} oversized bow clips", "2-3|a mini tiara"],
    acc=dict(
        neck=["a pearl necklace with a heart charm", "a pink gem choker", "a gold heart pendant", "layered pearls"],
        ears=["heart earrings", "pearl drop earrings", "pink gem studs"],
        hands=["a pink gem cocktail ring", "heart rings", "pearl rings"],
        wrists=["a pink charm bracelet", "a sparkling tennis bracelet", "a heart-lock bracelet", "satin gloves"],
        waist=["a pink chain belt", "a bow belt"], hair=["a voluminous high ponytail with a bow", "glitter hair clips", "a ribbon in the hair"],
        face=["heart-shaped sunglasses", "glossy pink lips"], ankle=["an ankle bow", "a pearl anklet"], extra=["a pink mini handbag", "a heart-shaped purse"]),
)

# capped on purpose: uniform-style pieces only exist at levels 1-2 (see README)
STYLES["Preppy Uniform"] = dict(
    desc="preppy uniform-inspired outfits: pleats, blazers, knee socks (modest levels only)",
    palette=["navy blue", "grey", "dark green", "burgundy", "white", "black", "tan"],
    one=["1|{c} pinafore dress over a white blouse", "1|{c} sailor-collar dress with a ribbon", "1-2|{c} pleated mini dress with a white collar"],
    top=["1|white button-up blouse with a ribbon tie", "1|white button-up shirt with a loose necktie", "1|{c} knit sweater vest over a collared shirt", "1|{c} cardigan over a white blouse",
         "1-2|{c} fitted blazer with an emblem", "2|white blouse tied at the waist"],
    bottom=["1|{c} pleated knee-length skirt", "1|{c} plaid pleated skirt", "1-2|{c} pleated mini skirt", "2|{c} tartan mini skirt"],
    outer=["1|{c} blazer", "1|{c} knit cardigan", "1|{c} duffel coat"],
    legs=["1|{c} knee-high socks", "1|white ankle socks", "1|opaque {c} tights", "1-2|{c} over-the-knee socks"],
    feet=["1|brown leather loafers", "1|black mary-jane shoes", "1|polished oxfords"],
    head=["1|a ribbon hair bow", "1|a plain headband"],
    acc=dict(
        neck=["a small silver locket", "a ribbon bow tie", "a thin pearl necklace"],
        ears=["tiny pearl studs"], hands=["a simple signet ring"], wrists=["a leather watch", "a thin bangle"],
        waist=["a slim leather belt"], hair=["a ribbon hair bow", "a neat hairband"], face=["round glasses"], ankle=[], extra=["a leather satchel", "a school-crest pin on the blazer"]),
)

# oversized, soft, hide-the-body clothes: what you pull on when you feel self-conscious (covered / cute levels only)
STYLES["Baggy Comfy"] = dict(
    desc="baggy, oversized comfy clothes: big hoodies, loose sweatpants, hiding in soft layers; at Skimpy and Micro the hoodie shrinks to a micro-cropped one with a chest cutout and the sweatpants sit low",
    palette=["grey", "oatmeal beige", "black", "faded navy", "dusty pink", "lavender", "sage green", "cream", "washed denim blue"],
    one=["1|{c} oversized hoodie dress with the sleeves covering the hands", "1|{c} huge baggy t-shirt worn as a dress", "1|{c} loose flannel pyjama set", "1|{c} fluffy one-piece onesie with a hood",
         "1-2|{c} oversized sweatshirt dress hanging off one shoulder", "2|{c} slouchy knit sweater dress that swallows the body"],
    top=["1|{c} extra-large hoodie with the sleeves pulled over the hands", "1|{c} baggy oversized knit sweater with long sleeves", "1|{c} huge faded band tee",
         "1|{c} loose heavy sweatshirt", "1|{c} oversized zip-up hoodie", "1-2|{c} slouchy off-shoulder oversized sweater", "2|{c} baggy cropped hoodie over a loose tee"],
    bottom=["1|{c} baggy sweatpants", "1|{c} loose pyjama pants", "1|{c} wide-leg baggy jeans", "1|{c} baggy cargo pants", "1|{c} loose joggers rolled at the waist",
            "1-2|{c} soft fleece shorts under a big top", "2|{c} comfy leggings under an oversized top"],
    outer=["1|{c} oversized chunky cardigan pulled tight around the body", "1|{c} big oversized flannel shirt worn open", "1|{c} thick blanket-like wrap cardigan", "1|{c} huge puffer jacket"],
    legs=["1|{c} thick knit leg warmers", "1|{c} chunky wool socks"],
    feet=["1|{c} fluffy slippers", "1|{c} comfy plain sneakers"],
    head=["1|a hood pulled up", "1|a slouchy knit beanie", "1|a messy bun with a scrunchie", "1|a soft headband"],
    acc=dict(
        neck=["a thin plain chain", "a soft scarf"], ears=["tiny stud earrings"], hands=["a simple ring"], wrists=["a hair tie on the wrist", "a friendship bracelet"],
        waist=[], hair=["a scrunchie", "a claw clip", "a plain hair tie"], face=["oversized round glasses"], ankle=[],
        extra=["a canvas tote bag", "over-ear headphones around the neck", "a plush keychain on a bag", "a phone held in one hand",
               "a steaming mug of hot coffee held in both hands", "a paperback book held in one hand", "a mug of hot chocolate held in both hands"]),
)

# accessories that fit anywhere (used for blends and for the "nothing selected" case)
GENERIC_ACC = dict(
    neck=["a layered gold chain necklace", "a velvet choker", "a pearl strand", "a heart pendant", "a thin silver chain"],
    ears=["gold hoop earrings", "pearl studs", "crystal drops"],
    hands=["stacked rings", "a statement cocktail ring", "thin silver rings"],
    wrists=["a stack of bangles", "a charm bracelet", "a tennis bracelet", "a leather cuff"],
    waist=["a chain belt", "a belly chain", "a slim belt"],
    hair=["hair clips", "a bow in the hair", "a headband"], face=["tinted sunglasses"], ankle=["a delicate anklet"], extra=["a small shoulder bag"],
)

ACC_SLOT_ORDER = ["neck", "ears", "wrists", "hands", "waist", "hair", "ankle", "face", "extra"]

# how the outfit sentence is built from the slots
SLOT_ORDER = ["head", "outer", "top", "one", "bottom", "legs", "feet"]

from .outfit_data_extra import STYLE_ADD as _ADD   # Japanese kawaii and brand sets
STYLES.update(_ADD)
from .boho_data import OUTFIT as _BOHO
STYLES["Boho Hippie"] = _BOHO
from .outfit_data_more import MORE as _MORE   # emo, scene, neon raver, masquerade, mourning veils, dominant, submissive
STYLES.update(_MORE)
from .outfit_data_more import ADD as _EXTRA_PIECES, HEAD_CHANCE   # extra pieces for older styles: low-rise + thong combos, cropped jackets
for _s, _slots in _EXTRA_PIECES.items():
    for _slot, _lines in _slots.items():
        if _s in STYLES:
            STYLES[_s][_slot] = list(STYLES[_s].get(_slot, [])) + _lines
from .cosplay_data import STYLE as _COSPLAY   # fixed character looks
STYLES["Cosplay"] = _COSPLAY
from .pastel_data import STYLE as _PASTEL   # adult-coded pastel kawaii (works at every level)
STYLES["Pastel Pop"] = _PASTEL
STYLE_NAMES = list(STYLES)


# Skimpy / Micro pieces for styles that have none of their own (30 of the 39 styles have no Micro): the roll borrows these
# instead of sliding down to a hoodie-and-skirt outfit. Same format: "levels|text", slots one / top / bottom.
GENERIC_SKIMPY = dict(
    one=["4|{c} cut-out bodycon mini dress with a plunging neckline", "4|{c} strappy cage-detail mini dress", "4|{c} high-cut bodysuit with thigh-high side cut-outs",
         "5|{c} string-strap micro dress with wide side cut-outs", "5|{c} criss-cross strap bodysuit leaving the sides bare", "5|{c} thin-strap micro one-piece cut to barely cover"],
    top=["4|{c} cropped bandeau top", "4|{c} tiny halter crop top with a plunging neckline", "4|{c} strappy cut-out crop top",
         "5|{c} tiny triangle top on thin straps", "5|{c} clear-strap micro bandeau", "5|{c} thin criss-cross strap top that barely covers"],
    bottom=["4|{c} ultra-short micro skirt", "4|{c} low-slung string-side mini skirt", "4|{c} high-cut micro shorts",
            "5|{c} string-side micro bottoms", "5|{c} micro skirt barely covering the hips", "5|{c} low-slung micro hot pants"],
)
# Skimpy / Micro keep accessories to jewellery and a bag
MICRO_SLOTS = ("neck", "ears", "wrists", "extra")
MICRO_EXTRA_OK = r"bag|purse|clutch|handbag|backpack|volleyball|drink|cocktail|towel|suspender|\btie\b|flip phone|phone with|phone held|mug of|paperback"
STYLE_MICRO_SLOTS = {"Beach": ("face", "hair"), "Gyaru": ("hands", "hair", "face", "waist")}                                # Beach may also add sunglasses and a flower at Skimpy / Micro
HAIR_ACC_OK = r"goggle|flower|hibiscus|plumeria|clip|\\bpin\\b|bow\\b|ribbon|scrunchie|headband|barrette|comb"      # hair-slot extras that are accessories, not a hairstyle
CHILDLIKE_STYLES = {"Sanrio Cute", "Doll Style", "Harajuku Kawaii", "Preppy Uniform"}   # not rolled at Revealing and up
MICRO_PIERCINGS = ["a small nose stud", "a navel piercing", "a row of tiny ear piercings"]
MICRO_ACC_MAX = {4: 4, 5: 3}


# Skimpy (4) and Micro (5) pieces in each style's own language: 'slutty but classy' for streetwear / brands, dark and strappy for goth, and so on.
# Styles not listed here borrow GENERIC_SKIMPY above. Add your own lines or styles here.
STYLE_SKIMPY = {
    "Beach": dict(
        top=["1-2|{c} loose tropical-print button-up shirt with the sleeves rolled", "1-2|{c} Miami-style pastel camp-collar shirt worn open over a white tee",
             "1|{c} printed palm-leaf resort shirt, relaxed fit", "5|{c} micro string bikini top with thin ties"],
        bottom=["1-2|{c} light-wash jeans rolled at the ankle", "1|white linen trousers rolled at the ankle", "1-2|{c} rolled-up boyfriend jeans", "5|{c} micro string bikini bottoms with thin side ties"],
        one=["4|{c} skintight micro towel wrapped as a dress, knotted at the chest", "5|{c} skintight micro towel dress barely covering, tucked at the chest"],
        ),
    "Streetwear Brands": dict(
        top=["4|{c} skintight cropped tube top under an open oversized shirt", "4|{c} cropped zip hoodie worn open over a skintight tube top",
             "5|{c} skintight cropped tube top", "5|{c} skintight ribbed cropped tube top with a logo waistband", "5|{c} skintight cropped tube top with a zip down the front",
             "5|{c} Supreme box-logo skintight cropped tube top", "5|{c} Off-White-style skintight cropped tube top with diagonal stripes", "5|{c} Palace tri-ferg skintight cropped tube top"],
        bottom=["4|{c} micro denim skirt", "4|{c} ultra-short micro shorts with a logo waistband",
                "5|{c} micro skirt", "5|{c} micro denim skirt riding low on the hips", "5|{c} micro skirt with a logo waistband", "5|{c} pleated micro skirt barely covering", "5|{c} BAPE-camo micro skirt"]),
    "Athleisure Brands": dict(
        top=["4|{c} cropped zip jacket worn open over a sports bra", "5|{c} skintight cropped tube top", "5|{c} tiny sports bra top with thin cross-back straps"],
        bottom=["4|{c} ultra-short biker shorts", "5|{c} micro tennis skirt barely covering", "5|{c} high-cut micro bike shorts"]),
    "Y2K Brands": dict(
        top=["4|{c} rhinestone cropped baby tee, open at the front", "5|{c} tiny rhinestone halter top", "5|{c} skintight cropped tube top with a glitter logo"],
        bottom=["4|{c} low-rise micro mini skirt", "5|{c} micro mini skirt with a rhinestone belt", "5|{c} low-slung micro hot pants"]),
    "High Street Trend": dict(
        top=["4|{c} ribbed cropped tank, tight and short", "5|{c} skintight cropped tube top", "5|{c} knotted micro tie-front top"],
        bottom=["4|{c} satin micro mini skirt", "5|{c} micro skirt with a thigh-high slit", "5|{c} low-slung micro skirt"]),
    "Luxury Houses": dict(
        top=["4|{c} silk blouse worn open over a skintight bandeau", "5|{c} skintight cropped silk tube top", "5|{c} chain-strap micro bandeau"],
        bottom=["4|{c} tailored micro skirt", "5|{c} leather micro skirt barely covering", "5|{c} satin micro skirt with a thigh-high slit"]),
    "Alt Brands": dict(
        top=["4|{c} mesh long-sleeve over a skintight bandeau", "5|{c} skintight cropped tube top with straps and buckles", "5|{c} tiny buckled strap top"],
        bottom=["4|{c} pleated micro skirt with chains", "5|{c} micro skirt with buckled straps", "5|{c} low-slung micro skirt with a chain belt"]),
    "Goth": dict(
        top=["4|{c} lace-up corset top, open back", "5|{c} strappy lace micro bralette", "5|{c} criss-cross strap bandeau with lace trim"],
        bottom=["4|{c} pleated micro skirt", "5|{c} lace micro skirt barely covering", "5|{c} strappy low-slung micro skirt"]),
    "Sporty Girl": dict(
        top=["4|{c} cropped zip jacket worn open over a sports bra", "5|{c} tiny cross-strap sports top", "5|{c} skintight cropped tube top"],
        bottom=["4|{c} ultra-short pleated tennis skirt", "5|{c} micro tennis skirt barely covering", "5|{c} high-cut micro shorts"]),
    "Gyaru": dict(
        top=["4|{c} cropped off-shoulder top, tight and short", "5|{c} tiny bandeau top with a ribbon tie", "5|{c} skintight cropped tube top"],
        bottom=["4|{c} frilled micro mini skirt", "5|{c} micro skirt with a ribbon belt", "5|{c} low-slung micro skirt"]),
    "Neon Raver": dict(
        top=["4|{c} neon mesh crop over a skintight bandeau", "5|{c} neon tape-strap micro top", "5|{c} tiny neon triangle top on thin straps"],
        bottom=["4|{c} neon micro skirt", "5|{c} neon micro skirt barely covering", "5|{c} UV string-side micro shorts"]),
}


# Beach: the accessories the beach look is about
BEACH_EXTRA = dict(hair=["a hibiscus flower tucked in the hair", "a plumeria flower behind the ear", "a white flower in the hair"],
                   face=["oversized round sunglasses", "cat-eye sunglasses", "tiny retro sunglasses"],
                   extra=["a volleyball held under one arm", "a beach volleyball held on the hip", "a volleyball resting on the hip",
                           "a tropical cocktail with a tiny paper umbrella", "a coconut drink with a straw", "a frosty tropical drink with a pineapple wedge",
                           "a striped beach towel draped over one shoulder", "a rolled beach towel tucked under one arm"])


# Gym wear for the sporty styles at Revealing / Skimpy / Micro: skintight, almost sheer stretch fabric, micro cuts, sporty headwear.
_GYM = dict(
    one=["4-5|{c} skintight almost-sheer stretch gym bodysuit, cut high on the hip", "5|{c} micro gym unitard with cut-outs in thin stretch fabric"],
    top=["3-4|{c} skintight sheer-stretch sports bra top, nearly see-through", "4|{c} skintight ribbed cropped tube top", "4|{c} cut-out racerback sports bra with strappy cross-back",
         "5|{c} micro sports bra barely covering", "5|{c} micro tube top in thin stretch fabric", "5|{c} tiny halter sports bra with ring detail",
         "5|{c} skintight almost-sheer micro tube top", "4-5|{c} cropped zip jacket worn open over a micro sports bra"],
    bottom=["3-4|{c} skintight high-cut sports shorts", "4|{c} skintight micro sports shorts", "4|{c} ultra-short pleated tennis skirt with built-in briefs",
            "4|{c} micro leggings cut high on the hip and ending mid-thigh", "5|{c} micro tennis skirt barely covering", "5|{c} micro gym shorts cut like panties",
            "5|{c} skintight micro sports pants in thin stretch fabric", "5|{c} micro panty-cut sports briefs"],
    legs=["3-5|{c} sheer stretch knee-high sports socks", "4-5|{c} thigh-high compression socks"],
    feet=["3-5|{c} chunky running sneakers", "3-5|{c} platform sneakers", "3-5|{c} high-top trainers"],
    head=["3-5|a {c} sports headband", "3-5|a {c} baseball cap worn backwards", "3-5|a sports visor", "3-5|a {c} sweatband", "4-5|a {c} cap with a high ponytail pulled through"],
)
for _n in ("Sporty Girl", "Athleisure Brands", "Boxing & Gym Brands"):
    STYLE_SKIMPY[_n] = {k: list(v) for k, v in _GYM.items()}
HEAD_OK_AT_MICRO = {"Sporty Girl", "Athleisure Brands", "Boxing & Gym Brands"}                  # sporty headwear stays at Micro


# Dominant / Submissive had nothing at Covered, so a Covered roll of those themes slid into "any style" (beach shirts, kigurumi hoodies ...). Covered pieces in their own language:
STYLE_SKIMPY["Dominant"] = dict(
    one=["1|{c} sleek long-sleeve tailored dress with a high collar"],
    top=["1|{c} crisp high-collar blouse with a neat bow", "1|{c} fitted tailored blazer over a plain shirt", "1|{c} structured leather-look jacket, buttoned up"],
    bottom=["1|{c} tailored pencil skirt", "1|{c} high-waisted wide-leg tailored trousers"],
    legs=["1|opaque {c} tights"],
    feet=["1|{c} polished leather ankle boots", "1|{c} knee-high leather boots"],
    head=["1|a leather peaked cap"])
STYLE_SKIMPY["Submissive"] = dict(
    one=["1|{c} soft knit sweater dress"],
    top=["1|{c} oversized soft cardigan over a camisole", "1|{c} neat blouse with a peter-pan collar and a ribbon"],
    bottom=["1|{c} pleated skirt with a ribbon at the waist", "1|{c} knee-length soft skirt"],
    legs=["1|{c} knee-high socks"],
    feet=["1|{c} mary-jane shoes", "1|white sneakers"])
# props: the Dominant look always carries one (never an explicit toy)
STYLE_ACC_EXTRA = {"Dominant": dict(extra=["a coiled leather whip held in one hand", "a leather riding crop held in one hand", "a leather paddle held in one hand", "a braided leather whip resting on the shoulder"])}
DOMINANT_PROPS = r"whip|crop|paddle"


# Covered (1) and Revealing (3) pieces for styles that have none of their own (a themed roll used to jump to "any style" or a different level)
GENERIC_SKIMPY["one"] += ["1|{c} simple knee-length dress with sleeves", "3|{c} fitted dress with a plunging neckline and a thigh slit"]
GENERIC_SKIMPY["top"] += ["1|{c} fitted long-sleeve top", "1|{c} soft knit sweater", "3|{c} low-cut fitted top with a deep neckline", "3|{c} off-shoulder crop top showing a little midriff"]
GENERIC_SKIMPY["bottom"] += ["1|{c} straight trousers", "1|{c} knee-length skirt", "3|{c} short skirt with a thigh slit", "3|{c} low-rise tight shorts"]

PG_NO_GENERIC = set()                                # a latex roll at Covered / Cute is not a thing: those use another style


# Latex at Covered / Cute: fully covering latex, no more falling back to random styles (kigurumi, shark hoodies, beach drinks ...)
STYLE_SKIMPY["Latex"] = dict(
    one=["1-2|{c} glossy latex long-sleeve dress with a high neck", "2|{c} latex pencil dress with a front zip"],
    top=["1-2|{c} glossy latex high-neck long-sleeve top", "1-2|{c} fitted latex turtleneck", "2|{c} latex shirt, buttoned up"],
    bottom=["1-2|{c} glossy latex trousers", "1-2|{c} latex pencil skirt below the knee", "2|{c} high-waisted latex skirt"],
    outer=["1-2|{c} long glossy latex trench coat", "1-2|a long {c} latex robe worn open", "1-2|a long translucent {c} organza robe worn open over the outfit"],
    legs=["1-2|opaque {c} tights"],
    feet=["1-2|{c} glossy latex ankle boots", "1-2|{c} polished knee-high boots"],
    head=["1-2|a {c} latex headscarf"])
STYLE_ACC_EXTRA["Latex"] = dict(extra=["a glossy latex handbag", "a structured {c} latex handbag", "a small latex clutch", "a latex tote bag"])

# Latex at Revealing .. Micro: robes, boots and stockings that were missing above Revealing
STYLE_SKIMPY["Latex"]["outer"] += ["3-5|a long glossy {c} latex robe worn open", "4-5|an open sheer {c} robe over the latex", "5|a short {c} latex robe hanging off the shoulders"]
STYLE_SKIMPY["Latex"]["feet"] += ["5|{c} glossy latex thigh-high boots", "5|{c} latex stiletto heels"]
STYLE_SKIMPY["Latex"]["legs"] += ["4-5|{c} latex thigh-high stockings"]
LATEX_OUTER_AT_MICRO = {"Latex"}


# Kigurumi mixed with strap harnesses (breast, hip / butt, thigh straps with O-rings), hood up or down, more strap the skimpier it gets
STYLE_SKIMPY["Kigurumi"] = dict(
    one=["3|{c} fox kigurumi onesie unzipped to the navel with the hood up, over a strappy O-ring breast harness",
         "3|{c} unicorn kigurumi unzipped low with the hood up and a strappy breast harness across the chest",
         "3|{c} bunny kigurumi romper with the hood down and a thin O-ring chest harness",
         "3|{c} cat kigurumi unitard cut high on the thigh, hood up, with leather thigh straps and O-rings",
         "3|{c} wolf kigurumi with the hood down, open at the chest over a strappy harness",
         "3|{c} panda kigurumi unzipped to the waist, hood up, with thigh straps",
         "4|{c} cropped fox kigurumi top with the hood up, a strappy O-ring breast harness and tail shorts with hip straps",
         "4|{c} unicorn kigurumi bikini-cut set with the hood down, a strappy breast harness and thigh straps with O-rings",
         "4|{c} cat kigurumi cut-out bodysuit with the hood up and a leather strap harness with O-rings across the chest and hips",
         "4|{c} bunny kigurumi micro shorts with a tail, hood up, a strappy breast harness and a thigh harness",
         "4|{c} wolf kigurumi crop top with the hood down, a harness with silver O-rings and cut-out hips",
         "5|{c} fox kigurumi with the hood up, paw mitts and a minimal strap harness with O-rings across the chest and hips",
         "5|{c} unicorn kigurumi hood down with a micro strap harness, thigh straps and an O-ring hip and butt harness",
         "5|{c} cat-ear kigurumi hood up, a micro strappy breast harness, a hip harness and thigh straps with O-rings",
         "5|{c} bunny kigurumi hood down, fluffy paw gloves and a thin strap harness with O-rings on the chest, hips and thighs"],
    legs=["3-5|{c} fluffy thigh-high leg warmers with paw prints", "3-5|{c} thigh-high stockings with paw prints"],
    feet=["3-5|{c} fluffy paw boots", "3-5|{c} platform paw-print boots", "3-5|{c} stiletto boots with fur cuffs"])


# Emo at every level: band-print micro tube tops, plaid micro mini skirts, pentagram / strap harnesses, fishnet, striped gloves and striped socks
STYLE_SKIMPY["Emo"] = dict(
    top=["3|{c} skintight micro tube top with a My Chemical Romance band print", "3|{c} cropped band tee with bold text, tied up at the ribs",
         "4|{c} skintight micro tube top with a bold emo band logo print", "4|{c} pentagram strap breast harness with O-rings over a skintight bandeau",
         "4|{c} cropped plaid shirt worn open over a micro band tube top",
         "5|{c} pentagram strap breast harness with silver O-rings, skin showing between the straps", "5|{c} thin cross-strap breast harness with a small pentagram ring",
         "5|{c} skintight micro tube top with an emo band logo print"],
    bottom=["3|{c} plaid micro mini skirt", "4|{c} plaid micro mini skirt barely covering", "4|{c} low-slung plaid micro skirt with a chain belt",
            "5|{c} plaid micro mini skirt barely covering the hips", "5|{c} low-slung plaid micro skirt with strap detail"],
    legs=["3-5|{c} fishnet leggings", "3-5|{c} skintight striped thigh-high leggings", "3-5|{c} black and white striped knee-high socks starting at the ankle"],
    feet=["4-5|{c} platform creepers", "4-5|{c} knee-high lace-up boots"])
STYLE_ACC_EXTRA["Emo"] = dict(neck=["a loose cute striped tie", "a skinny black tie worn loose with the collar open", "a short pink-and-black checkered tie"], extra=["black suspenders hanging down at the sides", "black elastic suspenders with silver clips", "red plaid suspenders worn off the shoulders"], wrists=["black and white striped fingerless gloves", "fingerless striped arm gloves", "studded wristbands with striped fingerless gloves"])


# Scene kid shares the emo skeleton (band prints, plaid, fishnet, striped legwear, strap harnesses) in loud neon colours, with tutu and star / heart twists
STYLE_SKIMPY["Scene"] = {k: list(v) for k, v in STYLE_SKIMPY["Emo"].items()}
STYLE_SKIMPY["Scene"]["top"] = STYLE_SKIMPY["Scene"]["top"] + [
    "3|{c} skintight micro tube top with a neon band logo print", "4|{c} star-print micro tube top with a tiny bow",
    "4|{c} heart strap breast harness over a skintight bandeau", "5|{c} heart ring strap breast harness, skin showing between the straps"]
STYLE_SKIMPY["Scene"]["bottom"] = STYLE_SKIMPY["Scene"]["bottom"] + [
    "3-4|{c} micro tutu skirt with a tight waistband", "4-5|{c} rainbow-striped micro mini skirt"]
STYLE_ACC_EXTRA["Scene"] = {k: list(v) for k, v in STYLE_ACC_EXTRA["Emo"].items()}


# goggle / sunglasses hybrids worn pushed up on the head or hanging at the neck: dark, punk and emo looks (not full steampunk)
GOGGLES_NECK = ["round tinted goggle-sunglasses hanging around the neck on a cord", "small round dark-lens goggles hanging around the neck", "tinted goggle-sunglasses resting on the collarbone on a thin chain"]
GOGGLES_HAIR = ["small round tinted goggle-sunglasses pushed up on the head", "dark round-lens goggles resting on top of the head"]
for _s in ("Goth", "Emo", "Scene", "Punk", "Grunge", "Alt Brands"):
    _d = STYLE_ACC_EXTRA.setdefault(_s, {})
    _d["neck"] = list(_d.get("neck", [])) + GOGGLES_NECK
    _d["hair"] = list(_d.get("hair", [])) + GOGGLES_HAIR


# Gyaru: the accessories are half of the look, and they stay at every skimpiness level (neck / ears / wrists / hands / hair / waist are allowed at Skimpy and Micro for this style)
STYLE_ACC_EXTRA["Gyaru"] = dict(
    neck=["several layered thin gold chain necklaces with a small cross pendant", "a pearl strand necklace with a crown pendant", "a rhinestone heart pendant on a thin chain", "a layered chain necklace with a small padlock charm"],
    ears=["large gold hoop earrings", "dangling rhinestone star earrings", "pearl drop earrings with a bow"],
    wrists=["a fluffy leopard-print scrunchie on the wrist", "stacked rhinestone bangles", "several pearl and bead bracelets stacked up the forearm", "a chunky gold charm bracelet", "a wide white studded cuff"],
    hands=["long decorated acrylic nails with rhinestones and tiny charms", "long glittery pink gel nails with 3D bows", "several stacked rings with big rhinestones", "long French-tip nails with tiny rhinestones"],
    waist=["a wide white studded belt with a big buckle", "a leopard-print ribbon tied at the waist", "a chain belt with rhinestones"],
    hair=["a big leopard-print hair bow with pearl strands", "a rhinestone hair clip with a bow", "a pink satin ribbon bow in the hair", "a pearl headband across the hair", "a big pink flower hair clip", "a heart-shaped rhinestone hair pin"],
    face=["oversized sunglasses", "pink-tinted heart-shaped sunglasses"],
    extra=["a pink flip phone covered in dangling charms held up in one hand", "a white handbag covered with dangling charms and tassels", "a big black studded shoulder bag with plush charms", "a quilted chain shoulder bag", "a small glittery bag with a bow"])


# jacket season: the jacket is the whole point, so it is always worn (every level, Micro included, worn open over a tiny top)
JACKET_FIRST = {"Puffer & Cropped Jackets"}


# Baggy Comfy at Revealing, Skimpy and Micro: still hoodies, sweats and soft knits, just cropped, cut out, mesh or worn low (tube tops are the cosy kind of revealing)
STYLE_SKIMPY["Baggy Comfy"] = dict(
    top=["3|{c} cropped oversized hoodie with long baggy sleeves covering the hands, cut off just under the chest",
         "3|{c} soft ribbed tube top under a baggy unzipped hoodie hanging off the shoulders",
         "3-4|{c} baggy cropped hoodie with a keyhole cutout across the chest, the hood up and long baggy sleeves",
         "4|{c} micro-cropped baggy hoodie with a large chest cutout, the hood up and long baggy sleeves covering the hands",
         "4|{c} oversized sheer mesh long-sleeve top with baggy sleeves over a soft tube top",
         "4|{c} baggy fishnet long-sleeve sweater over a soft bandeau",
         "4-5|{c} soft cotton tube top under a cropped hoodie worn open and slipping off the arms",
         "5|{c} micro-cropped hooded sweatshirt with a wide cutout across the chest, the hood up and long baggy sleeves",
         "5|{c} baggy fishnet sweater over a tiny soft tube top"],
    bottom=["3|{c} low-waist baggy sweatpants with a high-rise thong showing above the waistband",
            "3-4|{c} oversized sweatpants rolled down low on the hips with a thong strap showing",
            "4|{c} fleece micro shorts with a thong strap above the waistband",
            "4-5|{c} low-slung baggy joggers hanging at the hips, a string thong visible above them",
            "5|{c} fluffy micro shorts barely covering",
            "5|{c} soft fleece micro skirt barely covering the hips"],
    legs=["3-5|{c} thick knit leg warmers", "3-5|{c} chunky wool thigh-high socks"],
    feet=["3-5|{c} fluffy slippers", "3-5|{c} chunky wool socks"])
