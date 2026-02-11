"""
Ejercicio de práctica en Python
Tema: Tupla
Nivel: Básico
"""
""""
Enunciado:
Crea la siguiente tupla:
- (1, 2, 3, 2, 4, 2, 5)
Pide al usuario que ingrese un número.
Usa el método count() para mostrar cuántas veces aparece ese número en la tupla.
Si el número no aparece, muestra un mensaje indicando que no se encontró en la tupla.
"""""

numero = (1, 2, 3, 2, 4, 2, 5)
numeroUser = int(input("Por favor, ingrese un número: "))
cantidad = numero.count(numeroUser)
if (cantidad > 0):
    print("El numero insertado aparecé un total de:",cantidad)
else:
    print("Numero no encontrado")