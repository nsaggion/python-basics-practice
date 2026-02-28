"""
Ejercicio de práctica en Python.
Tema: Importacion.
Nivel: Medio.
"""
"""
Enunciado:
Importe el módulo random.
Genere un número aleatorio entre 1 y 10.
Pida al usuario que intente adivinar el número.
Si el usuario acierta:
Mostrar:
"¡Correcto! Adivinaste el número."
Si no pide hasta que advine o se acaben los intentos"
"""
import random

def pedir_numero(mensaje):
    return int(input(mensaje))
intentos = 3
numeroAleatorio = random.randint(1, 10)
numUserio = pedir_numero("Por favor ingrese un numero del 1 al 10: ")
while True:
    if numUserio > 10 or numUserio < 1:
        numUserio = pedir_numero("Número fuera de rango. Intente nuevamente: ")
        continue
    if numUserio == numeroAleatorio:
        print("¡Correcto! Adivinaste el número.")
        break
    else:
        if intentos == 0:
            print(f"Incorrecto. El número era {numeroAleatorio}")
            break
        print(f"Incorrecto. Le quedan un total de {intentos} intentos")
        intentos -=1
    numUserio = pedir_numero("Pruebe otravez: ")