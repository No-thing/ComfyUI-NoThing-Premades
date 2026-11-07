"""
More outfit styles for the No_Thing Outfit Roulette: emo and scene, neon raver, masquerade, mourning veils, dominant and submissive fashion.
Same format as outfit_data.py ("levels|text", {c} = main colour, {c2} = accent). Merged into STYLES at the bottom of outfit_data.py.
Levels: 1 covered, 2 cute / a little skin, 3 low-cut and sheer, 4 bold cut-outs, 5 minimal-fabric straps.
"""
M = {}


def S(name, desc, palette, one=(), top=(), bottom=(), outer=(), legs=(), feet=(), head=(), **acc):
    M[name] = dict(desc=desc, palette=list(palette), one=list(one), top=list(top), bottom=list(bottom), outer=list(outer),
                   legs=list(legs), feet=list(feet), head=list(head), acc={k: list(v) for k, v in acc.items()})


S("Emo", "emo: black skinny jeans, band tees, studded belts, striped sleeves, side-swept fringe, guyliner",
  ["black", "black", "charcoal grey", "deep red", "dark purple"],
  one=["1-2|{c} band-tee dress with a studded belt", "2|{c} plaid pinafore dress over a striped long-sleeve", "2-3|{c} torn fishnet-sleeve mini dress with a corset belt",
       "3|{c} lace-up bodycon mini dress with a heart-shaped neckline"],
  top=["1|{c} oversized black band tee", "1|{c} zip-up hoodie with skull print", "1-2|{c} striped long-sleeve shirt under a black band tee", "2|{c} cropped band tee with a safety pin",
       "2|{c} off-shoulder fishnet-sleeve top", "2-3|{c} mesh long-sleeve with a bralette underneath", "3|{c} tie-front crop tee with studded straps",
       "3-4|{c} torn tank top with visible bra straps", "4|{c} lace-up corset crop top with chain details"],
  bottom=["1|{c} skinny jeans with rips", "1|{c} baggy black cargo pants with chains", "1-2|{c} plaid mini skirt", "2|{c} pleated plaid skirt with a studded belt",
          "2-3|{c} denim micro skirt with fishnet tights", "3|{c} low-rise skinny jeans with a studded belt", "3-4|{c} ripped micro shorts over fishnets"],
  outer=["1|{c} studded denim vest", "1-2|{c} oversized hoodie hanging off one shoulder", "2|{c} cropped faux-leather jacket", "2|{c} checkered flannel tied at the waist"],
  legs=["1-2|{c} and white striped knee-high socks", "2|{c} fishnet tights under torn jeans", "2-3|{c} striped thigh-highs", "3|{c} ripped fishnet stockings"],
  feet=["1|{c} high-top sneakers with white laces", "1-2|{c} Converse", "2|{c} chunky buckle boots", "2-3|{c} platform creepers", "3|{c} knee-high lace-up boots"],
  head=["1|a black beanie", "1-2|a skull-print bandana", "2|a studded headband"],
  neck=["a black studded choker", "a heart-lock necklace", "a loose necktie", "a spiked collar", "a skull pendant"], ears=["black spike earrings", "safety-pin earrings"],
  wrists=["striped arm warmers", "studded wristbands", "black rubber bracelets", "fingerless gloves"], hands=["black nail polish with chipped tips", "skull rings"],
  waist=["a studded belt", "a belt with a chain wallet"], hair=["side-swept fringe with a red streak", "choppy layered black hair with a coloured streak"],
  face=["heavy black eyeliner and smudged eyeshadow", "a small lip ring"], ankle=["a chain anklet"], extra=["a skull backpack", "a bat-wing shoulder bag", "a messenger bag covered in band pins"])

