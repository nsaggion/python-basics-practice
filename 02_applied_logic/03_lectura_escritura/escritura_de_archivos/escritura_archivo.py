"""
Ejercicio de práctica en Python.
Tema: Funciones.
Nivel: Medio.
"""
"""
Enunciado:
Pida al usuario que ingrese su nombre.
Cree un archivo llamado:
usuario.txt
Escriba dentro del archivo el siguiente mensaje:
- Bienvenido, [nombre]
Cierre el archivo.
Muestre un mensaje confirmando que el archivo fue creado correctamente
"""
nombre = input("Ingrese su nombre profavor: ")
archivo = open("usuario.txt","w")
archivo.write(f"Bienvenido,{nombre}")
archivo.close()
print("Archivo creado correctamente.")