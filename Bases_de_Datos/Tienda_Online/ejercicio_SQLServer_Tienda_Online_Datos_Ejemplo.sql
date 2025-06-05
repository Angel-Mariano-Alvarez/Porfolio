-- Crear tabla Clientes
CREATE TABLE Clientes (
    id_cliente INT PRIMARY KEY IDENTITY(1,1),
    nombre NVARCHAR(50) NOT NULL,
    apellido NVARCHAR(50) NOT NULL,
    email NVARCHAR(100) UNIQUE NOT NULL,
    telefono NVARCHAR(20)
);

-- Crear tabla Productos
CREATE TABLE Productos (
    id_producto INT PRIMARY KEY IDENTITY(1,1),
    nombre NVARCHAR(100) NOT NULL,
    descripcion NVARCHAR(MAX),
    precio DECIMAL(10,2) CHECK (precio > 0),
    stock INT CHECK (stock >= 0)
);

-- Crear tabla Pedidos
CREATE TABLE Pedidos (
    id_pedido INT PRIMARY KEY IDENTITY(1,1),
    id_cliente INT NOT NULL,
    fecha DATE NOT NULL,
    estado NVARCHAR(20) CHECK (estado IN ('pendiente', 'enviado', 'entregado', 'cancelado')),
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);

-- Crear tabla Detalle_Pedido
CREATE TABLE Detalle_Pedido (
    id_detalle INT PRIMARY KEY IDENTITY(1,1),
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT CHECK (cantidad > 0),
    precio_unitario DECIMAL(10,2) CHECK (precio_unitario > 0),
    FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido),
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
);

-- Insertar datos en Clientes
INSERT INTO Clientes (nombre, apellido, email, telefono) VALUES
('Laura', 'Gómez', 'laura.gomez@correo.com', '600123456'),
('Carlos', 'Pérez', 'carlos.perez@correo.com', '611234567'),
('Elena', 'Martínez', 'elena.martinez@correo.com', '622345678');

-- Insertar datos en Productos
INSERT INTO Productos (nombre, descripcion, precio, stock) VALUES
('Curso de SQL Server', 'Curso introductorio al manejo de bases de datos relacionales en SQL Server', 99.99, 50),
('Curso de Python', 'Curso básico de programación con Python aplicado a datos', 89.99, 40),
('Curso de Power BI', 'Curso de análisis de datos con Power BI para principiantes', 109.99, 30);

-- Insertar datos en Pedidos
INSERT INTO Pedidos (id_cliente, fecha, estado) VALUES
(1, '2025-05-01', 'entregado'),
(2, '2025-05-03', 'enviado'),
(3, '2025-05-05', 'pendiente');

-- Insertar datos en Detalle_Pedido
INSERT INTO Detalle_Pedido (id_pedido, id_producto, cantidad, precio_unitario) VALUES
(1, 1, 1, 99.99),
(1, 2, 1, 89.99),
(2, 3, 1, 109.99),
(3, 1, 2, 99.99);
