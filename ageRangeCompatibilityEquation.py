"""
Programa que calcula un rango de edad entre 2 edades
diferentes
"""
import math

def age_range(age):
    if age <= 14:
        # Si la edad es <= 14, utilizamos la fórmula alternativa
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)
    else:
        # Si la edad es mayor a 14, utilizamos la fórmula estándar
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor((age - 7) * 2)

    # Devolvemos el rango en el formato adecuado
    return f"{min_age}-{max_age}"


# Pedir al usuario que ingrese la edad
def main():
    age = int(input("Ingrese la edad de la persona: "))
    result = age_range(age)
    print(f"El rango de edad recomendado es: {result}")

# Ejecutar el programa principal
main()
