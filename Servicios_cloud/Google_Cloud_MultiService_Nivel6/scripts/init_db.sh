cd ~/Porfolio/Servicios_cloud/Google_Cloud_MultiService_Nivel6

cat > scripts/init_db.sh <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DB="${PROJECT_DIR}/db/app.sqlite"
SCHEMA="${PROJECT_DIR}/db/schema.sql"
sudo chown -R gcmulti:gcmulti "${PROJECT_DIR}/db"
sudo -u gcmulti python3 - <<PY
import sqlite3, pathlib
db = pathlib.Path("${DB}")
schema = pathlib.Path("${SCHEMA}").read_text()
db.parent.mkdir(parents=True, exist_ok=True)
with sqlite3.connect(db.as_posix()) as conn:
    conn.executescript(schema)
print("DB inicializada en:", db)
PY
EOF

chmod +x scripts/init_db.sh
