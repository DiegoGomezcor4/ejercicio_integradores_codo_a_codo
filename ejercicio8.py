from ejercicio7 import Cuenta, Persona

class CuentaJoven(Cuenta):
    def __init__(self, titular=None, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion
    
    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self, nueva_bonificacion):
        if isinstance(nueva_bonificacion, (int, float)) and nueva_bonificacion >= 0:
            self._bonificacion = nueva_bonificacion
        else:
            print("Error: La bonificación debe ser un número no negativo.")
    
    def es_titular_valido(self):
        if self._titular and self._titular.es_mayor_de_edad() and self._titular.edad < 25:
            return True
        return False
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No se puede retirar dinero, el titular no es válido.")

    def mostrar(self):
        super().mostrar()
        print(f"Tipo de cuenta: Cuenta Joven")
        print(f"Bonificación: {self._bonificacion}%")

# Ejemplo de uso
persona_joven = Persona("Ana", 20, "87654321")
cuenta_joven = CuentaJoven(persona_joven, 500.0, 5.0)
cuenta_joven.mostrar()

cuenta_joven.retirar(100)
cuenta_joven.mostrar()
