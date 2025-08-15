#!/usr/bin/env bash
# Metadata startup script para GCE (opcional).
# Descarga repo y lanza deploy automáticamente.
set -euo pipefail

REPO_URL="${REPO_URL:-}"
PROJECT_DIR="/opt/Google_Cloud_MultiService"

apt-get update -y
apt-get install -y git

if [[ -n "${REPO_URL}" ]]; then
  rm -rf "${PROJECT_DIR}" || true
  git clone "${REPO_URL}" "${PROJECT_DIR}"
  bash "${PROJECT_DIR}/scripts/deploy.sh"
  systemctl enable gcmulti.service
  systemctl start gcmulti.service
fi
