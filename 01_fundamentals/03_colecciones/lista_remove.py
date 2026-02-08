"""
Ejercicio de práctica en Python
Tema: Listas
Nivel: Básico
"""
"""
Enunciado:
Crea una lista con los siguientes frutas: manzana, banana, naranja, pera.

Luego:
- Muestra la lista original.
- Pide al usuario que escriba el nombre de una fruta.
- Si la fruta existe en la lista:
- Elimínala usando remove()
- Muestra la lista actualizada
- Si la fruta no existe, muestra un mensaje indicando que no se encontró
"""

frutas = ["manzana", "banana", "naranja", "pera"]
print ("Llista de frutas: ",frutas)
nuevaFruta = str(input("Ingrese el nombre de una fruta: "))

for i in range (0, len(frutas)):
    if nuevaFruta in frutas[i]:
        frutas.remove(nuevaFruta)
        print (frutas)
        break
    else:
        print("La fruta",nuevaFruta,"no se encontró.")
        break