S("Scene", "scene kid: neon and black, tutus, striped warmers, big colourful hair, band tees, bows and stars",
  ["hot pink", "neon green", "electric blue", "purple", "black", "white"],
  one=["1-2|{c} cartoon-print tee dress with a tutu skirt", "2|{c} neon tutu dress with a star-print bodice", "2-3|{c} star-print halter mini dress", "3|{c} corset mini dress with a ruffled skirt"],
  top=["1|{c} graphic band tee with a cartoon print", "1|{c} neon zip-up hoodie", "1-2|{c} striped long-sleeve under a neon tee", "2|{c} off-shoulder star-print top",
       "2|{c} crop tee with a skull and bow print", "3|{c} neon bandeau with a bow", "3-4|{c} tied-up crop band tee with fishnet sleeves"],
  bottom=["1|{c} skinny jeans with neon patches", "1-2|{c} plaid mini skirt", "2|{c} layered tutu skirt", "2|{c} zebra-print mini skirt", "2-3|{c} neon pleated micro skirt with chains",
          "3|{c} denim micro shorts with a studded belt"],
  outer=["1|{c} oversized graphic hoodie", "1-2|{c} cropped zip hoodie with a star print", "2|{c} fluffy neon cropped cardigan"],
  legs=["1-2|{c} striped knee-high socks", "2|{c} rainbow leg warmers", "2|{c} star-print tights", "2-3|{c} checkered thigh-highs"],
  feet=["1|{c} bright high-top sneakers", "1-2|{c} checkered slip-on shoes", "2|{c} neon platform sneakers", "2-3|{c} platform boots with buckles"],
  head=["1-2|a big bow headband", "2|a neon trucker cap", "2|a pair of cat-ear headphones"],
  neck=["a studded choker with a star charm", "a neon bead necklace", "a skull-and-bow necklace"], ears=["star stud earrings", "neon hoop earrings"],
  wrists=["a stack of neon jelly bracelets", "striped arm warmers", "a studded bracelet"], hands=["neon nail polish with stars", "colourful rings"],
  waist=["a studded belt with a bow", "a rainbow belt"], hair=["big teased hair with neon streaks", "flat-ironed layered hair with a bow", "rainbow hair extensions"],
  face=["raccoon-eye liner with bright shadow", "heart-shaped glasses"], ankle=[], extra=["a plush cartoon backpack", "a neon shoulder bag with pins"])

S("Neon Raver", "neon rave and festival: contrasting neon colours, mesh, holographic, UV, kandi, fur boots, LED",
  ["neon pink", "electric blue", "acid yellow", "UV purple", "neon green", "holographic silver", "neon orange"],
  one=["2|{c} holographic mini dress with neon trim", "3|{c} sheer mesh bodycon dress with neon straps", "3-4|{c} cut-out mini dress with a {c2} harness", "4|{c} reflective strappy micro dress"],
  top=["1-2|{c} oversized crop tee with a UV print", "2|{c} holographic bralette top", "2-3|{c} fishnet crop top over a bralette", "3|{c} mesh halter top", "3-4|{c} reflective strap bralette",
       "4|{c} cage bralette with {c2} straps", "4-5|{c} star pasties with chain straps"],
  bottom=["1-2|{c} wide-leg neon cargo pants", "2|{c} pleated mini skirt with chains", "2-3|{c} holographic micro skirt", "3|{c} booty shorts with a {c2} waistband",
          "3-4|{c} mesh micro skirt over neon briefs", "4|{c} reflective string-side micro shorts"],
  outer=["1-2|{c} fluffy cropped jacket", "2|{c} holographic puffer vest", "2-3|{c} sheer neon duster"],
  legs=["1-2|{c} leg warmers", "2|{c} fishnet tights", "2-3|{c} holographic thigh-highs", "3|{c} UV mesh stockings"],
  feet=["1-2|{c} platform sneakers", "2|{c} fluffy neon fur boots", "2-3|{c} holographic platform boots", "3|{c} thigh-high platform boots"],
  head=["1-2|a neon bucket hat", "2|LED cat ears", "2|a holographic visor", "2-3|a headband of glowing flowers"],
  neck=["a stack of neon kandi necklaces", "a UV choker", "a LED collar"], ears=["neon hoop earrings", "glowing star earrings"],
  wrists=["arms full of neon kandi bracelets", "holographic wristbands", "glow bracelets"], hands=["neon rings", "UV nail art"],
  waist=["a neon chain belt", "a holographic belly chain"], hair=["neon space buns", "UV-reactive pigtails", "pastel neon braids"],
  face=["holographic face gems and neon liner", "glitter freckles", "round neon sunglasses"], ankle=["a glow-bead anklet"], extra=["a clear festival backpack", "a LED fanny pack"])

