
# 📝 Informe de Pruebas - Reto 4 SGBD - Unidad 4

## 1️⃣ Introducción

Este informe documenta las pruebas realizadas sobre los procedimientos almacenados desarrollados en Oracle Database para la gestión de Clientes y Pedidos.

## 2️⃣ Entorno de pruebas

Oracle Database con Oracle SQL Developer.

## 3️⃣ Pruebas realizadas

### CrearCliente

```sql
BEGIN
    CrearCliente('Juan Perez', 'Calle Falsa 123', '555-1234');
END;
```

### ObtenerCliente

```sql
BEGIN
    ObtenerCliente(1);
END;
```

### ActualizarCliente

```sql
BEGIN
    ActualizarCliente(1, 'Juan Perez Modificado', 'Calle Verdadera 456', '555-5678');
END;
```

### EliminarCliente

```sql
BEGIN
    EliminarCliente(1);
END;
```

### CrearPedido

```sql
BEGIN
    CrearPedido(2, SYSDATE, 'Pedido de prueba', 150);
END;
```

### ObtenerPedido

```sql
BEGIN
    ObtenerPedido(1);
END;
```

### ActualizarPedido

```sql
BEGIN
    ActualizarPedido(1, 2, SYSDATE, 'Pedido modificado', 200);
END;
```

### EliminarPedido

```sql
BEGIN
    EliminarPedido(1);
END;
```

## 4️⃣ Resultados esperados

Operaciones CRUD ejecutadas correctamente.

## 5️⃣ Conclusión

Las pruebas han sido diseñadas para validar el correcto funcionamiento de los procedimientos almacenados.


