def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}

    print(palabras)
    
    for palabra in palabras:
        palabra = palabra.lower()  # Convertir la palabra a minúsculas para considerar mayúsculas y minúsculas juntas
        palabra = palabra.strip(".,?!")  # Eliminar signos de puntuación al inicio o final de la palabra
        
        if palabra:  # Ignorar cadenas vacías después de quitar puntuación
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                frecuencia[palabra] = 1
    
    return frecuencia

cadena = input("Ingrese una cadena de caracteres: ")
resultado = contar_palabras(cadena)
print("Frecuencia de palabras:")
for palabra, frecuencia in resultado.items():
    print(f"{palabra}: {frecuencia}")
