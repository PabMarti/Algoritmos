"""
Programa para pdoer tener las medidas redimencionadas de una pantalla (PARTE 1)
"""
import math

def convert_to_16_9_height_constant(x, y):
    # Calcula la nueva anchura para mantener la relación 16:9
    new_x = math.ceil(y * 16 / 9)
    return (new_x, y)

# Ejemplo de uso
print(convert_to_16_9_height_constant(1440, 1080))  # Output: (1920, 1080)
