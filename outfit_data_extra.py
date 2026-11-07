"""
More outfit styles for the No_Thing Outfit Roulette: Japanese kawaii / street styles and well-known brand sets.
Same format as outfit_data.py ("levels|text", {c} = main colour, {c2} = accent). Merged into STYLES at the bottom of outfit_data.py.
Brand names are only prompt words: they steer the look, no logos are promised.
"""
X = {}


def S(name, desc, palette, one=(), top=(), bottom=(), outer=(), legs=(), feet=(), head=(), **acc):
    X[name] = dict(desc=desc, palette=list(palette), one=list(one), top=list(top), bottom=list(bottom), outer=list(outer),
                   legs=list(legs), feet=list(feet), head=list(head), acc={k: list(v) for k, v in acc.items()})


# ------------------------------------------------------------------------------------------ Japanese
S("Harajuku Kawaii", "Harajuku decora and fairy-kei: pastel layers, charms, candy colours (6%DOKIDOKI, Swimmer, Spank!)",
  ["pastel pink", "mint green", "lavender", "baby blue", "butter yellow", "rainbow pastel", "white and pastel pink"],
  one=["1-2|{c} pastel dungaree dress over a striped long-sleeve tee", "2|{c} fairy-kei tulle party dress with star prints", "2|{c} Swimmer-style strawberry print sundress",
       "2-3|{c} ruffled jumper dress with a heart bib", "3|{c} candy-colour puff-sleeve mini dress with ribbons"],
  top=["1|oversized {c} pastel cartoon-print sweatshirt", "1-2|{c} fluffy knit cardigan with bunny ears on the hood", "2|{c} puff-sleeve blouse with a big Peter Pan collar",
       "2|{c} rainbow-trim crop tee with a cute character print", "2|{c} baby-doll tee with pastel lace trim", "2-3|{c} 6%DOKIDOKI-style heart-print crop top",
       "3|{c} cropped sailor-collar blouse with ribbon ties"],
  bottom=["1|{c} pastel pleated midi skirt", "1-2|{c} tutu skirt layered over bloomers", "2|{c} checkered mini skirt with a cute chain", "2|{c} rainbow-print tulle skirt",
          "2-3|{c} pleated micro skirt with a charm belt", "3|{c} cargo mini skirt with ribbons"],
  outer=["1-2|{c} oversized pastel bomber jacket with patches", "2|{c} fluffy faux-fur jacket with a character hood", "2|{c} puffy pastel puffer coat"],
  legs=["1-2|rainbow striped over-the-knee socks", "2|{c} fishnet tights under pastel socks", "2-3|{c} heart-print thigh-high socks"],
  feet=["1-2|{c} chunky platform sneakers", "2|{c} Mary Jane platform shoes with ribbon", "2|{c} pastel platform boots with plush pom-poms"],
  head=["1-2|a pile of colourful hair clips", "2|a plush bunny-ear headband", "2|an oversized pastel bow", "2|a pastel bucket hat with pins"],
  neck=["a candy bead necklace", "a layered charm necklace", "a heart-shaped locket choker"], ears=["star clip-on earrings", "pastel bead earrings"],
  wrists=["a pile of rainbow bead bracelets", "a plastic candy-charm bracelet"], hands=["chunky pastel resin rings", "sweet-treat rings"],
  waist=["a heart-link charm belt"], hair=["twin-tails with big bows", "colourful hair clips", "pastel hair extensions in two buns"],
  face=["heart-shaped sunglasses", "heart face stickers"], ankle=["a pastel bead anklet"], extra=["a plush-character backpack", "a cute character shoulder bag covered in keychains"])

