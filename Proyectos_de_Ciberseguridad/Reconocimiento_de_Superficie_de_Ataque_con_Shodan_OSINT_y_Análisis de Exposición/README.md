# Reconocimiento de Superficie de Ataque con Shodan: OSINT y Análisis de Exposición

## Descripción del Proyecto

Este proyecto forma parte de mi formación en Seguridad Informática (IFCT0050 del SEPE) y se centra en el uso de Shodan, un motor de búsqueda de dispositivos conectados a Internet, para realizar tareas de reconocimiento pasivo y evaluar la superficie de ataque externa. Simulando el rol de un consultor de seguridad, mi objetivo fue identificar qué información sobre infraestructuras está públicamente accesible y qué riesgos de seguridad puede representar esta exposición.

El ejercicio busca demostrar la importancia de la Inteligencia de Fuentes Abiertas (OSINT) en ciberseguridad y la necesidad crítica de una configuración segura de los servicios expuestos en Internet.

## Tecnologías Utilizadas

* **Herramienta Principal:** Shodan (interfaz web)
* **Conceptos Aplicados:** Reconocimiento pasivo, OSINT, análisis de vulnerabilidades, evaluación de riesgos, concienciación sobre exposición de servicios.

## Fases del Ejercicio y Análisis de Resultados

A continuación, se presentan las búsquedas más significativas realizadas en Shodan, destacando su propósito, los resultados clave obtenidos y la evaluación del riesgo asociado.

### 1. Exploración Inicial y Visión Global

* **Objetivo:** Familiarizarse con el dashboard de Shodan y comprender las estadísticas globales de exposición de dispositivos.
* **Resultados Clave:** Observación de la distribución geográfica de dispositivos, los puertos más comunes y las organizaciones con mayor presencia.
* **Análisis de Riesgos:** Esta fase inicial ayuda a contextualizar la magnitud de la exposición global y subraya cómo los atacantes pueden obtener una visión general de las tecnologías y los patrones de implementación.

### 2. Identificación de Servicios Específicos por Ubicación (España)

* **Consulta:** `country:ES port:80,443,22,21,3389`
* **Propósito:** Analizar la exposición de servicios comunes (Web HTTP/S, SSH, FTP, RDP) en el territorio español. Permite identificar la infraestructura básica de red expuesta por país y por ciudad.
* **Resultados Clave:**
    * **Resultados totales:** 1,109,976 dispositivos con alguno de los puertos especificados abiertos en España.
    * **Distribución por ciudades principales:**
        * Madrid: 583,861
        * Barcelona: 95,642
        * Valencia: 34,120
        * Zaragoza: 29,871
        * Sevilla: 15,743
    * Esto indica una significativa superficie de ataque externa en España, concentrada principalmente en grandes núcleos urbanos.
* **Análisis de Riesgos:** La exposición de estos puertos es común, pero una mala configuración, el uso de versiones obsoletas de software, o la presencia de credenciales débiles puede llevar a accesos no autorizados. Especial atención a los servicios FTP (puerto 21) y RDP (puerto 3389) por su historial de vulnerabilidades y su frecuente uso en movimientos laterales por parte de atacantes. La alta concentración en ciudades clave representa un objetivo atractivo para actores maliciosos.
* **Captura de Pantalla:** ![Consulta country:ES](Captura%20consulta-country-ES.PNG)

### 3. Dispositivos con Configuraciones Inseguras (Credenciales por defecto)

* **Consulta:** `city:"Madrid" "default password"`
* **Propósito:** Identificar dispositivos o servicios que están utilizando credenciales por defecto en una ubicación específica.
* **Resultados Clave:** Se encontró **1 dispositivo** con esta condición en Madrid. Este hallazgo, aunque numéricamente pequeño, es crítico, ya que un solo dispositivo con credenciales por defecto representa una brecha de seguridad grave.
* **Análisis de Riesgos:** **Riesgo ALTO/CRÍTICO.** El uso de contraseñas por defecto es una de las vulnerabilidades más fáciles de explotar, permitiendo el acceso no autorizado inmediato a sistemas que podrían contener información sensible o ser utilizados como punto de pivote para ataques internos. Es una señal clara de malas prácticas de seguridad y una oportunidad de ataque de bajo esfuerzo para un adversario. Incluso un único dispositivo mal configurado puede comprometer toda una red.
* **Captura de Pantalla:** ![Default Password Madrid](Captura%20consulta-city-MAD.PNG)

### 4. Búsqueda de Vulnerabilidades Conocidas (CVEs) y Limitaciones

