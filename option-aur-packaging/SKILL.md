---
name: option-aur-packaging
description: Prepare, update, validate, migrate, and publish Arch User Repository packages for Option-family apps, including PKGBUILD, .SRCINFO, release-tarball hashes, package identity, GitHub Actions, and AUR rename workflows. Use when an Option app adds or changes AUR packaging, cuts a release distributed through AUR, changes binary or repository names, or needs independent verification of an AUR publication.
---

# Option AUR Packaging

Treat AUR packaging as a distribution surface with its own identity and verification. Do not infer the AUR package name from the repository, Cargo package, npm package, or executable without checking the repository's packaging files.

## Preflight

1. Inspect the project before editing:
   - `Cargo.toml`, `package.json`, workspace manifests, binaries, and install documentation.
   - `packaging/aur/PKGBUILD`, `.SRCINFO`, `bump.sh`, `publish.sh`, and `.github/workflows/*aur*` when present.
2. Build an identity table: product name, GitHub repository, release tag, source archive URL, Cargo/npm package, executable, AUR `pkgname`, `provides`, `conflicts`, and `replaces`.
3. Preserve deliberate differences. A registry package may have a different name from the binary and AUR package.
4. Check the working tree, current branch, remote, current version, and whether the intended tag/release already exists. Do not overwrite unrelated user changes.

## Update an Existing Package

1. Confirm the release tag and source archive URL. Prefer the actual GitHub tag archive used by the release rather than a moving branch.
2. Update `pkgver`, `pkgrel`, `source`, dependencies, optional dependencies, install files, and checksums in `PKGBUILD`.
3. Regenerate `.SRCINFO` with `makepkg --printsrcinfo > .SRCINFO` from the package directory when `makepkg` is available. Do not hand-edit generated metadata unless there is no alternative.
4. Run packaging checks:
   - `bash -n` for shell scripts.
   - `makepkg --printsrcinfo` and a source/checksum validation when available.
   - `namcap PKGBUILD` and the built package when available.
   - The project's own format, test, release-build, and install smoke checks.
5. Check that the installed command, `--version`, desktop entry, and documentation use the intended identity.

## Publish Safely

1. Make the GitHub tag/release and release asset state authoritative before updating AUR metadata.
2. If the project uses automation, prefer its existing workflow and required secrets over a new one-off script.
3. Push only when the user has requested publication and credentials/remote state are confirmed.
4. Verify independently after publication using the direct AUR Git remote and, when useful, the AUR web/RPC view. A local commit or a successful workflow dispatch is not proof that the package is published or indexed.
5. Report exact package name, version, commit, remote, and verification result. Separate “prepared locally”, “pushed”, and “indexed/visible”.

## Rename or Migrate an AUR Package

Treat an AUR rename as a migration, not a GitHub-style rename:

- Publish the new package under the intended name with correct metadata.
- Use `provides`, `conflicts`, and `replaces` only when they accurately describe compatibility.
- Preserve the old package until the official merge/deletion path is completed.
- Verify both old and new package state before claiming the rename is finished.
- Never delete an AUR repository or package as a shortcut without explicit authorization and a verified target.

## Common Failure Guards

- Never use a moving branch as a release source when a tag is intended.
- Never assume `pkgname`, executable name, Cargo package name, and GitHub repository name match.
- Never claim “AUR released” from a local `PKGBUILD`, a GitHub release, or an unverified workflow alone.
- Never put credentials, tokens, or private SSH material in the skill, repository, logs, or generated package files.