S("Doll Style", "Japanese doll fashion: frilly sweet / classic / gothic dresses (Angelic Pretty, Baby the Stars Shine Bright, Metamorphose, Innocent World)",
  ["pastel pink", "cream", "mint green", "lavender", "black", "wine red", "navy blue", "white and pink"],
  one=["1-2|{c} Angelic Pretty-style sweet jumperskirt with a sweets print", "1-2|{c} Innocent World-style classic dress with a lace collar", "2|{c} Baby the Stars Shine Bright-style cupcake-skirt dress",
       "2|{c} Metamorphose-style OP dress with ruffles and bows", "2|{c} puff-sleeve tea-party dress with a petticoat", "2-3|{c} gothic doll dress with a corset bodice and lace trim",
       "3|{c} short sweet dress with a layered petticoat showing"],
  top=["1|{c} high-neck lace blouse with a bow", "1-2|{c} puff-sleeve blouse with a cameo brooch", "2|{c} frilled cut-sew with a heart print"],
  bottom=["1-2|{c} full skirt with a lace hem over a petticoat", "2|{c} tiered ruffle skirt with ribbon trim", "2|{c} bell-shaped skirt with strawberry print", "3|{c} short tulle skirt with a frilly hem"],
  outer=["1-2|{c} velvet bolero with ribbon ties", "2|{c} cape-collar jacket with bows", "2|{c} cropped cardigan with pearl buttons"],
  legs=["1-2|white lace-trim ankle socks", "2|{c} over-the-knee socks with bows", "2|white frilled tights"],
  feet=["1-2|{c} rocking-horse shoes", "2|{c} tea-party strap shoes with a bow", "2|{c} heart-buckle platform shoes"],
  head=["1-2|a big satin bow headdress", "2|a lace bonnet with ribbons", "2|a mini top hat on a headband", "2|{c} bow clips on both sides"],
  neck=["a cameo choker", "a ribbon-tie neck bow", "a pearl necklace with a heart pendant"], ears=["pearl drop earrings"], wrists=["lace cuffs", "a bow bracelet"],
  hair=["long curled twin-tails with a bow", "curly hair with a headdress", "a wig with long ringlets"], extra=["a heart-shaped shoulder bag", "a mini basket bag", "a frilly parasol"])

S("Jirai Kei", "Jirai-kei 'landmine' girl: black and pink ruffles, ribbons, mass-produced cute (Liz Lisa, Ank Rouge, Rojita, Secret Honey)",
  ["black and pink", "black", "baby pink", "wine red", "white and black", "lavender"],
  one=["1-2|{c} Rojita-style ruffled lace dress with ribbons", "2|{c} Ank Rouge-style heart-neck dress with a lace hem", "2|{c} Secret Honey-style off-shoulder dress with bows",
       "2-3|{c} Liz Lisa-style puff-sleeve mini dress with lace trim", "3|{c} lace-up corset mini dress with ruffles"],
  top=["1-2|{c} frilled lace blouse with a big ribbon", "2|{c} Liz Lisa-style off-shoulder knit top with a bow", "2|{c} cold-shoulder tee with heart prints", "2-3|{c} cropped ruffle blouse with a corset waist",
       "3|{c} lace-up bustier-style top over a sheer blouse"],
  bottom=["1-2|{c} tiered mini skirt with lace", "2|{c} pleated mini skirt with a heart buckle belt", "2|{c} tulle mini skirt with ribbons", "3|{c} short plaid skirt with chains"],
  outer=["2|{c} oversized hoodie with bunny ears", "2|{c} cropped cardigan with heart buttons", "2-3|{c} fluffy faux-fur bolero"],
  legs=["2|{c} black-and-pink ribbon tights", "2|{c} fishnet tights", "2-3|{c} over-the-knee socks with bows"],
  feet=["1-2|{c} platform Mary Janes", "2|{c} chunky platform sneakers", "2|{c} heart-buckle platform shoes"],
  head=["2|a big black satin bow", "2|a lace headband", "2|heart-shaped hair clips"],
  neck=["a ribbon choker with a heart pendant", "a pink lace choker", "a cross pendant necklace"], ears=["heart earrings", "cross studs"],
  wrists=["a pink-and-black charm bracelet", "a lace wrist cuff"], hair=["twin-tails with big bows", "long straight hair with hime bangs", "a high bunch with a ribbon"],
  face=["a medical eye-patch accessory"], extra=["a heart-shaped shoulder bag with chains", "a backpack covered in plush charms", "a coffin-shaped bag"])

