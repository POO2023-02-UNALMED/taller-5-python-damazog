from zooAnimales.animal import Animal

class Ave(Animal):
    _halcones = 0
    _aguilas = 0
    _listado = []
    def __init__(self, nombre = None, edad = None, habitat = None, genero = None, zona = None, colorPlumas = None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)
    
    @ classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    
    @ classmethod
    def crearHalcon(cls, nombre, edad, genero, zona = None):
        halcon = Ave(nombre, edad, "montanas", genero, zona, "cafe glorioso")
        cls._halcones += 1
        return halcon
    
    @ classmethod
    def crearAguila(cls, nombre, edad, genero, zona = None):
        aguila = Ave(nombre, edad, "montanas", genero, zona, "blanco y amarillo")
        cls._aguilas += 1
        return aguila