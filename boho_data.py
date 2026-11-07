"""Boho Hippie: modern festival hippie. Dreadlocks, braids and beads in the hair, patchwork and crochet clothes, layered crystal / shell jewellery, hand-poked tattoos."""

_ACC = ("neck", "ears", "hands", "wrists", "waist", "hair", "face", "ankle", "extra")
_O = dict(
    desc="modern boho hippie: patchwork skirts, crochet tops, kimonos, harem pants, tie-dye, layered crystal and shell jewellery",
    palette=["rust orange", "burnt orange", "mustard yellow", "forest green", "emerald green", "cream", "sage green", "terracotta", "faded indigo", "dusty rose"],
    one=["1|{c} patchwork maxi dress with mismatched printed panels", "1-2|{c} tiered gypsy maxi dress with an embroidered bodice", "1-2|{c} tie-dye sundress with thin straps",
         "2|{c} crochet halter mini dress with open-weave panels", "2-3|{c} hand-knitted crochet mini dress", "3|{c} sheer embroidered voile kaftan dress worn over a bikini",
         "3-4|{c} macramé-and-bead fringe mini dress with an open weave over the hips", "4|{c} hand-beaded open-weave fishnet mini dress worn over a bikini set",
         "4-5|{c} knotted rope-and-bead macramé wrap with a long fringe hem, worn over a tiny bikini set"],
    top=["1|{c} oversized chunky cream knit sweater with a big sunflower motif, sleeves pushed up", "1|{c} oversized hand-knitted sweater with a large sun-and-flower pattern", "1|{c} loose hand-embroidered peasant blouse", "1|{c} fitted black turtleneck sleeveless top", "1-2|{c} tie-dye cropped tee", "2|{c} crochet granny-square crop top",
         "2|{c} off-shoulder smocked peasant top", "2-3|{c} halter crochet triangle top with long ties", "3|{c} yellow-and-orange striped crochet bralette top",
         "3|{c} lace-up bandeau with fringe", "3-4|{c} beaded macramé halter top", "4|{c} tiny crochet triangle top tied with cord", "4-5|{c} shell-and-bead strung bandeau", "3|{c} sheer embroidered floral bustier with a strappy cage front and delicate lace trim", "3-4|{c} olive-and-gold crochet halter top with long fringe ties", "4|{c} wide open-weave gold-and-olive crochet bandeau top with knotted cords"],
    bottom=["1|{c} patchwork tiered maxi skirt with mismatched fabrics and woven trim", "1|{c} long patchwork tiered maxi skirt in mismatched olive, mustard and purple printed fabrics with a frayed hem", "1|{c} wide-leg harem pants with a printed pattern", "1-2|{c} long wrap skirt with a hand-block print",
            "2|{c} tie-dye flared mini skirt", "2|{c} low-slung patchwork wrap skirt with a wide leather-and-stud belt", "2-3|{c} crochet mini skirt over a bikini bottom",
            "3|{c} high-slit gypsy skirt with beaded tassels", "3-4|{c} sheer printed sarong tied low on the hips over a bikini bottom", "4|{c} fringed micro skirt with a beaded belt",
            "4-5|{c} knotted crochet string micro skirt", "3-4|{c} open-weave olive-and-gold crochet mini skirt with long side ties and leopard-print cord", "4|{c} low-slung chunky crochet shorts with fringe and lace-up sides"],
    outer=["1|{c} long printed kimono cardigan", "1-2|{c} oversized hand-knitted patchwork cardigan", "2|{c} fringed suede vest", "2-3|{c} flowing emerald-green floral-print silk kimono robe worn open",
           "3|{c} sheer embroidered kimono robe with wide sleeves"],
    legs=["1|{c} wool leg warmers", "2|{c} sheer printed tights with a patchwork hem", "2-3|{c} crochet thigh-high stockings"],
    feet=["1|chunky dark brown platform lace-up boots", "1|barefoot", "1|worn leather ankle boots", "1-2|woven leather sandals", "2|leather lace-up sandals with beads", "2|barefoot with toe rings"],
    head=["1|a wide-brim felt hat", "2|a wide-brim cream felt hat with a gold chain headpiece and chains with beads draped across the forehead", "2|a hand-knitted olive-and-gold headband tied across the forehead", "1-2|a patterned head wrap", "2|a crocheted beanie", "2|a thin beaded headband across the forehead"],
    neck=["layered cowrie shell choker, pearl necklaces and a long rose-quartz crystal pendant", "layered long crystal-pendant necklaces", "a large peace-sign pendant on a long chain with shell strands", "a hand-wrapped amethyst pendant and cowrie shell necklaces",
          "a round locket-style amulet pendant on a hemp cord", "layered beaded and shell chokers with a pendant", "a crescent moon pendant on a long chain"],
    ears=["large dangling feather earrings", "ear cuffs with beads", "chunky hoop earrings with turquoise stones", "ear stacks with small hoops and a dangling charm"],
    hands=["a large spiral mandala tattoo on the back of the hand", "bright green nail polish with stacked rings", "hand-poked tattoos on the fingers and back of the hands", "stacked silver rings with turquoise stones", "a large moonstone ring on each hand", "mandala henna-style hand tattoos"],
    wrists=["chunky knitted olive-and-gold crochet arm cuffs covering the forearms and hands", "stacked beaded and wooden bracelets", "stacked thick gold bangles and pearl bead bracelets", "wrapped leather and bead cuffs", "gemstone bead bracelets", "woven friendship bracelets up the forearm", "arm tattoos in blackwork and traditional style on both forearms"],
    waist=["a layered gold chain belly chain", "a wide leather belt with studs and metal buckles", "a belly chain with hanging beads", "a woven tassel belt"],
    hair=["wooden and bone beads threaded through the hair", "cowrie shells threaded through the hair strands", "a thin braid with feathers and beads", "a patterned fabric wrap woven through the hair",
          "small flowers pinned into the hair", "gold cuffs wrapped around the hair strands", "string and thread wraps with tiny charms on the locks"],
    face=["a septum ring, a nose stud and a tongue piercing", "bold winged eyeliner with freckles drawn across the nose and glitter face gems", "round wire-rim glasses", "round tortoiseshell glasses with soft bangs", "a small nose ring or septum ring", "a lip piercing", "freckles with glowing skin", "glittery festival face gems at the temples"],
    ankle=["an anklet with tiny bells", "a beaded anklet", "toe rings and a thin silver anklet"],
    extra=["large botanical and sunflower tattoos on the arms, shoulders and thighs", "a colourful patchwork shoulder bag with a peace-sign patch", "a woven shoulder basket", "a small embroidered pouch", "a handheld guitar nearby", "a bundle of dried herbs", "a crystal held in one hand", "a vintage film camera in hand"],
)

