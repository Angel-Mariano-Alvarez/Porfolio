# Proyectos de Ciberseguridad

Esta carpeta está dedicada a recopilar proyectos y ejercicios prácticos realizados en el ámbito de la seguridad informática y ciberseguridad. Mi objetivo es aplicar los conocimientos adquiridos, demostrando habilidades en el análisis de vulnerabilidades, configuración segura de sistemas, scripting para seguridad y otras áreas clave.

Este repositorio se mantiene vivo y se irá actualizando periódicamente con nuevos desarrollos propios, laboratorios y pruebas de concepto (PoC).

## Proyectos Incluidos

### 1. Análisis de Vulnerabilidades con Nmap y Nessus
* **Descripción:** Este proyecto aborda la configuración de un laboratorio de ciberseguridad y la realización de un análisis de vulnerabilidades utilizando herramientas estándar de la industria como Nmap para el reconocimiento de red y Nessus para un escaneo más exhaustivo. Incluye la interpretación de resultados y la elaboración de un informe ejecutivo simulado.
* **Tecnologías Clave:** Kali Linux, Metasploitable3, Nmap, Nessus.
* **Estado:** Completado (primer ejercicio del curso de Seguridad Informática).
* **Enlace al Proyecto:** [Ver Proyecto](./Analisis_Nmap_Nessus)

### 2. Reconocimiento de Superficie de Ataque con Shodan: OSINT y Análisis de Exposición
* **Descripción:** Este proyecto se centra en el uso de Shodan, un motor de búsqueda de dispositivos conectados a Internet, para realizar tareas de reconocimiento pasivo y evaluar la superficie de ataque externa. Simula el rol de un consultor de seguridad para identificar información públicamente accesible sobre infraestructuras y los riesgos de seguridad asociados a esta exposición, demostrando la importancia de la Inteligencia de Fuentes Abiertas (OSINT) y la configuración segura de servicios.
* **Tecnologías Clave:** Shodan (interfaz web), OSINT, análisis de vulnerabilidades, evaluación de riesgos.
* **Estado:** Completado (ejercicio del curso de Seguridad Informática).
* **Enlace al Proyecto:** [Ver Proyecto](./Reconocimiento_de_Superficie_de_Ataque_con_Shodan_OSINT_y_An%C3%A1lisis%20de%20Exposici%C3%B3n)

### 3. Análisis de Tráfico de Red con Wireshark: Protocolos Cifrados vs. No Cifrados
* **Descripción:** Proyecto enfocado en el uso de Wireshark para capturar y analizar tráfico de red, demostrando la diferencia crítica entre la seguridad de protocolos cifrados (HTTPS, SSH) y la vulnerabilidad de protocolos no cifrados (HTTP, Telnet) ante la interceptación de datos sensibles.
* **Tecnologías Clave:** Wireshark, protocolos de red (HTTP, HTTPS, Telnet, SSH, DNS), análisis de paquetes.
* **Estado:** Completado (ejercicio realizado en entorno de laboratorio en clase).
* **Enlace al Proyecto:** [Ver Proyecto](./An%C3%A1lisis_de_Tr%C3%A1fico_de_Red_con_Wireshark)

### 4. SSH Seguro y Robusto: Clave Pública, Banner Legal, UFW, Fail2Ban y Port Knocking
* **Descripción:** Proyecto integral de hardening del acceso SSH en Kali Linux. Incluye cambio de puerto, desactivación de login por root, autenticación por clave pública, configuración de firewall UFW, sistema de port knocking con knockd y protección contra fuerza bruta con Fail2Ban. Además, se incorpora un banner legal, un sistema de monitorización de logs en tiempo real y secuencias de emergencia.
* **Tecnologías Clave:** Kali Linux, OpenSSH, UFW, Fail2Ban, Knockd, SSH-keygen, PuTTY.
* **Estado:** Completado (ejercicio avanzado del curso SEPE IFCT0050).
* **Enlace al Proyecto:** [Ver Proyecto](./SSH_Seguro_y_Robusto)

### 5. Automatizador de Informes de Vulnerabilidades (Tooling & Python)
* **Descripción:** Herramienta de desarrollo propio (CLI) diseñada para automatizar la fase de documentación en auditorías. El script ingesta datos en bruto, enriquece la información consultando la **API del NIST NVD** (con gestión de caché inteligente) y genera automáticamente informes ejecutivos en Word con gráficos estadísticos y tablas de detalle. Demuestra capacidad de programación defensiva y automatización de procesos.
* **Tecnologías Clave:** Python 3, Pandas (Data Analysis), Matplotlib (Visualization), REST API, Python-Docx.
* **Estado:** Completado (Desarrollo propio de Tooling).
* **Enlace al Proyecto:** [Ver Proyecto](./Automatizador_Informes_Vulnerabilidades)

### 6. Automatizador Servidor ALerta Vulnerabilidades (NVD Scanner & Email Alerts)
* **Descripción:** Servicio de vigilancia digital (Daemon) diseñado para la monitorización continua de nuevas vulnerabilidades. El sistema consulta la API del NIST en tiempo real, filtra CVEs críticos basándose en los fabricantes de la organización y envía alertas automáticas por correo electrónico. Implementa persistencia con SQLite, rotación de logs y medidas de seguridad operacional (OpSec) para despliegues en servidores Linux.
* **Tecnologías Clave:** Python 3, Systemd (Linux Services), SQLite, NIST API, SMTP, Logging, Regex.
* **Estado:** Completado (Desarrollo propio de Tooling & DevSecOps).
* **Enlace al Proyecto:** [Ver Proyecto](./Automatizador_Servidor_ALerta_Vulnerabilidades)

## Estado de la Carpeta

-   [x] Primer proyecto añadido y documentado.
-   [x] Segundo proyecto (Shodan) añadido y documentado.
-   [x] Tercer proyecto (Wireshark) añadido y documentado.
-   [x] Cuarto proyecto (SSH Seguro) añadido y documentado.
-   [x] Quinto proyecto (Automatizador Python) añadido y documentado.
-   [x] Sexto proyecto (Sistema de Alertas) añadido y documentado.
-   [ ] Inclusión de nuevos proyectos personales y laboratorios avanzados.

---
> Angel Mariano Álvarez López  
> angelmarianoalvarez@gmail.com  
> [LinkedIn](https://www.linkedin.com/feed/?trk=guest_homepage-basic_google-one-tap-submit)