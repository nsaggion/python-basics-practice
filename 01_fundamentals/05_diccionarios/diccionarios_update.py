"""
Ejercicio de práctica en Python
Tema: Diccionarios
Nivel: Básico
"""
"""
Crea un diccionario llamado libro con las claves:
"titulo"
"autor"
"año"
Muestra el diccionario.
Agrega una nueva clave llamada "editorial" con un valor inventado.
Modifica el valor del "año" por otro diferente.
Muestra el diccionario actualizado.
"""
libro = {"titulo":"Random","autor":"Estanislao Bachrach","año":2018}
print("El siguiente diccionario continene",libro)
libro.update({"editorial":"Grijalbo","año":2019})
print("Diccionario actualizado",libro)