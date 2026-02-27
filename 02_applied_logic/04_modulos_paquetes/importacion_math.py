"""

"""
"""
Enunciado: 
Importa el módulo math.
Pide al usuario un número.
Muestra:
Su raíz cuadrada
Su valor elevado al cuadrado usando math.pow()
"""
import math

num = int(input("Ingrese un numero porfavor: "))
raizQuadrada = math.sqrt(num)
elevado = math.pow(num,2)
print(f"La raíz cuadrada de {num} és {raizQuadrada} y elevado al cuadrado és {elevado}")