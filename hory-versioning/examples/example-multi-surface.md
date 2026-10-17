# Changelog

We follow [Semantic Versioning](https://semver.org/) and [Keep a Changelog](https://keepachangelog.com/). CLI and Desktop version separately.

<details>
<summary>To see more about versioning, expand this.</summary>

Every version string starts with `v` (required), e.g. `v0.2.10`, `v0.1.4-beta`.

Here the installable surfaces are **CLI** and **Desktop**. Other Option apps swap in their own names the same way — e.g. **GTK**, **Web**, **GNOME** — whatever you actually ship.

| Part | What you install | Example |
| --- | --- | --- |
| **CLI** | `optmusic` / `msc` in the terminal | `v0.2.10` |
| **Desktop** | the visual app | `v0.1.4-beta` |

A new CLI does not always mean a new Desktop app, and the other way around.

Sometimes one cut ships **both** surfaces. That is a **mixed release**: one tag with an `m` before the channel (ex: `v0.2.10m-beta`), and the notes break out each surface so a small touch on one side does not look equal to a large cut on the other.

Each release heading is the version and date (`## v0.2.10m-beta · 29/07/2026`); under it, a short summary ends with a plain sentence like: “This version was made for both desktop and CLI with a beta release channel on 29/07/2026 (v0.2.10m-beta).”

### What the Desktop suffix means

| Suffix | In plain words |
| --- | --- |
| **-alpha** | Very early. Expect missing pieces and lots of bugs. |
| **-beta** | Mostly there, but still rough. Fine to try; not the “official” install. |
| **-stable** | Ready for daily use. This is what we put on GitHub Releases and the AUR. |

We only call something **stable** when we mean it. While the desktop app is still settling, builds stay **beta**.

Older desktop builds (`v0.1.0`, `v0.1.1`) had no channel suffix. From `v0.1.2-beta` on, every desktop (and mixed) version includes one.

</details>

## v0.2.10m-beta · 29/07/2026

Desktop bundle id rename, with a matching CLI identity touch. This version was made for both desktop and CLI with a beta release channel on 29/07/2026 (v0.2.10m-beta).

### Desktop

- Bundle identifier is now `io.option.music` (was `com.aefireflylabs.optmusic`). Reinstall the `.desktop` file if an old install still shows up under the previous id.
- Various other small tweaks

### CLI

- Help / about text now mention the same `io.option.music` family id where relevant.
- Various other small tweaks

## v0.2.9m-beta · 29/07/2026

Shared config path move under `~/.option/music/`. This version was made for both desktop and CLI with a beta release channel on 29/07/2026 (v0.2.9m-beta).

### Desktop

- Settings UI and on-disk state read/write the new `~/.option/music/` layout (config, cache, playlists).
- First launch migrates leftover data from `~/option/music/` when present.
- Various other small tweaks

### CLI

- `msc` / `optmusic` resolve config and cache from `~/.option/music/` the same way as Desktop.
- Various other small tweaks

## v0.1.2-beta · 21/07/2026

Big Desktop beta: playlists, shelves, focus, download, playback tools, lyrics and tags. This version was made for desktop with a beta release channel on 21/07/2026 (v0.1.2-beta).

- Local playlists: create, rename, delete, add/remove tracks; import and export M3U. Same engine as `msc playlist …` on the CLI.
- Smart shelves for recent listening gaps: Played this week, No cover, Incomplete albums.
- Listening focus mode hides the chrome so you only get cover + scrub (Esc to leave).
- Desktop yt-dlp download dialog (search → select → download into the music folder).
- Pitch & speed, ReplayGain (`off` / `track` / `album`), offline lyrics, and light tag edit from the UI.
- Various other UI polish
