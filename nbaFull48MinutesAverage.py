"""
Programa que calcula el promedio de puntos anotados
en un partido de la NBA
"""
def nba_extrap(ppg, mpg):
    # Si mpg es 0, entonces no hay puntos y regresamos 0
    if mpg == 0:
        return 0
    # Calcular la extrapolación de puntos a 48 minutos
    extrapolated_ppg = (ppg / mpg) * 48
    # Redondear el resultado a un decimal
    return round(extrapolated_ppg, 1)


# Pedir al usuario los datos por consola
def main():
    ppg = float(input("Ingrese los puntos por juego (ppg): "))
    mpg = float(input("Ingrese los minutos por juego (mpg): "))

    # Calcular la extrapolación
    result = nba_extrap(ppg, mpg)
    print(f"Puntos por 48 minutos: {result}")


# Ejecutar el programa principal
main()
