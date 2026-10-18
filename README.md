# SkillsByHory

Agent skills for the **Option** family (`optionTerm`, `optionMusic`, `optionFiles`, `opsh`, `optionSDK`, …).

These are Cursor / Codex-style skills: folders with a `SKILL.md` plus optional examples. Point your agent skills path here, or copy individual skills into `~/.agents/skills/` / `~/.cursor/skills/`.

Local-first. No daemon. No telemetry. Same spirit as the rest of Option.

## Skills

| Skill | What it does |
|-------|----------------|
| [`hory-versioning`](skills/hory-versioning/) | Option-style changelogs: `v` tags, channels, mixed `m` releases, surface sections. Examples for multi-surface, GNOME, and CLI apps. |
| [`option-aur-packaging`](skills/option-aur-packaging/) | Prepare, validate, migrate, and independently verify AUR packages, `PKGBUILD`, `.SRCINFO`, and package identities. |
| [`option-release`](skills/option-release/) | Plan, cut, publish, and independently verify releases across CLI, Desktop, GNOME, Web, registries, GitHub, and AUR. |
| [`option-local-first`](skills/option-local-first/) | Design local state, migrations, privacy boundaries, XDG paths, caches, sessions, and safe filesystem behavior. |
| [`option-gitignore`](skills/option-gitignore/) | Create, normalize, and audit `.gitignore` files across the family's Rust, Tauri, Web, and SQLite stacks. |
| [`breakable-commits`](skills/breakable-commits/) | Split one update into a clean chain of logical commits (3 → up to 100) without spam; split existing big commits and push the series to GitHub. |

## Install

**Copy into your personal skills dir** (picks up automatically in Cursor):

```bash
cp -a skills/hory-versioning skills/option-aur-packaging skills/option-release skills/option-local-first skills/option-gitignore skills/breakable-commits ~/.agents/skills/
# or
cp -a skills/hory-versioning skills/option-aur-packaging skills/option-release skills/option-local-first skills/option-gitignore skills/breakable-commits ~/.cursor/skills/
```

**Or** keep this repo as the source of truth and symlink:

```bash
ln -s "$(pwd)/skills/hory-versioning" ~/.agents/skills/hory-versioning
```

## Layout

```text
SkillsByHory/
  README.md
  skills/hory-versioning/
    SKILL.md
    examples/
      example-multi-surface.md
      example-gnome.md
      example-cli.md
```

## Adding a skill

1. Initialize the skill with the shared `skill-creator` workflow.
2. Create `skill-name/SKILL.md` with YAML frontmatter (`name`, `description`).
3. Put shared fixtures under `skill-name/examples/` when the agent should mirror a template.
4. List it in the table above and validate it with `quick_validate.py`.

## License

Apache-2.0 — same as the Option family apps, unless a skill folder says otherwise.
