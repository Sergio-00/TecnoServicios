ordenes = [
    {"codigo": "OS-001", "prioridad": "alta", "pendiente": True},
    {"codigo": "OS-002", "prioridad": "normal", "pendiente": True},
    {"codigo": "OS-003", "prioridad": "alta", "pendiente": False},
    {"codigo": "OS-004", "prioridad": "alta"},
]


def seleccionar_pendientes(registros, prioridad):
    # Retorna códigos de la prioridad indicada con pendiente exactamente True.
    # No modifiques la lista recibida. Define qué ocurre si falta el campo.
    resultados = []
    for reg in registros:
        if reg.get("prioridad") == prioridad and reg.get("pendiente") is True:
            resultados.append(reg["codigo"])
    return resultados


# Pruebas con resultados y sin resultados
print("Prueba con resultados (Alta):", seleccionar_pendientes(ordenes, "alta"))
print("Prueba sin resultados (Baja):", seleccionar_pendientes(ordenes, "baja"))

print("\n- Explicación -")
print(
    "Para el campo ausente en OS-004 se utilizo el metodo de diccionario '.get(\"pendiente\")'. Si el campo no existe, esto devuelve 'None' sin que el programa falle."
)
print(
    'No se debe confundir una cadena con un booleano porque no son equivalentes, la validación se debe hacer con \'is True\'. Si alguien pusiera "pendiente": "True", la condición fallaría.'
)
