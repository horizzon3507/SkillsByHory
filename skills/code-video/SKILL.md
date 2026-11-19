---
name: code-video
description: Generate videos by writing and running code (Python/Pillow/matplotlib frames encoded with ffmpeg), the way Claude does in its code-execution sandbox. Use when the user asks to make, render, or animate a video, motion graphic, explainer, title card, data animation, or GIF from a description, and no footage needs to be filmed or AI-generated.
license: Apache-2.0
---

# Code video

Make a video by writing a program that draws it. This reproduces the environment claude.ai uses: there is no video tool there, only a Linux sandbox with a shell and file tools, where the model writes code, runs it, checks the result, and hands over the file. The exact source text of that environment is in [reference/claude-environment.md](reference/claude-environment.md).

Press hard on two points: every video is rendered and looked at before it is delivered, and the deliverable is the `.mp4` file itself, never the script alone.

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
2. **Write the plan as a timeline before any code.** Scenes with start and end seconds, what is on screen, what moves. Fix resolution, fps and duration now: 1280x720 at 30 fps unless asked otherwise, 1080x1920 for vertical.
3. **Write one script** in the work dir that defines `frame(t, i, size)` and calls `render()` from `scripts/codevideo.py`. Make every position and opacity a function of `t`; never keep state between frames, so any frame can be rendered alone.
4. **Render a draft first.** Half resolution or 10 fps, to catch layout and timing mistakes in seconds.
5. **Look at it.** Run `scripts/review.sh out.mp4`, then open the contact sheet with the image-view tool. Check: text inside the frame and readable, nothing overlapping, the first and last frames not blank, duration and resolution as planned. Fix and re-render until the sheet is right.
6. **Render final, copy to outputs, deliver the file** with one line on what it is. Keep the script next to it so the user can ask for changes.

## Drawing rules that prevent the usual failures

- Width and height must be even, and the output must be H.264 `yuv420p` with `+faststart`, or it will not play in browsers, Slack and phones. `render()` does this.
- Ease every movement (`ease_out` for entrances, `ease_in_out` for moves). Linear motion looks mechanical.
- Text: at least 36 px at 720p, anchored with `anchor="mm"`, kept 5% away from each edge. Measure with `draw.textbbox` before placing long strings.
- Hold each readable screen for at least 1.5 s plus 0.3 s per word.
- Draw at the final size. Scaling small frames up blurs text.
- For anti-aliased shapes, draw on a 2x canvas and downscale with `Image.LANCZOS`.

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
