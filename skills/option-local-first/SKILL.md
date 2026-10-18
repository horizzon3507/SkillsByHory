---
name: option-local-first
description: Design, review, migrate, and validate local-first state for Option-family apps, including configuration, data, cache, sessions, filesystem behavior, privacy boundaries, XDG paths, schema migrations, and safe recovery. Use when adding persistence, choosing storage paths, migrating legacy state, integrating local files, handling secrets, or reviewing telemetry and network behavior.
license: Apache-2.0
---

# Option Local First

Keep the user's data on their machine, make storage paths predictable, and make migrations recoverable. Network access, telemetry, background daemons, and destructive filesystem effects require an explicit product decision; they are never implied by “local-first”.

## Storage Model

Separate state by purpose:

- Config: user-editable preferences and stable settings.
- Data: user-owned content, libraries, playlists, notes, or indexes that must survive cache cleanup.
- Cache: disposable downloads, thumbnails, previews, and derived data.
- Runtime/session: locks, temporary state, PTY sessions, and restore data with a clear retention policy.
- Logs: minimal diagnostics; never include tokens, passwords, private keys, or full sensitive paths unless explicitly requested.

Prefer the Option family layout `~/.option/<app-slug>/`, unless the product already documents an XDG-native layout. If XDG variables are supported, honor `XDG_CONFIG_HOME`, `XDG_DATA_HOME`, `XDG_CACHE_HOME`, and `XDG_STATE_HOME` consistently. Keep paths configurable where the app handles user-owned content such as music or documents.

## Persistence Rules

1. Create parent directories deliberately with appropriate permissions; do not silently fall back to a repository, `/tmp`, or a cloud path for durable user data.
2. Write important files atomically: write a temporary sibling file, flush when appropriate, then rename. Do not truncate the only good copy before a successful write.
3. Handle missing, empty, malformed, and old files with safe defaults and actionable diagnostics.
4. Keep schema/version markers close to persisted data and make migrations idempotent.
5. Preserve unknown settings when feasible, and retain a recoverable backup before a migration that rewrites user data.
6. Make cleanup scope explicit. Cache cleanup must not delete user data, and “delete” should use the host Trash/recycle path when the platform supports it unless permanent deletion is explicitly requested.

## Privacy and Security

- Default to no telemetry, analytics, crash upload, daemon, or network request.
- If a network feature is required, document the endpoint, data sent, opt-in/opt-out behavior, offline behavior, and failure mode before implementing it.
- Keep secrets out of source, logs, crash reports, command lines, shell history, and user-visible diagnostics.
- Use explicit process arguments and safe path handling; never interpolate untrusted filenames into shell code.
- Treat `HttpOnly`/opaque sessions, API credentials, and local tokens as secrets even when they are stored on disk.
- Avoid permissions broader than necessary and explain any access to user directories, audio devices, graphics protocols, or external processes.

## Migration Workflow

1. Identify the old and new paths/formats and inspect identity before touching data.
2. Count and classify affected files or records. Never claim migration success from a process exit code alone.
3. Use a dry run or temporary fixture when possible, then copy/move rather than destroy.
4. Keep a backup or rollback path until the new state has been read back successfully.
5. Make the migration repeatable: a second run should be a no-op or safely converge.
6. Validate permissions, file counts, representative contents, app startup, and the old-path behavior after migration.

## Acceptance Checklist

- Fresh start works with no pre-existing state.
- Existing valid state round-trips without loss.
- Malformed or partial state fails safely and gives a useful recovery path.
- A migration handles old, new, and already-migrated layouts.
- Cache removal leaves user data intact.
- Offline operation remains usable for local features.
- No secret or private content appears in logs or command output.
- Tests use isolated temporary directories and do not touch the real home directory.
