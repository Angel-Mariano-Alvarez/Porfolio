@echo off
REM --- Forzar codificacion UTF-8 para ver caracteres correctamente ---
chcp 65001 > nul
REM --------------------------------------------------------

cd /d "%~dp0"

echo.
echo ===============================================================
echo   GENERADOR DE INFORMES DE VULNERABILIDADES
echo ===============================================================
echo.

REM --- CONFIGURACION DE API KEY ---
REM INSTRUCCIONES: Reemplaza "TU_API_KEY_AQUI" con tu clave real de NVD.
REM Consiguela gratis en: https://nvd.nist.gov/developers/request-an-api-key
REM NO subo mi clave real a repositorios publicos.

set NVD_API_KEY=INGRESA AQUI LA CLAVE QUE CONSEGUISTE

echo [INFO] API Key de NVD cargada.
echo.

REM Solicitar datos al usuario
set /p archivo="Ingresa el nombre del archivo Excel (ej: vulnes.xlsx): "
set /p infraestructura="Ingresa el nombre de la Organizacion (ej: Empresa S.L): "
set /p mesanio="Ingresa periodo de analisis (ej: Noviembre 2025): "

REM Ejecutar el script
echo.
echo [INFO] Iniciando generacion de informe...
echo.

python generar_informe.py "%archivo%" "%infraestructura%" "%mesanio%"

echo.
echo ===============================================================
echo [SUCCESS] PROCESO COMPLETADO
echo ===============================================================
echo.

pause