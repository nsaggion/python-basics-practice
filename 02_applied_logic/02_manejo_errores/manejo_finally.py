"""
Ejercicio de práctica en Python.
Tema: Funciones.
Nivel: Medio.
"""
"""
Enunciado:
Crea un programa que:
Pida al usuario que ingrese un número.
Intente convertirlo a entero.
Si la conversión es correcta:
Muestra:
"Número válido."
Si ocurre un error:
Muestra:
"Error: Debes ingresar un número entero."
Pase lo que pase (haya error o no), el programa debe mostrar al final:
"Fin del programa."
"""
try:
    num = input ("Ingrese un numero: ")
    num = int(num)
except ValueError:
    print("Error: Debes ingresar un número entero.")
else:
    print("Número vàlido.")
finally:
    print("Final del progrma.")