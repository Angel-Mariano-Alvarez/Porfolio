
# 📖 Guía de Uso de los Procedimientos Almacenados - Reto 4 SGBD

## CLIENTES

### Crear Cliente
```sql
BEGIN
    CrearCliente('Juan Perez', 'Calle Falsa 123', '555-1234');
END;
```

### Obtener Cliente
```sql
BEGIN
    ObtenerCliente(1);
END;
```

### Actualizar Cliente
```sql
BEGIN
    ActualizarCliente(1, 'Juan Perez Modificado', 'Calle Verdadera 456', '555-5678');
END;
```

### Eliminar Cliente
```sql
BEGIN
    EliminarCliente(1);
END;
```

## PEDIDOS

### Crear Pedido
```sql
BEGIN
    CrearPedido(2, SYSDATE, 'Pedido de prueba', 150);
END;
```

### Obtener Pedido
```sql
BEGIN
    ObtenerPedido(1);
END;
```

### Actualizar Pedido
```sql
BEGIN
    ActualizarPedido(1, 2, SYSDATE, 'Pedido modificado', 200);
END;
```

### Eliminar Pedido
```sql
BEGIN
    EliminarPedido(1);
END;
```

---

**Autor:** Ángel Mariano Álvarez López  
**Curso:** Bases de Datos - Nivel 4 - FUNDAE / Código Samurái
