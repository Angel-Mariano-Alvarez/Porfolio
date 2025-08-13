<?php
$mysqli = new mysqli('127.0.0.1', 'root', 'Root1234!', 'db_puscgce', 3306);
if ($mysqli->connect_errno) {
    die('Error conexión: '.$mysqli->connect_error);
}
$res = $mysqli->query("SELECT NOW() as ahora, COUNT(*) as registros FROM texts");
$row = $res->fetch_assoc();
echo "<h1>Conexión OK a Cloud SQL</h1>";
echo "<p>Fecha servidor SQL: {$row['ahora']}</p>";
echo "<p>Registros en texts: {$row['registros']}</p>";
$mysqli->close();
?>