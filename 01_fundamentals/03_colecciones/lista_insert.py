"""
Ejercicio de práctica en Python
Tema: Listas
Nivel: Básico
"""
"""
Enunciado:
Crea una lista con los siguientes números: 10, 20, 30, 40

Luego:
- Pide al usuario que ingrese un número.
- Pide al usuario que ingrese una posición (índice).
- Inserta el número en la posición indicada usando insert().
- Muestra la lista final.
- Si la posición ingresada no es válida, muestra un mensaje de error.
"""

numeros = [10,20,30,40]

num = int(input("Porfavor, ingrese un numero: "))
posicion = int(input("Ahora ingrese la posición para el numero anterior: "))

if posicion > 4 or posicion < 0:
    print("Error, la posición ingresada no és valia")
else:
    numeros.insert(posicion,num)
    print(numeros)