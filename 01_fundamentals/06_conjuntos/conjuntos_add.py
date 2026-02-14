"""
Ejercicio de práctica en Python
Tema: Conjuntos
Nivel: Básico
"""
"""
Enunciado:
Crea un conjunto llamado colores con los siguientes elementos:
- "rojo"
- "azul"
- "verde"
Muestra el conjunto.
Pide al usuario que ingrese un nuevo color.
Agrega ese color al conjunto usando add().
Muestra el conjunto actualizado.
"""
colores = {"rojo","azul","verde"}
print(colores)
usrColores = input("Por favor ingrese un color: ")
colores.add(usrColores)
print(colores)
