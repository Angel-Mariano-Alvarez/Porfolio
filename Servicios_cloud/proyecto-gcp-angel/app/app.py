# Importamos las herramientas necesarias: Flask para la web y socket para el nombre del host.
from flask import Flask, jsonify
import socket

# Creamos la aplicación.
app = Flask(__name__)
# AÑADIMOS ESTA LÍNEA para que respete los acentos y caracteres en español.
app.json.ensure_ascii = False

# Esta función se ejecuta cuando alguien visita la página principal del sitio web.
@app.route('/')
def index():
    # Obtengo el nombre interno de la máquina que está ejecutando este código.
    hostname = socket.gethostname()

    # Preparo la respuesta con los textos de la "Opción C".
    response_data = {
        "titulo": "Proyecto Cloud de Ángel Álvarez",
        "mensaje": "Instancia activa. Estado operativo: OK.",
        "fuente_peticion": f"Sirviendo desde la instancia: {hostname}"
    }

    # Envio la respuesta en formato JSON, un estándar para las APIs web.
    return jsonify(response_data)

# Esto es necesario para que se pueda ejecutar el servidor de prueba fácilmente.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)