"""
Ejercicio de práctica en Python
Tema: control_de_bucles
Nivel: Básico
"""
"""
Enunciado:
Pide al usuario un número positivo N.
Luego recorre los números desde 1 en adelante (por ejemplo hasta 100) y encuentra el primer número que sea múltiplo de N.
Cuando lo encuentres, debes mostrarlo y terminar el bucle inmediatamente usando break.
"""

num = input("Inserte un número; ")
num = int(num)

for i in range(1,101):
    if i % num == 0:
        print("Primer múltiplo encontrado: ",i)
        break


