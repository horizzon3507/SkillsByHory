---
name: breakable-prs
description: Split a large change into a sequence or stack of small pull requests where each is independently mergeable to main. Use when the user asks to break work into reviewable PRs, build stacked PRs, split a big diff for review, or when one PR would be too large to review honestly.
license: Apache-2.0
---

# Breakable PRs

Turn one big diff into a **chain of reviewable PRs** — each one independently mergeable to main, green on CI, and small enough that a reviewer can actually read it. PRs are the most expensive artifact in the chain: they ping reviewers, burn CI and queue for merge. Split along merge boundaries, never along line counts.

## Size buckets (decide first)

| Bucket | What it looks like | Target PRs |
|--------|--------------------|------------|
| **Simple** | a change that fits one honest review (~≤400 meaningful lines, one concern) | **1 PR** — splitting is the smell, not the cure |
| **Medium** | multi-surface change, layered feature, migration with a mechanical part | 2–5 |
| **Large** | architecture change, repo-wide rollout, feature that must land dark | 5–12, split by boundary or flag |

Reviewable size beats file count: a 600-line generated lockfile diff reviews fine; 300 lines of intertwined logic does not. Treat **≤400 meaningful lines** as the ceiling, not the goal.

## Sequential or stacked (decide second)

- **Sequential into main** — default. Each PR branches off main and merges on its own; every state of main stays clean. Use whenever the next PR does not need the previous PR's code.
- **Stacked** — PR N branches off PR N-1 (`gh pr create --base <prev-branch>`). Only when a later PR genuinely depends on earlier code **and** reviews move fast. Warn once: feedback on PR 1 means rebasing the whole stack. Never stack more than ~5 without asking.
- **Feature-flagged single PR** — when the split exists only to hide unfinished work, prefer one PR with the new path behind a flag over three PRs of dead code.

## Workflow

1. **Inventory** — `git status` / diff the change. Find the merge boundaries: schema/migrations → backend/API → client/frontend → wiring → docs. Classify the bucket.
2. **Plan the chain** — ordered PR list before branching: title, base, contents, why it merges alone.
3. **Slice rules**
   - Every PR must **merge to main independently**: CI green, no broken intermediate state, reviewable without reading the next PR.
   - Mechanical change (codemod, rename, regen) → its own PR, before the hand-written one touching the same lines.
   - Generated files and lockfiles → their own clearly-labeled PR, or folded into the one that caused them.
   - No PR that only adds unreachable code — hide it behind a flag or merge it with the PR that wires it.
4. **Create the chain** — first PR ready for review; later PRs as **drafts** (stacked on their base, or held locally). Note merge order in each PR body.
5. **Keep the chain alive** — when an earlier PR changes in review, rebase dependents and say so. Never leave a stale stack silently.

## Anti-spam checklist (hard rules)

- No splitting by file count or line count alone — boundaries come from what merges alone.
- No PR that breaks main if merged without its siblings.
- No chain where PR 4 is "fix what PR 2 broke" — fix PR 2.
- Draft or hold later PRs — opening 8 PRs at once notifies 8 times and rots daily.
- PR count is a **consequence** of merge boundaries, not a quota.

## Examples

See [examples/example-stacked-split.md](examples/example-stacked-split.md) for a medium feature cut into a 4-PR sequential chain.

Related: `breakable-commits` splits inside each PR, `breakable-issues` cuts the same work at value boundaries, `breakable-work` plans all three levels at once.
