# Análisis de Tráfico de Red con Wireshark: Protocolos Cifrados vs. No Cifrados

## Descripción del Proyecto

Este proyecto forma parte de mi formación en Seguridad Informática (IFCT0050 del SEPE) y se centra en el **análisis de tráfico de red utilizando Wireshark**. El objetivo principal fue comprender las diferencias entre la comunicación a través de protocolos cifrados (HTTPS, SSH) y no cifrados (HTTP, Telnet), y demostrar los riesgos de seguridad asociados a la transmisión de información sensible en texto plano.

El ejercicio se realizó en un entorno controlado de laboratorio en clase, lo que me permitió interactuar con servicios específicos y observar el comportamiento real del tráfico.

## Tecnologías Utilizadas

* **Herramienta Principal:** Wireshark
* **Conceptos Aplicados:** Análisis de paquetes, sniffing de red, protocolos de red (HTTP, HTTPS, Telnet, SSH, DNS), cifrado, seguridad de la información.
* **Entorno de Laboratorio:** Máquinas virtuales (Kali Linux), servidor de pruebas configurado para HTTP y Telnet (específico del entorno de clase).

## Fases del Ejercicio y Análisis de Resultados

A continuación, se describen las fases clave del ejercicio, los pasos realizados y los principales hallazgos.

### 1. Preparación y Configuración Inicial

* **Objetivo:** Instalar y configurar Wireshark en el entorno de análisis.
* **Acciones Realizadas:** Instalación de Wireshark, identificación y selección de la interfaz de red activa para la captura de tráfico.

### 2. Análisis de Tráfico HTTP (No Cifrado)

* **Objetivo:** Demostrar la exposición de credenciales y otros datos sensibles en tráfico HTTP.
* **Acciones Realizadas:**
    * Visita a un sitio web de prueba HTTP (`http://www.celfi.gob.ar/login` o similar, si se usó este o uno equivalente accesible públicamente).
    * Introducción de credenciales de prueba (`admin`/`password123`).
    * Captura de tráfico en Wireshark.
    * **Filtros aplicados:** `http.request.method == POST`, `http.request.uri contains "login"`, `http.authbasic`.
* **Resultados Clave:** Se pudo observar claramente las credenciales (`admin` y `password123`) transmitidas en texto plano dentro de los paquetes HTTP, evidenciando la falta de seguridad.
* **Análisis de Riesgo:** Demostración directa de cómo un atacante podría interceptar y robar credenciales o información sensible en una red no cifrada.

### 3. Análisis de Tráfico HTTPS (Cifrado)

* **Objetivo:** Comparar el tráfico HTTPS con el HTTP y observar cómo el cifrado protege la información.
* **Acciones Realizadas:**
    * Acceso a una página web HTTPS (ej. `https://www.gmail.com`).
    * Intento de autenticación con credenciales ficticias.
    * Captura de tráfico en Wireshark.
    * **Filtros aplicados:** `tls`, `ssl`, `tls.handshake.type == 1`, `ssl.record.content_type == 22`.
* **Resultados Clave:** Se observaron los handshakes TLS/SSL, pero el contenido de los datos de la aplicación (credenciales, etc.) aparecía ilegible/cifrado, confirmando la protección proporcionada por HTTPS.
* **Análisis de Riesgo:** Confirmación de que, aunque el tráfico HTTPS no es completamente "invisible" (se ven los metadatos de la conexión), la información crítica está protegida.

### 4. Análisis de DNS y Resolución de Nombres

* **Objetivo:** Entender cómo Wireshark puede usarse para monitorear las consultas y respuestas DNS.
* **Acciones Realizadas:** Navegación a diferentes sitios web.
* **Filtros aplicados:** `dns`, `dns.qry.name contains "login"`, `dns.qry.type == 1`.
* **Resultados Clave:** Observación de las solicitudes y respuestas DNS, mostrando la resolución de nombres de dominio a direcciones IP.

### 5. Análisis de Telnet (No Cifrado) y SSH (Cifrado)

* **Objetivo:** Comparar el tráfico de protocolos de acceso remoto no cifrados y cifrados.
* **Consideración importante:** Esta parte del ejercicio se realizó con un **servidor de pruebas específico proporcionado en el entorno de clase**. Por razones de seguridad y replicabilidad en un entorno doméstico, no fue posible replicar la conexión a un servidor Telnet/SSH controlable de la misma manera.
* **Acciones Realizadas (en clase):**
    * Conexión a un servidor Telnet de pruebas, introducción de credenciales y ejecución de comandos.
    * Conexión a un servidor SSH de pruebas, introducción de credenciales y ejecución de comandos.
* **Resultados Clave (observados en clase):**
    * **Telnet:** Se confirmaba que todo el tráfico, incluyendo credenciales y comandos, era visible en texto plano en Wireshark (`telnet-data`).
    * **SSH:** El tráfico SSH aparecía cifrado, mostrando solo metadatos de la conexión y no el contenido de los comandos o credenciales.
* **Análisis de Riesgo:** Reforzó la importancia crítica de usar SSH en lugar de Telnet para cualquier acceso remoto para evitar la interceptación de datos sensibles.

## Conclusiones y Lecciones Aprendidas

Este ejercicio práctico con Wireshark fue invaluable para comprender la naturaleza del tráfico de red y la importancia del cifrado. Las principales lecciones aprendidas incluyen:

* **Vulnerabilidad de los Protocolos No Cifrados:** La exposición de información sensible, como credenciales, en protocolos como HTTP y Telnet es un riesgo de seguridad mayor que se puede explotar fácilmente mediante herramientas de sniffing.
* **Esencialidad del Cifrado:** HTTPS y SSH demuestran cómo el cifrado protege la confidencialidad de las comunicaciones, incluso si los atacantes pueden interceptar los paquetes, no pueden leer su contenido.
* **Habilidad de Análisis:** Wireshark es una herramienta fundamental para la inspección, depuración y análisis forense de redes, permitiendo identificar anomalías, actividades sospechosas y la efectividad de las medidas de seguridad.
* **Configuración Segura:** Refuerza la necesidad de implementar configuraciones seguras y políticas de seguridad que prioricen el uso de protocolos cifrados para proteger los datos en tránsito.
* **Limitaciones del Entorno:** Aunque no todas las partes del ejercicio pudieron ser replicadas en un entorno doméstico debido a la necesidad de servidores específicos, el conocimiento adquirido sobre el análisis y la identificación de riesgos se mantiene.

## Estado del proyecto
- [x] Terminado
- [ ] En desarrollo
- [ ] En pausa

## Autor
Ángel Mariano Álvarez López  
📧 angelmarianoalvarez@gmail.com