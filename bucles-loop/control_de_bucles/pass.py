"""
Ejercicio de práctica en Python
Tema: control_de_bucles
Nivel: Básico
"""
"""
Enunciado:
Pide al usuario una cadena de texto (por ejemplo una palabra).
Recorre cada carácter y:
- Si el carácter es una vocal (a, e, i, o, u), no hagas nada (usa pass)
- Si el carácter es una consonante, muestra la consonante por pantalla
Al final, el programa habrá impreso solo las consonantes.
"""

texto = input ("Inserte una palabra una palabra en minuscula; ")

for letra in texto:
    if letra in "a e i o u":
        pass
    else:
        print(letra)