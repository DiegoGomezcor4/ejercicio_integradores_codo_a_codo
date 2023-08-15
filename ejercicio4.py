""" Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
que reciba el diccionario generado con la función anterior y devuelva una tupla con la
palabra más repetida y su frecuencia. """

def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    
    for palabra in palabras:
        palabra = palabra.lower()
        palabra = palabra.strip(".,?!")
        
        if palabra:
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                frecuencia[palabra] = 1
    
    return frecuencia

def palabra_mas_repetida(diccionario):
    max_frecuencia = 0
    palabra_max = None
    
    for palabra, frecuencia in diccionario.items():
        if frecuencia > max_frecuencia:
            max_frecuencia = frecuencia
            palabra_max = palabra
    
    return palabra_max, max_frecuencia

cadena = input("Ingrese una cadena de caracteres: ")
resultado = contar_palabras(cadena)
print("Frecuencia de palabras:")
for palabra, frecuencia in resultado.items():
    print(f"{palabra}: {frecuencia}")

palabra_rep, frec_rep = palabra_mas_repetida(resultado)
print(f"Palabra más repetida: '{palabra_rep}' con frecuencia: {frec_rep}")
