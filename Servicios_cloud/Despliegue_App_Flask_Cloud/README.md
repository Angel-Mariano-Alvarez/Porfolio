# Despliegue App Flask en Google Cloud

## Descripción del Proyecto

Este proyecto forma parte del curso **"Servicios Cloud" de FUNDAE**, y corresponde a los retos 7, 8 y 9 del nivel 4. Se ha desarrollado una aplicación Flask y se ha desplegado con éxito en **Google Cloud Platform (GCP)**, usando una **instancia VM**, una **plantilla** y un **grupo de instancias gestionado**, todo ello mediante la configuración de **startup scripts** y la apertura de puertos adecuados.

Este README documenta de forma organizada todos los pasos realizados y se apoya en capturas de pantalla agrupadas en la carpeta `Capturas_pantalla`.

## Estructura del Proyecto

Despliegue_App_Flask_Cloud/
│
├── Capturas_pantalla/
│   ├── 01-startup_sh.PNG
│   ├── 02-configuracion_instancia.png
│   ├── 03-so_firewall.PNG
│   ├── 04-verificacion_archivos.png
│   ├── 05-instancia_creada.PNG
│   ├── 06-ejecucion_startup_sh.png
│   ├── 07-verificacion_navegador.png
│   ├── 08.01_nombre_region_plantilla.PNG
│   ├── 08.02_maquina_plantilla.PNG
│   ├── 08.03_firewall_plantilla.PNG
│   ├── 08.03_script_plantilla.PNG
│
├── app.py
├── requirements.txt
├── startup.sh
└── README.md

## Pasos Realizados

### 1. Preparación del entorno

- Se creó una carpeta en la instancia `/home/angel/app` y se subieron los archivos:
  - `app.py`: aplicación Flask.
  - `requirements.txt`: con las dependencias necesarias (`Flask`, `gunicorn`).
  - `startup.sh`: script de arranque para lanzar automáticamente la app con Gunicorn.

📸 Captura recomendada: `01-startup_sh.PNG`

### 2. Creación de la instancia

- Se creó una **VM en GCP** con sistema operativo Debian y tipo `e2-micro`.
- Se activó el **acceso HTTP** desde el firewall.
- Se comprobó que los archivos estuvieran bien ubicados dentro de la instancia.

📸 Capturas recomendadas:
- `02-configuracion_instancia.png`
- `03-so_firewall.PNG`
- `04-verificacion_archivos.png`
- `05-instancia_creada.PNG`

### 3. Ejecución y prueba de la app

- Se instaló manualmente el entorno:
  ```bash
  sudo apt update
  sudo apt install python3-pip
  pip install flask gunicorn
  ```
- Se dio permiso de ejecución al script y se ejecutó:
  ```bash
  chmod +x startup.sh
  ./startup.sh
  ```
- Se verificó la ejecución de la app accediendo desde el navegador a la IP externa.

📸 Capturas recomendadas:
- `06-ejecucion_startup_sh.png`
- `07-verificacion_navegador.png`

### 4. Automatización del despliegue con plantilla

- Se creó una **plantilla de instancia** especificando:
  - Nombre, zona y tipo de máquina
  - Script de inicio completo
  - Puertos abiertos vía firewall
- Se revisó que el script estuviera copiado completo en la plantilla.

📸 Capturas recomendadas:
- `08.01_nombre_region_plantilla.PNG`
- `08.02_maquina_plantilla.PNG`
- `08.03_firewall_plantilla.PNG`
- `08.03_script_plantilla.PNG`

### 5. Despliegue final con grupo de instancias gestionado

- Se configuró un grupo de instancias a partir de la plantilla.
- Se comprobó el estado del grupo, y que la app se lanzaba automáticamente.
- Se accedió desde el navegador para validar el funcionamiento.

ℹ️ Se decidió **no añadir capturas de esta fase** al porfolio por su carácter repetitivo.

## Notas para el porfolio

- Este proyecto demuestra la capacidad de desplegar una aplicación web real en GCP.
- Las capturas más relevantes han sido seleccionadas y nombradas siguiendo la estructura lógica del despliegue.
- El script `startup.sh` y el uso de Gunicorn aseguran un despliegue robusto y profesional.

## Estado del Proyecto

- [x] Proyecto Finalizado
- [x] Validado el funcionamiento desde navegador
- [x] Limpieza de recursos (instancias, plantillas, grupos)

## Autor

Ángel Mariano Álvarez López  
📧 angelmarianoalvarez@gmail.com  
🔗 [GitHub Porfolio](https://github.com/Angel-Mariano-Alvarez/Porfolio)

