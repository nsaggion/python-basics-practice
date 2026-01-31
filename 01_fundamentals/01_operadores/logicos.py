"""
Ejercicio de práctica en Python
Tema: Operadores lógicos
Nivel: Básico
"""
"""
Enunciado; Pide al usuario su edad y si tiene permiso (sí/no).
El programa debe indicar si la persona puede acceder a una actividad especial.

Reglas:
- Debe ser mayor o igual a 18 años y tener permiso.
- Si no cumple alguna condición, no puede acceder.
"""

permiso = input("Usted tiene permiso (Sí/No): ")
MayorEdad = input ("Cuantos años tienes?: ")

MayorEdad = int(MayorEdad)

if "Sí" in permiso and MayorEdad >= 18:
        print("¡Puedes entrar sin problema!")
else: 
        print("Lo siento, no puede entrar")