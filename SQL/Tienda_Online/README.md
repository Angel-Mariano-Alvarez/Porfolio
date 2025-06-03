* Proyecto de Base de Datos – Tienda Online

Este proyecto forma parte de los ejercicios prácticos del curso **"Sistemas Gestores de Bases de Datos"** del programa **Código Samurái – FUNDAE**, y tiene como objetivo diseñar, implementar y consultar una base de datos relacional para una tienda online.

* Estructura del modelo

El modelo incluye las siguientes entidades principales:
- **Clientes**
- **Productos**
- **Pedidos**
- **Detalle_Pedido**
- **Pagos**
- **Direcciones**

Estas entidades están relacionadas de forma normalizada, con claves primarias, foráneas y restricciones `CHECK` y `UNIQUE`.

* Archivos incluidos

- `tienda_kimonos_oracle`: script de creación de tablas Clientes y Pedidos, inserciones de datos de ejemplo, y procedimientos almacenados para operaciones CRUD en Oracle. 
- `modelo_base_datos_Tienda_Online.sql`: script de creación de tablas en SQL Server, con todas las restricciones definidas.
- `ejercicio_SQLServer_Tienda_Online_Datos_Ejemplo.sql`: inserciones con datos de ejemplo para clientes, productos y pedidos.
- `consultas_mysql_Tienda_Online.sql`: conjunto de consultas SQL (JOIN, SUM, AVG, subconsultas, etc.) preparadas para MySQL/MariaDB.
- `diagrama_ER_Tienda_Online.png`: diagrama entidad-relación que representa gráficamente la estructura de la base de datos.
- `README.md`: descripción general del proyecto, objetivos y archivos incluidos.

* Objetivo del proyecto

Este proyecto demuestra conocimientos prácticos en:
- Diseño de bases de datos relacionales
- Lenguaje SQL (DDL y DML)
- Consultas de análisis de datos
- Normalización y modelado entidad-relación
- Trabajo con distintos motores de base de datos (SQL Server y MySQL)

---

**Autor:** Ángel Mariano Álvarez López  
📧 angelmarianoalvarez@gmail.com


