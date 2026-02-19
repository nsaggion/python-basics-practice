"""
Ejercicio de práctica en Python.
Tema: Funciones.
Nivel: Básico.
"""
"""
Enunciado:
Crea una función llamada sumar.
Debe recibir dos números como parámetros.
Debe devolver la suma de esos dos números usando return.
Pide dos números al usuario.
Llama a la función.
Guarda el resultado en una variable.
Muestra el resultado.
"""
def sumar(*numeros):
    total = 0;
    for i in numeros:
        total += i
    return total
numero1 = int(input("Ingrese un numero profavor: "))
numero2 = int(input("Ingrese un segundo numero para la suma profavor: "))
print("La suma de los numeros és: ",sumar(numero1,numero2))