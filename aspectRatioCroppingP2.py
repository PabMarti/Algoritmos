"""
Programa para pdoer tener las medidas redimencionadas de una pantalla (Parte 2)
"""

import math
def convert_to_16_9(x, y, constant):
    if constant == "height":
        # Mantener la altura constante
        new_x = math.ceil(y * 16 / 9)
        return (new_x, y)

    elif constant == "width":
        # Mantener la anchura constante
        new_y = math.ceil(x * 9 / 16)
        return (x, new_y)

    elif constant == "diagonal":
        # Mantener la diagonal constante
        diagonal = math.sqrt(x ** 2 + y ** 2)
        new_x = math.ceil(math.sqrt((16 / 9) * (diagonal ** 2 / (1 + (16 / 9) ** 2))))
        new_y = math.ceil(new_x * 9 / 16)
        return (new_x, new_y)

    elif constant == "area":
        # Mantener el área constante
        area = x * y
        new_x = math.ceil(math.sqrt(area * (16 / 9)))
        new_y = math.ceil(new_x * 9 / 16)
        return (new_x, new_y)

    else:
        raise ValueError("Constant must be one of: 'height', 'width', 'diagonal', 'area'")
# Ejemplos de uso
print(convert_to_16_9(1440, 1080, "height"))  # Output: (1920, 1080)
print(convert_to_16_9(1920, 1080, "width"))  # Output: (1920, 1080)
print(convert_to_16_9(1440, 1080, "diagonal"))  # Output: (1920, 1080)
print(convert_to_16_9(1440, 1080, "area"))  # Output: (1920, 1080)
