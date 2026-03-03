"""
Ejercicio de práctica en Python.
Tema: Importación.
Nivel: Medio.
"""
"""
Enunciado:
Crea las siguientes funciones:
sumar(a, b)
restar(a, b)
multiplicar(a, b)
dividir(a, b) (maneja división por cero)
Agrega un bloque:
if __name__ == "__main__":
Dentro de ese bloque:
- Pide dos números al usuario
- Pide una operación (+, -, *, /)
Muestra el resultado usando tus funciones
"""
def suma(a,b):
    return a + b
def restar(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    return a / b
if __name__ == "__main__":
    try:
        num1 = int(input("Ingrese un numero porfavor: "))
        num2 = int(input("Ingrese otro numero porfavor: "))
    except ValueError:
        print("Error: Debes ingresar números válidos.")
    else:
        operacion = input("Ingrese una operación de la sigüentes operaciones: +, -, *, /: ")
        if  operacion == "+": print("El resultado final és: ",suma(num1,num2))
        elif operacion == "-": print("El resultado final és: ",restar(num1,num2))
        elif operacion == "*": print("El resultado final és: ",multiplicar(num1,num2))
        elif operacion == "/":
            try:
                resultado = dividir(num1,num2)
                print("El resultado final és: ", resultado)
            except ZeroDivisionError:
                print("Error: No se puede dividir por cero.")
        else: print("Signo de operación incorrecto.")