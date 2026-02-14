"""
Ejercicio de práctica en Python
Tema: Conjuntos
Nivel: Básico
"""
"""
Crea un conjunto llamado animales con los siguientes elementos:
"perro"
"gato"
"conejo"
"loro"
Muestra el conjunto.
Pide al usuario que ingrese el nombre de un animal que quiera eliminar.
Si el animal existe en el conjunto:
Elimínalo usando remove().
Muestra el conjunto actualizado.
Si el animal no existe:
Muestra un mensaje indicando que no se encontró.
"""
animales = {"perro","gato","loro"}
print("Conjunto de animales actual",animales)
usrAnimal = input("Porfavor ingrese el nombre de un animal: ")
if usrAnimal in animales:
    animales.remove(usrAnimal)
    print("Conjunto actualizado",animales)
else:
    print("No se encontró")