S("Masquerade", "masquerade ball: ballgowns and corset dresses, feathered and lace eye masks, opera gloves, jewelled headpieces",
  ["black", "deep burgundy", "midnight blue", "emerald green", "ivory", "deep red", "violet"],
  one=["2|{c} velvet ballgown with a corseted bodice and a full skirt", "2-3|{c} off-shoulder lace ballgown with a long train", "3|{c} corset mini dress with feather trim",
       "3|{c} satin mermaid gown with a high slit", "3-4|{c} sheer beaded gown with a plunging neckline", "4|{c} backless corset gown with a thigh-high slit"],
  top=["2|{c} lace corset top with satin ribbons", "2-3|{c} off-shoulder velvet bodice", "3|{c} sheer embroidered bodice over a bustier", "3-4|{c} jewelled underbust corset over a sheer blouse"],
  bottom=["2|{c} full tulle skirt with a gold trim", "2-3|{c} satin skirt with a thigh slit", "3|{c} high-slit velvet maxi skirt", "3-4|{c} sheer lace overskirt over briefs"],
  outer=["1-2|{c} velvet opera cape", "2|{c} feather-trimmed shawl", "2-3|{c} sheer embroidered robe"],
  legs=["2|{c} sheer stockings with a seam", "3|{c} lace-top thigh-highs"],
  feet=["2|{c} satin pumps with jewelled buckles", "3|{c} strappy gold heels", "3|{c} velvet lace-up heeled boots"],
  head=["2|a jewelled filigree headpiece", "2-3|a feathered fascinator", "3|a lace crown with dangling beads"],
  neck=["a jewelled choker", "a velvet ribbon choker with a cameo", "a pearl collar necklace", "a gold filigree collar"], ears=["chandelier earrings", "pearl drop earrings"],
  wrists=["opera-length satin gloves", "long lace gloves", "jewelled cuffs"], hands=["a ring with a large dark gemstone", "gold filigree rings"],
  waist=["a jewelled corset belt", "a satin sash with a brooch"], hair=["an updo with feathers and jewels", "loose curls with a jewelled comb"],
  face=["a venetian eye mask with gold filigree", "a black lace masquerade eye mask with ribbon ties", "a feathered half mask with crystals", "a porcelain half mask with gold paint",
        "a beaded cat-eye mask", "a sheer black face veil with a jewelled edge"], ankle=["a delicate chain anklet"], extra=["a feathered fan", "a mask held on a stick", "a velvet clutch"])

S("Mourning Veils", "Victorian mourning and veiled gothic: black lace gowns, funeral veils, face veils and netting, jet jewellery, black roses",
  ["black", "black", "black", "charcoal grey", "deep burgundy", "dark plum"],
  one=["1-2|{c} high-neck Victorian mourning dress with long lace sleeves", "2|{c} lace gown with a high collar and a long skirt", "2-3|{c} velvet gown with a corseted waist and a lace veil",
       "3|{c} sheer lace mourning gown over a slip", "3-4|{c} corseted black lace gown with a plunging neckline", "4|{c} sheer tulle gown with embroidered lace patches"],
  top=["1|{c} lace high-neck blouse with cameo buttons", "1-2|{c} velvet bodice with lace sleeves", "2|{c} sheer lace long-sleeve with a ribbon collar", "3|{c} lace corset top with a sheer lace shawl",
       "3-4|{c} tulle bralette under an open lace jacket"],
  bottom=["1|{c} long layered black skirt", "2|{c} tiered lace skirt", "2-3|{c} velvet skirt with a slit", "3|{c} sheer lace skirt over black shorts", "3-4|{c} tulle micro skirt with a lace hem"],
  outer=["1|{c} long black lace cape", "1-2|{c} hooded velvet cloak", "2|{c} cropped lace shrug", "2-3|{c} sheer funeral shawl"],
  legs=["1-2|{c} opaque tights with lace tops", "2|{c} sheer black stockings with a seam", "3|{c} lace thigh-highs"],
  feet=["1-2|{c} lace-up ankle boots", "2|{c} buttoned Victorian boots", "3|{c} knee-high lace-up heeled boots"],
  head=["1-2|a black hat with a birdcage veil", "2|a wide-brim black hat with a long lace veil", "2|a lace mantilla veil", "2-3|a black feather headpiece with a short net veil",
        "3|a hooded lace veil"],
  neck=["a jet-bead choker", "a black velvet ribbon with a cameo", "a black rose pendant", "a high lace collar"], ears=["jet drop earrings", "black pearl earrings"],
  wrists=["black lace gloves", "long satin gloves", "a jet bracelet"], hands=["a black onyx ring", "a skull ring", "a mourning ring with braided hair"],
  waist=["a black satin sash", "a velvet waist cincher"], hair=["a loose black veil pinned in the hair", "an updo with black roses"],
  face=["a black birdcage face veil covering the eyes", "a long black mourning veil over the face", "a sheer black net veil covering the whole face", "a lace face veil with a beaded edge",
        "a black mesh face covering with only the lips showing", "a veiled half-face of lace"], ankle=["a lace ankle ribbon"], extra=["a bouquet of black roses", "a black lace parasol", "a small prayer book"])

