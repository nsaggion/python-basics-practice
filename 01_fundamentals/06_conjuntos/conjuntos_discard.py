"""
Ejercicio de práctica en Python
Tema: Conjuntos
Nivel: Básico
"""
"""
Crea un conjunto llamado numeros con los valores:
10, 20, 30, 40
Muestra el conjunto.
Pide al usuario que ingrese un número para eliminar.
Usa discard() para eliminar el número (sin usar if).
Muestra el conjunto actualizado.
"""
numeros = {10, 20, 30, 40}
print("Conjunto actual",numeros)
numUser = int(input("Por favor ingrese un numero para eliminar: "))
numeros.discard(numUser)
print("Conjunto actualizado",numeros)