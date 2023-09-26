from zooAnimales.animal import Animal

class Reptil(Animal):
    _iguanas = 0
    _serpientes = 0
    _listado = []
    def __init__(self, nombre = None, edad = None, habitat = None, genero = None, zona = None, colorEscamas = None, largoCola = None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)
    
    @ classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)
    
    @ classmethod
    def crearIguana(cls, nombre, edad, genero, zona = None):
        iguana = Reptil(nombre, edad, "humedal", genero, zona, "verde", 3)
        cls._iguanas += 1
        return iguana
    
    @ classmethod
    def crearSerpiente(cls, nombre, edad, genero, zona = None):
        serpiente = Reptil(nombre, edad, "jungla", genero, zona, "blanco", 1)
        cls._serpientes += 1
        return serpiente
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def getLargoCola(self):
        return self._largoCola