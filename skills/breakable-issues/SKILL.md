---
name: breakable-issues
description: Break a large feature or milestone into a small set of well-scoped tracker issues with acceptance criteria and explicit dependencies. Use when the user asks to turn a big task into GitHub/Linear issues, plan a milestone, or split work that would otherwise be one untracked mega-issue.
license: Apache-2.0
---

# Breakable issues

Turn one big ask into a **small set of issues** — each one independently valuable, scoped to a few days of work, with acceptance criteria and declared dependencies. Issues are published artifacts: they notify people, get triaged, and live in a shared tracker. Default to fewer; a checklist item is not an issue.

## Size buckets (decide first)

| Bucket | What it looks like | Target |
|--------|--------------------|--------|
| **Simple** | one feature, one owner, days of work | **1 issue** — often a single issue with a tasklist, not a split |
| **Medium** | feature crossing surfaces or phases, sequential dependencies | 3–7 issues, tasklists for the small steps |
| **Large** | milestone, multi-surface rollout, work for more than one cycle | 8–15 issues under **1 epic**, rarely more |

When in doubt, go down a bucket. Splitting later is cheap; un-creating 12 noisy issues is not.

## Epic, issue or tasklist (decide per unit)

- **Epic** — only when the work spans more than one cycle or more than one owner. An epic with 3 children is just an issue wearing a hat.
- **Issue** — a unit that ships value on its own and can be picked up without asking "where do I start". It needs a different owner, parallel scheduling or a hard dependency boundary to justify existing.
- **Tasklist item** — anything under roughly half a day, or a step that only makes sense inside its parent's context. `Issue: rename the prop` is spam; `- [ ] rename the prop` inside the parent issue is not.

## Workflow

1. **Inventory** — read the feature/milestone ask. List the units of work, the surfaces they touch and the dependencies between them. Classify the bucket.
2. **Draw the dependency graph first** — every issue gets `blocked by` where needed. Parallel-independent units may become sibling issues; strictly sequential steps usually collapse into one issue with a tasklist.
3. **Scope each issue** — title states the outcome, never the step (`Add usage export to billing settings`, not `Billing part 2/9`). Body: one paragraph of context, acceptance criteria as a checklist, explicit `blocked by`/`blocks` lines. No invented priorities, assignees, sprints or milestones — placeholder or ask.
4. **Write the plan before creating anything** — output the full set as markdown: titles, bodies, dependency arrows, which issues hang under the epic. Creating is step two.
5. **Create only after approval** — issues are published: they notify watchers and land in triage queues. With go-ahead, use `gh issue create` (or the tracker's CLI/API) in dependency order, linking children to the epic.

## Anti-spam checklist (hard rules)

- Sub-half-day task → checklist item, never an issue.
- No issues that exist only to be closed by the next one — fold sequential steps into one issue.
- No title numbering (`part 3/9`) — the epic's tasklist and the `blocked by` graph carry the order.
- No invented assignees, priorities, sprints or milestones.
- Issue count is a **consequence** of value boundaries, not a quota. A medium feature that is honestly 2 issues gets 2, not the bucket minimum.

## Examples

See [examples/example-milestone-split.md](examples/example-milestone-split.md) for a medium feature planned as 5 issues with tasklists — and no epic.

Related: `breakable-prs` cuts the same work at merge boundaries, `breakable-commits` at history boundaries, `breakable-work` plans all three levels at once.
