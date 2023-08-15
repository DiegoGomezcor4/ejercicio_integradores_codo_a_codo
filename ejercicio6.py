""" Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad """

class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str):
            self._nombre = nuevo_nombre
        else:
            print("Error: El nombre debe ser una cadena de texto.")
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("Error: La edad debe ser un número entero no negativo.")
    
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, nuevo_dni):
        if isinstance(nuevo_dni, str) and len(nuevo_dni) == 8:
            self._dni = nuevo_dni
        else:
            print("Error: El DNI debe ser una cadena de 8 caracteres.")
    
    def mostrar(self):
        print(f"Nombre: {self._nombre}")
        print(f"Edad: {self._edad}")
        print(f"DNI: {self._dni}")
    
    def es_mayor_de_edad(self):
        return self._edad >= 18

# Ejemplo de uso
persona = Persona()
persona.nombre = "Juan"
persona.edad = 25
persona.dni = "12345678"
persona.mostrar()

if persona.es_mayor_de_edad():
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")
