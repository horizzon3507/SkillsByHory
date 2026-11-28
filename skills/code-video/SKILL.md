---
name: code-video
description: Generate art-directed videos by writing and running code (Python/Pillow/matplotlib frames encoded with ffmpeg), the way Claude does in its code-execution sandbox. Use when the user asks to make, render, or animate a video, motion graphic, explainer, title card, data animation, or GIF from a description, and no footage needs to be filmed or AI-generated.
license: Apache-2.0
---

# Code video

Make a video by writing a program that draws it. This reproduces the environment claude.ai uses: there is no video tool there, only a Linux sandbox with a shell and file tools, where the model writes code, runs it, checks the result, and hands over the file. The exact source text of that environment is in [reference/claude-environment.md](reference/claude-environment.md).

Press hard on three points: the video needs a real art direction before code, every video is rendered and looked at before it is delivered, and the deliverable is the `.mp4` file itself, never the script alone. For visual quality, treat [reference/visual-quality.md](reference/visual-quality.md) as part of this skill, not optional reading.

## The environment, mapped

| Claude sandbox | Here |
| --- | --- |
| `bash_tool`, `create_file`, `str_replace`, `view` | the agent's own shell, file-write, file-edit, and image-view tools |
| `/home/claude` scratch dir | `~/.code-video/work/<project>/` |
| `/mnt/user-data/outputs` | `~/.code-video/outputs/` |
| `present_files` | attach the file to the reply to the user |
| "read SKILL.md first" | this file |
| pip with pre-installed pillow, numpy, matplotlib | `~/.code-video/venv` from `scripts/setup.sh` |

## Workflow

1. **Set up once per machine.** Run `scripts/setup.sh`. It installs ffmpeg if missing, creates the venv with Pillow, numpy and matplotlib, and prints the paths. Use `~/.code-video/venv/bin/python` for everything below.
2. **Write the art direction before any code.** Create `ART_DIRECTION.md` in the work dir with: the one message, audience, mood, exact palette hexes, font choices, composition pattern, what the lead visual is, the world/material it belongs to, one signature detail, and what must not appear. Do not start from a generic gradient plus centered white text.
3. **Write the plan as a timeline.** Scenes with start and end seconds, what is on screen, what moves. Cast every moving element as lead, support, decoration, or static. Fix resolution, fps and duration now: 1280x720 at 30 fps unless asked otherwise, 1080x1920 for vertical.
4. **Render style frames first.** Export two or three key moments as PNGs before rendering video. Open them. If the still frame would not work as a poster, the video will not be saved by motion.
5. **Write one script** in the work dir that defines `frame(t, i, size)` and calls `render()` from `scripts/codevideo.py`. Make every position and opacity a function of `t`; never keep state between frames, so any frame can be rendered alone. Reuse `scripts/video_design.py` when it already has the primitive you need.
6. **Render a draft first.** Full resolution at 10-15 fps is usually better than half resolution, because small text and spacing must be judged honestly.
7. **Look at it.** Run `scripts/review.sh out.mp4`, then open the contact sheet with the image-view tool. Critique it with the checklist in `reference/visual-quality.md`: hierarchy, spacing, type size, color balance, overlap, first/last frame, duration and resolution. Fix and re-render until the sheet is right.
8. **Render final, copy to outputs, deliver the file** with one line on what it is. Keep the script next to it so the user can ask for changes.

## Visual rules that prevent programmer-looking videos

- **One lead per scene.** The viewer must know where to look. Everything else is support, decoration, or static.
- **Compose on a grid.** At 720p use 64-80 px outer margins, consistent columns, and deliberate asymmetry. Do not center every element by default.
- **Type is the design.** Use at most two families. Hero type is normally 72-120 px at 720p; important support is 32-44 px. Tiny interface copy is allowed inside a mock UI, never as the main message. Measure with `draw.textbbox` before placing long strings.
- **Use a chosen palette, not a random one.** Normally one background, one primary, one accent, and neutrals. Aim for a 60/30/10 balance. Write exact hexes in `ART_DIRECTION.md` and reuse them.
- **Depth must be intentional.** One or two of shadow, blur, glow, grain or texture is enough. Floating particles, glass cards and neon gradients are decoration, not a concept.
- **Do not use UI mockups as a substitute for design.** If the video is about a product, crop or abstract the interface; a whole generic app window rarely looks good in a motion piece.
- **Hold readable screens** for at least 1.5 s plus 0.3 s per word.
- Width and height must be even, and the output must be H.264 `yuv420p` with `+faststart`, or it will not play in browsers, Slack and phones. `render()` does this.
- Draw at the final size. Scaling small frames up blurs text. For anti-aliased shapes, draw on a 2x canvas and downscale with `Image.LANCZOS` when needed.

## Motion rules

- Ease every movement (`ease_out` for entrances, `ease_in_out` for moves). Linear motion only for continuous loops.
- One entrance per container. If the parent moves, its content is already there; do not also stagger every child.
- Order follows importance, not DOM order. The lead moves first and furthest; support moves less; decoration usually fades only.
- Overlap related movement. Uniform stagger is forbidden: equal delays, equal distance and equal easing read as a metronome.
- Exits are simultaneous, shorter and simpler than entrances.
- Scale duration by distance and size. Big moves can take 500-800 ms; small UI-like moves should finish closer to 200-350 ms.

## Which library

| Content | Use |
| --- | --- |
| Titles, shapes, UI mockups, kinetic text | Pillow `ImageDraw` |
| Charts and data animation | matplotlib with the `Agg` backend, `fig.canvas.buffer_rgba()` per frame |
| Pixel effects, gradients, particles | numpy arrays |
| Stitching clips, adding audio, subtitles, GIF | ffmpeg directly |
| Math animation in the 3Blue1Brown style | Manim, installed into the venv on demand |
| A design that already exists as a web page | headless browser screenshots per frame, then ffmpeg |

## ffmpeg recipes

```bash
# add narration or music, trimmed to the video
ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac -shortest out.mp4
# concatenate clips with identical size and fps
ffmpeg -f concat -safe 0 -i list.txt -c copy out.mp4
# GIF with a good palette
ffmpeg -i video.mp4 -vf "fps=15,scale=640:-1:flags=lanczos,split[a][b];[a]palettegen[p];[b][p]paletteuse" out.gif
# single frame at 2.5 s for inspection
ffmpeg -ss 2.5 -i video.mp4 -frames:v 1 frame.png
```

## Example

[examples/hello_video.py](examples/hello_video.py) renders a six-second title card:

```bash
~/.code-video/venv/bin/python examples/hello_video.py ~/.code-video/outputs/hello.mp4
scripts/review.sh ~/.code-video/outputs/hello.mp4
```
