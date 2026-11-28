# Visual quality for code-generated video

This file is the design gate. Read it before writing the video script and again when the contact sheet is open. A technically correct render with weak art direction is not finished.

## 1. Art direction brief

Write `ART_DIRECTION.md` before code. Keep it short, but make every decision explicit:

```md
# Art direction

- Message: one sentence the viewer should remember
- Audience: who this is for
- Mood: 2-3 concrete words (for example: precise, warm, editorial)
- Lead visual: the one thing the eye lands on first
- Composition: title card / split screen / editorial crop / data stage / abstract system
- Palette: exact hexes, with roles
  - background:
  - primary:
  - accent:
  - text/neutrals:
- Type: families, weights, sizes
- Motion idea: one gesture, not a list of effects
- World/material: where the subject naturally lives (terminal, paper, stage, instrument panel, night city, print editorial)
- Signature detail: one specific visual detail only this video needs
- Must not appear: generic gradient, floating particles, stock icons, app-window mockup, etc.
```

Put the richness in the lead visual or content. Keep the chrome quiet. If every surface glows, nothing is important; if only one crafted moment carries the color, the viewer knows where to look.

If the brief says only "modern, clean, blue gradient", start over. Those words do not constrain anything.

## 2. Composition

Pick a pattern and commit to it.

| Pattern | Use when | Composition rule |
| --- | --- | --- |
| Editorial title card | Brand pieces, intros, simple messages | Large type anchored left or lower-left; one visual accent; generous negative space |
| Split stage | Before/after, product versus idea, two concepts | One dominant side, not a perfect 50/50 split unless contrast is the point |
| Cropped product | Software explainers | Crop into the interface; show the meaningful control large instead of the whole window |
| Data stage | Charts and metrics | Chart is the lead; labels are few and large; axes are muted |
| Abstract system | Protocols, networks, motion mood pieces | One repeated geometric motif with controlled variation, not random decoration |

Rules:

- At 720p, keep important content inside 64-80 px outer margins.
- Use asymmetry deliberately. Perfect centering is for logos and final locks, not every scene.
- Negative space is a shape. Do not fill it because it is empty.
- Limit each scene to one lead. If two elements compete, scale one down or cut it.
- Align edges. Random x positions make even good colors look accidental.

## 3. Typography

- Use at most two families: usually one display/heading face and one text face.
- At 720p: hero 72-120 px, section titles 48-64 px, important support 32-44 px. Small copy is allowed only inside deliberate product mockups.
- Titles should have a clear line break. Do not let Pillow wrap wherever pixels happen to end.
- Use uppercase sparingly, with tracking. Use `tracked_text()` from `video_design.py` rather than inserting spaces by hand.
- Measure every important string with `draw.textbbox`. Check the right edge, not just the center.
- Contrast is non-negotiable. If text sits on a busy glow or image, dim the background behind it or move the text.

## 4. Color and depth

- Choose roles before rendering: background, primary, accent, neutral text. Exact hexes go in the brief.
- A good default balance is 60% background, 30% primary/neutral forms, 10% accent.
- One accent can carry the whole piece. Two competing accents usually look like a template.
- Gradients need a light direction and a reason. A purple-blue radial glow is not a personality.
- Pick one or two depth techniques: soft shadow, blur, glow, grain, texture. More becomes noise.
- Grain should be barely visible. If the viewer notices noise before content, reduce it.

## 5. Motion choreography

Write the motion as one gesture per scene.

| Role | Treatment |
| --- | --- |
| Lead | Moves first, travels furthest, stays longest |
| Support | Follows with shorter, smaller movement |
| Decoration | Fades only, or does not animate |
| Static | Does not move |

Rules:

- Entrances use strong ease-out. Movement through space uses ease-in-out. Continuous loops may be linear.
- Overlap related elements. Uniform stagger is forbidden: equal delay, distance and easing reads mechanical.
- One entrance per container. Never slide a panel in and then stagger all of its children too.
- Exits are shorter and simpler. Do not reverse-stagger a whole scene out.
- Motion must explain hierarchy or transition. If it is only decoration, cut it.

## 6. Style frames and review

Before rendering video, export stills for at least:

1. the first meaningful composition,
2. the densest frame,
3. the final frame.

Open them as images. Ask:

- Where does the eye land first? Is that the intended lead?
- Would this still work as a poster without motion?
- Is any text smaller than it needs to be?
- Does anything look like a default template: centered white title, blue-purple glow, rounded cards, floating particles?
- Are margins and alignment consistent across frames?
- Is the first frame intentional and the last frame a clean ending?

Then render the draft and inspect the contact sheet at thumbnail scale. Thumbnails expose hierarchy problems that full-size inspection hides.

## 7. Before you finish

| Detection pattern | Fix |
| --- | --- |
| Centered white text over a generic gradient | Choose a composition pattern; move type onto a grid; give the piece a lead visual |
| Three identical cards in a row | Cut, merge, or turn them into one visual system; cards are rarely a concept |
| Several floating particles/glows with no meaning | Remove most decoration; keep one motif tied to the message |
| Every object enters with the same distance and delay | Make one lead, reduce support movement, vary overlap |
| Main message below 32 px at 720p | Increase type, shorten copy, or simplify the scene |
| A whole app window fills the video | Crop to the meaningful control or abstract the interface into shapes |
| Text nearly touches an edge or overlaps decoration | Respect margins; measure with `textbbox`; dim or move the background |
| First or final frame is empty or transitional | Start on an intentional composition; end on a held final lockup |
| More than two accent colors compete | Reassign roles; keep one accent and neutrals |
| Contact sheet looks fine but motion feels mechanical | Check easing and overlap; do not add more effects |

If two or more rows apply, do not polish the render yet. Redo the art direction.
