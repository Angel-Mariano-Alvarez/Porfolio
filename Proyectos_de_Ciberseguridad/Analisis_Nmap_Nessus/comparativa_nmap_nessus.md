
# Comparativa de análisis: Nmap vs Nessus

Este archivo resume las diferencias y complementariedades entre las herramientas Nmap y Nessus utilizadas en el análisis de vulnerabilidades sobre la máquina Metasploitable2.

## 1. Objetivo de cada herramienta

| Herramienta | Propósito principal |
|-------------|---------------------|
| Nmap        | Detección de puertos abiertos y servicios activos |
| Nessus      | Análisis detallado de vulnerabilidades sobre los servicios detectados |

## 2. Ejemplo de resultados detectados

| Puerto | Servicio detectado por Nmap      | Vulnerabilidad detectada por Nessus |
|--------|----------------------------------|--------------------------------------|
| 21     | vsftpd 2.3.4                     | vsftpd backdoor vulnerability        |
| 22     | OpenSSH 4.7p1                    | Weak SSH Algorithms Enabled          |
| 80     | Apache httpd 2.2.8               | Apache Directory Listing Enabled     |
| 139    | Samba smbd 3.X                   | Samba 'nttrans' Heap Overflow        |

## 3. Diferencias clave

- **Nmap** detecta servicios y versiones, pero **no alerta de vulnerabilidades específicas**.
- **Nessus** analiza los servicios encontrados (por Nmap o internamente) e identifica CVEs, severidad y posibles mitigaciones.
- Nessus clasifica las vulnerabilidades por nivel de severidad (Baja, Media, Alta, Crítica).
- Nmap no requiere credenciales, Nessus puede configurarse para escaneos autenticados.

## 4. Conclusión

Ambas herramientas son complementarias. Nmap es ideal para reconocer el entorno, mientras que Nessus es imprescindible para evaluar riesgos reales en base a bases de datos de CVEs. Utilizar ambas en conjunto mejora el alcance y profundidad de un análisis de seguridad.

