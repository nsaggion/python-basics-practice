"""
Ejercicio de práctica en Python
Tema: Bucles-Loop
Nivel: Básico
"""
"""
Enunciado:
Pide al usuario un número entero positivo N.
Recorre los números desde 1 hasta N utilizando un for y:
- Muestra todos los números que sean múltiplos de 3
- Al final, muestra la suma total de esos múltiplos
"""

num = input("Inserte un numero; ")
num = int (num)

sum = 0

for i in range(1, num+1):
    if (i%3==0):
        print("El siguiente numero és multiplo de 3;",i)
        sum = sum + i
print("La suma total de los numeros és;",sum)