OUTFIT = {k: v for k, v in _O.items() if k not in _ACC}
OUTFIT["acc"] = {k: v for k, v in _O.items() if k in _ACC}

STYLES_HAIR = [   # "levels|tags|category|text"   category: "Dreads & Boho"
    "4-6|fierce soft|Dreads & Boho|{c} {len} thick dreadlocks, loose and wild, with wooden beads and cowrie shells threaded through some locks",
    "5-6|fierce|Dreads & Boho|{c} {len} dreadlocks in a mix of thick and thin locks, partly wrapped in colourful thread and fabric, with beads and small charms",
    "4-6|cute soft|Dreads & Boho|{c} {len} dreadlocks in two space buns on top of the head with the long ends hanging down, decorated with cowrie shells",
    "4-6|soft|Dreads & Boho|{c} {len} soft, wavy synthetic-look dreadlocks mixed with loose wavy strands, with a few beads and wrapped accents",
    "5-6|fierce soft|Dreads & Boho|{c} {len} thick dreadlocks half tied up in a top knot, the rest falling loose down the back with metal cuffs and feathers",
    "4-6|sultry soft|Dreads & Boho|{c} {len} wild, voluminous dreadlocks with crimped wavy ends and loose face-framing strands, tied back with a patterned head wrap",
    "4-6|fierce|Dreads & Boho|{c} {len} dreadlocks on one side and a shaved sidecut on the other, with silver cuffs on the locks",
    "5-6|soft sultry|Dreads & Boho|{c} {len} loose, wavy, messy hair with several thin braids and cowrie shells and beads threaded through, falling over the shoulders",
    "4-6|soft|Dreads & Boho|{c} {len} hair in long, thin tribal-style braids with beads and wooden rings on the ends",
    "5-6|cute soft|Dreads & Boho|{c} {len} hair in two long braided pigtails wrapped with coloured thread and feathers on the ends",
    "4-6|soft fierce|Dreads & Boho|{c} {len} dreadlocks tied up in a high, loose bun with long locks hanging down and a patterned fabric wrap around the head",
    "5-6|fierce soft|Dreads & Boho|{c} {len} very long, thick dreadlocks in different thicknesses reaching the hips, wrapped with rust and cream thread and beads",
    "5-6|fierce soft|Dreads & Boho|{c} {len} very big, tall dreadlocks piled up in a high loose ponytail on top of the head with the long ends cascading down, gold cuffs and pearl beads on the locks, a knitted headband across the forehead",
    "5-6|soft sultry|Dreads & Boho|{c} {len} dreadlocks tied up high with loose wavy front pieces framing the face, a knitted headband and small gold wraps on the locks",
    "4-6|soft|Dreads & Boho|{c} {len} loose, tousled beachy waves with a few thin braids and a gold chain headpiece draped across the forehead",
]
