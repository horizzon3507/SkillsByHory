"""Render a video from a Python function that draws one frame at a time.

    from codevideo import render, ease_out, clamp, font

    def frame(t, i, size):          # t seconds, i frame index, size (w, h)
        return PIL.Image or HxWx3 uint8 numpy array

    render(frame, "out.mp4", duration=6, fps=30, size=(1280, 720))

Frames are piped raw into ffmpeg, so nothing is written to disk but the mp4.
"""

import shutil
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageFont

FONT_CANDIDATES = (
    "/System/Library/Fonts/Helvetica.ttc",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    "C:/Windows/Fonts/arial.ttf",
)


def clamp(x, lo=0.0, hi=1.0):
    return max(lo, min(hi, x))


def progress(t, start, end):
    """0..1 position of t inside [start, end]."""
    return clamp((t - start) / (end - start)) if end > start else float(t >= end)


def ease_out(x):
    return 1 - (1 - clamp(x)) ** 3


def ease_in_out(x):
    x = clamp(x)
    return 4 * x**3 if x < 0.5 else 1 - (-2 * x + 2) ** 3 / 2


def lerp(a, b, x):
    return a + (b - a) * x


def font(size, path=None):
    for candidate in (path, *FONT_CANDIDATES):
        if candidate and Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default(size)


def render(frame, out, duration, fps=30, size=(1280, 720), audio=None, crf=18):
    """Call frame(t, i, size) for every frame and encode H.264 yuv420p mp4.

    audio: optional path to an audio file, muxed as AAC and trimmed to the video.
    """
    if shutil.which("ffmpeg") is None:
        raise RuntimeError("ffmpeg not found; run scripts/setup.sh")
    w, h = size
    if w % 2 or h % 2:
        raise ValueError("width and height must be even for yuv420p")
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    total = round(duration * fps)

    cmd = ["ffmpeg", "-v", "error", "-y",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}", "-r", str(fps), "-i", "-"]
    if audio:
        cmd += ["-i", str(audio), "-c:a", "aac", "-b:a", "192k", "-shortest"]
    cmd += ["-c:v", "libx264", "-preset", "medium", "-crf", str(crf),
            "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(out)]

    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    try:
        for i in range(total):
            img = frame(i / fps, i, size)
            if isinstance(img, Image.Image):
                img = np.asarray(img.convert("RGB"))
            if img.shape != (h, w, 3) or img.dtype != np.uint8:
                raise ValueError(f"frame {i}: expected uint8 {(h, w, 3)}, got {img.dtype} {img.shape}")
            proc.stdin.write(img.tobytes())
    finally:
        proc.stdin.close()
        code = proc.wait()
    if code:
        raise RuntimeError(f"ffmpeg exited with {code}")
    return out
