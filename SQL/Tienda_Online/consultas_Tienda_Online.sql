
-- Consulta 1: Total de ventas por categoría de producto
-- NOTA: Asumimos que existe una tabla 'Categorias' relacionada con 'Productos'
SELECT c.nombre AS categoria, SUM(dp.cantidad * dp.precio_unitario) AS total_ventas
FROM Detalle_Pedido dp
JOIN Productos p ON dp.id_producto = p.id_producto
JOIN Categorias c ON p.id_categoria = c.id_categoria
GROUP BY c.nombre;

-- Consulta 2: Promedio de gasto por cliente
SELECT cl.id_cliente, cl.nombre, cl.apellido,
       AVG(gasto.total) AS promedio_gasto
FROM Clientes cl
JOIN (
    SELECT p.id_cliente, SUM(dp.cantidad * dp.precio_unitario) AS total
    FROM Pedidos p
    JOIN Detalle_Pedido dp ON p.id_pedido = dp.id_pedido
    GROUP BY p.id_cliente
) AS gasto ON cl.id_cliente = gasto.id_cliente
GROUP BY cl.id_cliente;

-- Consulta 3: Productos más vendidos en orden descendente
SELECT p.nombre, SUM(dp.cantidad) AS total_vendidos
FROM Detalle_Pedido dp
JOIN Productos p ON dp.id_producto = p.id_producto
GROUP BY p.id_producto
ORDER BY total_vendidos DESC;

-- Consulta 4: Clientes sin pedidos
SELECT cl.id_cliente, cl.nombre, cl.apellido
FROM Clientes cl
LEFT JOIN Pedidos p ON cl.id_cliente = p.id_cliente
WHERE p.id_pedido IS NULL;

-- Consulta 5: Subconsulta con LEFT JOIN con la tabla de pedidos
-- Devuelve clientes y el número de pedidos realizados
SELECT cl.id_cliente, cl.nombre, (
    SELECT COUNT(*) FROM Pedidos p WHERE p.id_cliente = cl.id_cliente
) AS numero_pedidos
FROM Clientes cl;

-- Consulta 6: Clientes con valores nulos en el número de pedidos (LEFT JOIN + WHERE IS NULL)
SELECT cl.id_cliente, cl.nombre
FROM Clientes cl
LEFT JOIN (
    SELECT id_cliente, COUNT(*) AS total_pedidos
    FROM Pedidos
    GROUP BY id_cliente
) AS pedidos_cliente ON cl.id_cliente = pedidos_cliente.id_cliente
WHERE pedidos_cliente.total_pedidos IS NULL;
