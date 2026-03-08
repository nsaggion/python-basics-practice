"""
Ejercicio de práctica en Python.
Tema: Importación.
Nivel: Medio.
"""
"""
Archivo que contine modulos con operaciones basicas.
"""
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

if __name__ == "__main__":
    print("Probando módulo operaciones...\n")
    a = 10
    b = 5

    print("Suma:", sumar(a, b))
    print("Resta:", restar(a, b))
    print("Multiplicación:", multiplicar(a, b))

    try:
        print("División:", dividir(a, b))
    except ZeroDivisionError:
        print("No se puede dividir por cero")