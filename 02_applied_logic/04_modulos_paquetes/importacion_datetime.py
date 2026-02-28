"""
Ejercicio de práctica en Python.
Tema: Importacion.
Nivel: Medio.
"""
"""
Enunciado:
Crea un programa que:
Importe el módulo datetime.
Obtenga la fecha y hora actual.
Muestre en pantalla:
Año
Mes
Día
Hora
Minutos
"""
import datetime
fecha = datetime.datetime.now();
print(f"Año: {fecha.year}")
print(f"Mes: {fecha.month}")
print(f"Día: {fecha.day}")
print(f"Hora: {fecha.hour}")
print(f"Minutos: {fecha.minute}")