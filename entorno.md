# Registro de Entorno y Exploración (Actividad A4)

## 1. Especificaciones del Sistema

- **Sistema Operativo:** Windows 10
- **Versión de Python:** 3.14.6
- **Versión de Git:** 2.55.0.windows.3
- **Versión de mongosh:** 2.13.0
- **Servidor MongoDB:** MongoDB Community Server 9.0.2

## 2. Errores Corregidos y Dificultades

- **Síntoma:** Error de conexión (Connection refused) al intentar ejecutar `mongosh` hacia `127.0.0.1:27017`.
- **Causa diagnosticada:** Ausencia del servidor local activo o instancia proporcionada en ese puerto.
- **Acción correctiva:** Se descargó e instaló MongoDB Community Server localmente. Dado que la guía asume una configuración previa del instructor, fue necesario crear manualmente la base de datos y el usuario de práctica para habilitar la autenticación requerida.

## 3. Configuración Autónoma del Entorno

Para habilitar el acceso autenticado exigido por la práctica, se ejecutaron los siguientes comandos como administrador local antes de iniciar la prueba:

```javascript
use tecnoservicios_lab

db.createUser({
  user: "aprendiz_nosql",
  pwd: "[CONTRASEÑA_AQUI]",
  roles: [
    { role: "readWrite", db: "tecnoservicios_lab" }
  ]
})
```

## 4. Conexión a la Base de Datos

**Comando de conexión utilizado:**

```bash
mongosh "mongodb://127.0.0.1:27017/tecnoservicios_lab" --username aprendiz_nosql --authenticationDatabase tecnoservicios_lab

```

**Resultados de la comprobación de conectividad:**

```javascript
// db = db.getSiblingDB("tecnoservicios_lab");
tecnoservicios_lab;

// db.runCommand({ping: 1});
{
  ok: 1;
}

// db.getName();
tecnoservicios_lab;
```

## 5. Ejecución de Exploración (01_explorar.js)

**Comando de conexión utilizado:**

```bash
mongosh "mongodb://127.0.0.1:27017/tecnoservicios_lab" --username aprendiz_nosql --authenticationDatabase tecnoservicios_lab --file scripts/01_explorar.js
```

**Resultados de la ejecución:**

```javascript
{
  _id: 'OS-DEMO-001',
  cliente_alias: 'Cliente ficticio 01',
  equipo: {
    codigo: 'EQ-DEMO-001',
    tipo: 'portatil',
    accesorios_recibidos: [
      'cargador',
      'estuche'
    ]
  },
  falla_reportada: 'No enciende',
  prioridad: 'alta',
  estado: 'recibida',
  requiere_diagnostico: true,
  fecha_ingreso: ISODate('2026-10-06T13:00:00.000Z')
}
1
true
```
