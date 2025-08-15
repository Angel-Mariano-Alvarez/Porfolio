#!/usr/bin/env bash
set -euo pipefail

# Ruta del proyecto (ajusta si lo necesitas)
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
APP_DIR="${PROJECT_DIR}/src"
PY_ENV="/opt/gcmulti-venv"

# Paquetes base
sudo apt-get update -y
sudo apt-get install -y python3-venv python3-pip curl

# Virtualenv
sudo rm -rf "${PY_ENV}" || true
sudo python3 -m venv "${PY_ENV}"
sudo "${PY_ENV}/bin/pip" install --upgrade pip
sudo "${PY_ENV}/bin/pip" install -r "${APP_DIR}/requirements.txt"

# Crear usuario de servicio
id -u gcmulti &>/dev/null || sudo useradd -r -s /usr/sbin/nologin gcmulti

# Permisos mínimos
sudo chown -R gcmulti:gcmulti "${PROJECT_DIR}"
sudo chmod -R 755 "${PROJECT_DIR}"

# Service unit
SERVICE_FILE="/etc/systemd/system/gcmulti.service"
sudo bash -c "cat > ${SERVICE_FILE}" << 'UNIT'
[Unit]
Description=Google Cloud Multi-Service API (gunicorn)
After=network.target

[Service]
Environment=PYTHONUNBUFFERED=1
User=gcmulti
Group=gcmulti
WorkingDirectory=__WORKDIR__
ExecStart=__VENV__/bin/gunicorn -w 2 -b 0.0.0.0:8000 api:app
Restart=always

[Install]
WantedBy=multi-user.target
UNIT

sudo sed -i "s|__WORKDIR__|${APP_DIR}|g" "${SERVICE_FILE}"
sudo sed -i "s|__VENV__|${PY_ENV}|g" "${SERVICE_FILE}"

# Inicializar DB si no existe
python3 - <<'PY'
import os, sqlite3, pathlib
base = pathlib.Path("__APP_DIR__").resolve()
db_path = base.parent / "db" / "app.sqlite"
schema = (base.parent / "db" / "schema.sql").read_text()
db_path.parent.mkdir(parents=True, exist_ok=True)
with sqlite3.connect(db_path.as_posix()) as conn:
    conn.executescript(schema)
print("DB inicializada en:", db_path)
PY
sudo sed -i "s|__APP_DIR__|${APP_DIR}|g" /etc/systemd/system/gcmulti.service

# Recargar systemd
sudo systemctl daemon-reload

echo "Instalación completada. Usa: sudo systemctl start gcmulti.service"
