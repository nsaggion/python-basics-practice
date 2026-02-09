"""
Ejercicio de práctica en Python
Tema: Listas
Nivel: Básico
"""
""""
Enunciado:
- Crea una lista con 6 números enteros desordenados (los que tú quieras).
- Muestra la lista original.
- Ordena la lista de menor a mayor usando sort().
- Muestra la lista ordenada.
- Luego ordena la lista de mayor a menor usando sort() nuevamente.
- Muestra la lista final.
"""""

numeros = [15,102,5,98,234,1968]
print("Lista original",numeros)
numeros.sort()
print("Lista ordenada de menor a mayor",numeros)
numeros.sort(reverse=True)
print("Lista ordenada de mayor a menor",numeros)