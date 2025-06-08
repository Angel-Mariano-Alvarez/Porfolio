
# 🔐 Documentación de Implementación de Encriptación de Datos

## Encriptación en Reposo en MySQL

### Paso 1: Activar Transparent Data Encryption (TDE) en MySQL Enterprise (alternativa: encriptación manual en versión Community)

### Paso 2: Encriptación de columnas sensibles

```sql
-- Ejemplo usando función AES_ENCRYPT

CREATE TABLE Pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    fecha_nacimiento VARBINARY(255),
    intervenciones VARBINARY(255),
    alergias VARBINARY(255)
);

-- Insertar datos encriptados
INSERT INTO Pacientes (nombre, fecha_nacimiento, intervenciones, alergias)
VALUES (
    'Juan Pérez',
    AES_ENCRYPT('1985-02-15', 'mi_clave_secreta'),
    AES_ENCRYPT('Apendicectomía', 'mi_clave_secreta'),
    AES_ENCRYPT('Penicilina', 'mi_clave_secreta')
);

-- Leer datos desencriptados
SELECT
    nombre,
    CAST(AES_DECRYPT(fecha_nacimiento, 'mi_clave_secreta') AS CHAR) AS fecha_nacimiento,
    CAST(AES_DECRYPT(intervenciones, 'mi_clave_secreta') AS CHAR) AS intervenciones,
    CAST(AES_DECRYPT(alergias, 'mi_clave_secreta') AS CHAR) AS alergias
FROM Pacientes;
```

## Encriptación en Tránsito (SSL/TLS)

- Configurar SSL en el servidor MySQL (`my.cnf`):
```ini
[mysqld]
require_secure_transport = ON
ssl_cert = /etc/mysql/server-cert.pem
ssl_key = /etc/mysql/server-key.pem
ssl_ca = /etc/mysql/ca-cert.pem
```

- Configurar el cliente para usar SSL:
```bash
mysql --ssl-ca=/etc/mysql/ca-cert.pem --ssl-cert=/etc/mysql/client-cert.pem --ssl-key=/etc/mysql/client-key.pem -u usuario -p
```

---

**Autor:** Ángel Mariano Álvarez López  
**Curso:** Bases de Datos - Nivel 4 - FUNDAE / Código Samurái