S("Gyaru", "Gyaru: tanned glam, mini skirts, platform boots (Egoist, Rady, Liz Lisa, Moussy, SLY, Emoda)",
  ["white", "black", "baby pink", "beige", "gold metallic", "red", "denim blue", "leopard print"],
  one=["2|{c} Egoist-style bodycon mini dress with a ribbon", "2-3|{c} Rady-style tube mini dress with a frilled hem", "3|{c} halter mini dress with a deep v", "3-4|{c} one-shoulder cut-out bodycon dress",
       "4|{c} lace-up bodycon mini dress"],
  top=["1-2|{c} oversized knit sweater with off-shoulder neckline", "2|{c} Liz Lisa-style frilled blouse", "2-3|{c} cropped fur-trim cardigan", "3|{c} halter crop top with ties",
       "3-4|{c} tiny tube top with gold chain", "4|{c} wrap-around bandeau top"],
  bottom=["1-2|{c} denim shorts with frayed hem", "2|{c} tennis mini skirt", "2-3|{c} pleated mini skirt", "3|{c} Moussy-style ripped denim micro shorts", "3-4|{c} leather micro skirt",
          "4|{c} tiny bodycon micro skirt"],
  outer=["2|{c} oversized faux-fur coat", "2|{c} cropped denim jacket with fur lining", "2-3|{c} SLY-style cropped bomber jacket"],
  legs=["2|{c} loose socks", "2-3|black over-the-knee socks", "3|{c} leopard-print tights"],
  feet=["1-2|{c} platform sneakers", "2-3|{c} thigh-high platform boots", "3|{c} gladiator heels", "2-3|{c} chunky Ugg-style platform boots"],
  head=["2|a big hair bow", "2|a sparkly headband", "2-3|a cowboy hat"],
  neck=["a layered gold chain necklace", "a rhinestone choker"], ears=["large gold hoop earrings", "pearl studs with dangling stars"], wrists=["gold bangles", "a watch with a crystal band"],
  hands=["rhinestone nails with long acrylic tips", "stacked rings"], hair=["voluminous curled hair with a half-up bow", "a big gyaru updo with curled side strands"],
  face=["oversized sunglasses"], extra=["a quilted chain shoulder bag", "a mini handbag with charms"])

S("Idol Stage", "J-pop idol stage costumes: matching sequin dresses, ribbons, sparkle (AKB, Hello! Project, Johnny's female-group look)",
  ["white and pink", "pastel blue", "red and white", "gold metallic", "white and gold", "bright coral"],
  one=["2|{c} idol stage dress with a flared tulle skirt and sequin bodice", "2|{c} puff-sleeve sparkly mini dress with a big back bow", "2-3|{c} sequin bolero-and-skirt idol costume",
       "3|{c} short ruffled stage dress with a sheer yoke", "3|{c} sailor-collar-style stage dress with gold buttons"],
  top=["2|{c} satin bolero over a ribbon bandeau top", "2-3|{c} off-shoulder frilled stage crop top", "3|{c} sparkly corset-style stage top"],
  bottom=["2|{c} short layered tulle skirt with sparkle", "2|{c} pleated glitter mini skirt", "3|{c} sequin mini skirt with a ribbon waistband"],
  outer=["2|{c} cropped military-style stage jacket with gold buttons and epaulettes", "2|{c} satin stage cape with a ribbon clasp"],
  legs=["2|white knee-high socks with bows", "2-3|{c} sheer tights with sparkle", "3|{c} thigh-high socks with ribbons"],
  feet=["2|{c} glitter platform boots", "2|white lace-up knee-high boots", "2-3|{c} strappy sparkly heels"],
  head=["2|a satin headband bow", "2|a jewelled hair crown", "2|ribbon hair ties on both sides"],
  neck=["a bow-tie choker", "a sparkly pendant on a ribbon"], ears=["star earrings", "sparkly drops"], wrists=["satin ribbon wristbands", "sparkly cuffs"],
  hair=["a high ponytail with a big bow", "twin-tails with sparkle ribbons"], extra=["a light stick and a heart-shaped mic"])

S("Sanrio Cute", "Sanrio-style characters on everything: Hello Kitty, My Melody, Kuromi, Cinnamoroll, Pompompurin merch looks",
  ["pink and white", "baby pink", "baby blue", "black and purple", "butter yellow", "white and red"],
  one=["1-2|{c} Hello Kitty print pinafore dress", "2|{c} Cinnamoroll cloud-print sundress", "2|{c} My Melody hooded dress with bunny ears", "2|{c} Kuromi-style black and purple hooded mini dress with a skull bow",
       "2-3|{c} Pompompurin pinafore mini dress"],
  top=["1|{c} Hello Kitty face hoodie", "1-2|{c} My Melody oversized tee", "1-2|{c} Kuromi graphic crop sweatshirt", "2|{c} Cinnamoroll fluffy knit cardigan", "2|{c} Sanrio character cropped tank with a tie waist"],
  bottom=["1|{c} Sanrio pyjama-print trousers", "1-2|{c} pleated skirt with a Hello Kitty print", "2|{c} denim skirt with Sanrio patches", "2|{c} Kuromi-style black tulle mini skirt"],
  outer=["1-2|{c} Hello Kitty bomber jacket with embroidery", "2|{c} fluffy My Melody hooded jacket", "2|{c} Kuromi varsity jacket"],
  legs=["1-2|Hello Kitty knee-high socks", "2|{c} bunny-ear ankle socks", "2|{c} pastel striped over-the-knee socks"],
  feet=["1-2|{c} Sanrio sneakers", "2|{c} chunky platform sneakers with a character charm", "2|{c} Mary Jane platform shoes"],
  head=["1-2|a Hello Kitty bow clip", "2|a plush character hood", "2|a Cinnamoroll ear headband"],
  neck=["a Hello Kitty pendant necklace", "a heart-shaped locket"], ears=["character stud earrings"], wrists=["a Sanrio charm bracelet", "a jelly watch"], hair=["pink twin-tails with character clips"],
  extra=["a character shoulder bag", "a mini plush backpack covered in keychains"])

