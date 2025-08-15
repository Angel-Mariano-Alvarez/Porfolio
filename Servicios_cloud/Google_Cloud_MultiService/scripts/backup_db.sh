#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DB="${PROJECT_DIR}/db/app.sqlite"
DST_DIR="${PROJECT_DIR}/db/backups"
mkdir -p "${DST_DIR}"
ts=$(date +'%Y%m%d_%H%M%S')
cp "${DB}" "${DST_DIR}/app_${ts}.sqlite"
echo "Backup creado en ${DST_DIR}/app_${ts}.sqlite"
