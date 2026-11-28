"""Small design primitives for code-generated videos.

These helpers exist so videos start from deliberate typography, color and
composition instead of a pile of ad-hoc rounded rectangles. They are building
blocks, not a template: choose the palette and layout in ART_DIRECTION.md first.
"""

from dataclasses import dataclass

import numpy as np
from PIL import Image, ImageDraw, ImageFilter


@dataclass(frozen=True)
class Palette:
    background: str
    primary: str
    accent: str
    text: str
    muted: str
    panel: str


def rgb(hex_color):
    h = hex_color.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgba(hex_color, alpha=255):
    return rgb(hex_color) + (int(alpha),)


def mix(color_a, color_b, x):
    a = rgb(color_a) if isinstance(color_a, str) else color_a[:3]
    b = rgb(color_b) if isinstance(color_b, str) else color_b[:3]
    x = max(0.0, min(1.0, x))
    return tuple(round(a[i] + (b[i] - a[i]) * x) for i in range(3))


def with_alpha(color, alpha):
    if isinstance(color, str):
        return rgba(color, alpha)
    if len(color) == 3:
        return color + (int(alpha),)
    return color[:3] + (int(color[3] * max(0.0, min(1.0, alpha))),)


def radial_backdrop(size, base, glows=(), vignette=0.34):
    """Return an RGBA background with normalized radial glows.

    glows: iterable of (x, y, radius, hex_color, intensity), where x/y are
    0..1 canvas positions, radius is relative to the smaller dimension, and
    intensity is roughly how much of the glow color to add at the center.
    """
    w, h = size
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    x = xx / max(1, w)
    y = yy / max(1, h)
    arr = np.zeros((h, w, 3), dtype=np.float32)
    arr[:] = rgb(base)
    for gx, gy, radius, color, intensity in glows:
        scale = min(w, h) / max(w, h)
        dx = (x - gx) * (w / min(w, h))
        dy = (y - gy) * (h / min(w, h))
        g = np.exp(-((dx * dx + dy * dy) / max(0.0001, radius * radius)))
        target = np.array(rgb(color), dtype=np.float32)
        arr += (target - arr) * (g[..., None] * intensity)
    cx = (x - 0.5) * 1.2
    cy = (y - 0.5) * 1.2
    shade = np.clip(1.0 - vignette * (cx * cx + cy * cy), 0.55, 1.0)
    arr *= shade[..., None]
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB").convert("RGBA")


def add_grain(img, amount=3.0, seed=0):
    """Add subtle monochromatic grain to an RGB/RGBA image."""
    if amount <= 0:
        return img
    arr = np.asarray(img.convert("RGBA")).astype(np.int16)
    rng = np.random.default_rng(seed)
    noise = rng.normal(0, amount, arr.shape[:2])[..., None]
    arr[..., :3] = np.clip(arr[..., :3] + noise, 0, 255)
    return Image.fromarray(arr.astype(np.uint8), "RGBA")


def text_size(draw, value, font, tracking=0):
    box = draw.textbbox((0, 0), value, font=font)
    width = box[2] - box[0]
    if tracking and len(value) > 1:
        width += tracking * (len(value) - 1)
    return width, box[3] - box[1]


def tracked_text(draw, xy, value, font, fill, tracking=0, anchor="la"):
    """Draw letterspaced text.

    Horizontal anchors: l (left), m (middle), r (right). Vertical anchors follow
    Pillow's text anchor letters where possible; the common useful forms are
    'la', 'lm' and 'mm'.
    """
    x, y = xy
    width, height = text_size(draw, value, font, tracking)
    horizontal = anchor[0] if anchor else "l"
    vertical = anchor[1] if len(anchor) > 1 else "a"
    if horizontal == "m":
        x -= width / 2
    elif horizontal == "r":
        x -= width
    if vertical == "m":
        y -= height / 2
    elif vertical in ("d", "s"):
        y -= height
    cursor = x
    for ch in value:
        draw.text((cursor, y), ch, font=font, fill=fill, anchor="la")
        ch_w, _ = text_size(draw, ch, font)
        cursor += ch_w + tracking


def fit_font(draw, value, font_factory, max_width, start_size, min_size, tracking=0):
    """Return the largest font from font_factory(size) fitting max_width."""
    probe = font_factory(start_size)
    for size in range(int(start_size), int(min_size) - 1, -2):
        probe = font_factory(size)
        width, _ = text_size(draw, value, probe, tracking)
        if width <= max_width:
            return probe
    return probe


def draw_panel(img, box, radius, fill, outline=None, width=1, shadow=True, shadow_alpha=90, blur=18, offset=(0, 12)):
    """Draw a rounded panel with a soft shadow onto an RGBA image."""
    if shadow:
        layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(layer)
        shifted = (box[0] + offset[0], box[1] + offset[1], box[2] + offset[0], box[3] + offset[1])
        shadow_draw.rounded_rectangle(shifted, radius=radius, fill=(0, 0, 0, shadow_alpha))
        layer = layer.filter(ImageFilter.GaussianBlur(blur))
        img.alpha_composite(layer)
    draw = ImageDraw.Draw(img, "RGBA")
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)
    return draw


def draw_rule(draw, xy, width, color, thickness=4, progress=1.0):
    """Draw a horizontal rule partially revealed from left to right."""
    x, y = xy
    w = width * max(0.0, min(1.0, progress))
    if w <= 0:
        return
    draw.rounded_rectangle((x, y, x + w, y + thickness), radius=thickness / 2, fill=color)


def wave_delay(index, first=0.0, step=0.09, decay=0.82):
    """Non-uniform stagger delays in seconds: 0, step, step*(1+decay), ..."""
    if index <= 0:
        return first
    total = 0.0
    current = step
    for _ in range(index):
        total += current
        current *= decay
    return first + total
