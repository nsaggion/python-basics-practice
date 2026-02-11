"""
Ejercicio de práctica en Python
Tema: Tupla
Nivel: Básico
"""
""""
Enunciado:
Crea la siguiente tupla:
- ("Ana", "Luis", "Carlos", "Marta", "Sofía")
Pide al usuario que ingrese un nombre.
Si el nombre existe en la tupla:
- Muestra la posición en la que se encuentra usando el método index().
Si el nombre no existe:
- Muestra un mensaje indicando que no se encontró.
"""""

nombre = ("Ana", "Luis", "Carlos", "Marta", "Sofía")
nombreUser = input("Por favor ingrese un nombre: ")

if nombreUser in nombre:
    print("La posicion en la que se encuentra es:",nombre.index(nombreUser)+1)
else:
    print("No se encontró")