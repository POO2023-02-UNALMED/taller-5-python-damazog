from animal import Animal

class Pez(Animal):
    _salmones = 0
    _bacalaos = 0
    _listado = []
    def __init__(self, nombre = None, edad = None, habitat = None, genero = None, zona = None, colorEscamas = None, cantidadAletas = None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)
    
    @ classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
    
    @ classmethod
    def crearSalmon(cls, nombre, edad, genero, zona):
        salmon = Pez(nombre, edad, "oceano", genero, zona, "rojo", 6)
        cls._salmones += 1
        return salmon
    
    @ classmethod
    def crearBacalao(cls, nombre, edad, genero, zona):
        bacalao = Pez(nombre, edad, "oceano", genero, zona, "gris", 6)
        cls._bacalaos += 1
        return bacalao