# ComfyUI-NoThing-Premades

> **Security update (2026-11-12):** the Workflow Check node is gone for good. An earlier build could install a node pack from a GitHub link written in a workflow note, and it also downloaded model files. Both features are removed with the whole node: nothing in this pack runs `git`, `pip` or downloads anything now. If you used an older version, update, and check `custom_nodes` for packs you do not recognise. Thanks to lonecatone23 for reporting it.

**No_Thing Roulette Bar and Prompt Bars.** A completely free roulette randomiser for ComfyUI: pick a Style, how much, what stays in frame, the body shape and the face shape, press **Roll all**, and the prompt writes itself (roughly millions of combinations). Face, hair, body, makeup, outfit and underwear in one wide node, with Simple and Advanced pages, a fixed seed to repeat any roll, and tips in the node.

Free to use, not free to copy: see [LICENSE](LICENSE). Works with the [LightCraft Edit Page](https://github.com/No-thing/ComfyUI-LightCraft). Install: copy this folder into `ComfyUI/custom_nodes/`, restart ComfyUI, hard-refresh the browser.

---

**No_Thing Prompt Bar** - one node that replaces the string literals, bypass switches and text-join
nodes. A bar of square buttons; each button is a piece of prompt text. Orange glow = on, purple
outline = off.

Two nodes (same engine, different starting buttons), both under the "No_Thing" category:
- **No_Thing Prompt Bar (Look)** - Body, Face, Lighting, Lens, Effects (your premades)
- **No_Thing Prompt Bar (Detail)** - Skin Detail, Hair Detail, Realism

## Install
Copy this folder into `ComfyUI/custom_nodes/`, restart ComfyUI, hard-refresh the browser.

## Use
- Click a button to switch it on/off. Rows marked "one at a time" (Body, Face, Lighting) switch the others off.
- Click a row's name to switch that whole row off. "All off" clears everything.
- Hover a button: the strip at the bottom shows its prompt text. With nothing hovered it lists what is on.
- Shift+click a button, or press **Edit**, to change it. In Edit mode:
  - click a button: rename it, rewrite its prompt, move it left/right, delete it
  - **+** at the end of a row adds a button; **+ Add row** adds a new row
  - click a row name: rename the row, make it "one at a time", move it up/down, delete it
- **Join** decides how texts are glued: New line, Space or Comma.
- Drag the node wider and the buttons repack; the height follows by itself.

## Wiring
- `prefix`: your base prompt comes first (optional). `suffix`: text added at the end (optional).
- `prompt` (STRING): the finished prompt. `active` (STRING): names of the buttons on, e.g.
  `Body: Bimbo, Lighting: Golden Hour` (handy for file names or metadata).
- Everything is saved inside the workflow. Nothing else to configure.

## No_Thing Outfit Roulette (clothes)
One node that rolls a random outfit of clothes. Underwear and lingerie have their own node now (below). You choose only what you care about; every row you leave empty is
chosen at random.
- **ON / OFF** switch (top left of the node): off = the node adds no outfit and just passes `prefix` / `suffix` through.
- **Skimpy**: Covered, Cute, Revealing, Skimpy, Micro (pick several = it picks one of them each run)
- **Style**: Casual, Kigurumi, Dresses, Y2K, Goth, Latex, Grunge, Punk, Barbie, Preppy Uniform.
  Pick several and the pieces are mixed across them (Goth + Latex = a goth/latex blend).
  "One style per outfit" (Options) keeps the whole outfit in one of the styles you picked.
  "No shoes", "No bottoms" and "No tops" (Options) keep a cropped composition clean: whatever is out of frame is left out of the prompt, so the model is not pushed to pull back and show it. Entries that mix halves are cut to the visible half ("lace bra with matching thong" becomes "matching thong" under No tops).
- **Accessories**: None, Few (1-2), Some (3-4), Loaded (5-7): necklaces, rings, bracelets, earrings, belts,
  hair pieces and so on, taken from the chosen styles.
- **Colour**: optional; empty = the style's own palette.
- Nothing picked at all = a random level, 1-3 random styles, random accessories, random colours.
- Wiring: `prefix` / `suffix` are optional text; `prompt` = prefix + outfit + suffix, `outfit` = just the
  outfit, `active` = what was rolled (level, styles, accessory count, colour). The `seed` decides the roll:
  "randomize" gives a new outfit every run, "fixed" repeats the same one.
- If a style has nothing at the level you asked for (for example Latex at Covered) it uses the nearest level
  that has something, and `active` says so.
- **Preppy Uniform only exists at Covered and Cute.** It is never combined with the skimpier levels: pick it
  with Skimpy and you get the Cute version.
- The Outfit Roulette is for clothes you can wear outside the bedroom: no lingerie, underwear, harnesses or BDSM gear (those are in the Underwear Roulette). Everything is clothing description only (what is worn, never what is shown). The dataset is in
  `outfit_data.py`; lines look like `"3-4|{c} lace plunge bralette"` (levels, then text; `{c}` = main colour).
  You can also add lines without touching that file by creating `outfit_custom.json`, e.g.
  `{"Goth": {"top": ["3|{c} lace corset top"], "acc": {"neck": ["a bat-wing choker"]}}}`.

**More styles (26 in total).** Japanese: Harajuku Kawaii (6%DOKIDOKI, Swimmer), Doll Style (Angelic Pretty, Baby the Stars Shine Bright, Metamorphose, Innocent World), Jirai Kei (Liz Lisa, Ank Rouge, Rojita, Secret Honey), Gyaru (Egoist, Rady, Moussy, SLY), Idol Stage, Sanrio Cute, Coquette, Mori Girl. Brand sets: Streetwear Brands, Athleisure Brands, Luxury Houses, High Street Trend, Alt Brands, Heritage Brands, Y2K Brands. Brand names are only prompt words that steer the look. They live in `outfit_data_extra.py`. Most of these top out around Revealing / Skimpy; when a style has nothing at the level you picked, the nearest level is used and the summary says so.

## No_Thing Underwear Roulette (lingerie)
Its own node, separate from the clothes. Roughly 290 sets in 12 families plus 60-odd add-ons. Pick only what you care about; every empty row is rolled.
Options: "No bottoms" (torso crop, only bras and tops are mentioned) and "No tops" (lower-body crop, only panties, garters and legwear). Bars saved in an older workflow gain the buttons automatically; reload the page.

- **Coverage**: Soft, Classic, Seductive, Bold, Micro (pick several = one of them each run)
- **Style**: Designer (famous houses: Agent Provocateur, La Perla, Honey Birdette, Bordelle, Savage X Fenty, Fleur du Mal, Maison Close, Chantal Thomass, Aubade, Coco de Mer, Intimissimi, For Love & Lemons, Bluebella, Thistle & Spire and more), Lace Classics, Corsets, Bodysuits & Teddies, Babydolls & Slips, Harness & Strappy, Sheer & Mesh, Latex & PVC, Kawaii & Sweet, Branded Lounge (Calvin Klein / Playboy / Victoria's Secret styles and sporty sets), Pin-up Vintage, Bridal & Romantic. Nothing picked = one or two families at random.
- **Add-ons**: which extras may be added - Legwear, Garter belt, Gloves & neck, Headwear, Layer (robes). **Add-on amount**: None, Few (1), Some (2), Loaded (3-4).
- **Colour**: optional; empty = the family's own palette.
- Same wiring as the Outfit Roulette: `prefix` / `suffix`, `prompt`, `underwear` (just the set) and `active`; ON / OFF switch, Random off, edit a button's text. Use it alone, or with the Outfit Roulette when you want clothes and underwear both rolled.
- Add lines in `underwear_data.py` (`"3-4|{c} lace plunge bralette"`) or in `underwear_custom.json`: `{"Corsets": ["3|{c} my corset"], "extras": {"Legwear": ["2|{c} my stockings"]}}`.
- Clothing descriptions only (what is worn, never what is shown).

## No_Thing Makeup Roulette (looks)
Rolls a makeup look. Rows: **Intensity** (Natural, Soft, Glam, Bold, Extreme), **Look** (8 families: Japanese & East Asian, American & Glam, Doll & Anime, Goth & Dark, Punk & Grunge, Y2K & Retro-Futurism, Modest & Understated, Overdone & Hyper-Stylized; 66 looks), **Add-ons** (Lips, Cheeks, Eyes, Details), **Add-on amount**, **Colour**. Nothing picked in a row = anything goes. A picked colour always shows up, even in looks with their own colours. Your own lines go in `makeup_custom.json`: `{"Goth & Dark": ["4|my look"], "extras": {"Lips": ["3|a plum lip"]}}` (levels 1-5 like the other roulettes). Outputs: `prompt`, `makeup`, `active`.

## No_Thing Head Roulette (face, eyes, lips, hair)
Same idea as the Outfit Roulette: pick only what you care about, every empty row is rolled. Rows: **Face** shape, **Eye shape** (almond canted "predatory", cat eye / fox, siren, hooded, doe, downturned, monolid, wide-set, deep-set, narrow slanted), **Eye size**, **Eye colour**,
**Lip shape**, **Lip size**, **Hair length** (Pixie to Hip), **Hairstyle** groups (Straight, Waves & curls, Bob & short, Bangs, Ponytails & twin tails, Buns & braids, Half-up & retro, Edgy cuts) and **Hair colour**.
Hairstyles only appear at lengths they make sense at (a pixie never gets a waist-length braid). Output is a phrase like `with a heart-shaped face ..., very large almond-shaped, upturned canted eyes ..., full pouty lips ..., and jet black waist-length hair in a high, swishing ponytail.`
Add hairstyles in `head_custom.json`: `{"hair": ["3-6|cute|Buns & braids|{c} {len} hair in a side braid"]}` (lengths 1-6, tags, group, text; `{c}` = hair colour, `{len}` = length word).

## No_Thing Body Roulette (figure)
Rows: **Body type** (Bimbo, Slim stack, Bottom heavy, Skinny, Athletic), **Bust**, **Waist**, **Hips & butt**, **Legs**, **Height**.
A row you leave empty is chosen to fit the rolled body type (a Bimbo gets a tiny waist and a very large bust, an Athletic body gets toned legs). A row you pick always wins.
Add types in `body_custom.json`: `{"My type": {"text": "a long-limbed figure", "tags": "soft", "pools": {"bust": ["Small"], "waist": ["Slim"]}}}`.

## No_Thing Lighting (click and choose)
Not a roulette: you click what you want, rows you leave empty are left out. **Setup** (single spotlight, two-point, rim light, backlit glow, neon glow, soft glamour),
**Palette** (ready colour pairs like Pink + Cyan, Magenta + Blue, Purple + Pink, Red + Purple), or pick **Key colour** and **Rim colour** yourself (pink, hot magenta, purple, violet, cyan, electric blue, red, crimson, amber, peach, teal, white),
**Mood** (soft & dreamy, hard & dramatic, low-key moody) and **Extras** (lens flare, bokeh, haze, glossy highlights). A palette overrides the single colours. Colour only, with no setup = "lit by pink and cyan light".

All three have the ON/OFF switch (off = `prefix` / `suffix` pass through). Everything describes an adult woman's features and lighting only.

### Editing what the buttons say (Head, Body and Lighting)
Shift+click a button, or press **Edit text** and click, to rewrite the text a button adds to the prompt. A small orange dot marks buttons you changed; **Reset to default** in the editor puts the original back.
- Head / Body: the text is used as written. For eyes and lips, the size word is put in front of your text (so write "almond-shaped eyes with ..."). Hair colour takes a comma-separated list of colour words to pick from.
- Lighting: Setup texts may use `{key}` and `{rim}` where the light colours should go. Colour buttons hold the colour word.
- Hairstyle and Palette buttons are not editable (they steer the roll instead of adding text).

### Sizing
These nodes are as tall as their buttons need. Dragging the node taller or shorter snaps back, and nothing is ever drawn outside the frame. Drag the node wider and the buttons repack.

### Random on / off (Outfit, Head and Body)
The small **Random** button next to ON/OFF glows orange when the dice are on (the default). Switch it off and the node stops rolling: the prompt is built from exactly the buttons you picked, in the wording on the buttons (use **Edit** or Shift+click to change a button's text; edited buttons get an orange dot).
- Outfit: picked Style, Skimpy, Colour and Accessories texts are joined, e.g. `wearing dark gothic clothes, low-cut with thigh slits and sheer panels, mainly black, with a few accessories.` In random mode the Outfit buttons only steer the roll, so their edited text is used when Random is off.
- Head / Body: the first button you picked in each row is used, rows with nothing picked are left out (a hairstyle group uses its first style).
- Lighting never rolls, so it has no Random button.
- Old saved nodes keep the buttons they were saved with (for example the removed Vibe row or the longer Body type list): add a fresh node to get the current buttons.
- All the button panels are now more compact (smaller buttons, tighter spacing).

**Seed report.** The Outfit, Body, Face and Hair roulettes now send the seed they used back to the browser, so the LightCraft Edit Page can lock the exact roll behind a picture (Face tab opens = locked, Compare = unlocked).

## Style (Roulette Bar)

The first row of the Roulette Bar is **Style**: one dropdown (searchable, grouped) that steers the outfit, makeup and underwear dice together and gives them a matching colour scheme: one main colour and one contrasting accent, shared by all three parts (Neon Raver = neon pink with electric blue, Goth = black with blood red, and so on). A new seed gives a new but still fitting pair. "Any style" leaves everything random. **Fine-tune** shows the six parts (lock, re-roll, choose exactly what each may roll). Themes live in `themes_data.py`; add your own the same way.

New data: Emo, Scene, Neon Raver, Masquerade, Mourning Veils, Dominant and Submissive outfits; Emo & Scene, Masquerade & Veils and Neon Rave makeup; Dominant, Submissive and Masquerade & Veils underwear sets; a Veils & masks add-on (face veils, mourning veils, mesh face covers, masquerade masks).

## Beach, sporty, techwear and jackets

New outfit styles: **Beach** (huge sun hats, sheer white dresses, bikini strings), **Sporty Girl** (cropped hoodie over a sports bra, low-waist sweatpants with a high-rise thong), **Boxing & Gym Brands** (Lonsdale, Everlast, Gymshark, Venum; one brand per roll), **Cyber Techwear**, **Y2K Techwear** and **Puffer & Cropped Jackets** (cropped pilot bomber, cropped leather, shiny and oversized puffers). Matching themes: Beach Day, Sporty Girl, Boxing Gym, Cyber Techwear, Y2K Techwear, Jacket Season.

Y2K, Goth, Emo, Scene, Punk, Grunge, Casual and Streetwear also got low-rise + high-rise thong combinations (camo cargo pants + studded belt, ultra-low-rise jeans, low-rise plaid with a chain belt) and cropped jackets.

**No jackets** (Options row): switches off every jacket, coat, puffer, bomber and cardigan in the roll (and strips them from fixed-text mode), so the outfit stays easy to isolate. Styles built entirely from jackets (Puffer & Cropped Jackets) fall back to any style when it is on.

## Simple and Advanced pages (Roulette Bar)

The bar now has two big tabs next to the ON/OFF switch, with **Clear all** and **Roll all** in the upper right.
- **Simple:** a **Style** square (click to search and pick, arrows to step), a **How much** square (Covered, Cute, Revealing, Skimpy, Micro: click to step, click a bar to jump, the last level again clears it) and the prompt the bar rolled, in a wide box.
- **Advanced:** the style bar, **Join** (new line / space / comma), and the six parts with locks, dice and every button, exactly as before.
- Switching plays a motion: the old page leaves quickly, then each block of the new page grows from its upper-left corner while sliding into place, one after another.

Pictures: put square PNGs in `web/icons/` named after the style (`beach_day.png`, `goth.png`, `y2k_pop.png`: lower-case, spaces and `&` become `_`) and `level_1.png` ... `level_5.png` for the amount square. They are found on start-up (restart ComfyUI after adding some). Styles without a picture show a brand-orange tile with initials.


## Covered means PG (Roulette Bar)

The Bar rolls the outfit first and reads how skimpy it came out. Every other part then follows it:

| Outfit level | Body | Face / makeup | Underwear | Outfit pieces |
|---|---|---|---|---|
| 1 Covered | vague build + height only ("an extremely slim, petite frame") - no bust, stomach, waist, hips, butt or thigh words | no plump / pouty / overlined lips, no hooded or siren eyes, no sheer veils | none | no sheer, bra, harness, garter, corset, thong, bikini, cut-out, bondage / latex styles |
| 2 Cute | same vague build | same soft face and makeup | none | no harness, garter, corset, sheer, thong |
| 3 Revealing | full body wording | normal | follows the outfit (thongs, plunge, garter) | normal |
| 4 Skimpy | full | normal | lingerie-model level | normal |
| 5 Micro | full | normal | most revealing set | normal |

If the Skimpy row has only Covered (or Cute) switched on and a chosen style has nothing at that level, the Bar picks another style instead of creeping up a level.
The six single nodes behave as before; only the Bar links the parts.


## In frame square (Roulette Bar, Simple page)

A fourth square between "How much" and the prompt. A silhouette fills the part of the body that is in the picture; click to step, or click a bar to jump.

| Step | In the prompt | Left out |
|---|---|---|
| 1 Full body | everything | |
| 2 No feet | everything above the ankles | shoes, socks |
| 3 Top only | top, jacket, face, hair, bust and waist | bottoms, legwear, shoes, hips and legs |
| 4 Bottoms only | bottoms, legwear, hips, legs | top, jacket, face, hair, makeup, shoes |

It switches on the old "No shoes / No bottoms / No tops" options for the outfit and underwear, and trims the body wording. Old saved bars load as Full body.


## Masks and veils are the focus (Roulette Bar)

If the outfit or underwear rolls a mask or veil, the Bar drops the makeup part. An eye mask keeps only face shape and lips (no eye detail); a veil or face covering drops the face part too. The Masquerade Ball and Mourning Veils styles always roll a mask or veil.


## Skimpy and Micro stay skimpy

* 30 of the 39 outfit styles have no Micro pieces of their own. They used to slide down to a lower level (a hoodie and a skirt); now they borrow generic strap / cut-out cuts in the style's colours (`GENERIC_SKIMPY` in outfit_data.py - add your own lines there).
* At Skimpy and Micro the outfit gets only necklaces, earrings / piercings, bracelets and a bag, at most 4 (Skimpy) or 3 (Micro) of them. No hats or outer jackets at Micro, and no hair accessories whenever the Bar's hair part is on.
* Ten styles (streetwear, athleisure, Y2K, high street, luxury, alt, goth, sporty, gyaru, neon raver) have their own Skimpy / Micro pieces in `STYLE_SKIMPY` (e.g. Streetwear Micro = a skintight cropped tube top + a micro skirt). Skimpy can still carry an open shirt, jacket or robe; Micro never does.

## Shape square (Roulette Bar, Simple page)

A fifth square next to **In frame**: the general body shape in five steps, **Very slim, Slim, Balanced, Curvy, Hourglass** (click to step, click a bar to jump, click again after Hourglass to clear it so any shape is rolled). It decides the body type of the Body part; your own Bust / Waist / Hips picks still win. At Covered and Cute the wording stays vague (no anatomy), only the build changes. The square plays a shape-key animation from `web/shape_morph.png` (31 pre-rendered frames of your skinny silhouette morphing into the thick one and beyond, eased with the same expo curve as the other squares). Still pictures: `web/icons/shape_1.png` ... `shape_5.png` (made by morphing your skinny and thick silhouettes; replace them any time and list them in `index.json`, same as the `level_N.png` icons). Without them the square draws a simple figure that morphs between steps. The old prompt box is now a "Did you know" tips panel (the finished prompt is next to the Saver in the workflow); it shows a new tip for every seed and a click shows the next one. It is narrower to make room (the bar's minimum width is now 900).

### Luxury Couture (underwear)
A new Underwear style with 37 high-end designer lingerie sets: sheer silk and organza robes, Chantilly and Leavers lace, gold-hardware strap harnesses (pentagram, star, art deco, constellation, filigree chains), thigh straps and hip / backside harnesses, pearls and crystals. It leaves out bunny ears, fishnets, face veils and gothic chokers, and never adds a second robe on top of a set that already has one. Nodes saved before it existed get the button added automatically. It is also picked by the Club Glam, Boudoir Romantic and Masquerade Ball styles.



## Face square (Roulette Bar, Simple page)
A sixth square next to **Shape**: the face shape, **Oval, Heart, Round, Square, Diamond, Long, V-line, Angular, Soft full** (click to step, click a bar to jump, click again after the last one to clear it so any face is rolled). It is the same row as the **Face** button row on the Face card in Advanced, so the two always agree; picking a shape here switches the other Face buttons off. Eyes and lips are still rolled freely. The node is a little wider than before to make room for the square.

## Boho Hippie (theme)
Modern festival hippie: dreadlocks, braids, beads, shells and wraps in the hair (new hair category "Dreads & Boho"), patchwork skirts, crochet, kimonos, chunky sweaters, layered crystal jewellery, hand-poked tattoos, and a "Boho Crochet" lingerie family. Icon: web/icons/boho_hippie.png.
