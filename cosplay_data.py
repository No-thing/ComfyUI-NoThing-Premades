"""Cosplay: 27 well-known characters, each a complete fixed look (hair + outfit + props) at all five levels.
All characters are adults. Entries are 'level|text'; the Roulette Bar's Cosplay theme turns hair, makeup and underwear off because the look is the character."""

CHARACTERS = {
 "2B from NieR Automata": ("short white bob with a black blindfold", [
    "a long black coat-dress with a high collar, black leather gloves and black knee-high boots",
    "a black gothic mini dress with puffed sleeves and a white ribbon at the neck, black gloves and knee-high boots",
    "a black gothic mini dress with a keyhole front and a high leg opening, black thigh-high boots",
    "a black gothic micro dress with a deep keyhole and open sides, long black gloves and thigh-high boots",
    "a tiny black gothic micro dress held together by thin straps, skin showing at the chest and hips, thigh-high boots"]),
 "Jessica Rabbit": ("long red side-swept waves covering one eye", [
    "a long glossy red satin evening gown with long purple opera gloves",
    "a long glossy red satin gown with a high neckline, long purple opera gloves and a sparkling hem",
    "a glossy red satin gown with a deep neckline and a high leg opening, long purple opera gloves",
    "a skintight glossy red sequin micro gown with a plunging neckline and a thigh-high opening, purple opera gloves",
    "a tiny glossy red sequin micro dress held up by thin straps with deep cleavage showing, purple opera gloves"]),
 "Catwoman": ("sleek black hair under a black cat-ear cowl with goggles", [
    "a black leather jacket and black leather trousers with black boots and a whip at the hip",
    "a fitted black leather catsuit zipped to the collar, black boots and goggles on the head, a whip at the hip",
    "a skintight glossy black leather catsuit zipped halfway down, black boots and a whip at the hip",
    "a glossy black leather micro catsuit with a low zip and open hips, black thigh-high boots and a whip",
    "a glossy black leather strap catsuit cut away at the chest and hips, black thigh-high boots and a whip"]),
 "Harley Quinn": ("blonde pigtails dyed pink and blue at the tips", [
    "a red and black jester jacket over a white shirt, red and black trousers, a baseball bat over the shoulder",
    "a red and black varsity jacket over a white tee, tiny red and black shorts and a baseball bat",
    "a red and black jacket over a cropped white tee, red and blue glitter hot pants, fishnet tights and a baseball bat",
    "an open red and black jacket over a red and blue micro top, glitter micro shorts, torn fishnet tights and a baseball bat",
    "a red and blue glitter micro bikini with an open jacket slipping off the shoulders, fishnet tights and a baseball bat"]),
 "Poison Ivy": ("long wavy red hair with green leaves and flowers woven in", [
    "a long green leaf-print dress with a vine belt and ivy wrapped around the arms",
    "a green leaf-print mini dress with a flower-petal skirt and ivy vines around the arms",
    "a green leaf-bodice mini dress with a plunging neckline and a high leg opening, ivy vines winding around the legs",
    "a green leaf micro bodysuit cut away at the sides, ivy vines wound around the arms and legs, knee-high green boots",
    "a micro bikini made of green leaves held together by ivy vines, ivy wound around the arms and legs"]),
 "Lara Croft": ("long brown braid over one shoulder", [
    "a fitted teal tank top, tan cargo trousers, black boots, twin holsters on the hips and a backpack",
    "a teal tank top, tan cargo shorts, hiking boots, twin holsters and a backpack",
    "a tight teal tank top, tiny tan shorts, thigh-strap holsters, fingerless gloves and hiking boots",
    "a teal micro tank top tied at the ribs, tan micro shorts with low-slung holster belts, fingerless gloves and boots",
    "a teal micro tube top and tan micro shorts barely covering, holster straps across the hips and thighs, hiking boots"]),
 "Tifa Lockhart from Final Fantasy VII": ("very long black hair tied with a ribbon near the ends", [
    "a white tank top, a long black skirt with suspenders, red fingerless gloves with metal plates and red boots",
    "a white tank top, a short black pleated skirt with suspenders, black arm guards and red boots",
    "a tight white cropped tank top, a black micro pleated skirt with suspenders, arm guards and red boots",
    "a white micro tank top riding up the ribs, a black micro skirt with suspenders, arm guards and red boots",
    "a skintight white micro tube top, a barely-covering black micro skirt with suspenders hanging loose, arm guards, red boots"]),
 "Bayonetta": ("short black bob with a long curl on the forehead, thin round glasses and a beauty mark", [
    "a sleek black catsuit with gold brooches, black pistol heels and thin round glasses",
    "a black bodycon dress with gold brooches, black pistol heels and thin round glasses",
    "a skintight black bodysuit with gold brooches and a deep neckline, thigh-high pistol-heel boots, thin round glasses",
    "a black bodysuit of woven hair cut away at the chest and hips with gold brooches, thigh-high heels, round glasses",
    "ribbons of black hair wrapped across her body in thin strips, gold brooches, thigh-high heels, round glasses"]),
 "Chun-Li from Street Fighter": ("dark brown hair in two buns with white ribbons", [
    "a blue silk cheongsam-style dress with gold embroidery and white puffy sleeves, spiked gold bracelets, brown tights and white boots",
    "a blue silk mini qipao with gold trim, spiked bracelets, brown tights and white lace-up boots",
    "a blue silk qipao mini dress with a high leg opening, spiked bracelets, tan tights and white boots",
    "a blue silk qipao micro dress with open sides, spiked bracelets, thigh-high tan stockings and white boots",
    "a tiny blue qipao top with gold trim and a barely covering micro skirt, spiked bracelets, white boots"]),
 "Mai Shiranui from King of Fighters": ("high auburn ponytail tied with a red ribbon", [
    "a red and white shinobi robe tied with a red sash, a red folding fan",
    "a short red and white kimono-style dress with a red sash, a folding fan and tabi socks",
    "a red and white shinobi outfit with a deep neckline and a low front panel, a folding fan",
    "a tiny red and white shinobi top with a deep open front, a micro loincloth flap held by a sash, thigh-high stockings, a fan",
    "a red and white micro halter wrap with an open front, a micro loincloth flap held by a sash, a folding fan"]),
 "Morrigan Aensland from Darkstalkers": ("long wavy green hair with a bat-wing headpiece", [
    "a long black leopard-print dress with bat-wing shoulders and purple accents, purple stockings",
    "a black leopard-print mini dress with purple bat-wing details, purple tights and black boots",
    "a black leopard-print bodysuit with a heart-shaped opening, purple pantyhose, small bat wings on the head and back",
    "a black leopard-print micro bodysuit with a heart cut-out, purple stockings and small bat wings",
    "a black leopard-print micro bikini with a heart cut-out, purple stockings, bat wings on the head and back"]),
 "Yor Forger from Spy x Family": ("long black hair in a half-up style with a gold hairband", [
    "a red sweater, a long black skirt and a gold hairband",
    "a red off-shoulder sweater dress, black tights and a gold hairband",
    "a short black assassin dress with a deep neckline and a high leg opening, black thigh-high boots, gold spike blades",
    "a black micro assassin dress with open sides and a plunging neckline, thigh-high boots and gold spike blades",
    "a tiny black micro dress held by thin straps, open at the sides, thigh-high boots and gold spike blades"]),
 "Makima from Chainsaw Man": ("straight copper-red hair in a low braid, ringed yellow eyes", [
    "a white blouse, a black tie, black suit trousers and black dress shoes",
    "a white blouse and black tie, a black pencil skirt, black tights and black dress shoes",
    "a white blouse unbuttoned low with a loosened black tie, a short black pencil skirt, black stockings and heels",
    "an open white blouse tied under the chest with a loose black tie, a black micro pencil skirt, thigh-high stockings",
    "a white blouse hanging open with a loose black tie, a tiny black micro pencil skirt, thigh-high stockings"]),
 "Misato Katsuragi from Evangelion": ("long dark purple-brown hair with a gold cross pendant", [
    "a red jacket over a black dress shirt and a black skirt, a gold cross pendant",
    "a red jacket over a black mini dress, black tights and boots, a gold cross pendant",
    "an open red jacket over a tight black mini dress with a deep neckline, black stockings and boots, a cross pendant",
    "an open red jacket over a black micro bodycon dress, thigh-high stockings, a cross pendant",
    "an open red jacket over a black micro tube top and a tiny micro skirt, a cross pendant"]),
 "Faye Valentine from Cowboy Bebop": ("short purple bob with a yellow hairband", [
    "a yellow open vest over a white blouse, high-waisted yellow shorts with suspenders and brown boots",
    "a yellow vest top, short yellow shorts with suspenders, a red choker and knee-high boots",
    "a short yellow vest top with a deep neckline, tiny yellow shorts with suspenders, a red choker and knee-high boots",
    "a yellow micro vest top, micro yellow shorts with suspenders, a red choker and thigh-high boots",
    "a yellow micro bikini top and micro shorts held by suspenders, a red choker and boots"]),
 "Yennefer from The Witcher": ("long curly black hair, violet eyes", [
    "a black high-collared velvet dress with white trim and a star-shaped obsidian pendant",
    "a black velvet gown with white trim, an obsidian star pendant and long black gloves",
    "a black velvet dress with a deep neckline and a high leg opening, an obsidian star pendant and black gloves",
    "a black velvet micro dress with a plunging neckline and white trim, an obsidian pendant, long gloves and thigh-high boots",
    "a micro black velvet top and tiny skirt with white trim, an obsidian star pendant, long gloves and thigh-high boots"]),
 "Wonder Woman": ("long dark wavy hair with a golden tiara", [
    "a red and blue armoured tunic with a gold eagle on the chest, a golden lasso, silver bracers and red boots",
    "a red and gold armoured top with a blue star-spangled skirt, silver bracers, a golden lasso and red boots",
    "a red armoured top with a gold eagle, a blue star-spangled micro skirt, silver bracers, a golden lasso and knee-high boots",
    "a red and gold armoured micro top, blue star-spangled micro shorts, silver bracers, a golden lasso and red knee-high boots",
    "a gold eagle micro bikini top and star-spangled micro bottoms, silver bracers, a golden lasso and red knee-high boots"]),
 "Widowmaker from Overwatch": ("long dark purple hair in a high ponytail, pale blue-toned skin", [
    "a purple and black fitted combat suit with a high collar, purple gloves, boots and a sleek sniper rifle",
    "a purple fitted combat jumpsuit with a lower neckline and black belts, a sniper rifle",
    "a purple skintight combat bodysuit with a plunging neckline, thigh-high boots and a sniper rifle",
    "a purple skintight micro bodysuit with a plunging V down to the navel and open sides, thigh-high boots and a sniper rifle",
    "a purple micro strap bodysuit with a deep V and open sides, thigh-high boots and a sniper rifle"]),
 "Ahri from League of Legends": ("long silver-white hair with fox ears and nine fluffy white fox tails", [
    "a long white and gold silk dress with a high collar and long sleeves, a glowing blue orb",
    "a short white and gold silk dress with pink ribbons, a glowing blue orb",
    "a white and gold silk mini dress with a deep neckline and a high leg opening, long white sleeves, a glowing blue orb",
    "a white and gold silk micro dress with a plunging neckline and open sides, long white sleeves, a glowing blue orb",
    "a white silk micro wrap with gold trim barely held together, long white sleeves, a glowing blue orb"]),
 "Maleficent": ("a black horned headdress, pale skin, sharp cheekbones and red lips", [
    "a long black hooded gown with a high collar and long sleeves, black horns and a staff with a green glow",
    "a long black gown with a high collar and long sleeves, black horns and a staff with a green glow",
    "a black gown with a deep neckline and a high leg opening, long black sleeves, black horns and a glowing green staff",
    "a black micro dress with a plunging neckline and open sides, a high horned collar, thigh-high boots and a glowing green staff",
    "a black micro bikini set with a high horned collar and a sheer black cape, black horns and a glowing green staff"]),
 "Megara from Hercules": ("long brown hair in a high ponytail", [
    "a long flowing lilac Greek tunic with a gold belt",
    "a short lilac Greek tunic with a gold belt, gold bracelets and sandals",
    "a short lilac Greek tunic with a deep neckline and a high leg opening, a gold belt, gold bracelets and sandals",
    "a lilac micro Greek tunic with a plunging neckline and open sides, a gold belt and laced gladiator sandals",
    "a tiny lilac wrapped Greek micro tunic held by gold straps, a gold belt and laced gladiator sandals"]),
 "Cruella de Vil": ("black and white split-dyed hair", [
    "a long black and white fur coat over a black dress, long black gloves",
    "a black and white fur-trimmed mini dress with a red lining, long red gloves and black heels",
    "an open black and white fur coat over a black dress with a deep neckline, red gloves and heels",
    "an open fur coat over a black micro dress with a plunging neckline, red gloves and thigh-high boots",
    "a black and white fur coat worn open over a black micro bikini set, red gloves and thigh-high boots"]),
 "Samus Aran from Metroid": ("a long blonde ponytail", [
    "an orange and red armoured power suit with a green visor and an arm cannon",
    "an orange and red armoured jacket and fitted trousers with an arm cannon",
    "a skintight blue Zero Suit with a light armour belt, a pistol strapped to the thigh",
    "a skintight blue Zero Suit with a low zip and open hips, a pistol and high-heeled boots",
    "a blue Zero Suit torn open at the chest and hips, a pistol and high heels"]),
 "Revy from Black Lagoon": ("a dark brown ponytail, a tribal tattoo on her arm", [
    "a loose black tank top, long jeans with a gun belt, a tribal tattoo on the arm and twin pistols in shoulder holsters",
    "a black tank top, denim shorts with a gun belt, a tribal arm tattoo and two pistols in shoulder holsters",
    "a tight black knotted tank top, tiny denim cut-off shorts, shoulder holsters and a tribal arm tattoo",
    "a black micro bikini top with shoulder holsters, tiny denim micro shorts and a tribal arm tattoo",
    "a black micro tube top, barely covering micro denim shorts, shoulder holsters and a tribal tattoo on the arm"]),
 "Jinx from Arcane": ("very long blue twin braids", [
    "a pink and black asymmetric long-sleeve top, loose black shorts over striped tights, crossed bullet belts, boots and a shark-mouth rocket launcher",
    "a pink and black striped top with a bullet belt, tiny black shorts, one striped stocking, boots and a shark-mouth rocket launcher",
    "a short pink and black crop top, black micro shorts with crossed bullet belts, one striped thigh-high stocking, boots and a rocket launcher",
    "a pink and black micro top held by bullet belts, black micro shorts, one striped thigh-high stocking and boots",
    "crossed bullet belts across the chest as a micro top, black micro shorts barely covering, one striped thigh-high stocking and boots"]),
 "D.Va from Overwatch": ("long brown hair with a headset and pink whisker marks on the cheeks", [
    "a blue and white pilot jumpsuit with pink bunny emblems and a high white collar, white gloves and boots",
    "a blue and white form-fitting pilot suit with pink accents and a bunny logo, white gloves, boots and a headset",
    "a skintight blue pilot bodysuit with a deep neckline and open sides, white gloves, thigh-high boots and a headset",
    "a skintight blue micro pilot bodysuit with a plunging neckline and cut-outs, white gloves and thigh-high boots",
    "a blue and white micro pilot bikini set with bunny emblems, white gloves, thigh-high boots and a headset"]),
 "Pomni from The Amazing Digital Circus": ("short ginger hair under a red and blue split jester hat with two bell-tipped horns", [
    "a red and blue split-colour jester jumpsuit with a big white ruffled collar and bell cuffs, striped boots",
    "a red and blue split-colour jester mini dress with a big white ruffled collar and bell cuffs, striped tights and boots",
    "a red and blue split-colour jester bodysuit with a deep neckline and a big ruffled collar, bell cuffs, striped thigh-high stockings",
    "a red and blue jester micro bodysuit with open sides and a white ruffled collar, bell cuffs, striped thigh-high stockings",
    "a tiny red and blue jester micro bikini with a white ruffled collar, bell cuffs and striped thigh-highs"]),
}

ENTRIES = [f"{lv}|a {name} cosplay with {hair}, in {outfit}" for name, (hair, looks) in CHARACTERS.items() for lv, outfit in enumerate(looks, 1)]

STYLE = dict(desc="well-known game, cartoon and show characters, each a complete fixed look",
             palette=["black"], one=ENTRIES, top=[], bottom=[], outer=[], legs=[], feet=[], head=[], acc={})
