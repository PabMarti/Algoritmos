"""
Programa que calcula los litros que debe tomar Nathan
"""
import math

def calculate_litres():
    # Solicitar el tiempo de ciclismo en horas
    time = float(input("Ingrese el tiempo en horas: "))

    # Calcular el número de litros, redondeando hacia abajo
    litres = math.floor(time * 0.5)

    # Retornar el resultado
    return litres


# Ejecutar la función y mostrar el resultado
print("Litros que beberá Nathan:", calculate_litres())
