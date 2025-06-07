
-- ==============================================
-- Procedimientos Almacenados - Reto 4 SGBD
-- ==============================================

-- ==== CLIENTES ====

-- Crear Cliente
CREATE OR REPLACE PROCEDURE CrearCliente (
    p_Nombre IN VARCHAR2,
    p_Direccion IN VARCHAR2,
    p_Telefono IN VARCHAR2
)
IS
BEGIN
    INSERT INTO Clientes (Nombre, Direccion, Telefono)
    VALUES (p_Nombre, p_Direccion, p_Telefono);
    COMMIT;
END;
/

-- Obtener Cliente
CREATE OR REPLACE PROCEDURE ObtenerCliente (
    p_ClienteID IN NUMBER
)
IS
    v_Nombre Clientes.Nombre%TYPE;
    v_Direccion Clientes.Direccion%TYPE;
    v_Telefono Clientes.Telefono%TYPE;
BEGIN
    SELECT Nombre, Direccion, Telefono
    INTO v_Nombre, v_Direccion, v_Telefono
    FROM Clientes
    WHERE ClienteID = p_ClienteID;

    DBMS_OUTPUT.PUT_LINE('Nombre: ' || v_Nombre);
    DBMS_OUTPUT.PUT_LINE('Direccion: ' || v_Direccion);
    DBMS_OUTPUT.PUT_LINE('Telefono: ' || v_Telefono);
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Cliente no encontrado.');
END;
/

-- Actualizar Cliente
CREATE OR REPLACE PROCEDURE ActualizarCliente (
    p_ClienteID IN NUMBER,
    p_Nombre IN VARCHAR2,
    p_Direccion IN VARCHAR2,
    p_Telefono IN VARCHAR2
)
IS
BEGIN
    UPDATE Clientes
    SET Nombre = p_Nombre,
        Direccion = p_Direccion,
        Telefono = p_Telefono
    WHERE ClienteID = p_ClienteID;
    COMMIT;
END;
/

-- Eliminar Cliente
CREATE OR REPLACE PROCEDURE EliminarCliente (
    p_ClienteID IN NUMBER
)
IS
BEGIN
    DELETE FROM Clientes WHERE ClienteID = p_ClienteID;
    COMMIT;
END;
/

-- ==== PEDIDOS ====

-- Crear Pedido
CREATE OR REPLACE PROCEDURE CrearPedido (
    p_ClienteID IN NUMBER,
    p_FechaPedido IN DATE,
    p_Detalle IN VARCHAR2,
    p_Monto IN NUMBER
)
IS
BEGIN
    INSERT INTO Pedidos (ClienteID, FechaPedido, Detalle, Monto)
    VALUES (p_ClienteID, p_FechaPedido, p_Detalle, p_Monto);
    COMMIT;
END;
/

-- Obtener Pedido
CREATE OR REPLACE PROCEDURE ObtenerPedido (
    p_PedidoID IN NUMBER
)
IS
    v_ClienteID Pedidos.ClienteID%TYPE;
    v_FechaPedido Pedidos.FechaPedido%TYPE;
    v_Detalle Pedidos.Detalle%TYPE;
    v_Monto Pedidos.Monto%TYPE;
BEGIN
    SELECT ClienteID, FechaPedido, Detalle, Monto
    INTO v_ClienteID, v_FechaPedido, v_Detalle, v_Monto
    FROM Pedidos
    WHERE PedidoID = p_PedidoID;

    DBMS_OUTPUT.PUT_LINE('ClienteID: ' || v_ClienteID);
    DBMS_OUTPUT.PUT_LINE('FechaPedido: ' || v_FechaPedido);
    DBMS_OUTPUT.PUT_LINE('Detalle: ' || v_Detalle);
    DBMS_OUTPUT.PUT_LINE('Monto: ' || v_Monto);
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Pedido no encontrado.');
END;
/

-- Actualizar Pedido
CREATE OR REPLACE PROCEDURE ActualizarPedido (
    p_PedidoID IN NUMBER,
    p_ClienteID IN NUMBER,
    p_FechaPedido IN DATE,
    p_Detalle IN VARCHAR2,
    p_Monto IN NUMBER
)
IS
BEGIN
    UPDATE Pedidos
    SET ClienteID = p_ClienteID,
        FechaPedido = p_FechaPedido,
        Detalle = p_Detalle,
        Monto = p_Monto
    WHERE PedidoID = p_PedidoID;
    COMMIT;
END;
/

-- Eliminar Pedido
CREATE OR REPLACE PROCEDURE EliminarPedido (
    p_PedidoID IN NUMBER
)
IS
BEGIN
    DELETE FROM Pedidos WHERE PedidoID = p_PedidoID;
    COMMIT;
END;
/

-- ==============================================
-- Fin de Procedimientos - Reto 4 SGBD
-- ==============================================
