#!/bin/bash

# Navegar a la ruta del proyecto
cd /home/angel/Porfolio/Servicios_Cloud/Despliegue_App_Flask_Cloud

# Activar el entorno virtual
source venv/bin/activate

# Ejecutar Gunicorn para servir la aplicación
gunicorn -b 0.0.0.0:5000 app:app

