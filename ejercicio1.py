def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

mcd = calcular_mcd(numero1, numero2)
print("El máximo común divisor de", numero1, "y", numero2, "es:", mcd)
