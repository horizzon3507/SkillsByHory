---
name: breakable-commits
description: Break one large update into a clean series of logical commits without spam. Use when the user asks to split a big change into multiple commits, commit "piece by piece", make atomic commits, or when a single commit would touch many files/features. Applies to pushes to GitHub (the user's), from 10 up to even 100 commits.
---

# Breakable commits

Turn one blob of work into a **chain of real commits** — each one compiling, meaningful, and reviewable. The point is a readable history, not tiny fragments. Never spam: no one-line "fix typo from previous commit" chains, no empty commits, no "wip" commits.

## Size buckets (decide first)

| Bucket | What it looks like | Target commits |
|--------|--------------------|----------------|
| **Simple** | a feature added to one area, a refactor touching a handful of files, a dependent-bump + code adjustment | 3–8 |
| **Medium** | feature touching several modules, multi-surface change, big dependency migration with follow-ups | 8–20 |
| **Large** | big feature across surfaces, architecture migration, mass mechanical change over dozens of files | 15–40, up to **100** when the change genuinely spans that much (e.g. repo-wide mechanical rewrite, per-module feature rollout) |

"Simple" means *simple update* — not necessarily small in lines. A 400-line change in one function can still be one commit if it's one logical step.

## Workflow

1. **Inventory** — `git status`, `git diff --stat` (uncommitted) or `git log -1 --format=%H` (one big commit to split). Classify the bucket.
2. **Plan the chain** — write the ordered commit list before committing anything. Order by dependency: shared types/helpers → interfaces → implementations → wiring → docs/changelog.
3. **Split rules**
   - One **logical unit** per commit: a feature block, a module's part of a migration, a test suite, a changelog entry.
   - Every commit must **build/package** on its own. If it can't, merge it with its dependency commit — never ship broken intermediates.
   - Mechanical change + hand-written change on the same lines → two commits (mechanical first).
   - Generated files, lockfiles: one commit, clearly labeled (`chore: regen lockfiles after X`).
4. **Slicing an already-made commit** — soft-reset (`git reset --soft HEAD~1`), then stage per unit with `git add` of the planned files (or `git add -p` inside files). Never force-push over shared branches without asking.
5. **Message style** — conventional-commit prefixes (`feat:`, `fix:`, `refactor:`, `test:`, `docs:`, `chore:`), imperative subject ≤ 72 chars, body only when it clarifies. No numbering in subjects (`feat: part 3/17` is spam — the history IS the list).
6. **Push** — push the chain as one block. If the user asked to push to their GitHub, push to their remote (`origin` or whichever the user names).

## Anti-spam checklist (hard rules)

- No commits with zero diff (`--allow-empty` only to mark a release/tag point and only if the user asks).
- No consecutive commits touching the same file for trivial reasons — fold them.
- Catch-all: leftover trailing bits after the chain → one final `chore:` commit, not a snowfall of singles.
- Commit count is a **consequence** of logical units, not a quota. If 100 is the right number for a repo-wide rewrite, fine; if a medium update needs 9, don't pad to 10.

## Examples

See [examples/example-large-split.md](examples/example-large-split.md) for a chain plan of a 40+ commit large update, and [examples/example-simple-split.md](examples/example-simple-split.md) for a 4-commit simple one.
