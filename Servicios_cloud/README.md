# Proyectos de Servicios Cloud

Esta carpeta contiene los ejercicios y proyectos realizados durante el curso **Servicios Cloud** impartido por FUNDAE. A lo largo del curso se aplican conocimientos prácticos sobre el uso de proveedores de servicios en la nube como **Google Cloud Platform (GCP)** y **Amazon Web Services (AWS)**, desde la creación de instancias hasta configuraciones seguras y despliegue de servicios.

Cada proyecto está documentado individualmente y refleja el enfoque técnico adoptado, herramientas utilizadas y buenas prácticas en entornos cloud.

## Proyectos por Nivel

### Nivel 3

#### 1. Despliegue de Instancia EC2 en AWS
- Lanzamiento de una instancia Ubuntu Server en AWS EC2.
- Configuración personalizada del grupo de seguridad.
- Conexión segura mediante clave `.pem`.
- Eliminación de la autenticación por contraseña vía SSH (hardening básico).

[`Despliegue_Instancia_EC2_AWS`](./Despliegue_Instancia_EC2_AWS)

**Tecnologías:** AWS EC2, SSH, Ubuntu Server  
**Estado:** Finalizado

#### 2. Almacenamiento Seguro en la Nube
- Configuración y gestión de buckets privados y cifrados en AWS S3 y Google Cloud Storage.
- Almacenamiento de información sensible con permisos estrictos.
- Generación de enlaces seguros (URLs pre-firmadas en AWS y URLs autenticadas en GCP) para acceso controlado.

[`Almacenamiento_Seguro-AWS_GCP`](./Almacenamiento_Seguro-AWS_GCP)

**Tecnologías:** AWS S3, Google Cloud Storage, Seguridad en la Nube  
**Estado:** Finalizado

---
### Nivel 4

#### 3. Despliegue Automatizado de una App Flask en GCP
- Automatización del despliegue de una aplicación web Python/Flask mediante un **script de inicio (startup script)**.
- Creación de una **Plantilla de Instancia** en GCP para asegurar despliegues consistentes y replicables.
- **Estudio de caso práctico:** Diagnóstico y resolución de una cadena de problemas realistas de red, permisos y configuración en el entorno de despliegue.

[`Despliegue_App_Flask_Cloud`](./Despliegue_App_Flask_Cloud)

**Tecnologías:** GCP Compute Engine, Python, Flask, Gunicorn, Git, SSH  
**Estado:** Finalizado

---

## Estado del repositorio
- [x] Proyectos finalizados y documentados.
- [ ] Más ejercicios en desarrollo.

## Autor
Ángel Mariano Álvarez López  
📧 angelmarianoalvarez@gmail.com