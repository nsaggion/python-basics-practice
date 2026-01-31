"""
Ejercicio de práctica en Python
Tema: Bucles-Loop
Nivel: Básico
"""
"""
Enunciado:
Define un número secreto (por ejemplo, 7) dentro del programa.
Luego:

- Pide al usuario que ingrese un número.
- Mientras el número ingresado no sea igual al número secreto:
- Muestra: "Incorrecto, prueba de nuevo"
- Vuelve a pedir un número
- Cuando acierte, muestra: "¡Acertaste!"
"""

adivinaNum = input ("Inserte un número para adivinar; ")
adivinaNum = int (adivinaNum)

while adivinaNum != 7:
    print ("Incorrecto, prueba de nuevo")
    adivinaNum = input ("Prueba otravez; ")
    adivinaNum = int (adivinaNum)
print ("¡Acertaste!")