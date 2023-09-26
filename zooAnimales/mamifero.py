from animal import Animal

class Mamifero(Animal):
    _caballos = 0
    _leones = 0
    _listado = []
    def __init__(self, nombre = None, edad = None, habitat = None, genero = None, zona = None, pelaje = None, patas = None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)
    
    @ classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)
    
    @ classmethod
    def crearCaballo(cls, nombre, edad, genero, zona):
        caballo = Mamifero(nombre, edad, "pradera", genero, zona, True, 4)
        cls._caballos += 1
        return caballo
    
    @ classmethod
    def crearLeon(cls, nombre, edad, genero, zona):
        leon = Mamifero(nombre, edad, "pradera", genero, zona, True, 4)
        cls._leones += 1
        return leon