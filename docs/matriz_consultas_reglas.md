**1. Matriz de Consultas (Q01–Q06)**

| ID  | Qué se busca (Necesidad)                                                | Quién lo usa        | Condiciones de búsqueda (Filtros)                                       | Datos a mostrar (Campos de salida)                                           | Cómo se organiza la lista (Orden)                          | Cada cuánto se usa (Frecuencia)                     |
| --- | ----------------------------------------------------------------------- | ------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------------- |
| Q01 | Ver órdenes de trabajo activas por urgencia.                            | Técnico / Recepción | Solo estados en proceso (ej. en reparación) y nivel de urgencia.        | Número de orden, urgencia, estado, código del equipo, fecha límite.          | Las más urgentes primero, luego las más próximas a vencer. | Uso constante todos los días.                       |
| Q02 | Ver las piezas y características de un equipo específico.               | Técnico             | El código exacto del equipo.                                            | Código, tipo (ej. celular, portátil) y piezas (memoria, batería).            | No aplica (se muestra un solo registro).                   | Cada vez que ingresa un equipo.                     |
| Q03 | Buscar los servicios pedidos por un cliente en unas fechas exactas.     | Recepción           | Identificación del cliente, fecha inicial, fecha final y estado actual. | Número de orden, equipo, estado, fecha de llegada, fecha límite.             | Las fechas de llegada más recientes primero.               | Solo cuando se requiere revisar un caso específico. |
| Q04 | Detectar reparaciones retrasadas.                                       | Administrador       | Órdenes activas cuya fecha límite ya pasó.                              | Número de orden, cliente, estado, fecha límite.                              | Las fechas más antiguas primero (las más retrasadas).      | Revisión diaria.                                    |
| Q05 | Revisar el historial de reparaciones de un equipo.                      | Técnico             | El código exacto del equipo.                                            | Número de orden, estado, daño reportado, fecha de llegada, fecha de entrega. | Las reparaciones más recientes primero.                    | Cada vez que se diagnostica un daño.                |
| Q06 | Contar cuántos servicios se hicieron en un mes por tipo de dispositivo. | Administrador       | El mes exacto a evaluar.                                                | Tipo de dispositivo y la cantidad total de servicios.                        | Los tipos con más servicios primero.                       | Una vez al mes.                                     |

**2. Reglas del Negocio**

- No pueden existir dos equipos con el mismo código ni dos órdenes con el mismo número.
- Toda orden de trabajo debe estar vinculada a un cliente y a un equipo ya registrados. La persona que trae el equipo no es obligatoriamente el dueño.
- El trabajo avanza por estas etapas: recibida, en diagnóstico, en reparación, lista para entrega, cerrada o cancelada.
- Una orden está activa durante las primeras cuatro etapas. Si se cierra o cancela, deja de estar pendiente.
- La fecha límite de entrega no puede ser anterior a la fecha en que el equipo llegó al taller.
- Un equipo solo puede tener una reparación activa a la vez. Las reparaciones terminadas pasan a formar su historial.
- El historial de reparaciones de un equipo no se borra automáticamente. Se necesita una norma clara antes de eliminar información antigua.

**3. Preguntas dirigidas al cliente y Riesgo**

- **Pregunta al cliente 1:** ¿Cuántas reparaciones hacen al mes y cuánto tiempo debemos guardar la información vieja antes de borrarla?
- **Pregunta al cliente 2:** ¿Una persona puede registrar reparaciones a nombre de una empresa en lugar de a su nombre personal?

- **Riesgo identificado:** Si guardamos todas las reparaciones antiguas de un equipo en un solo registro continuo, el archivo crecerá demasiado con los años, volverá lento el sistema y superará el tamaño máximo permitido por la base de datos.

**4. Diferenciación entre regla deseada y mecanismo**

- **Regla deseada:** La orden administrativa del negocio; por ejemplo, exigir que no se repitan los códigos de los equipos.

- **Mecanismo de implementación:** La configuración técnica que se hace en la base de datos para que rechace la operación y muestre un error si alguien intenta guardar un código repetido.
