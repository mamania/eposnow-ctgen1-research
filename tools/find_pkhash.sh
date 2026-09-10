#!/usr/bin/env bash
set -euo pipefail
TARGET="${1:-3720a9d9e03543ae4ad244d93d4b56ef588a499106c7d1f931f42704173a3414}"
ROOT="${2:-.}"
echo "Searching for ${TARGET:0:16} under $ROOT"
grep -Ril --binary-files=without-match "${TARGET:0:16}" "$ROOT" 2>/dev/null || true
echo
echo "Filename/text matches are not proof. Parse Firehose signing data and compare the full PK hash."
