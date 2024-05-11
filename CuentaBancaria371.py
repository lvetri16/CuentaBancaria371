#declaracion de clase cuenta
class Cuenta:
    def __init__(self):
        self._persona = ""
        self._cantidad = 0
    
    #definicion de los getter y setter del atributo persona
    @property
    def persona(self):
        return self._persona
    
    @persona.setter
    def persona(self, persona):
        self._persona = persona
    
    #definicion de los getter y setter del atributo cantidad
    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, cantidad):
        if cantidad >= 0:
            self._cantidad = cantidad
    
    # Definicion del Metodo ingresar cantidad   
    def ingresar_cantidad(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad
            
    #Definicion del metodo retirar cantidad
    def retirar_cantidad(self, cantidad):
        self._cantidad -= cantidad
    
    #Definicion del metodo mostrar datos
    def mostrar_datos(self):
        return f"Datos de la cuenta:\nPersona: {self._persona}\nCantidad: {self._cantidad}\n"

#Invoco la clase cuenta
cuenta = Cuenta()
cuenta.persona = "Juan"
cuenta.cantidad = 1000
cuenta.ingresar_cantidad(500)
cuenta.retirar_cantidad(600)
print(cuenta.mostrar_datos())