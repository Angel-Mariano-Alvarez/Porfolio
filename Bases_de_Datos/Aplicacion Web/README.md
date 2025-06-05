
# Proyecto Aplicación Web con Flask + Google Cloud SQL

## Descripción
Este proyecto forma parte del curso "Sistemas Gestores de Bases de Datos - Nivel 4" del itinerario de formación técnica de FUNDAE – Código Samurái. Consiste en una aplicación web funcional desarrollada en Python con Flask que permite gestionar una lista de clientes, conectándose a una base de datos MySQL alojada en Google Cloud SQL.

## Tecnologías y herramientas utilizadas
- Lenguaje: Python 3
- Framework: Flask
- ORM: SQLAlchemy
- Base de datos: Google Cloud SQL (MySQL)
- Frontend: HTML + Bootstrap
- Variables de entorno: dotenv
- Entorno: Google Cloud Platform (Cloud SQL, opcionalmente Cloud Run/App Engine)

## Estructura del proyecto
```
.
├── app_flask_cloudsql.py       # Código principal de la aplicación Flask
├── Base de datos.sql           # Script de creación de tabla en MySQL
├── requirements.txt            # Dependencias del proyecto
├── .env.example                # Ejemplo de configuración de entorno
├── templates/                  # Carpeta para archivos HTML (no incluida aquí)
└── README.md                   # Documentación del proyecto
```

## Instalación y ejecución
1. Clona el repositorio:
   ```bash
   git clone https://github.com/Angel-Mariano-Alvarez/Porfolio.git
   cd Porfolio/SQL/Aplicacion Web
   ```

2. Crea un entorno virtual (opcional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura tu archivo `.env` basado en `.env.example`:
   ```dotenv
   DB_USER=usuario
   DB_PASS=contraseña
   DB_NAME=nombre_basedatos
   DB_HOST=ip_cloudsql_o_hostname
   ```

5. Inicializa la base de datos:
   ```bash
   python
   >>> from app_flask_cloudsql import db
   >>> db.create_all()
   >>> exit()
   ```

6. Ejecuta la aplicación:
   ```bash
   python app_flask_cloudsql.py
   ```

Accede a la app desde `http://localhost:5000`.

## Resultados o capturas
- Gestión de clientes (listado, inserción, eliminación)
- Conexión con MySQL en entorno cloud
- Aplicación funcional con interfaz básica HTML

## Aprendizajes y mejoras
Este proyecto me ha permitido poner en práctica:
- Conexión segura entre una aplicación Python y una base de datos en la nube
- Uso de ORM (SQLAlchemy) para abstraer operaciones sobre la base de datos
- Gestión de variables de entorno con `.env`
- Despliegue local de aplicaciones web con Flask

Mejoras futuras:
- Implementación de validación de formularios y seguridad (CSRF, control de errores)
- Despliegue automático con Docker y Google Cloud Run
- Tests automatizados con `pytest`

## Estado del proyecto
- [x] Terminado
- [ ] En desarrollo
- [ ] En pausa

## Autor
Ángel Mariano Álvarez López  
📧 angelmarianoalvarez@gmail.com
