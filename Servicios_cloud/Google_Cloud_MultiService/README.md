# Google Cloud Multi‑Service – Nivel 6 Edition

Proyecto unificado en GCP que integra **API Flask**, **BD SQLite (cero coste)** y **observabilidad básica** mediante registros y métricas de sistema. Pensado para ejecutarse en una **VM e2‑micro** dentro de *Google Cloud Free Tier* (o Cloud Shell) con **costo 0 €**.

## 👀 Objetivo
Simular una **tienda online** mínima: inventario expuesto por API, operaciones de lectura/escritura, copias de seguridad y monitorización básica.

## 🔧 Arquitectura (mínima y gratuita)
- **GCE** (Ubuntu/Debian) e2‑micro
- **API Flask** sirviendo con **gunicorn**
- **SQLite** local (`db/app.sqlite`) → 0 €
- **Logging**: sistema (journald) y logs de app
- **Backups**: `scripts/backup_db.sh` (rotación simple)

> Alternativas opcionales sin coste recurrente: **MongoDB Atlas Free** (externo a GCP).

## 📁 Estructura
```
Google_Cloud_MultiService
├─ README.md
├─ src/
│  ├─ api.py
│  └─ requirements.txt
├─ db/
│  └─ schema.sql
├─ scripts/
│  ├─ deploy.sh
│  ├─ startup.sh
│  └─ backup_db.sh
└─ docs/
   └─ capturas/  (coloca aquí las PNG)
```

## 🚀 Despliegue rápido (Cloud Shell o VM)
```bash
# 1) Clonar este repo (o subir carpeta) y entrar
# git clone <tu_repo> Google_Cloud_MultiService && cd Google_Cloud_MultiService

# 2) Preparar entorno
chmod +x scripts/*.sh
./scripts/deploy.sh

# 3) Arrancar servicio
sudo systemctl enable gcmulti.service
sudo systemctl start gcmulti.service

# 4) Ver estado y logs
sudo systemctl status gcmulti.service
journalctl -u gcmulti.service -f
```

## 🔐 Firewall / Red (VM Google Cloud)
- Abre el puerto **8000** TCP en la regla de firewall de la VM.
- Accede a `http://IP_PUBLICA:8000/health` para probar.

## 🧪 Endpoints
- `GET /health` → estado
- `GET /items` → listar inventario
- `POST /items` → crear (JSON: `name`, `price`, `stock`)
- `PUT /items/<id>` → actualizar
- `DELETE /items/<id>` → borrar

## 💾 Backups
Ejecuta manualmente o programa con `cron`:
```bash
./scripts/backup_db.sh
```

## 🖼️ Capturas sugeridas (en `docs/capturas/`)
1. VM e2‑micro creada (detalles de máquina)
2. Regla de firewall puerto 8000
3. `systemctl status gcmulti.service`
4. Prueba del endpoint `/health` en el navegador
5. Log en tiempo real con `journalctl -u gcmulti.service -f`

## 🧭 Siguientes pasos (extensiones del Nivel 6)
- HTTPS con **Let's Encrypt** (si dispones de dominio)
- **Dashboards** en Cloud Monitoring (CPU, red) dentro del free tier
- **CI/CD** con Cloud Build (gatillado manual) – opcional

---

© 2025-08-14 Ángel Mariano Álvarez López – Proyecto educativo/portfolio.
