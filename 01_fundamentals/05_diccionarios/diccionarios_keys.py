"""
Ejercicio de práctica en Python
Tema: Diccionarios
Nivel: Básico
"""
"""
Enunciado:
Crea un diccionario llamado producto con las siguientes claves:
"nombre"
"precio"
"stock"
Asigna valores inventados.
Muestra todas las claves del diccionario usando keys().
Recorre las claves con un for y muéstralas una por una.
"""
producto = {"nombre":"Lapices","precio":1,"stock":"maximo"}
print("Las claves de producto són: ",producto.keys())
for i in producto:
    print(i)