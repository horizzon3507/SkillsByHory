"""Six-second editorial title card: python hello_video.py out.mp4"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from PIL import ImageDraw  # noqa: E402

from codevideo import ease_in_out, ease_out, font, lerp, progress, render  # noqa: E402
from video_design import add_grain, draw_panel, draw_rule, radial_backdrop, rgba, tracked_text, wave_delay  # noqa: E402

BG = "#0E1110"
PANEL = "#18201C"
TEXT = "#E5EBE2"
MUTED = "#8E9B90"
ACCENT = "#74F2A0"
ACCENT_DIM = "#2B6B45"

FONT_MONO = "/System/Library/Fonts/Menlo.ttc"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"


def mono(size):
    return font(size, path=FONT_MONO)


def bold(size):
    return font(size, path=FONT_BOLD)


def regular(size):
    return font(size, path=FONT_REG)


def frame(t, i, size):
    w, h = size
    sx = w / 1280
    sy = h / 720
    img = radial_backdrop(
        size,
        BG,
        glows=(
            (0.88, 0.12, 0.48, ACCENT_DIM, 0.16),
            (0.08, 0.92, 0.42, "#24352C", 0.18),
        ),
        vignette=0.28,
    )
    img = add_grain(img, amount=2.2, seed=11)
    d = ImageDraw.Draw(img, "RGBA")

    margin = 76 * sx
    top = 78 * sy

    # Quiet metadata row. The rule is the first moving object; the type is already there.
    rule_p = ease_out(progress(t, 0.15, 0.85))
    draw_rule(d, (margin, top), 210 * sx, rgba(ACCENT, 220), thickness=max(2, round(4 * sy)), progress=rule_p)
    tracked_text(
        d,
        (margin, top + 24 * sy),
        "CODEVIDEO / EXAMPLE",
        mono(round(18 * sy)),
        rgba(MUTED, 225),
        tracking=round(4 * sx),
        anchor="la",
    )

    # Editorial title: one lead, left aligned, no decorative icon cloud.
    title_p = ease_out(progress(t, 0.55, 1.35))
    code_p = ease_out(progress(t, 0.82, 1.65))
    title_size = round(106 * sy)
    x = margin
    y1 = lerp(255 * sy, 220 * sy, title_p)
    y2 = lerp(365 * sy, 330 * sy, code_p)
    d.text(
        (x + (1 - title_p) * 34 * sx, y1),
        "MOTION",
        font=bold(title_size),
        fill=rgba(TEXT, 255 * title_p),
        anchor="lm",
    )
    d.text(
        (x + (1 - code_p) * 26 * sx, y2),
        "WITH CODE",
        font=bold(title_size),
        fill=rgba(ACCENT, 255 * code_p),
        anchor="lm",
    )

    sub_p = ease_out(progress(t, 1.35, 2.05))
    d.text(
        (margin, 432 * sy + (1 - sub_p) * 14 * sy),
        "frames written as programs, not templates",
        font=regular(round(31 * sy)),
        fill=rgba(MUTED, 245 * sub_p),
        anchor="lm",
    )

    # The lead visual is a tiny timeline because that is what the product does.
    panel_p = ease_out(progress(t, 1.85, 2.55))
    px = margin
    py = lerp(555 * sy, 502 * sy, panel_p)
    pw = 760 * sx
    ph = 118 * sy
    panel_alpha = int(235 * panel_p)
    if panel_alpha:
        draw_panel(
            img,
            (px, py, px + pw, py + ph),
            radius=22 * sx,
            fill=rgba(PANEL, panel_alpha),
            outline=rgba("#314139", 130 * panel_p),
            width=max(1, round(1.5 * sx)),
            shadow=True,
            shadow_alpha=int(70 * panel_p),
            blur=round(16 * sx),
            offset=(0, round(10 * sy)),
        )
        d = ImageDraw.Draw(img, "RGBA")
        tracked_text(
            d,
            (px + 28 * sx, py + 24 * sy),
            "TIMELINE",
            mono(round(15 * sy)),
            rgba(MUTED, 210 * panel_p),
            tracking=round(3 * sx),
            anchor="la",
        )
        # Three lanes with non-uniform block timing. They loop gently rather than flying around.
        lanes = (py + 53 * sy, py + 76 * sy, py + 97 * sy)
        colors = (ACCENT, TEXT, MUTED)
        widths = (150, 118, 190)
        for lane, (yy, color, bw) in enumerate(zip(lanes, colors, widths)):
            d.rounded_rectangle(
                (px + 28 * sx, yy - 5 * sy, px + pw - 28 * sx, yy + 5 * sy),
                radius=5 * sy,
                fill=rgba("#0B0E0C", 180 * panel_p),
            )
            block_p = ease_in_out(progress(t, 2.15 + wave_delay(lane, step=0.12), 2.95 + wave_delay(lane, step=0.12)))
            bx = px + 28 * sx + (pw - 56 * sx - bw * sx) * (0.12 + 0.18 * lane) * block_p
            d.rounded_rectangle(
                (bx, yy - 5 * sy, bx + bw * sx, yy + 5 * sy),
                radius=5 * sy,
                fill=rgba(color, (170 if lane else 225) * panel_p),
            )
        playhead_p = progress((t - 2.0) % 3.6, 0.0, 3.6)
        play_x = px + 30 * sx + (pw - 60 * sx) * playhead_p
        d.line((play_x, py + 43 * sy, play_x, py + 108 * sy), fill=rgba(ACCENT, 235 * panel_p), width=max(2, round(2 * sx)))

    # Small end-note fades in and stays; the composition ends held, not blank.
    end_p = ease_out(progress(t, 4.65, 5.25))
    tracked_text(
        d,
        (w - margin, h - 64 * sy),
        "PYTHON + FFMPEG",
        mono(round(17 * sy)),
        rgba(MUTED, 215 * end_p),
        tracking=round(3 * sx),
        anchor="ra",
    )
    return img.convert("RGB")


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "hello.mp4"
    print(render(frame, out, duration=6, fps=30, size=(1280, 720)))
