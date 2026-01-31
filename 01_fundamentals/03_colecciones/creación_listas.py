"""
Ejercicio de práctica en Python
Tema: Listas
Nivel: Básico
"""
"""
Enunciado:
Crea una lista con 6 elementos (pueden ser números, palabras o una mezcla de ambos).
Luego:
- Muestra el elemento que se encuentra en la posición 0.
- Muestra el elemento que se encuentra en la posición 2.
- Muestra el elemento que se encuentra en la última posición usando índices.
- Pide al usuario que ingrese una posición y muestra el elemento que se encuentra en esa posición.
- Si la posición ingresada no existe en la lista, muestra un mensaje de error.
"""

lista = ["carne","pollo","pescado","chorizo","cerdo","cordero"]

print ("Primer elemento; ",lista[0])
print ("Tercer elemento; ",lista[2])
print ("Último elemneto; ",lista[-1])

num = int (input ("Por favor ingrese un numero; "))

while num > 5 or num < 0:
    print ("Numero fuera de rango")
    num = int(input("Vuelva a ingresar otro numero; "))
print ("La palabra en la posición",num,"es",lista[num] )