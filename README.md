# TecnoServicios y Bases de Datos NoSQL

Este repositorio contiene las evidencias de la Actividad E01 correspondientes al diagnóstico, fundamentos y entorno de trabajo del caso integrador TecnoServicios.

## Estructura del Proyecto

- `docs/`: Contiene la matriz de selección de modelos NoSQL y la matriz de formulación de reglas y consultas del negocio.
- `scripts/`: Almacena el código fuente de ejecución para la base de datos (`01_explorar.js`).
- `evidencias/`: Contiene el registro del entorno técnico (`entorno.md`), evidencias de conexión y ejecución de comandos sin exponer secretos.
- `diagnostico_nosql/`: Respuestas y archivos del diagnóstico de aprendizajes previos (entregado individualmente).

## Requisitos del Entorno

- Python 3.14.6
- Git 2.55.0
- MongoDB Community Server local activo en el puerto `27017`
- Cliente `mongosh`

## Instrucciones de Ejecución

El script de exploración inicial se conecta a la base de datos `tecnoservicios_lab` de forma autenticada. Ejecute el siguiente comando en la terminal desde la raíz del proyecto e ingrese la contraseña de la cuenta `aprendiz_nosql` cuando el sistema lo solicite:

```bash
mongosh "mongodb://127.0.0.1:27017/tecnoservicios_lab" --username aprendiz_nosql --authenticationDatabase tecnoservicios_lab --file scripts/01_explorar.js
```
