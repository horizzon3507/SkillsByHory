# Example — Simple update split

Scenario: adding a `--json` output flag to a CLI, ~8 files touched.

Bucket: **Simple** → 4 commits.

## Chain plan

```text
1. feat(cli): add --json argument plumbing          (arg parser + struct field)
2. feat(cli): emit JSON output for status command   (serializer + flag branch)
3. test(cli): cover --json for status and list      (tests only, they use step 1+2)
4. docs: document --json flag                       (README + changelog line)
```

## Notes

- Plumbing (flag) and behavior (output) are separate logical units — three files each, one commit each.
- Step 2 alone would compile but produce no output; step 3 depends on both. Never test before behavior.
- 4 commits, not 8 — one per file would be spam. Commit count follows units, not file count.
