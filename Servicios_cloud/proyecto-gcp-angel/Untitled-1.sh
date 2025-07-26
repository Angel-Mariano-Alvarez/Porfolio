#!/bin/bash

# --- 1. Preparación del Sistema ---
# Actualizo la lista de paquetes e instala las herramientas necesarias:
# python3-pip: para instalar paquetes de Python
# python3-venv: para crear entornos virtuales
# git: para descargar el código desde GitHub
apt-get update
apt-get install -y python3-pip python3-venv git

# --- 2. Descargo de la Aplicación (con Sparse Checkout) ---
# Crea la carpeta donde vivirá la aplicación
mkdir /app
cd /app

# Inicializa un repositorio de Git vacío y habilita el sparse checkout
git init
git remote add -f origin https://github.com/Angel-Mariano-Alvarez/Porfolio.git
git config core.sparseCheckout true

# Le dice a Git que solo queriero la carpeta del proyecto
echo "Servicios_cloud/proyecto-gcp-angel/*" > .git/info/sparse-checkout

# Descarga el contenido de esa carpeta
git pull origin main

# --- 3. Instalación y Ejecución de la Aplicación ---
# Entra en la carpeta del proyecto que se ha descargado
cd Servicios_cloud/proyecto-gcp-angel/

# Crea un entorno virtual para no mezclar dependencias
python3 -m venv venv
source venv/bin/activate

# Instala las librerías necesarias listadas en  requirements.txt
pip install -r requirements.txt

# Instala Gunicorn, un servidor de producción más robusto que el de prueba de Flask
pip install gunicorn

# Ejecuta la aplicación en segundo plano en el puerto 80 (HTTP estándar)
# "app:app" se refiere al archivo app.py y a la variable app que hay dentro
gunicorn --bind 0.0.0.0:80 app:app --daemon