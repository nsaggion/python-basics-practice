"""
Ejercicio de práctica en Python
Tema: Diccionario
Nivel: Básico
"""
"""
Enunciado:
- Crea un diccionario llamado persona con las siguientes claves:
"nombre"
"edad"
"pais"
- Asigna valores inventados.
Muestra:
- El nombre
- La edad
- Pide al usuario que ingrese una clave.
- Si la clave existe en el diccionario:
Muestra su valor.
- Si no existe:
Muestra un mensaje de error.
"""

persona = {"nombre":"Antonio","edad":23,"pais":"España"}
print("El nombre",persona["nombre"],"y su edad",persona["edad"])
clave = input("Por favor, ingrese una clave: ")
if clave in persona:
    print("Su valor es:",persona[clave])
else:
    print("La clave no existe")
