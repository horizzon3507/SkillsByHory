# SkillsByHory

Agent skills for the **Hory** family (`yourTerm`, `yourMusic`, `yourFiles`, `horysh`, `yourSDK`, …).

These are Cursor / Codex-style skills: folders with a `SKILL.md` plus optional examples. Point your agent skills path here, or copy individual skills into `~/.agents/skills/` / `~/.cursor/skills/`.

Local-first. No daemon. No telemetry. Same spirit as the rest of Hory.

## Skills

| Skill | What it does |
|-------|----------------|

## Install

**Copy into your personal skills dir** (picks up automatically in Cursor):

```bash
cp -a ~/.agents/skills/
# or
cp -a ~/.cursor/skills/
```

**Or** keep this repo as the source of truth and symlink:

```bash
```

## Layout

```text
 README.md
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

Apache-2.0 — same as the Hory family apps, unless a skill folder says otherwise.
