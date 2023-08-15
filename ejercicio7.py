class Cuenta:
    def __init__(self, titular=None, cantidad=0.0):
        self._titular = titular
        self._cantidad = cantidad
    
    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, nuevo_titular):
        if isinstance(nuevo_titular, Persona):
            self._titular = nuevo_titular
        else:
            print("Error: El titular debe ser una instancia de la clase Persona.")
    
    @property
    def cantidad(self):
        return self._cantidad
    
    def mostrar(self):
        print("Titular:")
        self._titular.mostrar()
        print(f"Cantidad en la cuenta: {self._cantidad}")
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad
    
    def retirar(self, cantidad):
        self._cantidad -= cantidad

# Ejemplo de uso
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

persona = Persona("Juan", 25, "12345678")
cuenta = Cuenta(persona, 1000.0)
cuenta.mostrar()

cuenta.ingresar(500)
cuenta.mostrar()

cuenta.retirar(200)
cuenta.mostrar()
