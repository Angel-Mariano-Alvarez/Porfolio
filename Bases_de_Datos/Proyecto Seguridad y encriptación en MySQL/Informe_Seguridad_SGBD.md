# Informe de Seguridad en Bases de Datos

## Introducción
La seguridad en bases de datos es un aspecto fundamental en la gestión de la información, especialmente cuando se trata de datos sensibles como los de pacientes, clientes o usuarios. Este informe presenta un resumen general de las mejores prácticas aplicadas en entornos MySQL, con énfasis en la encriptación de datos en tránsito y en reposo, así como en políticas de contraseñas.

Se complementa con documentación técnica específica y guías prácticas implementadas en el reto 7 del Nivel 6 del curso de bases de datos (FUNDAE – Código Samurái).


# 🛡️ Informe de Investigación sobre Seguridad en Sistemas Gestores de Bases de Datos

## 1️⃣ Fundamentos de Seguridad en Bases de Datos

La seguridad en bases de datos tiene como objetivo proteger la integridad, confidencialidad y disponibilidad de los datos. Es fundamental para evitar accesos no autorizados, manipulación o pérdida de información crítica.

## 2️⃣ Importancia de la Encriptación de Datos

La encriptación de datos protege la información de ser leída o manipulada por personas no autorizadas.

- **Encriptación en reposo:** protege los datos almacenados en el disco (archivos, backups, logs).
- **Encriptación en tránsito:** protege los datos que circulan entre la base de datos y las aplicaciones clientes.

### Tipos de Encriptación

- **En reposo:** Algoritmos como AES-256.
- **En tránsito:** Protocolos SSL/TLS.

## 3️⃣ Importancia de las Políticas de Contraseñas

El uso de contraseñas seguras evita que atacantes puedan obtener acceso con ataques de fuerza bruta.

- Requisitos típicos: longitud mínima, uso de mayúsculas, minúsculas, números y símbolos.
- Renovación periódica de contraseñas.
- Almacenamiento con hashing seguro (SHA-256, bcrypt).

## 4️⃣ Ejemplo de Uso Real

Un sistema de gestión de datos médicos debe garantizar que los datos de salud de los pacientes estén encriptados y que las credenciales de acceso se almacenen de manera segura.

---

**Autor:** Ángel Mariano Álvarez López  
**Curso:** Bases de Datos - Nivel 4 - FUNDAE / Código Samurái