S("Coquette", "Coquette and ballet-core: bows, lace, ribbons, pearls, soft femininity",
  ["baby pink", "cream", "white", "pastel pink", "dusty rose", "soft blue", "ivory"],
  one=["1-2|{c} lace-trim milkmaid dress with a ribbon", "2|{c} ruffled babydoll sundress with bows on the straps", "2|{c} satin slip dress with lace trim", "2|{c} tulle ballet-wrap mini dress",
       "2-3|{c} corset-bodice mini dress with a bow", "3|{c} sheer-sleeved lace mini dress"],
  top=["1-2|{c} lace-collar blouse with a bow", "1-2|{c} wrap-front ballet cardigan", "2|{c} bow-front ribbed crop top", "2|{c} puff-sleeve lace blouse", "2-3|{c} satin corset top with ribbon laces"],
  bottom=["1-2|{c} tiered tulle midi skirt", "2|{c} satin mini skirt with a bow", "2|{c} lace-trim pleated skirt", "2-3|{c} ballet wrap skirt"],
  outer=["1-2|{c} cropped knit cardigan with pearl buttons", "2|{c} faux-fur bolero", "2|{c} cropped cardigan with ribbon ties"],
  legs=["1-2|white lace-trim socks", "2|{c} sheer tights with a bow pattern", "2|{c} ballet-style ribbon-tied stockings"],
  feet=["1-2|{c} ballet flats with ribbon ties", "2|{c} satin kitten heels with bows", "2|{c} Mary Jane shoes"],
  head=["1-2|a big satin hair bow", "2|a lace headband", "2|a pearl hair clip"],
  neck=["a pearl necklace with a bow pendant", "a velvet ribbon choker", "a heart locket"], ears=["pearl drop earrings", "bow stud earrings"], wrists=["a pearl bracelet", "ribbon wrist ties"],
  hair=["a half-up half-down with a ribbon", "a ballerina bun with ribbons", "long waves with bows"], extra=["a satin bow mini bag", "a quilted heart bag"])

S("Mori Girl", "Mori and soft-natural: layered linen, earthy tones, cosy forest-girl looks",
  ["cream", "sage green", "oatmeal", "dusty brown", "mustard yellow", "dusty rose", "off-white"],
  one=["1|{c} layered linen pinafore dress", "1|{c} loose cotton smock dress with embroidery", "1-2|{c} floral prairie dress with a lace collar", "2|{c} wrap sundress with ruffles"],
  top=["1|{c} oversized linen shirt", "1|{c} chunky hand-knit cardigan", "1|{c} embroidered peasant blouse", "1-2|{c} puff-sleeve cotton top"],
  bottom=["1|{c} wide linen trousers", "1|{c} long tiered cotton skirt", "1-2|{c} pleated midi skirt", "2|{c} corduroy mini skirt"],
  outer=["1|{c} oversized knit cardigan", "1|{c} quilted cotton jacket", "1|{c} long wool coat with wooden buttons"],
  legs=["1|{c} cable-knit knee socks", "1|{c} thick tights"], feet=["1|{c} leather lace-up ankle boots", "1|{c} Mary Jane flats", "1|{c} canvas sneakers"],
  head=["1|a straw hat with a ribbon", "1|a knit beret", "1|a floral headscarf"],
  neck=["a wooden bead necklace", "a dried-flower pendant"], ears=["small wooden earrings"], wrists=["a leather cord bracelet"], hair=["a loose braid with a ribbon", "a low bun with wisps"],
  extra=["a canvas tote bag", "a wicker basket bag"])

