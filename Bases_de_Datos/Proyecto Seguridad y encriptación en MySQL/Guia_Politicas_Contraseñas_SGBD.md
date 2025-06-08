
# 🔏 Guía de Configuración de Políticas de Contraseñas en MySQL

## 1️⃣ Políticas de Contraseñas Fuertes

### Activar el plugin validate_password:

```sql
SHOW VARIABLES LIKE 'validate_password%';
```

### Configurar políticas:

```sql
SET GLOBAL validate_password.policy = 2; -- 0=Low, 1=Medium, 2=Strong
SET GLOBAL validate_password.length = 12;
SET GLOBAL validate_password.mixed_case_count = 1;
SET GLOBAL validate_password.number_count = 1;
SET GLOBAL validate_password.special_char_count = 1;
```

### Beneficios:

- Contraseñas más difíciles de vulnerar.
- Reduce el riesgo de ataques por fuerza bruta.

## 2️⃣ Protección de Contraseñas Almacenadas (Hashing)

Las contraseñas nunca deben almacenarse en texto plano.

Ejemplo en una tabla de usuarios:

```sql
CREATE TABLE Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50),
    password_hash VARBINARY(255)
);

-- Insertar una contraseña con SHA2 (como ejemplo básico):
INSERT INTO Usuarios (nombre_usuario, password_hash)
VALUES ('angel', UNHEX(SHA2('MiContraseñaSegura123!', 256)));

-- Verificar contraseña (ejemplo de consulta):
SELECT * FROM Usuarios
WHERE nombre_usuario = 'angel'
AND password_hash = UNHEX(SHA2('MiContraseñaSegura123!', 256));
```

### Beneficios del Hashing:

- Si la base de datos es comprometida, el atacante no obtiene las contraseñas en texto plano.
- Al usar algoritmos como bcrypt, se protege incluso contra ataques con hardware especializado.

---

**Autor:** Ángel Mariano Álvarez López  
**Curso:** Bases de Datos - Nivel 4 - FUNDAE / Código Samurái
