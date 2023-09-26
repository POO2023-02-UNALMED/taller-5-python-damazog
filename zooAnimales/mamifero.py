from zooAnimales.animal import Animal

class Mamifero(Animal):
    _caballos = 0
    _leones = 0
    _listado = []
    def __init__(self, nombre = None, edad = None, habitat = None, genero = None, pelaje = None, patas = None):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)
    
    @ classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)
    
    @ classmethod
    def crearCaballo(cls, nombre, edad, genero):
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        cls._caballos += 1
        return caballo
    
    @ classmethod
    def crearLeon(cls, nombre, edad, genero):
        leon = Mamifero(nombre, edad, "pradera", genero, True, 4)
        cls._leones += 1
        return leon
    
    def getPelaje(self):
        return self._pelaje
    
    def getPatas(self):
        return self._patas