class Cuenta:
    def __init__(self):
        self._persona = ""
        self._cantidad = 0
    
    @property
    def persona(self):
        return self._persona
    
    @persona.setter
    def persona(self, persona):
        self._persona = persona
    
    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, cantidad):
        if cantidad >= 0:
            self._cantidad = cantidad
            
    def ingresar_cantidad(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad
    
    def retirar_cantidad(self, cantidad):
        self._cantidad -= cantidad

    def mostrar_datos(self):
        return f"Datos de la cuenta:\nPersona: {self._persona}\nCantidad: {self._cantidad}\n"

cuenta = Cuenta()
cuenta.persona = "Juan"
cuenta.cantidad = 1000
cuenta.ingresar_cantidad(500)
cuenta.retirar_cantidad(600)
print(cuenta.mostrar_datos())