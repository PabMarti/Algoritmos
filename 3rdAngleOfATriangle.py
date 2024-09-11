"""
Programa para calcular el angulo del triangulo
"""
def find_third_angle():
    # Solicitar los dos ángulos del usuario
    angle1 = int(input("Ingrese el primer ángulo: "))
    angle2 = int(input("Ingrese el segundo ángulo: "))

    # Calcular el tercer ángulo
    third_angle = 180 - (angle1 + angle2)

    # Devolver el tercer ángulo
    return third_angle


# Ejecutar la función y mostrar el resultado
print("El tercer ángulo es:", find_third_angle())
