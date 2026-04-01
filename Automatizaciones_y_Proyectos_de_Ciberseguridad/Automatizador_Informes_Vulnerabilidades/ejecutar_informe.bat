@echo off
echo ============================================================
echo   GENERADOR DE INFORMES DE VULNERABILIDADES v2
echo ============================================================
echo.

:: --- CONFIGURACION FIJA ------------------------------------------------------
set EXCEL=datos_prueba_1000_vulns.xlsx
:: -----------------------------------------------------------------------------

:: --- DATOS QUE CAMBIAN EN CADA EJECUCION -------------------------------------
set /p EMPRESA=Nombre de la empresa:
set /p PERIODO=Periodo del informe (ej: Marzo 2026):
:: -----------------------------------------------------------------------------

echo.

if "%EMPRESA%"=="" (
    echo [ERROR] El nombre de empresa no puede estar vacio.
    pause
    exit /b 1
)

if "%PERIODO%"=="" (
    echo [ERROR] El periodo no puede estar vacio.
    pause
    exit /b 1
)

echo Empresa : %EMPRESA%
echo Periodo : %PERIODO%
echo Excel   : %EXCEL%
echo.

:: Instalar dependencias si no estan
echo [INFO] Verificando dependencias...
pip install -r requirements.txt --quiet
echo.

python generar_informe.py "%EXCEL%" "%EMPRESA%" "%PERIODO%"

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] El script termino con errores. Revisa informe_generator.log
) else (
    echo.
    echo [OK] Informe generado correctamente.
)

echo.
pause
