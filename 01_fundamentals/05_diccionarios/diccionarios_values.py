"""
Ejercicio de práctica en Python
Tema: Diccionarios
Nivel: Básico
"""
"""
Crea un diccionario llamado estudiante con las siguientes claves:
"nombre"
"edad"
"curso"
Asigna valores inventados.
Muestra todos los valores del diccionario usando values().
Recorre los valores con un for y muéstralos uno por uno.
"""
estudiante = {"nombre":"Pau","edad":16,"curso":"4tESO"}
print (estudiante.values())
for valores in estudiante.values():
    print(valores)
