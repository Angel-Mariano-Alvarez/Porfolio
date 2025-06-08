
# Seguridad y encriptación en MySQL

## Descripción
Este proyecto forma parte del Nivel 6 del curso "Sistemas Gestores de Bases de Datos" (FUNDAE – Código Samurái). El objetivo es aplicar buenas prácticas de seguridad sobre bases de datos MySQL, incluyendo encriptación de datos, uso de conexiones seguras, políticas de contraseñas y protección frente a accesos no autorizados.

## Estructura del proyecto
```
Seguridad_MySQL/
├── Informe_Seguridad_SGBD.md             # Informe general sobre seguridad en bases de datos
├── Documentacion_Encriptacion_SGBD.md    # Detalles sobre encriptación en tránsito y en reposo en MySQL
├── Guia_Politicas_Contraseñas_SGBD.md    # Guía práctica sobre políticas de contraseñas seguras
└── README.md                             # Documentación general del proyecto
```

## Contenido del proyecto

### 1. Seguridad general en bases de datos
- Conceptos de encriptación en tránsito y en reposo
- Buenas prácticas para proteger datos sensibles
- Roles de usuario y restricciones de acceso

### 2. Encriptación en MySQL
- Uso de `AES_ENCRYPT()` y `AES_DECRYPT()`
- Configuración de conexiones seguras (SSL/TLS)
- Consideraciones sobre claves y privacidad

### 3. Políticas de contraseñas
- Activación y configuración del plugin `validate_password`
- Requisitos de longitud, complejidad y caducidad
- Hashing de contraseñas con `SHA2` y `PASSWORD()`

## Aprendizajes
Este reto me permitió consolidar conocimientos clave sobre seguridad en entornos reales:
- Cómo implementar encriptación sin afectar el rendimiento
- Cómo proteger credenciales y accesos desde cliente
- Cómo aplicar políticas de contraseñas efectivas en MySQL

## Estado del proyecto
- [x] Terminado
- [ ] En desarrollo
- [ ] En pausa

## Autor
Ángel Mariano Álvarez López  
📧 angelmarianoalvarez@gmail.com
