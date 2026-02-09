"""
Ejercicio de práctica en Python
Tema: Listas
Nivel: Básico
"""
""""
Enunciado:
- Crea una lista con 5 números enteros (los que tú quieras).
- Muestra la lista original.
- Pide al usuario que ingrese una posición (índice).
- Si la posición es válida:
- Elimina el elemento en esa posición usando pop().
- Guarda el valor eliminado en una variable.
Muestra:
- El elemento eliminado.
- La lista actualizada.
- Si la posición no es válida, muestra un mensaje de error.
"""""

franquicias = ["Star Wars","Harry Potter","Marvel","DC","El Señor de los Anillos"]
print("Contenido de la lista ",franquicias)
indice = int(input("Ingrese un numero de la posición en la lista: "))

if indice < 0 or indice > 4:
    print("Indice fuera de rango")
else:
    elementoEliminado = franquicias.pop(indice)
    print("Elemento eliminado: ",elementoEliminado)
    print("Lista actualizada: ",franquicias)