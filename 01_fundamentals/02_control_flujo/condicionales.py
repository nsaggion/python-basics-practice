"""
Ejercicio de práctica en Python
Tema: Estructura de control
Nivel: Básico
"""

"""
Enunciado:
Pide al usuario que ingrese una temperatura en grados Celsius.
Según el valor ingresado, muestra uno de estos mensajes:

    - Si la temperatura es menor a 0: "Hace frío extremo"
    - Si la temperatura está entre 0 y 15: "Hace frío"
    - Si la temperatura está entre 16 y 25: "Clima agradable"
    - Si la temperatura está entre 26 y 35: "Hace calor"
    - Si la temperatura es mayor a 35: "Hace mucho calor"
"""

temp = input ("Ingrese la temperatura: ")
temp = int (temp)

if temp < 0:
    print ("Hace frío extremo")
elif temp >= 0 and temp <= 15:
    print ("Hace frio")
elif temp >= 16 and temp <= 25:
    print ("Clima agradable")

elif temp >= 26 and temp <= 35:
    print ("Hace calor")

else:
    print ("Hace mucho calor")
    