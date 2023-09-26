from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas = 0
    salamandras = 0
    _listado = []
    def __init__(self, nombre = None, edad = None, habitat = None, genero = None, colorPiel = None, venenoso = None): #quite zona de aca
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)
    
    @ classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    
    @ classmethod
    def crearRana(cls, nombre, edad, genero): #quite zona de aca
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True) #quite zona de aca
        cls.ranas += 1
        return rana
    
    @ classmethod
    def crearSalamandra(cls, nombre, edad, genero):#quite zona de aca
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False) #quite zona de aca
        cls.salamandras += 1
        return salamandra
    
    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self, colorpiel):
        self._colorPiel = colorpiel

    def isVenenoso(self):
        return self._venenoso