S("Dominant", "dominant fashion: leather, latex and PVC, harness dresses, thigh boots, long gloves, collars and heavy buckles",
  ["black", "black", "deep red", "gunmetal", "silver", "oxblood"],
  one=["2|{c} leather pencil dress with a zip front", "3|{c} latex catsuit with a front zip", "3|{c} PVC corset dress with buckles", "3-4|{c} leather harness dress with ring details",
       "4|{c} wet-look cut-out bodysuit with a ring-linked harness", "4-5|{c} leather strap dress with silver O-rings"],
  top=["2|{c} leather bustier with buckles", "2-3|{c} latex crop top with a high collar", "3|{c} PVC corset with a front busk", "3-4|{c} leather bra harness with silver rings",
       "4|{c} caged leather harness top", "4-5|{c} pentagram strap harness over the bust"],
  bottom=["2|{c} leather mini skirt", "2-3|{c} high-waisted latex skirt", "3|{c} PVC micro skirt with a zip", "3-4|{c} leather shorts with a buckled belt", "4|{c} strappy leather garter belt harness"],
  outer=["1-2|{c} long leather trench coat", "2|{c} cropped leather jacket", "2-3|{c} open latex duster"],
  legs=["2|{c} opaque tights", "2-3|{c} latex stockings", "3|{c} fishnet stockings with a garter belt", "3-4|{c} seamed thigh-highs"],
  feet=["2|{c} knee-high leather boots", "2-3|{c} stiletto ankle boots", "3|{c} thigh-high latex boots", "3-4|{c} patent platform thigh-high boots with buckles"],
  head=["2|a leather peaked cap", "2-3|a black veil with a leather headband"],
  neck=["a wide leather collar with an O-ring", "a spiked choker", "a studded leather collar with a chain", "a silver chain collar"], ears=["silver bar earrings", "black spike earrings"],
  wrists=["long black leather gloves", "buckled leather cuffs", "latex opera gloves"], hands=["heavy silver rings", "black lacquered nails"],
  waist=["a wide leather corset belt", "a chain waist harness"], hair=["a slicked-back high ponytail", "a sleek bob"],
  face=["sharp red lipstick and winged liner", "a leather half mask"], ankle=["a buckled ankle cuff"], extra=["a leather riding crop", "a chain leash held in one hand"])

S("Submissive", "submissive fashion: soft satin and lace, ribbon collars, pastel and white, delicate harnesses, bows, sheer layers",
  ["blush pink", "ivory", "white", "powder blue", "lavender", "soft red", "pastel pink"],
  one=["2|{c} satin slip dress with a ribbon collar", "2-3|{c} lace babydoll with a bow at the bust", "3|{c} sheer chemise with a ribbon choker", "3-4|{c} satin teddy with a ring-front collar",
       "4|{c} sheer bodysuit with a ribbon harness"],
  top=["1-2|{c} soft knit cropped sweater slipping off one shoulder", "2|{c} lace bralette with a satin bow", "2-3|{c} sheer blouse tied at the bust", "3|{c} satin ribbon bra harness",
       "3-4|{c} delicate strap harness over a lace bralette"],
  bottom=["1-2|{c} pleated mini skirt", "2|{c} satin shorts with a bow", "2-3|{c} lace-trim high-waisted briefs", "3|{c} satin tie-side panties", "3-4|{c} garter belt with satin ribbons"],
  outer=["1-2|{c} oversized white shirt worn open", "2|{c} sheer satin robe", "2|{c} soft cardigan falling off the shoulders"],
  legs=["1-2|{c} knee-high socks with a bow", "2|{c} lace-top thigh-highs", "2-3|{c} sheer stockings with satin clips"],
  feet=["1|{c} ballet flats with ribbon ties", "2|{c} Mary Jane shoes", "2-3|{c} satin ballet heels with ankle ribbons"],
  head=["1-2|a satin bow headband", "2|a lace bow in the hair"],
  neck=["a satin ribbon collar with a small bell", "a velvet choker with a ring", "a pearl choker", "a lace collar with a heart charm"], ears=["tiny pearl earrings"],
  wrists=["satin ribbon wrist cuffs", "lace wrist cuffs"], hands=["a simple pearl ring"], waist=["a satin ribbon waist tie"], hair=["twin ribbon braids", "loose waves with a bow"],
  face=["soft pink blush and glossy lips"], ankle=["a satin ribbon ankle tie", "a lace anklet"], extra=["a plush toy", "a ribbon leash held loosely"])