# ------------------------------------------------------------------------------------------ brand sets
S("Streetwear Brands", "Streetwear labels: Supreme, Stussy, Off-White, Palace, BAPE, Carhartt WIP, Fear of God Essentials",
  ["black", "white", "grey", "olive green", "red", "beige", "navy blue", "orange"],
  one=["1-2|{c} Carhartt WIP-style carpenter dungaree set", "2|{c} Fear of God Essentials-style matching hoodie and sweatpants set", "2-3|{c} oversized hoodie dress with a streetwear logo"],
  top=["1|oversized {c} Supreme box-logo hoodie", "1|{c} Stussy graphic tee", "1|{c} BAPE shark-hoodie", "1-2|{c} Off-White-style arrow-print tee", "1-2|{c} Palace tri-ferg tee", "2|{c} cropped boxy tee with a streetwear graphic",
       "2-3|{c} cropped zip hoodie with a tight fit"],
  bottom=["1|{c} baggy Carhartt WIP cargo pants", "1|{c} wide-leg skate jeans", "1-2|{c} Fear of God Essentials sweatpants", "2|{c} nylon track pants", "2-3|{c} low-rise baggy denim shorts", "3|{c} micro denim skirt with streetwear belt"],
  outer=["1|{c} Supreme x North Face nuptse puffer jacket", "1-2|{c} Stussy coach jacket", "1-2|{c} Palace shell jacket", "2|{c} Carhartt Detroit jacket", "2|{c} oversized varsity jacket"],
  legs=["1|{c} thick crew socks pulled up", "2|ripped fishnet tights under baggy jeans"],
  feet=["1|{c} Nike Dunk Low sneakers", "1|{c} Air Jordan 1 sneakers", "1|{c} New Balance 550 sneakers", "1-2|{c} Timberland boots", "2|{c} Adidas Samba sneakers"],
  head=["1|a Supreme box-logo cap", "1|a Stussy bucket hat", "1|a Carhartt beanie", "1-2|a Palace trucker cap", "1|a balaclava"],
  neck=["a chunky chain necklace", "a Cuban link chain"], ears=["hoop earrings", "diamond studs"], wrists=["a G-Shock watch", "a silver chain bracelet"], hands=["chunky silver rings"],
  waist=["a nylon utility belt"], face=["small oval sunglasses"], extra=["a crossbody sling bag", "a Carhartt backpack"])

S("Athleisure Brands", "Athleisure labels: Nike, Adidas, Lululemon, Gymshark, Alo Yoga, Puma, Fila, Champion",
  ["black", "white", "grey", "pastel pink", "navy blue", "sage green", "lilac", "neon green"],
  one=["1-2|{c} Lululemon-style zip-up unitard", "2|{c} Alo Yoga-style cut-out bodysuit", "2|{c} Gymshark-style seamless one-piece", "2|{c} Nike tennis dress", "2-3|{c} Adidas pleated sport dress with built-in shorts"],
  top=["1|{c} Champion reverse-weave hoodie", "1|{c} Nike Tech Fleece zip hoodie", "1|{c} Adidas oversized three-stripe tee", "1-2|{c} Lululemon oversized scuba hoodie", "2|{c} Nike cropped sports bra top with a swoosh",
       "2|{c} Gymshark seamless cropped tank", "2|{c} Alo Yoga cropped long-sleeve with a half zip", "3|{c} Alo Yoga bra top with strappy back", "3|{c} Puma tight sports crop top"],
  bottom=["1|{c} Nike Tech Fleece joggers", "1|{c} Adidas track pants with three stripes", "1-2|{c} Lululemon Align high-rise leggings", "2|{c} Gymshark seamless leggings", "2|{c} Alo Yoga high-waist airlift leggings",
          "2|{c} Fila tennis pleated skirt", "2-3|{c} Nike biker shorts", "3|{c} Lululemon micro tennis skort", "3-4|{c} Gymshark tiny booty shorts"],
  outer=["1|{c} Nike windbreaker", "1|{c} Adidas track jacket", "1-2|{c} Lululemon Define jacket", "2|{c} Alo Yoga cropped puffer", "2|{c} Champion cropped zip hoodie"],
  legs=["1|{c} Nike crew socks", "2|{c} Adidas knee-high tube socks"],
  feet=["1|{c} Nike Air Force 1 sneakers", "1|{c} Adidas Gazelle sneakers", "1|{c} New Balance 530 sneakers", "1-2|{c} Puma Speedcat sneakers", "1|{c} Nike Air Max sneakers"],
  head=["1|a Nike visor", "1|an Adidas cap", "2|a Lululemon headband", "2|a scrunchie"],
  wrists=["an Apple Watch with a sport band", "a sweatband"], ears=["white earbuds"], hair=["a high gym ponytail", "a sleek low bun"], face=["sport sunglasses"], waist=["a running belt"], extra=["a gym duffel bag", "a Lululemon belt bag", "a water bottle in a sling"])

