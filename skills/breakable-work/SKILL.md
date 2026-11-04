---
name: breakable-work
description: Plan a full work breakdown across the breakable ladder — tracker issues, pull requests and commit chains — as one nested plan. Use when the user asks to break down a whole feature or milestone end to end ("break this down", "plan the whole thing") and the work spans more than one level.
license: Apache-2.0
---

# Breakable work

Plan a whole piece of work as **one nested breakdown**: issues at the value level, PRs at the merge level, commits at the history level. This skill owns the ladder and the consolidated plan — it owns no slicing rules. Each level's rules live in its own skill: `breakable-issues`, `breakable-prs`, `breakable-commits`.

## The ladder

```text
issue (what ships value, tracked) → owner: breakable-issues
 PR (what merges to main, reviewed) → owner: breakable-prs
 commit (what lands in history) → owner: breakable-commits
```

Each level cuts the same work at a different boundary, and smaller levels nest inside larger ones — a commit never crosses a PR boundary, a PR never crosses an issue boundary. If a planned cut does, the plan is wrong at the level above.

## Workflow

1. **Scope the ask** — what is the work, and which levels actually apply? Skip levels honestly: a repo with no tracker may not need the issue level; a solo change may be commits only. Say which levels you are using and why — never pad the ladder.
2. **Cut top-down** — issues first (value boundaries), then PRs inside each issue (merge boundaries), then commits inside each PR (logical units). Apply the owning skill's rules at each level. If a sibling skill is not installed, enforce that level's floor yourself: issues carry acceptance criteria, PRs merge to main alone, commits build.
3. **Check the nesting** — walk the plan once: does every child fit inside exactly one parent? Dependencies declared only at issue level (`blocked by`); merge order only at PR level; build order only at commit level.
4. **Present one plan** — a single nested outline, dependency arrows drawn at the level that owns them. Get sign-off on the whole plan before executing any level.

## Output format

```text
Milestone/epic: <name>
├─ Issue 1: <outcome> (blocked by: —)
│ ├─ PR 1: <mergeable unit> (base: main)
│ │ └─ commits: 3 planned
│ └─ PR 2: <mergeable unit> (base: main, after PR 1)
└─ Issue 2: <outcome> (blocked by: Issue 1)
 └─ PR 3: <mergeable unit> (base: main)
```

Fill down only to the level the user asked for — "issues only" stops at level one; "all the way down" fills commits under each PR.

## Hard rules

- Own the routing and the consolidated plan; own **no** slicing rules — when a level needs judgment (epic vs issue, stacked vs sequential, what merges alone), defer to that level's skill.
- Never duplicate a sibling's rules here — each breakable skill ships alone, and two copies of a rule drift.
- A missing level must be a stated decision, not an omission.
- Executing any level (creating issues, opening PRs, pushing commits) happens only after the whole plan is approved — each artifact is more public than the last.

## Examples

See [examples/example-full-breakdown.md](examples/example-full-breakdown.md) for a milestone planned across all three levels.

Related: `breakable-issues`, `breakable-prs`, `breakable-commits` — the three levels this plan routes to.
