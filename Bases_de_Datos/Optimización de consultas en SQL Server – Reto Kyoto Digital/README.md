
# Optimización de consultas en SQL Server – Reto Kyoto Digital

## Descripción
Este proyecto forma parte del Nivel 5 del curso "Sistemas Gestores de Bases de Datos" del programa FUNDAE – Código Samurái. El reto consistía en mejorar el rendimiento de un conjunto de consultas SQL sobre una base de datos relacional, utilizando herramientas de análisis y técnicas de optimización como la creación de índices y la reescritura de consultas.

## Tecnologías y herramientas utilizadas
- Lenguaje: SQL (Microsoft SQL Server)
- Herramientas: SQL Server Management Studio (SSMS)
- Técnicas: índices no agrupados, índices de cobertura, CTEs, planes de ejecución

## Estructura del proyecto
```
.
├── reto_optimizacion.sql            # Scripts de creación de índices y consultas optimizadas
├── Informe_Reto_KyotoDigital.txt    # Análisis inicial, medidas aplicadas y evaluación de mejoras
├── RETO 2 TRANSCRIPCION.pdf         # Descripción oficial del reto formativo
└── README.md                        # Documentación del proyecto
```

## Objetivo del reto
- Identificar problemas de rendimiento como Table Scans y Joins ineficientes
- Crear índices específicos para columnas clave (Monto, ClienteID, Estado, FechaPedido)
- Comparar los planes de ejecución antes y después de la optimización
- Documentar el impacto de las mejoras en términos de eficiencia

## Resultados
- Reducción de hasta un 90% en el tiempo de ejecución de algunas consultas
- Sustitución de Table Scans por Index Seeks en múltiples casos
- Uso de índices de cobertura para optimizar operaciones complejas de filtrado y agrupación

## Aprendizajes y mejoras
Este reto me permitió aplicar conocimientos avanzados de optimización en SQL Server y me entrenó en:
- Análisis de planes de ejecución
- Identificación de cuellos de botella en bases de datos
- Uso eficaz de índices y estructuras de datos
- Evaluación cuantitativa del impacto de cada cambio

## Estado del proyecto
- [x] Terminado
- [ ] En desarrollo
- [ ] En pausa

## Autor
Ángel Mariano Álvarez López  
📧 angelmarianoalvarez@gmail.com
