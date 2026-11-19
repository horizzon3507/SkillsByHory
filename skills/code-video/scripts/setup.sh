#!/usr/bin/env bash
# Prepare the code-video environment: ffmpeg + a Python venv with the drawing stack.
# Idempotent. Override the location with CODE_VIDEO_HOME.
set -euo pipefail

HOME_DIR="${CODE_VIDEO_HOME:-$HOME/.code-video}"
VENV="$HOME_DIR/venv"

if ! command -v ffmpeg >/dev/null || ! command -v ffprobe >/dev/null; then
  if command -v brew >/dev/null; then brew install ffmpeg
  elif command -v apt-get >/dev/null; then sudo apt-get update -qq && sudo apt-get install -y -qq ffmpeg
  else echo "ffmpeg not found: install ffmpeg and re-run" >&2; exit 1
  fi
fi

mkdir -p "$HOME_DIR/work" "$HOME_DIR/outputs"
[ -x "$VENV/bin/python" ] || python3 -m venv "$VENV"
"$VENV/bin/python" -m pip install --quiet --upgrade pip
"$VENV/bin/python" -m pip install --quiet pillow numpy matplotlib

echo "python:  $VENV/bin/python"
echo "work:    $HOME_DIR/work"
echo "outputs: $HOME_DIR/outputs"
ffmpeg -version | head -1
