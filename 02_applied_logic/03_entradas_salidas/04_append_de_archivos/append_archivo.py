"""
Ejercicio de práctica en Python.
Tema: Funciones.
Nivel: Medio.
"""
"""
Enunciado:
Crea un programa que:
Pida al usuario que ingrese un mensaje.
Abra (o cree si no existe) un archivo llamado:
- registro.txt
Añada el mensaje al final del archivo.
Cada mensaje debe ir en una nueva línea.
Muestre un mensaje confirmando que se agregó correctamente.
"""
mensaje = input("Porfavor ingrese un mensaje: ")

with open("registro.txt","a") as archivo:
    archivo.write(mensaje+"\n")
print("El mensaje se agrego correctamente.")