S("Luxury Houses", "Luxury fashion houses: Chanel, Dior, Gucci, Versace, Prada, Saint Laurent, Balenciaga, Burberry, Miu Miu",
  ["black", "cream", "red", "navy blue", "gold metallic", "white", "camel", "emerald green"],
  one=["2|{c} Chanel-style tweed mini dress with gold buttons", "2|{c} Dior-style New Look dress with a nipped waist", "2|{c} Gucci-style floral silk midi dress", "2-3|{c} Versace-style baroque-print mini dress with gold hardware",
       "3|{c} Saint Laurent-style tuxedo mini dress", "3|{c} Prada-style nylon mini dress with a triangle logo", "3-4|{c} Versace-style safety-pin mini dress", "3|{c} Balenciaga-style sculpted bodycon dress"],
  top=["1-2|{c} Chanel-style bouclé tweed jacket-top", "1-2|{c} Burberry check trench-style shirt", "2|{c} Miu Miu cropped knit with a micro hem", "2|{c} Gucci-style silk blouse with a pussy bow", "2-3|{c} Dior-style bar-jacket crop top",
       "3|{c} Saint Laurent-style sheer blouse"],
  bottom=["1-2|{c} Chanel-style tweed pencil skirt", "2|{c} Burberry check pleated skirt", "2-3|{c} Miu Miu micro pleated mini skirt", "2|{c} Gucci-style tailored trousers", "3|{c} Versace-style leather micro skirt with gold medusa buckle"],
  outer=["1-2|{c} Burberry heritage trench coat", "1-2|{c} Chanel-style tweed jacket with chain hem", "2|{c} Saint Laurent leather biker jacket", "2|{c} Balenciaga oversized blazer", "2|{c} Max Mara-style camel wrap coat"],
  legs=["1-2|sheer black tights", "2|{c} Chanel-style two-tone stockings"],
  feet=["1-2|{c} Chanel two-tone slingback flats", "2|{c} Louis Vuitton-style monogram loafers", "2|{c} Saint Laurent platform heels", "2-3|{c} Jimmy Choo-style crystal pumps", "2|{c} Prada chunky leather boots"],
  head=["1-2|a Burberry check scarf", "2|a Gucci silk head scarf", "2|a Chanel-style pearl headband", "2|a Miu Miu beret"],
  neck=["a Chanel pearl necklace with a double-C pendant", "a Cartier-style love necklace", "a Van Cleef-style clover necklace", "a Versace gold chain"], ears=["Chanel-style pearl drop earrings", "Dior-style pearl logo earrings", "Gucci hoop earrings"],
  wrists=["a Cartier-style gold bangle", "a Rolex-style gold watch", "a Van Cleef-style clover bracelet"], hands=["a Cartier-style ring stack", "a large cocktail ring"], waist=["a Gucci double-G belt", "a Versace gold buckle belt"],
  face=["oversized Dior-style sunglasses", "Chanel-style cat-eye sunglasses"], extra=["a Chanel quilted flap bag", "a Hermes-style top-handle bag", "a Louis Vuitton Speedy-style bag", "a Prada nylon shoulder bag"])