# ------------------------------------------------------------------------------------------ beach, sporty, boxing, techwear, jackets
S("Beach", "beach day: huge sun hats, sheer white dresses, string bikinis, sarongs, straw bags, salt-tousled hair",
  ["white", "white", "sand beige", "turquoise", "coral", "sunny yellow", "black", "seafoam green", "coral pink"],
  one=["1|{c} flowy linen beach maxi dress", "1-2|sheer white gauze beach dress worn over a bikini", "2|{c} crochet beach dress with open sides", "2-3|sheer white cotton beach dress with the bikini visible underneath",
       "3|sheer white beach dress clinging wet to the skin over a string bikini", "3-4|{c} sheer mesh beach cover-up over a string bikini", "4|{c} high-cut one-piece swimsuit with cut-outs and tie sides",
       "4-5|{c} plunging halter one-piece with thin side strings"],
  top=["1-2|{c} linen shirt tied at the waist over a bikini top", "2|{c} cropped tank over a bikini top", "2|{c} bandeau bikini top", "3|{c} triangle bikini top tied with thin strings at the neck and back",
       "3-4|{c} string bikini top with small triangles", "4|{c} micro triangle string bikini top", "4-5|{c} sliding-triangle micro bikini top with thin ties"],
  bottom=["1-2|{c} sarong tied at the hip", "2|{c} high-waisted bikini bottoms", "2|{c} denim cut-off shorts over a bikini", "2-3|{c} crochet beach shorts", "3|{c} side-tie string bikini bottoms",
          "3-4|{c} low-rise string bikini bottoms with thin side strings", "4|{c} thong-cut Brazilian bikini bottoms with side ties", "4-5|{c} micro string bikini bottoms with thin ties"],
  outer=["1-4|sheer white kimono cover-up", "1-3|oversized white linen shirt worn open", "2-4|{c} sheer mesh beach robe", "2|{c} cropped open-knit cardigan"],
  legs=[],
  feet=["1-5|{c} leather flip-flops", "1-5|{c} strappy flat sandals", "1-5|barefoot with sand on the feet", "1-5|{c} jelly sandals"],
  head=["1-5|an oversized wide-brim straw sun hat", "1-5|a huge floppy white sun hat with a ribbon", "1-5|a wide-brim woven sun hat tilted low over the eyes", "1-5|a giant black sun hat with a wide brim",
        "1-5|a straw bucket hat", "1-5|a silk headscarf tied at the nape", "1-5|a wide-brim sun hat held in one hand"],
  neck=["a puka shell necklace", "a fine gold chain with a tiny shell", "a thin cord with a pearl"], ears=["gold hoop earrings", "shell earrings"],
  wrists=["a stack of woven bracelets", "a thin gold bangle"], hands=["a simple gold ring"], waist=["a beaded waist chain", "a fine gold belly chain"],
  hair=["salt-tousled beach waves", "a loose braid with seashells", "damp hair slicked back"], face=["oversized round sunglasses", "cat-eye sunglasses", "tiny retro sunglasses"],
  ankle=["a shell anklet", "a fine gold anklet"], extra=["a woven straw tote bag", "a beach towel over one shoulder", "a straw beach bag with a bottle of sunscreen"])

S("Sporty Girl", "sporty and gym girl: cropped hoodies over sports bras, low-waist sweatpants with a high-rise thong, bike shorts, sneakers",
  ["black", "grey", "white", "baby pink", "neon pink", "navy blue", "lilac", "sage green"],
  one=["1-2|{c} sporty zip-up unitard", "2|{c} tennis dress with built-in shorts", "3|{c} seamless sports bodysuit with cut-outs", "3-4|{c} backless gym bodysuit"],
  top=["1|{c} cropped hoodie over a matching sports bra", "1-2|{c} cropped zip hoodie worn open over a sports bra", "2|{c} cropped hoodie with a sports bra visible underneath", "2|{c} cropped training tee over a sports bra",
       "2-3|{c} high-neck sports bra", "3|{c} strappy racerback sports bra", "3-4|{c} cropped hoodie unzipped to the ribs over a sports bra", "4|{c} micro sports bra top with cut-outs"],
  bottom=["1|{c} baggy sweatpants", "2|{c} low-waist sweatpants with a high-rise thong visible above the waistband", "2-3|{c} low-rise sweatpants rolled at the waist with a high-rise thong strap showing above",
          "3|{c} low-rise track pants with a high-rise thong showing above the waistband", "3|{c} micro running shorts", "3-4|{c} low-rise booty shorts with a high-rise thong visible",
          "3|{c} pleated tennis mini skirt over bike shorts", "4|{c} ultra-low-rise sweatpants with a high-rise string thong strap pulled above them"],
  outer=["1-2|{c} cropped track jacket", "2|{c} cropped windbreaker", "2|{c} cropped zip-up fleece"],
  legs=["1|{c} white ankle socks", "1-2|{c} crew socks pulled up", "2|{c} ribbed knee-high socks"],
  feet=["1|{c} chunky running sneakers", "1|{c} white platform sneakers", "2|{c} high-top trainers"],
  head=["1|a baseball cap worn backwards", "1-2|a sports visor", "2|a sweatband"],
  neck=["a thin chain with a small pendant"], ears=["small gold hoops"], wrists=["a sports watch", "a sweatband on the wrist"], hands=[], waist=["a small gym belt bag"],
  hair=["a high ponytail", "a messy gym bun", "a sleek braided ponytail"], face=["sporty wrap sunglasses"], ankle=[], extra=["a gym duffel bag", "a water bottle", "a towel over the shoulder"])

