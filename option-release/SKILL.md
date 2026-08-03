---
name: option-release
description: Plan, cut, publish, and independently verify releases for Option-family projects across CLI, Desktop, GNOME, GTK, Web, Cargo, npm, GitHub Releases, and AUR. Use when bumping versions, creating CHANGELOG.md entries or tags, preparing mixed-surface releases, publishing artifacts, or checking whether a release actually reached its remote distribution channels.
---

# Option Release

Use this skill for the complete release lifecycle. Combine it with `$option-versioning` for changelog and tag semantics, and with `$option-aur-packaging` when AUR is a shipped surface.

## 1. Preflight and Surface Map

1. Inspect `AGENTS.md`, `VERSIONING.md`, `CHANGELOG.md`, manifests, workflows, packaging, desktop metadata, and install docs.
2. Map every shipped surface and its version source: CLI, Desktop/Tauri, GNOME/GTK, Web, library/SDK, and distribution packages.
3. Record the exact identity of each surface: repository, binary, package, bundle id, AUR package, tag, and artifact.
4. Check `git status`, branch, remote, current version, existing tags/releases, and authentication before editing or publishing.
5. Keep unrelated work untouched. Ask for direction if the requested version conflicts with existing artifacts or a live release.

## 2. Choose the Release Shape

Use `$option-versioning` and the closest existing example:

- Single surface: one version and surface-specific notes.
- Multiple surfaces with real user-facing changes on both: use the mixed `m` form before the channel, such as `v0.2.10m-beta`, with heavier work first.
- Do not bump or label a surface merely because it was present in the same repository. Use the smallest honest release.
- Keep registry/library versions plain SemVer unless the project explicitly adopts Option app-style channels.

## 3. Prepare the Release

1. Update every authoritative version file for the surfaces actually released. Do not replace a product's independent CLI/Desktop versioning with one guessed global version.
2. Add or update `CHANGELOG.md` in Option style, preserving historical facts and dates. Keep the summary human and list user-facing changes.
3. Update only documentation and metadata that must match the release: install commands, binary names, bundle identifiers, packaging, and workflow inputs.
4. Review the diff and run the project's validation commands. Typical checks include `cargo fmt --check`, `cargo test`, `cargo build --release`, `bun run typecheck`, `bun test`, and `bun run build`, but follow the repo's `AGENTS.md`.
5. Install or launch the produced artifact when possible. A successful compile is not visual QA, runtime QA, or proof that a stale installed binary was replaced.

## 4. Publish in Dependency Order

Use the project's existing workflow when one exists. The usual order is:

1. Commit the prepared release with a focused message.
2. Create and push the exact `v` tag required by the project.
3. Create the GitHub Release on that tag and confirm generated assets/source archives.
4. Update or trigger AUR packaging only after the authoritative tag/release exists.
5. Publish registries or platform artifacts that are part of the request.

Do not push, publish, delete, yank, or rename external resources unless the user requested that release action and the exact target is known.

## 5. Verify and Report

Verify each channel independently:

- Git: `git status`, commit hash, tag target, and `git ls-remote`.
- GitHub: release tag, `published` state, assets, and release URL using the repository's configured tooling.
- Registry: package name, version, and publication result.
- AUR: direct Git remote/package state and, when relevant, indexed web/RPC state.
- Local install: executable or app identity and `--version`/About output.

Report “prepared locally”, “committed”, “pushed”, “published”, and “indexed/visible” separately. Never call a release complete when any required channel is only assumed or unverified.
