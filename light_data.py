"""Dataset for the No_Thing Lighting chooser. {key} = the main light colour, {rim} = the second (rim / back / accent) colour."""

COLOURS = {   # button: words used in the prompt
    "Pink": "pink", "Hot magenta": "hot magenta", "Purple": "deep purple", "Violet": "ultraviolet violet",
    "Cyan": "bright cyan", "Electric blue": "electric blue", "Red": "saturated red", "Crimson": "deep crimson",
    "Warm amber": "warm amber", "Peach": "peach", "Teal": "teal", "White": "clean white",
}

PALETTES = {   # button: (key, rim)
    "Pink + Cyan": ("Pink", "Cyan"), "Magenta + Blue": ("Hot magenta", "Electric blue"), "Purple + Pink": ("Purple", "Pink"),
    "Red + Purple": ("Red", "Violet"), "Cyan + Magenta": ("Cyan", "Hot magenta"), "Peach + Violet": ("Peach", "Violet"),
    "Crimson + Teal": ("Crimson", "Teal"), "Pink + Amber": ("Pink", "Warm amber"),
}

SETUPS = {
    "Single spotlight": "a single hard {key} spotlight from above and slightly in front, a tight pool of light on her with a fast falloff into deep shadow",
    "Two-point": "two-point lighting: a soft {key} key light from the front left and a strong {rim} rim light from behind right, outlining her hair, shoulders and hips",
    "Rim light": "{rim} rim light tracing the edge of her silhouette, hair and shoulders, with her face softly lit by a dim {key} fill",
    "Backlit glow": "a strong {rim} backlight creating a glowing halo around her hair and body, with soft {key} light on the front",
    "Neon glow": "glowing {key} neon light with {rim} neon reflections washing across her skin in a dark room",
    "Soft glamour": "soft beauty lighting from a large {key}-tinted light above with a gentle fill and a {rim} accent in the background",
}

MOODS = {
    "Soft & dreamy": "soft, dreamy and diffused with a gentle bloom",
    "Hard & dramatic": "hard, high-contrast and dramatic with crisp shadow edges",
    "Low-key moody": "low-key and moody with deep shadows",
}

EXTRAS = {
    "Lens flare": "subtle anamorphic lens flare",
    "Bokeh lights": "glittering out-of-focus bokeh lights in the background",
    "Light haze": "a light haze in the air",
    "Glossy highlights": "glossy highlights on skin, hair and lips",
}
