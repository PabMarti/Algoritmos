"""
Programa que redondea un número
"""
def round_number():
    # Pedir al usuario que ingrese un número
    number = float(input("Ingrese un número: "))

    # Redondear el número a dos decimales
    rounded_number = round(number, 2)

    # Imprimir el resultado
    print(f"El número redondeado es: {rounded_number}")


# Ejecutar el programa
round_number()
