"""
Ejercicio de práctica en Python
Tema: Lista + Diccionario + Bucle.
Nivel: Básico
"""
"""
Enunciado:
Crea una lista con 5 nombres.
Crea un diccionario vacío llamado notas.
Recorre la lista con un for.
Para cada nombre, pide al usuario que ingrese una nota.
Guarda cada nombre como clave y la nota como valor en el diccionario.
Al final, muestra el diccionario completo.
"""
nombres = ["Andrea","Jorge","Sara","Miguel","Diana"]
notas = {}
for i in nombres:
    nota = int(input("Ingrese una nota: "))
    notas.update({i:nota})
print("Diccionario con el nombre más las notas",notas)