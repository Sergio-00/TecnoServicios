import json

texto_original = '{"codigo":"OS-001", "prioritaria":True, "fallas":["No enciende",]}'

# 1. Intenta cargar texto con json.loads.
print("- 1. Intento inicial -")
try:
    datos = json.loads(texto_original)
except Exception as error:
    print("El código fallo...\nEl error fue:", error)

# 2. Registra el error y corrige la sintaxis sin cambiar su intención.
# Correcciones:
# - El "True" debe ser "true".
# - Quitar la coma al final de "No enciende".
texto_corregido = '{"codigo":"OS-001", "prioritaria":true, "fallas":["No enciende"]}'

# 3. Muestra codigo, prioritaria y los tipos de ambos valores.
print("\n- 3. Resultado corregido -")
datos = json.loads(texto_corregido)
codigo = datos["codigo"]
prioritaria = datos["prioritaria"]

print(f"Código: {codigo} (Tipo de dato: {type(codigo)})")
print(f"Prioritaria: {prioritaria} (Tipo de dato: {type(prioritaria)})")

# 4. Explica las correcciones realizadas.
print("\n- 4. Explicación de las correcciones -")
print(
    "En los JSON se requiere que los booleanos se escriban en minúscula 'true' y no 'True' mayuscula como en Python."
)
print(
    "Además, JSON no permite comas al final del último elemento de un arreglo o diccionario."
)
