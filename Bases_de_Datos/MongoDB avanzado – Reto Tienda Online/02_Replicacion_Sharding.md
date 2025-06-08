Diseño de Arquitectura de Replicación y Sharding
# Diagrama de arquitectura
Cluster Sharded con réplicas por shard.
Config Servers (x3), Mongos Router (x2), Shards con ReplicaSet (Shard1, Shard2, Shard3).
# Replicación
Cada shard es un Replica Set con 1 Primary y 2 Secondaries.
Beneficios: alta disponibilidad, lecturas escalables.
# Sharding
Shard key para orders: user_id.
Shard key para products: category.
Beneficios: distribución horizontal de datos, escalabilidad.
# Conclusión
La arquitectura propuesta permite escalar horizontalmente y mejorar la disponibilidad de la base de datos.