S("Boxing & Gym Brands", "boxing and gym labels: Lonsdale, Everlast, Gymshark, Venum, Hayabusa, Title Boxing",
  ["black", "red", "white", "navy blue", "grey", "royal blue"],
  one=["1-2|{c} Gymshark seamless zip-up unitard", "3|{c} Gymshark cut-out seamless bodysuit"],
  top=["1|{c} Lonsdale cropped hoodie over a sports bra", "1-2|{c} Everlast cropped logo hoodie over a sports bra", "2|{c} Gymshark seamless cropped tank over a sports bra", "2|{c} Venum cropped fight tee",
       "2-3|{c} Gymshark seamless sports bra with a high neck", "3|{c} Everlast logo-band sports bra", "3-4|{c} Lonsdale strappy sports bra", "4|{c} Venum micro sports bra"],
  bottom=["1|{c} Lonsdale baggy sweatpants", "2|{c} Everlast boxing shorts with a wide logo waistband riding low over a high-rise thong strap", "2-3|{c} Lonsdale low-rise sweatpants with a high-rise thong visible above the waistband",
          "3|{c} Gymshark low-rise seamless leggings", "3|{c} Venum fight shorts cut high on the hip", "3-4|{c} Gymshark low-waist booty shorts with a high-rise thong showing", "4|{c} Everlast micro boxing shorts"],
  outer=["1-2|{c} Lonsdale cropped track jacket", "2|{c} Everlast satin boxing robe worn open", "2|{c} Gymshark cropped zip-up jacket"],
  legs=["1|{c} Everlast ankle socks", "2|{c} Gymshark crew socks"],
  feet=["1|{c} Everlast boxing boots", "1|{c} Lonsdale trainers", "2|{c} Venum fight shoes"],
  head=["1|a Lonsdale beanie", "1-2|a Gymshark cap", "2|a boxing headband"],
  neck=["a pair of Everlast boxing gloves hanging round the neck", "a thin chain"], wrists=["red boxing hand wraps", "a Gymshark sweatband"], hands=[], waist=["a championship-style belt over one shoulder"],
  hair=["a tight high ponytail", "braids tied back for training"], face=["a mouthguard hanging from the lip"], ankle=[], extra=["a Lonsdale gym bag", "a Venum duffel bag", "a speed rope"])

S("Cyber Techwear", "cyberpunk techwear: cropped tech jackets with straps and buckles, tactical harnesses, cargo pants, visors",
  ["black", "black", "charcoal grey", "neon green", "electric blue", "hot pink", "gunmetal"],
  one=["2|{c} techwear jumpsuit with straps and buckles", "3|{c} cut-out tactical bodysuit with a utility belt", "4|{c} mesh techwear bodysuit with a chest harness"],
  top=["1-2|{c} cropped tech jacket with straps and buckles worn over a sports bra", "2|{c} cropped utility vest over a fitted crop top", "2-3|{c} cropped nylon jacket with reflective panels over a bralette",
       "3|{c} mesh long-sleeve with a tactical chest harness", "3-4|{c} strappy tactical bra top with buckles", "4|{c} cropped zip-up tech bra top with straps"],
  bottom=["1-2|{c} wide cargo pants with straps and zips", "2-3|{c} low-rise techwear cargo pants with a high-rise thong visible above the waistband and a utility belt", "3|{c} low-rise tactical pants with buckles and a high-rise thong strap showing",
          "3|{c} tech mini skirt with straps over bike shorts", "3-4|{c} low-rise cargo shorts with a high-rise thong visible", "4|{c} micro tech shorts with thigh straps"],
  outer=["1-2|{c} cropped cyberpunk tech jacket with a high collar and straps", "2|{c} cropped shell jacket with reflective trim", "2|{c} cropped utility jacket with buckles", "2-3|{c} sheer techwear cape with a hood"],
  legs=["2|{c} mesh tights with buckled leg straps", "2-3|{c} thigh-high tech socks", "3|{c} fishnet tights under cargo shorts"],
  feet=["1-2|{c} chunky tech sneakers", "2|{c} tactical platform boots with buckles", "3|{c} knee-high techwear boots with straps"],
  head=["1-2|a black balaclava pulled down at the neck", "2|a futuristic visor"],
  neck=["a utility harness collar", "a glowing LED choker"], ears=["a row of small ear cuffs", "metal hoop earrings"],
  wrists=["a tactical wrist strap with a small display", "buckled arm straps"], hands=["fingerless tactical gloves", "chunky metal rings"], waist=["a utility belt with pouches", "a buckled strap belt with a chain"],
  hair=["a sleek bob with neon streaks", "twin buns with colour streaks"], face=["mirrored sunglasses", "a transparent visor"], ankle=[], extra=["a tactical crossbody pouch", "a holographic backpack"])

