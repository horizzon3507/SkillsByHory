# Example — Medium feature split into PRs

Scenario: project-level API tokens — new table, backend endpoints, settings UI, CLI flag. ~1,300 changed lines.

Bucket: **Medium** → 4 PRs. Sequential, not stacked — each merges to main independently.

## PR chain

```text
PR 1: feat(db): api_tokens table + migration       (base: main)      ~200 lines
PR 2: feat(api): token CRUD endpoints              (base: main)      ~350 lines
PR 3: feat(settings): token management UI          (base: main)      ~500 lines
PR 4: feat(cli): --token flag + login flow         (base: main)      ~250 lines
```

## Notes

- Cut along merge boundaries, not evenly — PRs 1–3 each merge alone; the UI ships without the CLI and nothing breaks.
- Not stacked: PR 3 does not need PR 4's code, and reviews can land in any order after PR 2. Stacking would only buy a rebase cascade.
- PR 4 goes last and could sit as a draft while 1–3 are in review — four open PRs at once is four notification threads.
- If the UI had to land dark, PR 3 would carry a feature flag instead of splitting into "dead UI" + "wire it up" PRs.
