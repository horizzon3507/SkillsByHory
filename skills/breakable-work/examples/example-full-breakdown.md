# Example — Full-ladder breakdown

Scenario: the same usage-billing feature as the `breakable-issues` example — but the user asked for the whole plan, issue to commit.

Levels used: **all three** — shared tracker (issues), team review (PRs), clean history (commits).

## Nested plan

```text
Milestone: usage-based billing
├─ Issue 1: Meter billable events in the API (blocked by: —)
│ └─ PR: event schema + ingestion endpoint (base: main)
│ └─ commits: schema+migration · endpoint · tests
├─ Issue 2: Daily usage aggregation job (blocked by: Issue 1)
│ └─ PR: rollup worker + backfill (base: main)
│ └─ commits: rollup table · worker · backfill · tests
├─ Issue 3: Usage page in billing settings (blocked by: Issue 2)
│ ├─ PR: usage endpoint (base: main)
│ │ └─ commits: endpoint · serializer · tests
│ └─ PR: settings UI + empty state (base: main)
│ └─ commits: page scaffold · chart · empty state · tests
└─ Issue 4: Over-limit email (blocked by: Issue 2)
 └─ PR: threshold check + notification (base: main)
 └─ commits: check job · template · guard · tests
```

## Notes

- The nesting holds: every PR lives in exactly one issue, every commit in exactly one PR. If the settings UI had crept into Issue 2's PR, the plan would be wrong at issue level — fix the issue cut, not the PR.
- Levels skipped on purpose in other contexts: no tracker → start at PRs; solo repo with no review → issues + commits.
- Plan presented before anything was created — issues approved first, then PRs opened in dependency order.
