import sqlite3

conexion = sqlite3.connect(":memory:")
conexion.executescript("""
    CREATE TABLE clientes(
        id INTEGER PRIMARY KEY, 
        alias TEXT
    );
    
    CREATE TABLE ordenes(
        id INTEGER PRIMARY KEY,
        cliente_id INTEGER,
        estado TEXT
    );

    INSERT INTO clientes VALUES
    (1, 'Cliente A'), (2, 'Cliente B'), (3, 'Cliente C');
    
    INSERT INTO ordenes VALUES
    (101, 1, 'recibida'), (102, 2, 'cerrada'), (103, 1, 'recibida');
""")


# Consulta:
# Relacionamos con JOIN las ordenes y clientes usando la clave foránea (cliente_id).
# Filtramos con WHERE por el estado de 'recibida'.
# Ordenamos con ORDER BY por el identificador de las ordenes.
consulta = """
    SELECT ordenes.id, clientes.alias
    FROM ordenes
    JOIN clientes ON ordenes.cliente_id = clientes.id
    WHERE ordenes.estado = 'recibida'
    ORDER BY ordenes.id;
"""

if consulta:
    print(conexion.execute(consulta).fetchall())

conexion.close()

print("\n- Explicación de las relaciones -")
print(
    "Relacioné las dos tablas utilizando el 'JOIN' y especificando con 'ON' que el campo 'cliente_id' de la tabla 'ordenes' debe ser igual al campo 'id' de la tabla 'clientes'."
)
