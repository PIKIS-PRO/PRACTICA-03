# Práctica 03 – Pruebas Automatizadas con Python
**Estudiante:** Martín Pico

## Descripción
Proyecto realizado para validar cálculos sobre el archivo `sri_ventas_2024.csv` mediante pruebas unitarias y medición de cobertura.  
Se desarrolló una clase que procesa las ventas por provincia y se evaluó su funcionamiento usando `unittest` y `coverage`.

## Estructura

src/procesador.py
tests/test_procesador.py
datos/sri_ventas_2024.csv
app.py


## Ejecución de Pruebas
```bash
python3 -m unittest discover

Cobertura de Código

coverage run -m unittest discover
coverage report
coverage html

La carpeta htmlcov/ contiene el informe visual de cobertura.
Resultados

    Pruebas ejecutadas correctamente.

    Cobertura total del proyecto: 96%.

Conclusión

Se comprobó que las funciones de análisis funcionan correctamente, y que las pruebas automatizadas y la medición de cobertura ayudan a verificar el comportamiento del código.