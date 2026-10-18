# Example — Large update split (architecture migration)

Scenario: migrating a Rust multi-surface app from manual state to a new settings crate, spanning 60 files across CLI + Desktop + core.

Bucket: **Large** → target ~25 commits (not padded).

## Chain plan (written before committing)

```text
1.  feat(core): add SettingsStore type and load/save errors
2.  feat(core): add SettingsStore persistence layer
3.  refactor(core): introduce SettingsStore trait for providers
4.  feat(core): implement SQLite provider for SettingsStore
5.  feat(core): implement JSON provider for SettingsStore
6.  test(core): cover SettingsStore round-trip and migrations
7.  refactor(cli): route config reads through SettingsStore trait
8.  feat(cli): migrate CLI settings to SettingsStore
9.  chore(cli): drop legacy CLI config structs
10. test(cli): update CLI config golden files
11. refactor(desktop): expose SettingsStore in app state
12. feat(desktop): bind settings UI to SettingsStore
13. fix(desktop): preserve unknown keys on settings save
14. refactor(desktop): remove old preferences serialization
15. test(desktop): settings integration smoke
16. feat(sdk): expose SettingsStore in public SDK
17. docs(sdk): document SettingsStore usage
18. feat(core): SettingsStore schema v2 migration
19. fix(core): handle partial schema v2 upgrades
20. test(core): migration edge cases from v1 profiles
21. chore: regen lockfiles after settings crate bump
22. chore(optionterm): adopt SettingsStore defaults
23. chore(optionmusic): adopt SettingsStore defaults
24. docs: update README settings section
25. chore: remaining dead-code cleanup from migration
```

## Why this works

- Dependency order: type → trait → providers → consumers → cleanup.
- Per-surface sections keep ownership obvious (core/cli/desktop/sdk).
- Lockfile + per-app adoption folds into single labelled commits, not one per file.
- No `part N/M` numbering; each subject stands alone.
- Every step compiles: consumers wired before old structs removed.
