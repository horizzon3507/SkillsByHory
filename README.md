# optionSkills

Agent skills for the **Option** family (`optionTerm`, `optionMusic`, `optionFiles`, `opsh`, `optionSDK`, …).

These are Cursor / Codex-style skills: folders with a `SKILL.md` plus optional examples. Point your agent skills path here, or copy individual skills into `~/.agents/skills/` / `~/.cursor/skills/`.

Local-first. No daemon. No telemetry. Same spirit as the rest of Option.

## Skills

| Skill | What it does |
|-------|----------------|
| [`option-versioning`](option-versioning/) | Option-style changelogs: `v` tags, channels, mixed `m` releases, surface sections. Examples for multi-surface, GNOME, and CLI apps. |
| [`option-aur-packaging`](option-aur-packaging/) | Prepare, validate, migrate, and independently verify AUR packages, `PKGBUILD`, `.SRCINFO`, and package identities. |
| [`option-release`](option-release/) | Plan, cut, publish, and independently verify releases across CLI, Desktop, GNOME, Web, registries, GitHub, and AUR. |
| [`option-local-first`](option-local-first/) | Design local state, migrations, privacy boundaries, XDG paths, caches, sessions, and safe filesystem behavior. |

## Install

**Copy into your personal skills dir** (picks up automatically in Cursor):

```bash
cp -a option-versioning option-aur-packaging option-release option-local-first ~/.agents/skills/
# or
cp -a option-versioning option-aur-packaging option-release option-local-first ~/.cursor/skills/
```

**Or** keep this repo as the source of truth and symlink:

```bash
ln -s "$(pwd)/option-versioning" ~/.agents/skills/option-versioning
```

## Layout

```text
optionSkills/
  README.md
  option-versioning/
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
