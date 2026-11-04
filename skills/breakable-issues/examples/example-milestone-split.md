# Example — Medium feature planned as issues

Scenario: usage-based billing — meter events in the API, aggregate daily, usage page in settings, over-limit email. One owner, fits one cycle, GitHub issues.

Bucket: **Medium** → 5 issues. **No epic** — one cycle and one owner means the milestone label is enough.

## Issue plan

```text
1. Meter billable events in the API (blocked by: —)
 tasklist: event schema · ingestion endpoint · idempotency
2. Daily usage aggregation job (blocked by: 1)
 tasklist: rollup table · worker · backfill script
3. Usage page in billing settings (blocked by: 2)
 tasklist: usage endpoint · chart · empty state
4. Over-limit email notification (blocked by: 2)
 tasklist: threshold check · template · send-once guard
5. Docs + changelog (blocked by: 3, 4)
```

## Notes

- Issue 1 carries the schema — everything hangs off it, so it goes first and blocks 2–4.
- "Add the prop", "write the test", "update the type" never became issues — they live in tasklists where they belong.
- No epic: one owner, one cycle. The milestone label does the grouping for free.
- Created only after this plan is approved — `gh issue create` in order, cross-linked with `blocked by`.
