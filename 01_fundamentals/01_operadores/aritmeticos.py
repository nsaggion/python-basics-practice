"""
Ejercicio de práctica en Python
Tema: Operadores aritméticos
Nivel: Básico
"""

"""
Enunciado; Pedir usuario dos numeros, Pide al usuario dos números enteros y muestra por pantalla:
- la suma
- la resta
- la multiplicación
- la división
"""

# Pedir a usuarios numero
num1 = input ("Introduce primer numero; ")
num2 = input ("Intoducce segundo nuemro; ")

# Conversión a nuemro.
num1 = int(num1)
num2 = int(num2)

# Salida de pantalla resultados de la operación.
print("Suma;", num1 + num2)
print("Resta;", num1 - num2)
print("Multipicación;", num1 * num2)

if num2 == 0: {
    print("No es posible hacer la división, el segundo numero es 0.")
} 
else: {
    print("Division; ", num1 // num2)
}

