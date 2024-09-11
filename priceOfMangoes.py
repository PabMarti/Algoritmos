"""
Programa que calcula el precio de mangos a partir de su descuento
por la cantidad
"""
def mango_offer():
    # Solicitar la cantidad de mangos y el precio por unidad
    quantity = int(input("Ingrese la cantidad de mangos: "))
    price_per_mango = float(input("Ingrese el precio por mango: "))

    # Calcular cuántos mangos se pagan
    paid_mangoes = (quantity // 3) * 2 + (quantity % 3)

    # Calcular el costo total
    total_cost = paid_mangoes * price_per_mango

    # Devolver el resultado
    return total_cost


# Ejecutar la función y mostrar el resultado
print("El costo total de los mangos es:", mango_offer())