S("High Street Trend", "High-street and online trend labels: Zara, H&M, Shein, Fashion Nova, Princess Polly, Brandy Melville, Urban Outfitters, Pretty Little Thing, Free People",
  ["black", "white", "beige", "baby pink", "sage green", "red", "chocolate brown", "denim blue", "lilac"],
  one=["1-2|{c} Zara linen-blend shirt dress", "2|{c} Free People boho floral mini dress", "2|{c} Princess Polly satin slip midi dress", "2|{c} Zara ruched midi dress with a slit", "2-3|{c} Pretty Little Thing bodycon mini dress",
       "3|{c} Fashion Nova ruched mini dress", "3|{c} Shein cut-out bodycon mini dress", "3-4|{c} Fashion Nova corset-front mini dress"],
  top=["1|{c} Brandy Melville cropped baby tee", "1|{c} Urban Outfitters oversized vintage band tee", "1-2|{c} Zara ribbed knit polo", "1-2|{c} H&M basic fitted tank", "2|{c} Princess Polly tie-front cropped shirt",
       "2|{c} Shein cropped puff-sleeve top", "2-3|{c} Free People off-shoulder lace top", "3|{c} Pretty Little Thing corset top", "3-4|{c} Fashion Nova tube top"],
  bottom=["1|{c} Zara wide-leg jeans", "1|{c} H&M straight high-rise jeans", "1-2|{c} Brandy Melville cargo parachute pants", "2|{c} Zara satin midi slip skirt", "2|{c} Princess Polly pleated tennis mini skirt", "2-3|{c} Shein denim mini skirt",
          "3|{c} Fashion Nova ruched mini skirt", "3-4|{c} Pretty Little Thing micro mini skirt"],
  outer=["1-2|{c} Zara oversized blazer", "1-2|{c} H&M long trench coat", "2|{c} Urban Outfitters cropped denim jacket", "2|{c} Zara faux-leather bomber jacket", "2|{c} Princess Polly faux-fur jacket"],
  legs=["1-2|{c} H&M sheer tights", "2|{c} Zara ribbed knee socks"],
  feet=["1|{c} Converse Chuck Taylor sneakers", "1-2|{c} Zara ankle boots", "1-2|{c} H&M ballet flats", "2|{c} Pretty Little Thing platform heels", "2|{c} Dr. Martens Mary Janes"],
  head=["1|a Zara claw clip", "1-2|a baseball cap", "2|a Brandy Melville scrunchie"],
  neck=["a layered gold chain necklace", "a dainty pendant necklace"], ears=["gold hoop earrings", "pearl studs"], wrists=["a stack of bangles", "a beaded bracelet"],
  face=["rectangular sunglasses"], extra=["a Zara shoulder bag", "a tote bag", "a mini crossbody bag"])

S("Alt Brands", "Alt and subculture labels: Dolls Kill, Killstar, Disturbia, Demonia, Hot Topic, Current Mood, Punk Rave",
  ["black", "black and red", "purple", "black and white", "neon pink", "blood red", "silver metallic"],
  one=["2|{c} Killstar-style gothic pinafore dress with occult prints", "2|{c} Dolls Kill-style plaid corset mini dress", "2-3|{c} Disturbia-style lace-up mini dress", "3|{c} Current Mood-style mesh-panel bodycon dress",
       "3-4|{c} Punk Rave-style studded corset mini dress"],
  top=["1-2|{c} Hot Topic band tee knotted at the waist", "1-2|{c} Killstar-style oversized hoodie with an occult print", "2|{c} Dolls Kill-style mesh long-sleeve top over a bralette-style crop", "2|{c} Disturbia-style graphic crop tee",
       "2-3|{c} Punk Rave-style lace-up corset top", "3|{c} Dolls Kill-style harness-strap crop top"],
  bottom=["1-2|{c} Dolls Kill-style baggy cargo pants with chains", "2|{c} Hot Topic plaid pleated mini skirt", "2|{c} Killstar-style tiered gothic maxi skirt", "2-3|{c} Disturbia-style vinyl mini skirt", "3|{c} Punk Rave-style studded micro skirt"],
  outer=["1-2|{c} Dolls Kill-style oversized studded denim jacket", "2|{c} Killstar-style long velvet coat", "2|{c} Hot Topic faux-leather biker jacket"],
  legs=["2|{c} ripped fishnet tights", "2|{c} striped over-the-knee socks", "2-3|{c} lace-up knee-high stockings"],
  feet=["1-2|{c} Demonia platform boots", "2|{c} Dr. Martens 1460 boots", "2|{c} Demonia creeper platform shoes", "2-3|{c} Demonia thigh-high platform boots"],
  head=["2|a spiked headband", "2|a studded black headband"],
  neck=["a spiked choker", "a Killstar occult pendant", "a layered chain necklace with a padlock"], ears=["safety-pin earrings", "ear cuffs"], wrists=["studded wristbands", "a spiked bracelet"],
  hands=["skull rings", "stacked black rings"], waist=["a double-buckle belt with chains"], face=["a lace choker"], extra=["a coffin-shaped bag", "a studded backpack"])

