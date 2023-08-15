def get_int_recursive():
    try:
        valor = int(input("Ingrese un valor entero: "))
        return valor
    except ValueError:
        print("Error: Ingrese un valor entero válido.")
        return get_int_recursive()

valor_entero = get_int_recursive()
print(f"El valor entero ingresado es: {valor_entero}")
