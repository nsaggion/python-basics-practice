"""
Ejercicio de práctica en Python
Tema: Diccionarios
Nivel: Básico
"""
"""
Crea un diccionario llamado auto con las siguientes claves:
"marca"
"modelo"
"año"
Asigna valores inventados.
Recorre el diccionario usando items().
Muestra cada elemento con el siguiente formato:
La clave es ___ y su valor es ___
"""
auto = {"marca":"Toyota","modelo":"Corolla","año":1966}
for clave, valor in auto.items():
    print("La clave es",clave, "y su valor es",valor)