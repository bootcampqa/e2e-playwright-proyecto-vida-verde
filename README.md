# Proyecto QA Manual y Automatizado de la web Bootcamp QA

En este proyecto se ha llevado a cabo un proceso completo de aseguramiento de la calidad (QA) sobre la funcionalidad principal de la web: https://bootcampqa.com
El proyecto se ha realizado en equipo siguiendo metodología ágil Scrum y BDD para el diseño de las pruebas antes del desarrollo, siguiendo buenas prácticas de testing.

## Plan de Pruebas, resultados y reporte de errores: [Ver Plan de Pruebas](https://github.com/Bootcamp-QA/plandepruebas.html)
En este documento se detalla el plan de pruebas, las funcionalidades probadas, el resultado de las pruebas ejecutadas y el reporte de errores.


## Automatización E2E - Tecnologías

- ![Python](https://img.shields.io/badge/Python-3.12%2B-blue)  
- ![Playwright](https://img.shields.io/badge/Playwright-v1.48-green)

## Resultados de las pruebas automatizadas

Se ha configurado un flujo de integración continua con github actions que ejecuta las pruebas después de cada cambio y una vez a la semana al final de cada sprint. Puede consultar en este enlace el resultado de la ultima ejecucion de pruebas y descargar el reporte de los resultados de las pruebas:

![Test Workflow](https://github.com/Bootcamp-QA/playwright-python-template/actions/workflows/playwright_tests.yml/badge.svg)

## Requisitos del Proyecto

### Python 3.12

Descarga e instala Python versión 3.12 desde su web oficial (https://www.python.org/downloads/)
Asegurate que Python se añade al PATH durante la instalación.


### Instalar Dependencias

Una vez instalado Python:

Clona este repositorio.

Accede a la carpeta del proyecto.

Ejecuta en la terminal:

``
pip install -r requirements.txt
``

``
playwright install
``


### Ejecutar los tests en local
Accede a la carpeta del proyecto.

Ejecuta en la terminal:

`pytest --headed`