* **Propósito:** La intención era localizar sistemas públicamente accesibles que fueran vulnerables a CVEs específicos, como EternalBlue (MS17-010), Heartbleed (CVE-2014-0160) y Shellshock (CVE-2014-6271), para comprender la persistencia de vulnerabilidades conocidas en la red.
* **Limitaciones Encontradas:** No fue posible realizar directamente búsquedas utilizando el filtro `vuln:` (`vuln:ms17-010`, `vuln:CVE-2014-0160`, `vuln:CVE-2014-6271`) con la cuenta gratuita de Shodan. Esta funcionalidad está típicamente reservada para usuarios con cuentas de pago o con privilegios académicos/de investigación.
* **Análisis de Importancia (a pesar de la limitación):** Aunque no se pudieron ejecutar estas consultas directamente, la importancia de esta fase es crítica. La existencia de sistemas con vulnerabilidades antiguas pero no parcheadas representa un **riesgo CRÍTICO**. Un atacante con una cuenta Shodan completa podría identificar estos sistemas fácilmente y explotarlos para ejecutar código remoto, filtrar información sensible o propagar malware. Esto subraya la vital importancia de:
    * Una gestión de parches rigurosa y continua.
    * La monitorización de la exposición de la infraestructura frente a CVEs conocidos.
    * La conciencia de que las herramientas, incluso en sus versiones básicas, ofrecen solo una parte del panorama completo.
    

### 5. Identificación de Dispositivos por Fabricante/Producto

* **Consulta:** `product:"MikroTik RouterOS"`
* **Propósito:** Identificar la cantidad y distribución global de dispositivos de red de un fabricante específico, como MikroTik, para comprender su exposición y el impacto potencial de vulnerabilidades en sus productos.
* **Resultados Clave:**
    * **Resultados totales:** 312,080 dispositivos MikroTik RouterOS expuestos globalmente.
    * **Países con mayor exposición:**
        * Brasil: 29,614
        * Rusia: 24,589
        * China: 20,297
        * India: 17,750
        * Indonesia: 15,610
    * Esta vasta cantidad de dispositivos expuestos a nivel mundial, con una alta concentración en ciertos países, indica una superficie de ataque significativa para posibles vulnerabilidades específicas de RouterOS.
* **Análisis de Riesgos:** La visibilidad masiva de dispositivos de un fabricante específico representa un riesgo elevado si se descubre una vulnerabilidad crítica en su software. Permite a los atacantes identificar fácilmente un gran número de objetivos potenciales. Un gran volumen de dispositivos, a menudo con paneles de administración accesibles, también puede ser objeto de ataques de fuerza bruta o de explotaciones dirigidas si no se configuran de forma segura (ej., uso de contraseñas robustas, cierre de puertos no esenciales, actualizaciones de firmware).
* **Captura de Pantalla:** ![MikroTik Exposure](Captura%20consulta-product-Mikrotik.PNG)

## Conclusiones y Lecciones Aprendidas

Este ejercicio con Shodan ha sido fundamental para comprender la importancia del **reconocimiento pasivo** como primera línea en la evaluación de la seguridad. Me ha permitido visualizar la inmensa cantidad de información y dispositivos expuestos públicamente en Internet, muchos de ellos con configuraciones inseguras o vulnerabilidades críticas no parcheadas.

Las principales lecciones aprendidas incluyen:

* La capacidad de Shodan para actuar como una poderosa herramienta de **inteligencia de amenazas y OSINT**, permitiendo a los atacantes (y defensores) escanear rápidamente la superficie global de Internet en busca de objetivos específicos.
* La **crítica necesidad de una configuración segura ("hardening")** de cualquier sistema o servicio expuesto a Internet, incluyendo la eliminación de contraseñas por defecto y la deshabilitación de servicios innecesarios.
* La vital importancia de una **gestión de parches rigurosa y continua** para proteger contra vulnerabilidades conocidas que, años después de su descubrimiento, siguen siendo un vector de ataque.
* El valor de combinar la información de Shodan con bases de datos de vulnerabilidades (CVEs) para realizar una evaluación de riesgo más precisa.
* **La realidad de las limitaciones de las herramientas en versiones gratuitas/básicas**, lo cual es una consideración importante en cualquier contexto de seguridad, requiriendo a menudo la combinación de múltiples fuentes o la inversión en licencias completas.

## Estado del proyecto
- [x] Terminado
- [ ] En desarrollo
- [ ] En pausa

## Autor
Ángel Mariano Álvarez López  
📧 angelmarianoalvarez@gmail.com

---

---