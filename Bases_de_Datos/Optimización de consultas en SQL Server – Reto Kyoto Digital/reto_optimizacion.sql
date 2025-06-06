
-- RETO: Optimización del Monasterio de Datos de Kyoto Digital
-- Autor: Noble Samurái de la Optimización

-- 1️⃣ Índice en Monto para consulta 1
CREATE NONCLUSTERED INDEX idx_Pedidos_Monto ON Pedidos (Monto);

-- 2️⃣ Índice en ClienteID para optimizar joins
CREATE NONCLUSTERED INDEX idx_Pedidos_ClienteID ON Pedidos (ClienteID);

-- 3️⃣ Índice en Estado para filtrar más rápido
CREATE NONCLUSTERED INDEX idx_Pedidos_Estado ON Pedidos (Estado);

-- 4️⃣ Índice en FechaPedido para agrupación por fecha
CREATE NONCLUSTERED INDEX idx_Pedidos_FechaPedido ON Pedidos (FechaPedido);

-- 5️⃣ Índice de cobertura en ClienteID + FechaPedido
CREATE NONCLUSTERED INDEX idx_Pedidos_ClienteID_FechaPedido ON Pedidos (ClienteID, FechaPedido);

-- 6️⃣ Consulta 2 reescrita con CTE
WITH PedidosEnviados AS (
    SELECT PedidoID, ClienteID, FechaPedido, Monto
    FROM Pedidos
    WHERE Estado = 'Enviado'
)
SELECT c.Nombre, p.FechaPedido, p.Monto
FROM Clientes c
JOIN PedidosEnviados p ON c.ClienteID = p.ClienteID;

-- 7️⃣ Consulta 3 optimizada
SELECT ClienteID, COUNT(*) AS NumPedidos
FROM Pedidos
WHERE FechaPedido BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY ClienteID
HAVING COUNT(*) > 5;
