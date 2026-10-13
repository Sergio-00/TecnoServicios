**Matriz de selección de modelos NoSQL**

| Caso                         | Modelo propuesto                 | Razón vinculada a una consulta                                                                                                                                            | Límite o costo                                                                                                                                  | Alternativa      |
| ---------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| Catálogo de dispositivos     | Documental (MongoDB)             | Un portátil usa RAM y un teléfono usa batería. Este modelo guarda los atributos diferentes en un solo documento JSON sin requerir columnas vacías para todos los equipos. | Si el historial de un equipo se anida infinitamente en su documento como un arreglo, superará los límites de tamaño y degradará el rendimiento. | Relacional (SQL) |
| Sesiones temporales          | Clave-valor (Redis)              | Guarda y recupera un dato temporal con fecha de vencimiento utilizando exclusivamente un identificador único (clave).                                                     | Es imposible realizar filtros sobre el contenido interno del dato; la búsqueda solo funciona si se conoce la clave exacta.                      | Documental       |
| Recorridos de relaciones     | Grafos (Neo4j)                   | Evalúa conexiones directas en red, como buscar qué técnico disponible tiene la habilidad específica para el servicio requerido.                                           | La configuración de la infraestructura y el mantenimiento del servidor son más complejos que en un motor documental.                            | Relacional (SQL) |
| Lecturas masivas por periodo | Familias de columnas (Cassandra) | Almacena altos volúmenes de datos históricos continuos para ser consultados a gran velocidad bajo un patrón de lectura ya definido.                                       | Estructura rígida; si cambian las preguntas o los filtros que necesita hacer el negocio, obliga a rediseñar la base de datos.                   | Documental       |

**Situación para conservar SQL**

- **Caso:** Facturación y pagos.

- **Justificación:** El manejo contable requiere un motor relacional estricto que garantice transacciones completas (todo o nada) y evite fallos de integridad, asegurando que no existan pagos asociados a facturas inexistentes.
