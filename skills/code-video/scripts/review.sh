#!/usr/bin/env bash
# Print a video's stream facts and write a contact sheet of evenly spaced frames,
# so the agent can look at what it rendered before delivering it.
# Usage: review.sh video.mp4 [sheet.png] [frames=12]
set -euo pipefail

VIDEO="$1"
SHEET="${2:-${VIDEO%.*}.sheet.png}"
N="${3:-12}"

ffprobe -v error -show_entries stream=codec_type,codec_name,width,height,r_frame_rate,pix_fmt:format=duration,size \
 -of default=noprint_wrappers=1 "$VIDEO"

DURATION=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$VIDEO")
COLS=4
ROWS=$(( (N + COLS - 1) / COLS ))
ffmpeg -v error -y -i "$VIDEO" \
 -vf "fps=$N/$DURATION,scale=480:-2,tile=${COLS}x${ROWS}:padding=6:margin=6" \
 -frames:v 1 "$SHEET"
echo "sheet=$SHEET"
