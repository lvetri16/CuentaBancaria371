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