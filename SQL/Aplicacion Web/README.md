
* Proyecto Aplicación Web con Flask + Google Cloud SQL

Este proyecto es parte del curso de bases de datos (Nivel 4 – FUNDAE / Código Samurái) y demuestra una aplicación web funcional que se conecta a una base de datos en la nube usando Google Cloud SQL.

**  Repositorio

📎 [Repositorio en GitHub](https://github.com/Angel-Mariano-Alvarez/Porfolio/tree/main/SQL/Aplicacion%20Web)

** Funcionalidades

-  Listar clientes
-  Añadir nuevos clientes
-  Eliminar clientes
-  Conexión segura a una base de datos MySQL alojada en Google Cloud SQL

** Tecnologías utilizadas

- **Lenguaje:** Python 3
- **Framework:** Flask
- **ORM:** SQLAlchemy
- **Base de datos:** Google Cloud SQL (MySQL)
- **Frontend:** HTML + Bootstrap (opcional)
- **Variables de entorno:** dotenv

**  Instalación y configuración

1. Clona el repositorio:
```bash
git clone https://github.com/Angel-Mariano-Alvarez/Porfolio.git
cd Porfolio/SQL/Aplicacion Web
```

2. Crea un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Configura tu archivo `.env`:
```dotenv
DB_USER=usuario
DB_PASS=contraseña
DB_NAME=nombre_basedatos
DB_HOST=ip_cloudsql_o_hostname
```

5. Inicializa la base de datos (una vez):
```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

6. Ejecuta la aplicación:
```bash
python app.py
```

Accede a la aplicación en `http://localhost:5000`.

## 🧪 Seguridad y despliegue

- Recomendado usar conexión SSL para Google Cloud SQL
- Se puede desplegar fácilmente en Google Cloud Run o App Engine

---

**Autor:** Ángel Mariano Álvarez López  
📧 angelmarianoalvarez@gmail.com
