---
name: option-gitignore
description: Create, standardize, and audit .gitignore files for Option-family repos across Rust, Tauri, Web/Bun/Vite, Prisma/SQLite, and GNOME/GTK surfaces. Use when adding a .gitignore to a new repo, normalizing an existing one to Option conventions, checking for leaked secrets or tracked junk, or when the user mentions Option gitignore style.
---

# Option Gitignore

One `.gitignore` style for the whole family: a shared base block plus stack sections, composed from the literal templates in `examples/`. Apps keep their lockfiles tracked; libraries/SDKs ignore `Cargo.lock`.

## File conventions

- Section header comments (`# Rust`, `# Secrets`), one blank line between sections, no trailing whitespace.
- Root-anchor repo-root paths: `/target/`, `/dist/` — never bare `target` or `dist`, which silently match directories at any depth.
- Trailing `/` for directories (`/node_modules/`); `*.ext` for file patterns; `**/name` only when the match must happen at any depth (`**/*.rs.bk`).
- Section order: stack build output → dependencies → secrets → logs → OS → editor → agent tooling → temp → `# Project`.
- Keep pre-existing project-specific entries (`/vte-dist/`, `/.cargo/config.toml`, `*.session-installed`); move them under `# Project` at the end instead of dropping them.
- Nested apps (`website/`, a web UI inside `src-tauri/`) get their own `.gitignore`; the root file covers repo-root noise plus root-anchored stack paths.

## Base block (always present)

```gitignore
# Secrets
.env
.env.*
!.env.example
!.env.*.example

# Logs
*.log

# OS
.DS_Store
Thumbs.db

# Editor
*.swp
*~
.idea/
.vscode/*
!.vscode/extensions.json

# Agent tooling
/.agents/
/.commandcode/
/.opencode/
command-code-session-*.html
skills-lock.json

# Temp
/.tmp/
```

The `.vscode/*` + `!.vscode/extensions.json` pair keeps shared extension recommendations tracked while ignoring local settings. If a repo intentionally tracks an agent directory (e.g. a skills repo shipping `.agents/`), remove that line for that repo only — verify rather than assume.

## Stack sections

Compose on top of the base block:

| Stack | Section entries | Lockfile rule |
|-------|-----------------|---------------|
| Rust app/bin | `# Rust` → `/target/`, `**/*.rs.bk` | `Cargo.lock` **tracked** — reproducible builds and AUR packaging depend on it |
| Rust lib/SDK | same, plus `/Cargo.lock` | ignored (optionSDK precedent) |
| Web (Bun/npm/Vite) | `# Dependencies` → `/node_modules/`; `# Build output` → `/dist/`, `/dist-ssr/`, `/out/`, `/.vite/`, `*.local` | `bun.lock` / `package-lock.json` **tracked** |
| Tauri | `# Tauri` → `/src-tauri/target/`, `/src-tauri/gen/`, `**/*.rs.bk`, `.cargo-target-clean` | `Cargo.lock` tracked |
| SQLite/Prisma | `# Local databases` → `*.db`, `*.db-journal`, `*.db-shm`, `*.db-wal`; `/src/generated/` when a generated Prisma client exists | — |

Framework extras, added only when the tooling is actually present: `/.output/`, `/.tanstack/` (TanStack), `/.next/` (Next), `/.turbo/`, `/coverage/`, `*.tsbuildinfo`.

## Templates

Literal files — copy the closest one and adapt:

| File | Use when |
|------|----------|
| [examples/gitignore-base](examples/gitignore-base) | Docs/config/skills repo with no build output (e.g. optionSkills) |
| [examples/gitignore-rust-app](examples/gitignore-rust-app) | Rust binary/GUI app — most of the family (opsh, optionTerm, optionFiles, …) |
| [examples/gitignore-rust-lib](examples/gitignore-rust-lib) | Rust library/SDK published to crates.io (optionSDK) |
| [examples/gitignore-web](examples/gitignore-web) | Bun/npm/Vite web app or website (optionDesign, optionMusic/website) |
| [examples/gitignore-tauri](examples/gitignore-tauri) | Tauri app — web frontend + `src-tauri/` Rust core |

## Workflow — new repo

1. Detect the stack: `Cargo.toml` (check `[package]` vs `[lib]`/published crate), `package.json`, `src-tauri/`, `prisma/`, nested `website/` or `web/` dirs.
2. Copy the closest template; add extra stack sections when the repo mixes surfaces (Rust app + `website/` → root file is rust-app; the website gets its own nested `.gitignore` from gitignore-web).
3. Append `# Project` entries for repo-specific artifacts already visible in `git status` untracked output or documented tooling.
4. Write `.gitignore`, then run the verification steps below.

## Workflow — audit/normalize existing

1. Detect the stack and read the existing `.gitignore`. List every current pattern before editing.
2. Preserve intentional project entries; migrate them to `# Project`.
3. Rewrite in canonical order: stack sections + base block. Fix anchoring (`target` → `/target/`), add missing secrets coverage (`.env`, `.env.*`), and remove dead patterns for tooling the repo doesn't use.
4. Check for files already tracked that the new file now ignores:

   ```bash
   git ls-files -ci --exclude-standard
   ```

   Untrack generated/noise hits with `git rm --cached <file>` so the ignore actually takes effect. If a hit is a secret (`.env`, keys), report it — removing it from history is a separate, explicit operation.
5. Scan for sensitive material already committed: `git ls-files | grep -iE '(^|/)\.env|\.(pem|key|p12)$|secrets?\.'` — report any hits instead of silently untracking.
6. Run verification below and report what changed section by section.

## Verification

```bash
git status --porcelain --ignored     # untracked vs ignored, sanity scan
git check-ignore -v <path>           # which rule matches a path
git ls-files -ci --exclude-standard  # tracked files matching ignore rules
```

A correct result: build output and dependency dirs show as ignored, lockfiles stay tracked, no `.env`/key material in `git ls-files`, and `git status` shows only files a human should commit.

## Common failure guards

- Never ignore `Cargo.lock` in an app or binary repo — Option apps, reproducible builds, and AUR `source` checksums rely on it. Libraries/SDKs are the only exception.
- Never ignore `bun.lock` / `package-lock.json` / `pnpm-lock.yaml`.
- `.env` and `.env.*` are always ignored; only `!.env.example`-style templates stay tracked.
- A tracked file is unaffected by `.gitignore` — adding the pattern alone does nothing; untrack it or leave it.
- Do not commit ignore patterns for tools nobody uses; sections should reflect the repo's real stack.
- Do not hide the change: when normalizing, show the diff and call out any file that becomes newly ignored.
