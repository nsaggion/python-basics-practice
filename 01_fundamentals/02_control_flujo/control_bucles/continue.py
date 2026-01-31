"""
Ejercicio de práctica en Python
Tema: control_de_bucles
Nivel: Básico
"""
"""
Enunciado:
Pide al usuario un número positivo N.
Luego recorre los números desde 1 hasta N.
Con ayuda de continue, salta (no muestres) todos los números que sean pares.
Al final, muestra solo los impares.
"""

num = int(input("Inserte un numero positivo, que sea mayor a 0; "))

while num <= 0:
    num = int(input("Pruebe otravez a insertar un numero positivo o mayor a 0; "))

for i in range(1,num+1):
    if i % 2 ==0:
        continue
    print(i)
