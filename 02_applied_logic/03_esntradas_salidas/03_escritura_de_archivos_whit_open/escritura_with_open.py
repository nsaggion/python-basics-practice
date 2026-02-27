"""
Ejercicio de práctica en Python.
Tema: Funciones.
Nivel: Medio.
"""
"""
Enunciado:
Crea un programa que:
Pida al usuario que ingrese su ciudad.
Cree (o sobrescriba) un archivo llamado:
ciudad.txt
Escriba dentro del archivo:
La ciudad ingresada es: [ciudad]
Muestre un mensaje confirmando que el archivo fue guardado correctamente.
"""
ciudad = input("Porfavor ingrese su ciudad: ")
with open("ciudad.txt","w") as archivo:
    archivo.write(f"La ciudad ingresada es: {ciudad}")
    print("Archivo creado correctamente.")