"""
Ejercicio de práctica en Python.
Tema: Funciones.
Nivel: Medio.
"""
"""
Enunciado:
Abra el archivo en modo lectura ("r")
Lea todo el contenido
Lo muestre por pantalla
Cierre el archivo
"""
archivo = open("texto.txt","r")
contenido = archivo.read()
print(contenido)
archivo.close()