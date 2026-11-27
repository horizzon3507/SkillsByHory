# SkillsByHory

Agent skills by **Hory** — general-purpose agent skills, local-first. No daemon, no telemetry.

These are Cursor / Codex-style skills: folders with a `SKILL.md` plus optional examples. Point your agent skills path here, or copy individual skills into `~/.agents/skills/` / `~/.cursor/skills/`.

## Skills

| Skill | What it does |
|-------|----------------|
| [`hory-versioning`](skills/hory-versioning/) | Hory-style changelogs: `v` tags, channels, mixed `m` releases, surface sections. Examples for multi-surface, GNOME, and CLI apps. |
| [`breakable-commits`](skills/breakable-commits/) | Split one update into a clean chain of logical commits (3 → up to 100) without spam; split existing big commits and push the series to GitHub. |
| [`breakable-prs`](skills/breakable-prs/) | Split a big change into a sequence or stack of small PRs, each independently mergeable to main. |
| [`breakable-issues`](skills/breakable-issues/) | Turn a feature or milestone into a small set of tracker issues with acceptance criteria and dependency order — tasklists over issue-spam. |
| [`breakable-work`](skills/breakable-work/) | Orchestrator: plan a whole breakdown across issues → PRs → commits as one nested plan. |

## Install

**Copy into your personal skills dir** (picks up automatically in Cursor):

```bash
cp -a skills/hory-versioning skills/breakable-commits skills/breakable-prs skills/breakable-issues skills/breakable-work ~/.agents/skills/
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

Apache-2.0 unless a skill folder says otherwise.
