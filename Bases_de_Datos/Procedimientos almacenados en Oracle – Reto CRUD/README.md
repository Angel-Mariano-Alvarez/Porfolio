
# Procedimientos almacenados en Oracle – Reto CRUD

## Descripción
Este proyecto fue desarrollado como parte del Nivel 5 del curso "Sistemas Gestores de Bases de Datos" impartido por FUNDAE – Código Samurái. El reto consistió en diseñar una base de datos para una tienda de kimonos y desarrollar procedimientos almacenados en Oracle para gestionar operaciones CRUD (Crear, Leer, Actualizar, Borrar) sobre las entidades Clientes y Pedidos.

## Tecnologías y herramientas utilizadas
- Lenguaje: SQL (Oracle PL/SQL)
- Motor de base de datos: Oracle Database
- Entorno: Oracle SQL Developer
- Procedimientos: almacenados (CRUD)

## Estructura del proyecto
```
.
├── script_creacion_tablas.sql           # Script SQL de creación de las tablas Clientes y Pedidos
├── procedimientos_clientes_pedidos.sql  # Scripts de procedimientos CRUD para ambas tablas
├── Informe_Pruebas_Reto4.md             # Informe con pruebas ejecutadas
├── Guia_Uso_Reto4.md                    # Guía de uso con ejemplos de invocación de procedimientos
└── README.md                            # Documentación general del proyecto
```

## Funcionalidades desarrolladas

### Para la tabla `Clientes`
- `CrearCliente`
- `ObtenerCliente`
- `ActualizarCliente`
- `EliminarCliente`

### Para la tabla `Pedidos`
- `CrearPedido`
- `ObtenerPedido`
- `ActualizarPedido`
- `EliminarPedido`

## Resultados
Todas las funciones CRUD fueron probadas con éxito, ejecutando los procedimientos desde Oracle SQL Developer. El diseño de la base de datos incluye relaciones entre tablas y el uso de claves primarias y foráneas, siguiendo buenas prácticas de modelado relacional.

## Aprendizajes y mejoras
Este reto me permitió:
- Consolidar el uso de procedimientos almacenados en Oracle
- Diseñar y probar operaciones complejas sobre tablas relacionadas
- Documentar y organizar un proyecto de base de datos completo

Como mejora futura, podría integrarse este backend con una aplicación web o interfaz de usuario para probar los procedimientos en un contexto más realista.

## Estado del proyecto
- [x] Terminado
- [ ] En desarrollo
- [ ] En pausa

## Autor
Ángel Mariano Álvarez López  
📧 angelmarianoalvarez@gmail.com
