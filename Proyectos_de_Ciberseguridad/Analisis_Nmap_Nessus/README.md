
# Análisis de Vulnerabilidades con Nmap y Nessus

## Descripción
Este proyecto forma parte del curso IFCT0050 – Ciberseguridad avanzada en entornos de las tecnologías de la operación (SEPE). El objetivo fue llevar a cabo un análisis de vulnerabilidades en un entorno virtualizado usando las herramientas Nmap y Nessus, simulando un escenario realista de auditoría.

## Entorno de red

![Diagrama de red](diagrama_red_nmap_nessus.png)

- **Plataforma de virtualización**: VMware Workstation 17.6.3
- **Máquinas virtuales**:
  - **Kali Linux** (2025-W23) – IP: `192.168.1.144` (auditoría + Nessus)
  - **Windows 11** (Win11_24H2) – IP: `192.168.1.147`
  - **Metasploitable2** – IP: `190.168.1.146`

## Fases del ejercicio

### 1. Verificación de conectividad

Se realizaron pruebas de `ping` desde Kali y Windows hacia la máquina Metasploitable2.

- ![Ping Kali](Captura_ping_Kali.PNG)
- ![Ping Windows](Captura_ping_windows.PNG)

### 2. Escaneo con Nmap

Se ejecutó un escaneo para identificar puertos abiertos y servicios visibles:

📄 [`resultados_nmap.txt`](resultados_nmap.txt)

### 3. Análisis de vulnerabilidades con Nessus

Se ejecutó un escaneo completo desde Nessus Essentials, instalado en Kali Linux, exportando el informe de vulnerabilidades encontradas:

📄 [`resultados_nessus.txt`](resultados_nessus.txt)

### 4. Comparativa entre herramientas

Se redactó un documento comparativo para identificar fortalezas y limitaciones de cada herramienta:

📄 [`comparativa_nmap_nessus.md`](comparativa_nmap_nessus.md)

## Conclusión

Este laboratorio permitió:

- Simular un entorno de pentesting real
- Evaluar la detección de servicios y vulnerabilidades
- Analizar el impacto de herramientas combinadas (Nmap + Nessus)
- Practicar la documentación técnica y la redacción de informes

## Estado del proyecto
- [x] Terminado
- [ ] En desarrollo
- [ ] En pausa

## Autor
Ángel Mariano Álvarez López  
📧 angelmarianoalvarez@gmail.com
