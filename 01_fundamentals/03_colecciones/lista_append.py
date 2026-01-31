"""
Ejercicio de práctica en Python
Tema: control_de_bucles
Nivel: Básico
"""
"""
Enunciado:
Crea una lista vacía llamada nombres.
Pide al usuario que ingrese 5 nombres y agrégalos a la lista usando el método append().
Al final, muestra la lista completa.
"""

nombre = []
for i in range(5):
    nombre.append(input ("Ingrese un total de 5 palabras; "))
print("Las palabras insertadas són; ",nombre)

