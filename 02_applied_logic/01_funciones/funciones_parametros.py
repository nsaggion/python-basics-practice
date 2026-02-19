"""
Ejercicio de práctica en Python.
Tema: Funciones.
Nivel: Básico.
"""
"""
Enunciado:
Crea una función llamada saludar_persona.
Debe recibir un parámetro llamado nombre.
Dentro de la función, imprimir:
- Hola, [nombre]
Pide el nombre al usuario.
Llama a la función pasando el nombre ingresado.
"""
def saludar_persona(nombre):
    print("Hola,",nombre)
nombre = input("Ingrese su nombre: ")
saludar_persona(nombre)