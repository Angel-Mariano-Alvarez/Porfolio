CREATE TABLE Clientes (
    id_cliente INT PRIMARY KEY IDENTITY(1,1),
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(20)
);

CREATE TABLE Direcciones (
    id_direccion INT PRIMARY KEY IDENTITY(1,1),
    id_cliente INT,
    calle VARCHAR(100),
    ciudad VARCHAR(50),
    provincia VARCHAR(50),
    cp VARCHAR(10),
    pais VARCHAR(50),
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);

CREATE TABLE Pagos (
    id_pago INT PRIMARY KEY IDENTITY(1,1),
    metodo_pago VARCHAR(50) NOT NULL,       -- Ej: Tarjeta, PayPal, Bizum
    estado_pago VARCHAR(20) CHECK (estado_pago IN ('pendiente', 'pagado', 'rechazado')),
    fecha_pago DATE
);

CREATE TABLE Productos (
    id_producto INT PRIMARY KEY IDENTITY(1,1),
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(MAX),
    precio DECIMAL(10,2) CHECK (precio > 0),
    stock INT CHECK (stock >= 0)
);

CREATE TABLE Pedidos (
    id_pedido INT PRIMARY KEY IDENTITY(1,1),
    id_cliente INT,
    id_pago INT,
    id_direccion INT,
    fecha DATE NOT NULL,
    estado VARCHAR(20) CHECK (estado IN ('pendiente', 'enviado', 'entregado', 'cancelado')),
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_pago) REFERENCES Pagos(id_pago),
    FOREIGN KEY (id_direccion) REFERENCES Direcciones(id_direccion)
);

CREATE TABLE Detalle_Pedido (
    id_detalle INT PRIMARY KEY IDENTITY(1,1),
    id_pedido INT,
    id_producto INT,
    cantidad INT CHECK (cantidad > 0),
    precio_unitario DECIMAL(10,2) CHECK (precio_unitario > 0),
    FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido),
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
);