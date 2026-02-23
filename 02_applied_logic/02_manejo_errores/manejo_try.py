"""
Ejercicio de práctica en Python.
Tema: Funciones.
Nivel: Medio.
"""
"""
Enunciado:
Crea un programa que:
Pida al usuario que ingrese un número.
Convierta el valor a entero.
Si el usuario escribe algo que no sea un número:
Muestra el mensaje:
"Error: Debes ingresar un número válido."
Si no hay error:
Muestra:
"Número ingresado correctamente."
"""
try:
    num = input("Porfavor ingrese un numero: ")
    num = int(num)
except ValueError:
    print("Error: Debes ingresar un número válido.")
else:
    print("Número ingresado correctamente.")
