# Changelog

We follow [Semantic Versioning](https://semver.org/) and [Keep a Changelog](https://keepachangelog.com/). optionTerm is a single GNOME surface.

<details>
<summary>To see more about versioning, expand this.</summary>

Every version string starts with `v` (required), e.g. `v0.2.1-stable`, `v0.2.0-beta`.

Here the installable surface is **GNOME** (GTK4 + libadwaita). Other Option apps swap in their own names the same way — e.g. **CLI**, **Desktop**, **Web** — whatever you actually ship.

| Part | What you install | Example |
| --- | --- | --- |
| **GNOME** | `optionterm` desktop terminal | `v0.2.1-stable` |

With one surface there is no `m` in the tag and no per-surface sections — just the version notes.

Each release heading is the version and date (`## v0.2.1-stable · 01/08/2026`); under it, a short summary ends with a plain sentence like: “This version was made for GNOME with a stable release channel on 01/08/2026 (v0.2.1-stable).”

### What the channel suffix means

| Suffix | In plain words |
| --- | --- |
| **-alpha** | Very early. Expect missing pieces and lots of bugs. |
| **-beta** | Mostly there, but still rough. Fine to try; not the “official” install. |
| **-stable** | Ready for daily use. This is what we put on GitHub Releases and the AUR. |

We only call something **stable** when we mean it. While a large rewrite is settling, builds stay **beta**.

Versions at `v0.2.0` and earlier shipped without a channel suffix. From later cuts on, every GNOME version includes one.

</details>

## v0.2.1-stable · 01/08/2026

Session restore depth, launch flags, bottom tabs and command presets. This version was made for GNOME with a stable release channel on 01/08/2026 (v0.2.1-stable).

- Split-tree session restore keeps nested pane orientation and divider ratios in `session.toml` (old flat `panes` lists still open as a horizontal chain).
- Window geometry — width, height and maximized — round-trips with the session.
- CLI launch surface on the same app: `--working-directory` / `-d`, `-e` / `--command` / `--`, and a directory positional; a second instance opens a tab in the primary window.
- Tab bar can sit under the content (`tabs = "bottom"`); Preferences and `window.tabs` accept it.
- `scroll.lines` sets VTE scrollback length (default 10 000).
- Named `[[command]]` presets (`name` + `argv`, optional `cwd`) show up in the command palette as “Run: …”.
- Chrome follows `gtk-decoration-layout` and the chrome font from `gtk-font-name` / DPI.
- Various other small tweaks

## v0.2.0-beta · 31/07/2026

Engine rewrite onto system VTE and a cleaner first-run config. This version was made for GNOME with a beta release channel on 31/07/2026 (v0.2.0-beta).

- Terminal surface embeds stock VTE via `vte4` instead of `libghostty-vt` and a custom Cairo paint path — no Zig at build time.
- First run writes built-in defaults only; Ghostty config import is gone. Existing optionTerm `config.toml` keys are kept.
- Search uses VTE regex find next/previous (match-count UI removed).
- Session restore is layout + cwd only; scrollback dumps from ≤0.1.x are cleared on save/restore.
- `TERM=xterm-256color` (was `xterm-ghostty`).
- Various other removals and cleanups (Kitty graphics path, custom PTY paint profiler, and related crates)

## v0.1.14 · 31/07/2026

Program identity for nested CLIs, clipboard OSC 52, and optional scrollback persistence. This version was made for GNOME with a stable release channel on 31/07/2026 (v0.1.14).

- `TERM_PROGRAM` / `TERM_PROGRAM_VERSION` on every PTY so tools can recognise optionTerm; `XTVERSION` includes the package version.
- OSC 52 clipboard writes land in the GTK clipboard (or primary selection).
- Optional `window.session_restore_scrollback` stores pane VT dumps under `~/.option/terminal/scrollback/` (off by default — history can hold secrets).
- Various other small tweaks
