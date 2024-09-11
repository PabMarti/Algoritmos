"""
Programa que calcula la edad de un perro y un gato
en años humanos :D
"""

#Calcula la edad de un perro y un gato en años humanos
from cgi import print_form

def calculate_pet_ages(humanYears):
    # Inicializar los años de gato y perro
    catYears = 0
    dogYears = 0

    # Primer año
    if humanYears >= 1:
        catYears += 15
        dogYears += 15

    # Segundo año
    if humanYears >= 2:
        catYears += 9
        dogYears += 9

    # Años adicionales
    if humanYears > 2:
        catYears += (humanYears - 2) * 4
        dogYears += (humanYears - 2) * 5

    # Retornar la lista con los años humanos, de gato y de perro
    return [humanYears, catYears, dogYears]

# Ejemplo de uso
#humanYears = 15
humanYears = int(input("Dame los años humanos: "))
ages = calculate_pet_ages(humanYears) # Output: [3, 28, 29]
print(f"Los años humanos son: {str(humanYears)}")
print(f"Los años en gato son: {str(ages[1])}")
print(f"Los años en gato son: {str(ages[2])}")
