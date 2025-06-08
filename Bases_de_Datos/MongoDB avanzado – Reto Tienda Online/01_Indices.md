Informe de Creación y Optimización de Índices
# Introducción
Nuestra tienda online gestiona una colección de productos (products) y otra de pedidos (orders).
Las consultas sobre productos y pedidos son frecuentes y deben ser rápidas.
# Estado inicial
Consultas sin índices experimentaban tiempos de respuesta altos, especialmente en búsquedas por categoría y pedidos por usuario.
# Proceso de creación de índices
1. Índice en products.category: db.products.createIndex({ category: 1 })
2. Índice compuesto en products.category + price: db.products.createIndex({ category: 1, price: 1 })
3. Índice en orders.user_id + order_date: db.orders.createIndex({ user_id: 1, order_date: -1 })
# Comparativa de rendimiento
Las consultas mostraron una mejora de rendimiento superior al 80%.
- Buscar productos en categoría "Electronics": de ~300 ms a ~20 ms
- Listar productos ordenados por precio: de ~500 ms a ~30 ms
- Pedidos de un usuario en último mes: de ~400 ms a ~25 ms
# Conclusiones
Los índices han mejorado significativamente el rendimiento de las consultas más comunes.
Se recomienda revisar y ajustar periódicamente los índices.