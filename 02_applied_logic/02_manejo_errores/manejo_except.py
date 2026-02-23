"""
Ejercicio de práctica en Python.
Tema: Funciones.
Nivel: Medio.
"""
"""
Enunciado:
Crea un programa que:
Pida al usuario que ingrese dos números.
Conviértelos a enteros.
Realiza la división del primero entre el segundo.
Muestra el resultado.
"""
try:
    num1 = input("Ingrese el primer numero: ")
    num2 = input("ingrese el segundo numero: ")
    num1 = int(num1)
    num2 = int(num2)
    resultado = num1 / num2
except ValueError:
    print("Error: Debes ingresar números válidos.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
else:
    print(resultado)