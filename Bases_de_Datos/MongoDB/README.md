
# Proyecto MongoDB – Gestión de Libros

## Descripción
Este proyecto forma parte del curso "Sistemas Gestores de Bases de Datos - Nivel 4" dentro del itinerario formativo de FUNDAE – Código Samurái. Representa un ejercicio introductorio de trabajo con bases de datos NoSQL orientadas a documentos, utilizando MongoDB.

## Tecnologías y herramientas utilizadas
- Lenguaje: JavaScript para consultas en consola MongoDB
- Base de datos: MongoDB
- Formato de datos: JSON
- Herramientas: mongoimport, mongoexport

## Estructura del proyecto
```
.
├── libros.json              # Colección completa de libros en formato JSON
├── libros_fantasia.json     # Exportación de libros del género Fantasía
├── consultas_mongodb.js     # Script de consultas ejecutadas en MongoDB
└── README.md                # Documentación del proyecto
```

## Resultados o capturas
- Consultas con `find` para filtrar libros por autor, género y año de publicación
- Agregación con `aggregate` para contar libros por género
- Exportación de subconjuntos de datos a archivos JSON

## Aprendizajes y mejoras
Este proyecto introductorio me ha permitido familiarizarme con:
- Estructuras de datos tipo documento (JSON)
- Comandos básicos de importación/exportación en MongoDB
- Operaciones de filtrado y agrupación de datos con `find` y `aggregate`

Como mejora futura, se podría implementar una estructura más compleja con validaciones, índices y relaciones simuladas entre colecciones.

## Estado del proyecto
- [x] Terminado
- [ ] En desarrollo
- [ ] En pausa

## Autor
Ángel Mariano Álvarez López  
📧 angelmarianoalvarez@gmail.com
