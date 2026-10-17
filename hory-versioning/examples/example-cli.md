# Changelog

We follow [Semantic Versioning](https://semver.org/) and [Keep a Changelog](https://keepachangelog.com/). yourapp is a single CLI surface.

<details>
<summary>To see more about versioning, expand this.</summary>

Every version string starts with `v` (required), e.g. `v0.2.0-stable`, `v0.1.0-stable`.

Here the installable surface is **CLI** (`yourapp` / `yapp`). Other apps swap in their own names the same way — e.g. **GNOME**, **Desktop**, **Web** — whatever you actually ship.

| Part | What you install | Example |
| --- | --- | --- |
| **CLI** | `yourapp` / `yapp` in the terminal | `v0.2.0-stable` |

With one surface there is no `m` in the tag and no per-surface sections — just the version notes.

Each release heading is the version and date (`## v0.2.0-stable · 18/07/2026`); under it, a short summary ends with a plain sentence like: “This version was made for CLI with a stable release channel on 18/07/2026 (v0.2.0-stable).”

### What the channel suffix means

| Suffix | In plain words |
| --- | --- |
| **-alpha** | Very early. Expect missing pieces and lots of bugs. |
| **-beta** | Mostly there, but still rough. Fine to try; not the “official” install. |
| **-stable** | Ready for daily use. This is what we put on GitHub Releases and the AUR. |

We only call something **stable** when we mean it.

</details>

## v0.2.0-stable · 18/07/2026

Filtering, home shortcuts, richer previews, `tree`, and AUR packaging. This version was made for CLI with a stable release channel on 18/07/2026 (v0.2.0-stable).

- Case-insensitive name filter with `/`; an empty filter restores the full directory.
- Jump home with `~` and toggle the previous location with `-`.
- Bounded text and source-code previews for common readable formats; the preview panel picks Kitty graphics, source text or file metadata as needed.
- `tree` / `t` command with configurable recursion depth.
- AUR package `yourapp` (optional ImageMagick) and a GitHub Release workflow that can refresh the AUR package.
- Various other small tweaks

## v0.1.0-stable · 18/07/2026

First public cut of the terminal file manager. This version was made for CLI with a stable release channel on 18/07/2026 (v0.1.0-stable).

- Dual binaries `yourapp` and short alias `yapp`, with an interactive alternate-screen UI.
- Keyboard navigation (arrows, Vim keys, paging, first/last), plus mouse row select and wheel scroll.
- Browse, open with the system app, hidden-file toggle, and sort by name, size or mtime.
- Internal clipboard with copy / cut / paste and collision-safe copy names; create, rename and confirmed delete.
- Plain `list` and `info` commands, with automatic plain-output fallback outside a TTY.
- Kitty Graphics Protocol image previews (optional ImageMagick for JPEG, GIF, WebP, BMP, TIFF) with Kitty / Ghostty / WezTerm detection.
- Various other UI polish and tests