S("Heritage Brands", "Classic heritage labels: Levi's, Wrangler, Carhartt, Ralph Lauren, Tommy Hilfiger, Lacoste, Fred Perry, Dickies",
  ["navy blue", "white", "red", "denim blue", "khaki", "forest green", "cream", "grey"],
  one=["1-2|{c} Ralph Lauren polo dress", "1-2|{c} Lacoste pique polo dress", "1-2|{c} Carhartt overall dungarees", "2|{c} Tommy Hilfiger striped sweater dress"],
  top=["1|{c} Ralph Lauren cable-knit sweater", "1|{c} Ralph Lauren polo with a pony logo", "1|{c} Lacoste pique polo shirt", "1|{c} Fred Perry twin-tipped polo", "1|{c} Tommy Hilfiger striped crewneck",
       "1|{c} Levi's graphic tee", "1-2|{c} Dickies work shirt", "2|{c} cropped Carhartt tee"],
  bottom=["1|{c} Levi's 501 jeans", "1|{c} Wrangler bootcut jeans", "1|{c} Dickies 874 work pants", "1|{c} Carhartt double-knee pants", "1-2|{c} Ralph Lauren chinos", "1-2|{c} Tommy Hilfiger pleated tennis skirt",
          "2|{c} Levi's denim mini skirt", "2-3|{c} Levi's 501 cut-off denim shorts"],
  outer=["1|{c} Levi's trucker denim jacket", "1|{c} Carhartt chore coat", "1|{c} Ralph Lauren quilted jacket", "1-2|{c} Tommy Hilfiger puffer jacket", "1-2|{c} Fred Perry Harrington jacket", "2|{c} Lacoste track jacket"],
  legs=["1|{c} Ralph Lauren knee socks", "1-2|{c} crew socks with a stripe"],
  feet=["1|{c} Timberland boots", "1|{c} Converse All Star sneakers", "1|{c} Vans Old Skool sneakers", "1|{c} Lacoste leather sneakers", "1|{c} Dr. Martens boots"],
  head=["1|a Ralph Lauren baseball cap", "1|a Carhartt beanie", "1-2|a Lacoste bucket hat"],
  neck=["a thin gold chain", "a neck scarf"], wrists=["a leather watch", "a braided leather bracelet"], waist=["a Levi's leather belt", "a web belt"], face=["aviator sunglasses"], extra=["a canvas tote", "a Carhartt backpack"])

S("Y2K Brands", "Early-2000s label looks: Juicy Couture, Baby Phat, Von Dutch, Ed Hardy, Bebe, Sean John, Paris Hilton era",
  ["hot pink", "baby pink", "chocolate brown", "white", "baby blue", "black", "lime green", "red"],
  one=["2|{c} Juicy Couture velour tracksuit set with a zip hoodie", "2|{c} Baby Phat-style rhinestone logo mini dress", "2-3|{c} Bebe-style rhinestone halter mini dress", "3|{c} Von Dutch-style bodycon mini dress", "3-4|{c} Paris Hilton-era sparkly mini dress"],
  top=["1-2|{c} Juicy Couture velour zip hoodie", "2|{c} Von Dutch graphic baby tee", "2|{c} Ed Hardy rhinestone graphic tee", "2-3|{c} Baby Phat cropped baby tee", "2-3|{c} Bebe halter top with rhinestones", "3|{c} Juicy Couture tiny velour crop top"],
  bottom=["1-2|{c} Juicy Couture velour pants with a word on the bum", "2|{c} low-rise flared jeans", "2|{c} Baby Phat low-rise jeans with rhinestones", "2-3|{c} cargo mini skirt with a chain belt", "3|{c} denim micro mini skirt", "3-4|{c} low-rise micro shorts"],
  outer=["1-2|{c} Juicy Couture velour jacket", "2|{c} cropped faux-fur jacket", "2|{c} Von Dutch trucker jacket"],
  legs=["2|white tube socks", "2|{c} sheer tights with rhinestones"],
  feet=["1-2|{c} Ugg boots", "2|{c} Juicy platform flip-flops", "2|{c} Heelys", "2-3|{c} rhinestone kitten heels"],
  head=["1-2|a Von Dutch trucker cap", "2|a velour headband", "2|butterfly clips in the hair"],
  neck=["a Juicy Couture charm necklace", "a rhinestone choker", "a name-plate necklace"], ears=["big hoop earrings", "rhinestone studs"], wrists=["a Juicy charm bracelet", "a jelly bracelet stack"], waist=["a studded belt", "a chain belt"],
  hair=["crimped hair with butterfly clips", "two small buns with face-framing strands"], face=["small tinted sunglasses"], extra=["a Juicy Couture velour handbag", "a tiny shoulder bag", "a Motorola Razr phone"])

STYLE_ADD = X
