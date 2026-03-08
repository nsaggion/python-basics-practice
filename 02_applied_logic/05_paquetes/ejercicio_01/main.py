"""
Ejecicio de práctica en Python.
Tema: Paquetes.
Nivel: Medio.
"""
"""
Enunciado:
Importa los diferentes paquetes creados anteriormente.
Muestra el resultado.
"""
from matematicas import operacion
from matematicas import estadisticas

print("Usando el módulo operaciones/estadisticas....")

print("Suma:",operacion.suma(5,7))
print("Resta:",operacion.resta(10,6))
print("Multiplicación:",operacion.multiplicar(9,9))

print("Promedio:", estadisticas.promedio(10,20))
print("Mayor:", estadisticas.mayor(5,8))