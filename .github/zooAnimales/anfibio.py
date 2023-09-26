from animal import Animal

class Anfibio(Animal):
    _Ranas = 0
    _salamandras = 0
    _listado = []
    def __init__(self, nombre = None, edad = None, habitat = None, genero = None, zona = None, colorPiel = None, venenoso = None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)
    
    @ classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    
    @ classmethod
    def crearRana(cls, nombre, edad, genero, zona):
        rana = Anfibio(nombre, edad, "selva", genero, zona, "rojo", True)
        cls._Ranas += 1
        return rana
    
    @ classmethod
    def crearSalamandra(cls, nombre, edad, genero, zona):
        salamandra = Anfibio(nombre, edad, "selva", genero, zona, "negro y amarillo", False)
        cls._salamandras += 1
        return salamandra