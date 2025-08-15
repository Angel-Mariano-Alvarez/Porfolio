cat > scripts/backup_db.sh <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

# Si no se ejecuta como 'gcmulti', relanzar el propio script como 'gcmulti'
if [[ "$(id -un)" != "gcmulti" ]]; then
  exec sudo -u gcmulti bash "$0" "$@"
fi

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DB="${PROJECT_DIR}/db/app.sqlite"
DST_DIR="${PROJECT_DIR}/db/backups"

mkdir -p "${DST_DIR}"
ts=$(date +'%Y%m%d_%H%M%S')
cp "${DB}" "${DST_DIR}/app_${ts}.sqlite"
echo "Backup creado en ${DST_DIR}/app_${ts}.sqlite"
EOF

chmod +x scripts/backup_db.sh