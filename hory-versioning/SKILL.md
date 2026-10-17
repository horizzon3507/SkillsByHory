---
name: hory-versioning
description: Apply Option-family changelog and versioning style (v tags, alpha/beta/stable channels, mixed m releases, surface sections, human summary lines). Use when creating or updating CHANGELOG.md / VERSIONING.md, cutting a release, or the user mentions Option-style versioning, channels, or mixed releases.
---

# Option versioning

Write and migrate changelogs in the **Option** family style. Match the closest example below; adapt surface names to the project (CLI, Desktop, GNOME, Web, GTK, …).

## Examples (read before writing)

| File | Shape | Use when |
|------|--------|----------|
| [examples/example-multi-surface.md](examples/example-multi-surface.md) | Multi-surface (CLI + Desktop) with `m` | App ships more than one installable surface |
| [examples/example-gnome.md](examples/example-gnome.md) | Single surface **GNOME** | GTK / desktop-only app (e.g. optionTerm) |
| [examples/example-cli.md](examples/example-cli.md) | Single surface **CLI** | Terminal-only app (e.g. optionFiles) |

**Always open the matching example** and mirror its structure (intro, `<details>` versioning blurb, headings, summary line, bullets). Do not invent a parallel layout.

## Workflow

1. **Detect surfaces** from the repo (binaries, desktop app, web, GTK, …). Pick multi-surface / GNOME / CLI example accordingly.
2. **Locate changelog** — prefer `CHANGELOG.md` at repo root. If missing, create one from the chosen example (replace product-specific names/paths with this project’s).
3. **If a changelog already exists** — keep historical facts; rewrite headings and entry shape to Option style. Preserve dates; convert to `DD/MM/YYYY` in headings. Add or refresh the top intro + `<details>` block to match the example (project surfaces, not Music/Term/Files copy-paste blindly).
4. **New release entry** — prepend under the details block:
   - Heading: `## vX.Y.Z[m][-channel] · DD/MM/YYYY`
   - One short summary sentence ending in human prose naming surface(s), channel, date, and tag again.
   - Mixed (`m`): `###` sections per surface, **heavier work first**.
   - Single surface: bullets only (no `###` surface split).
   - Detailed feature bullets; collapse noise as `Various other small tweaks` / `Various other bug fixes` / `Various other UI polish` (at most one catch-all per surface section or entry).
5. **Align versions** — update `Cargo.toml` / `package.json` / tags to the numeric (and channel) form the project already uses for artifacts; changelog tags always include the leading `v`.
6. **Do not** paste an agent rule checklist into the changelog. The public doc stays user-facing like the examples.

## Tag shape (agent checklist)

- Always `v` + SemVer.
- Channel: `-alpha` | `-beta` | `-stable` when the project uses channels (Desktop/GNOME/mixed).
- Mixed: insert `m` before the channel (`v0.2.10m-beta`) only when more than one surface truly changed; split notes per surface so weight is obvious.
- Prefer a single-surface cut when the other surface only “came along” with no real user-facing change.

## Libraries / SDKs

Plain SemVer on the package registry (e.g. crates.io). No surfaces, no `m`, no channel theater in the changelog unless the user explicitly wants Option app-style docs anyway.