S("Y2K Techwear", "Y2K tech and futuristic: silver nylon cropped jackets, parachute pants, reflective straps, mini goggles, metallic fabrics",
  ["silver metallic", "silver metallic", "black", "ice blue", "baby pink", "chrome", "white"],
  one=["2|{c} nylon zip jumpsuit with a cropped jacket", "3|{c} sheer holographic mini dress with a cropped shell jacket", "4|{c} wet-look cut-out bodysuit with silver straps"],
  top=["1-2|{c} cropped nylon jacket over a bandeau top", "2|{c} cropped puffer vest over a baby tee", "2-3|{c} cropped zip-up shell jacket over a bralette", "3|{c} holographic crop halter with silver zips",
       "3-4|{c} strappy bra top with ring details", "4|{c} mirrored tube top with straps"],
  bottom=["1-2|{c} wide parachute pants with toggles", "2-3|{c} low-waist parachute pants with a high-rise thong showing above the waistband", "3|{c} low-rise metallic cargo pants with a high-rise thong strap visible and a chain belt",
          "3|{c} reflective mini skirt with a silver zip", "3-4|{c} low-rise nylon micro shorts with a high-rise thong visible", "4|{c} mirrored micro skirt with strap details"],
  outer=["1-2|{c} cropped nylon bomber jacket", "2|{c} cropped windbreaker", "2|{c} cropped shiny puffer jacket", "2-3|{c} sheer holographic cropped jacket"],
  legs=["2|{c} leg warmers", "2-3|{c} fishnet tights", "3|{c} holographic thigh-highs"],
  feet=["1-2|{c} chunky futuristic platform sneakers", "2|{c} platform boots", "3|{c} knee-high platform boots"],
  head=["1-2|a silver bucket hat", "2|tiny rectangular goggles worn on the head", "2|a nylon visor cap", "2|a metallic headband"],
  neck=["a chrome chain choker", "a silver dog-tag necklace", "a holographic scarf"], ears=["silver hoop earrings", "mini orb earrings"], wrists=["a silver chain bracelet", "a clear plastic watch"],
  hands=["silver ring stack"], waist=["a metallic chain belt", "a reflective strap belt"], hair=["slicked sleek hair with butterfly clips", "a high pony with a silver scrunchie"],
  face=["tiny wraparound sunglasses", "a clear visor", "glitter on the cheekbones"], ankle=[], extra=["a mini metallic shoulder bag", "a silver tech backpack"])

S("Puffer & Cropped Jackets", "jacket season: cropped pilot bombers, cropped leather jackets, shiny and oversized puffers over little underneath",
  ["black", "white", "silver metallic", "baby pink", "red", "olive green", "chocolate brown", "ice blue"],
  top=["1|{c} fitted crop tee", "1|{c} ribbed tank top", "1-2|{c} sports bra", "2|{c} lace bralette", "2-3|{c} bandeau top", "3|{c} bikini top", "3-4|{c} strappy bralette",
       "4-5|{c} tiny bandeau top", "5|{c} tiny triangle bra top on thin straps"],
  bottom=["1|{c} baggy cargo pants", "1|{c} straight jeans", "2|{c} low-rise jeans with a studded belt", "2-3|{c} low-rise cargo pants with a high-rise thong showing above the waistband", "3|{c} leather mini skirt",
          "3|{c} low-rise leather pants with a high-rise thong visible", "3-4|{c} micro shorts", "4|{c} low-rise bike shorts with a thong strap above the waistband",
          "5|{c} micro skirt barely covering the hips", "5|{c} low-slung string micro shorts"],
  outer=["1|{c} oversized shiny puffer jacket zipped up", "1-5|{c} cropped puffer jacket", "1-3|{c} cropped pilot bomber jacket with a shearling collar", "1-5|{c} cropped leather biker jacket",
         "2-5|{c} cropped faux-leather moto jacket worn open", "2-4|{c} cropped varsity jacket worn open", "3-5|{c} cropped shearling-trim aviator jacket worn open", "1-2|{c} oversized bomber jacket"],
  legs=["1-2|{c} knee-high socks", "2|{c} fishnet tights", "2-5|{c} ribbed thigh-highs"],
  feet=["1|{c} chunky sneakers", "2-5|{c} platform boots", "2-5|{c} knee-high boots"],
  head=["1-2|a beanie", "2|a fur-trim hood up", "2|a trucker cap"],
  neck=["a thick chain necklace", "a silk scarf"], ears=["hoop earrings"], wrists=["a stack of bracelets"], hands=["chunky rings"], waist=["a studded belt", "a chain belt"],
  hair=["a sleek high ponytail", "loose waves"], face=["aviator sunglasses", "small slim sunglasses"], ankle=[], extra=["a mini shoulder bag", "a duffel bag"])

# ------------------------------------------------------------------------------------------ extra pieces for styles that already exist
ADD = {}


def A(style, **slots):
    ADD.setdefault(style, {}).update({k: list(v) for k, v in slots.items()})


JACKETS = ["1-2|{c} cropped pilot bomber jacket with a shearling collar", "2|{c} cropped leather biker jacket", "2|{c} cropped faux-leather moto jacket with studs", "2|{c} cropped shiny puffer jacket",
           "1-2|{c} oversized shiny puffer jacket", "2|{c} cropped nylon tech jacket with reflective panels", "2|{c} cropped varsity jacket", "2|{c} cropped denim jacket"]
