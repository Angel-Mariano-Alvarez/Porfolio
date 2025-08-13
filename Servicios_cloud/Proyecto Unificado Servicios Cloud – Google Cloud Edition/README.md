# Proyecto Unificado de Servicios Cloud – Google Cloud

Este proyecto integra en un único flujo varios retos prácticos del curso de Servicios Cloud, desplegando y conectando distintos servicios de Google Cloud Platform (GCP) en un entorno controlado y documentado paso a paso.

## 📋 Objetivos
- Crear un bucket en **Cloud Storage** y servir contenido web estático.
- Implementar una **Cloud Function** para procesar texto.
- Configurar **Cloud SQL** con MySQL y conectarlo a una VM.
- Desplegar una **VM con Apache** y conectarla a Cloud SQL mediante Cloud SQL Proxy.
- Gestionar reglas de **firewall** para habilitar tráfico HTTP.

---

## 1️⃣ Cloud Storage – Sitio web estático

Se crea un bucket público con un `index.html` de prueba para servirlo como sitio web estático.

![Captura 2.1](capturas/Captura%202.1.PNG)
![Captura 2.2](capturas/Captura%202.2.PNG)
![Captura 2.3](capturas/Captura%202.3.PNG)
![Captura 2.4](capturas/Captura%202.4.PNG)

---

## 2️⃣ Cloud Functions – Procesamiento de texto

Se implementa la función `contarPalabras` en **Node.js 20** usando Cloud Functions Gen2.  
La función recibe un texto vía HTTP POST en formato JSON y devuelve el número de palabras detectadas.

![Captura 4.1](capturas/Captura%204.1.PNG)
![Captura 4.2](capturas/Captura%204.2.PNG)
![Captura 4.3](capturas/Captura%204.3.PNG)
![Captura 4.4](capturas/Captura%204.4.PNG)

---

## 3️⃣ Cloud SQL – Base de datos MySQL

Se crea una instancia MySQL en Cloud SQL, se configura la base de datos `db_puscgce` y se añade una tabla `texts` para pruebas.

![Captura 5.1](capturas/Captura%205.1.PNG)
![Captura 5.2](capturas/Captura%205.2.PNG)
![Captura 5.3](capturas/Captura%205.3.PNG)
![Captura 5.4](capturas/Captura%205.4.PNG)
![Captura 5.5](capturas/Captura%205.5.PNG)

---

## 4️⃣ Firewall – Regla HTTP

Se crea una regla de firewall para permitir tráfico entrante en el puerto 80 y etiquetar las instancias que la usen.

![Captura 6.1](capturas/Captura%206.1.PNG)

---

## 5️⃣ VM con Apache + Cloud SQL Proxy

Se despliega una VM con Apache en GCP, se instala PHP y se configura el **Cloud SQL Proxy** para conectar la web con la base de datos MySQL.

![Captura 6.2](capturas/Captura%206.2.PNG)
![Captura 6.3](capturas/Captura%206.3.PNG)
![Captura 6.4](capturas/Captura%206.4.PNG)
![Captura 6.5](capturas/Captura%206.5.PNG)
![Captura 6.6](capturas/Captura%206.6.PNG)

---

## 📂 Estructura del proyecto

```
PUSC-GCE_Proyecto_Unificado_Servicios_Cloud/
│
├── capturas/                  # Evidencias gráficas de cada paso
├── codigo/
│   └── functions/contarPalabras
│       ├── index.js
│       └── package.json
├── sql/
│   ├── schema.sql
│   └── crud.sql
└── web/
    └── index.html
```

---

## 🚀 Tecnologías usadas
- **Google Cloud Storage** – Hosting de contenido estático.
- **Google Cloud Functions** – Funciones sin servidor (serverless).
- **Google Cloud SQL (MySQL)** – Base de datos relacional.
- **Google Compute Engine (VM)** – Servidor Apache con PHP.
- **Cloud SQL Proxy** – Conexión segura a Cloud SQL.
- **Google VPC Firewall** – Control de acceso a instancias.

---
## Estado del Proyecto

- [x] Proyecto Finalizado
- [x] Validado el funcionamiento 
- [x] Limpieza de recursos (instancias, plantillas, grupos)

## Autor

Ángel Mariano Álvarez López  
📧 angelmarianoalvarez@gmail.com  
🔗 [GitHub Porfolio](https://github.com/Angel-Mariano-Alvarez/Porfolio)