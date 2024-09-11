"""
Programa que calcula el pressure
"""
def calculate_total_pressure():
    # Constante de los gases ideales
    R = 0.082

    # Solicitar los valores de entrada desde la consola
    M1 = float(input("Ingrese la masa molar del primer gas (M1) en g/mol: "))
    M2 = float(input("Ingrese la masa molar del segundo gas (M2) en g/mol: "))
    m1 = float(input("Ingrese la masa del primer gas presente (m1) en gramos: "))
    m2 = float(input("Ingrese la masa del segundo gas presente (m2) en gramos: "))
    V = float(input("Ingrese el volumen del recipiente (V) en dm^3: "))
    T_C = float(input("Ingrese la temperatura (T) en grados Celsius: "))

    # Convertir la temperatura a Kelvin
    T_K = T_C + 273.15

    # Calcular la presión total
    P_total = ((m1 / M1) + (m2 / M2)) * (R * T_K) / V

    # Devolver el resultado
    return P_total


# Ejecutar la función y mostrar el resultado
print("La presión total es:", calculate_total_pressure(), "atm")