LOWRISE = ["3|{c} low-rise camo cargo pants with a high-rise thong showing above the waistband and a studded belt", "3|{c} ultra-low-rise baggy jeans with a high-rise lace thong pulled up above them and a studded belt",
           "3-4|{c} low-waist plaid pants with a high-rise thong strap above the waistband and a chain belt", "3-4|{c} low-rise leather pants with a high-rise string thong visible above the waistband",
           "3|{c} low-rise flared jeans with a high-rise rhinestone thong showing above the waistband", "3-4|{c} low-rise denim mini skirt with a high-rise thong strap pulled up above it",
           "3|{c} low-waist parachute pants with a high-rise thong showing", "3-4|{c} low-rise camo shorts with a high-rise thong and a studded belt"]

A("Y2K", outer=JACKETS[:6], bottom=LOWRISE[:5] + ["4|{c} low-rise micro skirt with a high-rise thong strap showing"],
  top=["3|{c} baby tee cropped above the ribs with a lace bra showing underneath", "3-4|{c} rhinestone tube top with a visible strap bra", "4|{c} cropped halter tied with thin strings"])
A("Goth", outer=["2|{c} cropped leather biker jacket", "2|{c} cropped pilot bomber jacket", "2|{c} cropped studded moto jacket", "2|{c} cropped faux-fur jacket"],
  bottom=["3|{c} low-rise camo pants with a high-rise thong showing above the waistband and a studded belt", "3-4|{c} low-rise leather pants with a high-rise lace thong visible and a chain belt",
          "3-4|{c} low-rise fishnet-panelled pants with a high-rise thong showing"],
  top=["3|{c} cropped corset top with a lace bra showing", "3-4|{c} cropped band tee tied up over a lace bralette", "4|{c} strappy harness top with a mesh long-sleeve"])
A("Emo", outer=["2|{c} cropped leather jacket", "2|{c} cropped studded denim jacket", "2|{c} cropped pilot bomber jacket", "2|{c} cropped zip hoodie"],
  bottom=["3|{c} low-rise camo pants with a high-rise thong showing above the waistband and a studded belt", "3|{c} ultra-low-rise skinny jeans with a high-rise lace thong visible and a studded belt",
          "3-4|{c} low-rise plaid pants with a high-rise thong strap showing and a chain belt", "4|{c} low-rise ripped micro shorts with a high-rise thong showing"],
  top=["3|{c} cropped band tee tied up over a bralette", "3-4|{c} cropped hoodie hanging off one shoulder over a lace bra"])
A("Scene", outer=["2|{c} cropped neon puffer jacket", "2|{c} cropped zip hoodie", "2|{c} cropped pilot bomber jacket"],
  bottom=["3|{c} low-rise camo pants with a high-rise thong showing above the waistband and a studded belt", "3-4|{c} ultra-low-rise skinny jeans with a high-rise neon thong visible",
          "3-4|{c} low-rise plaid mini skirt with a high-rise thong strap above it"],
  top=["3|{c} cropped band tee tied up over a neon bralette"])
A("Punk", outer=["2|{c} cropped leather biker jacket with studs", "2|{c} cropped denim vest jacket with patches"],
  bottom=["3|{c} low-rise camo pants with a high-rise thong showing above the waistband and a studded belt", "3-4|{c} low-rise tartan pants with a high-rise thong strap showing and a chain belt"])
A("Grunge", outer=["2|{c} cropped flannel jacket", "2|{c} cropped leather jacket", "2|{c} cropped denim jacket"],
  bottom=["3|{c} low-rise camo pants with a high-rise thong showing above the waistband and a studded belt", "3|{c} ultra-low-rise baggy jeans with a high-rise thong visible"])
A("Casual", outer=JACKETS[:3] + JACKETS[5:], bottom=["3|{c} low-rise baggy jeans with a high-rise thong showing above the waistband", "3|{c} low-waist sweatpants with a high-rise thong strap above them"])
A("Streetwear Brands", outer=["2|{c} cropped Nike puffer jacket", "2|{c} cropped Adidas track jacket", "2|{c} cropped North Face puffer jacket", "1-2|{c} oversized shiny Supreme puffer jacket"])
A("Latex", outer=["2|{c} cropped latex jacket", "2|{c} cropped patent leather jacket"])
A("Athleisure Brands", outer=["1-2|{c} cropped Nike windbreaker", "2|{c} cropped Adidas track jacket", "2|{c} cropped puffer jacket"])

HEAD_CHANCE = {"Beach": 0.75, "Cyber Techwear": 0.5, "Y2K Techwear": 0.4}
MORE = M
