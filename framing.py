"""
Framing helpers for the Outfit and Underwear roulettes: "No tops" / "No bottoms" / "No shoes" so a prompt only mentions what is in frame.
A torso crop with panties, fishnets or heels in the text makes the model pull the picture back to show them; these helpers keep the
words out of the prompt (whole entries that are only about the hidden half are skipped, mixed entries are cut down to the visible half).
"""
import re

NO_BOTTOMS = "No bottoms"
NO_TOPS = "No tops"

_LOW = (r"panty|panties|thongs?|g-?strings?|briefs?|boy-?shorts?|shorts|skirts?|skorts?|bottoms?|garters?|suspenders?|suspender belts?|stockings?|fishnets?|tights|thighs?|"
        r"hosiery|stay-ups?|leggings?|legs?|hot pants|bloomers|pants|trousers|jeans|joggers|sweatpants|heels?|boots?|socks?|knee|knees|ankles?|anklets?|hips?|hipsters?|cheeky|"
        r"tanga|brazilian|high-leg|high-waisted|low-rise|hem|slits?|tutu|petticoat|culottes|jumpsuit|romper|catsuit|unitard|"
        r"sneakers?|sandals?|pumps?|stilettos?|loafers?|mules?|flats|platforms?|creepers?|rollerblades|mary[- ]janes?|feet|foot|toes?")
LOW = re.compile(r"\b(" + _LOW + r")\b", re.I)

_TOP = (r"bras?|bralettes?|bustiers?|corsets?|camis?|camisoles?|(?<!-)tops?|pasties|bandeau|tube|halter|crop|tees?|t-?shirts?|shirts?|blouses?|sweaters?|knits?|cardigans?|hoodies?|"
        r"jackets?|coats?|blazers?|vests?|tanks?|tank|bolero|shrug|cape|gloves?|chokers?|collars?|necklaces?|earrings?|ears|horns|headbands?|masks?|veils?|hats?|caps?|"
        r"bodysuits?|teddy|teddies|babydoll|chemise|nightie|robe|kimono|gown|dress|slip")
TOP = re.compile(r"\b(" + _TOP + r")\b", re.I)
_SEG = re.compile(r"(,\s*|\s+and\s+|\s+with\s+|\s+plus\s+)", re.I)


def _segments(text):
    parts = _SEG.split(text)
    return [(parts[i], parts[i + 1] if i + 1 < len(parts) else "") for i in range(0, len(parts), 2)]      # (text, separator that follows)


def cut_bottoms(text):
    """Keep what comes before the first clause that talks about hips, legs or feet. None when nothing visible is left."""
    out = ""
    for seg, sep in _segments(text):
        if LOW.search(seg):
            break
        out += seg + sep
    out = re.sub(r"(,\s*|\s+and\s+|\s+with\s+|\s+plus\s+)$", "", out, flags=re.I).strip()
    out = re.sub(r"\s+(matching|coordinating)$", "", out, flags=re.I)
    return out if out and TOP.search(out) else None


def cut_tops(text):
    """Keep the lower-body part: from the first clause that talks about hips, legs or feet on. None when there is none."""
    segs = _segments(text)
    for i, (seg, _) in enumerate(segs):
        if LOW.search(seg) and not TOP.search(seg):
            keep = [(s_, p_) for j, (s_, p_) in enumerate(segs[i:]) if j == 0 or not TOP.search(s_)]      # later clauses about bras, collars ... go
            rest = "".join(s_ + p_ for s_, p_ in keep)
            rest = re.sub(r"(,\s*|\s+and\s+|\s+with\s+|\s+plus\s+)$", "", rest, flags=re.I).strip()
            rest = re.sub(r"^(a |an )?(matching|coordinating)\s+", "", rest, flags=re.I)
            c = re.search(r"\{c2?\}", text)
            if c and "{c" not in rest:
                rest = c.group(0) + " " + rest
            return re.sub(r"^(\{c2?\}\s+)(a|an|the)\s+", r"\1", rest)
    return None


def visible_text(text, no_tops=False, no_bottoms=False):
    """One roll line reduced to the half of the body that is in frame (None = drop the line)."""
    if no_bottoms:
        text = cut_bottoms(text)
        if text is None:
            return None
    if no_tops:
        text = cut_tops(text)
    return text


def strip_bits(sentence, no_tops=False, no_bottoms=False):
    """For random-off mode: drop comma-separated bits that name the hidden half."""
    bits = [b for b in re.split(r",\s*", sentence.rstrip(".")) if b.strip()]
    if no_bottoms:
        bits = [b for b in bits if not LOW.search(b)]
    if no_tops:
        bits = [b for b in bits if not TOP.search(b)]
    return ", ".join(bits)


_TOP_REF = re.compile(r"\s+(?:under|over|beneath|below|with|and)\s+(?:an?\s+|the\s+|big\s+)?(?:[\w-]+\s+){0,2}?(?:" + _TOP + r")\b[^,]*", re.I)


def lower_only(text):
    """A bottoms / legwear line without clauses that name the top half ('leggings under an oversized top' -> 'leggings')."""
    out = _TOP_REF.sub("", text).strip()
    return out or None
