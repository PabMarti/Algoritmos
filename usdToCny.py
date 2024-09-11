"""
Programa calcula la conversion de dolares
a Yuanes
"""
def usd_to_cny(usd):
    # Tasa de conversión de USD a CNY
    conversion_rate = 6.75

    # Convertir USD a CNY
    cny = usd * conversion_rate

    # Formatear el resultado con 2 decimales
    return f"{cny:.2f} CNY"


# Ejemplos de uso
#print(usd_to_cny(15))  # Output: '101.25 Chinese Yuan'
#print(usd_to_cny(465))  # Output: '3138.75 Chinese Yuan'

dol = int(input("Coloca la cantidad de dolares a cambiar: "))

conver = usd_to_cny(dol)
print(f"${dol} USD es igual a ¥{conver}")
