"""
Ejercicio de práctica en Python.
Tema: Funciones.
Nivel: Medio.
"""
"""
Enunciado:
Crea una función anónima (lambda) que:
Reciba un número.
Devuelva el cuadrado de ese número.
Pide un número al usuario.
Usa la función lambda para calcular el cuadrado.
Muestra el resultado.
"""
operacion = lambda x: x ** 2
numero = int(input("Profavor ingrese un número: "))
print("El cuadrado del número introducido és:",operacion(numero))
