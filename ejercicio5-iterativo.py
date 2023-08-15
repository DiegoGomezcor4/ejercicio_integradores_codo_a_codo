def get_int_iterative():
    while True:
        try:
            valor = int(input("Ingrese un valor entero: "))
            return valor
        except ValueError:
            print("Error: Ingrese un valor entero válido.")

valor_entero = get_int_iterative()
print(f"El valor entero ingresado es: {valor_entero}")
