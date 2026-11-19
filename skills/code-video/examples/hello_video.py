"""Six-second title card: python hello_video.py out.mp4"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from PIL import Image, ImageDraw  # noqa: E402

from codevideo import ease_out, font, lerp, progress, render  # noqa: E402

BG, FG, ACCENT = (14, 16, 22), (240, 240, 245), (98, 160, 255)
TITLE, SUB = font(96), font(36)


def frame(t, i, size):
    w, h = size
    img = Image.new("RGB", size, BG)
    d = ImageDraw.Draw(img)

    for k in range(24):
        x = w * k / 23
        y = h * 0.78 + math.sin(t * 2 + k * 0.5) * 28
        d.ellipse((x - 5, y - 5, x + 5, y + 5), fill=ACCENT)

    a = ease_out(progress(t, 0.3, 1.3))
    y = lerp(h * 0.45, h * 0.36, a)
    d.text((w / 2, y), "Video made with code", font=TITLE, anchor="mm",
           fill=tuple(round(lerp(b, f, a)) for b, f in zip(BG, FG)))

    b = ease_out(progress(t, 1.2, 2.0))
    d.rectangle((w / 2 - 260 * b, h * 0.47, w / 2 + 260 * b, h * 0.47 + 4), fill=ACCENT)
    d.text((w / 2, h * 0.55), "Pillow frames piped into ffmpeg", font=SUB, anchor="mm",
           fill=tuple(round(lerp(c, f, b)) for c, f in zip(BG, FG)))
    return img


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "hello.mp4"
    print(render(frame, out, duration=6, fps=30, size=(1280, 720)))
