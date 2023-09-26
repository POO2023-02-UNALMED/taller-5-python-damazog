class Animal:
    _totalAnimales = 0
    def __init__(self, nombre = None, edad = None, habitat = None, genero = None, zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales += 1

    @classmethod
    def totalPorTipo(cls):
        resultado = []
        from mamifero import Mamifero
        resultado.append(f"Mamiferos: {Mamifero.mamiferos}")
        from ave  import Ave
        resultado.append(f"Aves: {Ave.aves}")
        from reptil import Reptil
        resultado.append(f"Reptiles: {Reptil.reptiles}")
        from pez import Pez
        resultado.append(f"Peces: {Pez.peces}")
        from anfibio import Anfibio
        resultado.append(f"Anfibios: {Anfibio.anfibios}")
        return "\n".join(resultado)

    def __str__(self):
        if self._zona is not None:
            imprimible = "Mi nombre es " + self._nombre + ", tengo una edad de " + str(self._edad) + ", habito en " + self._habitat + " y mi genero es " + self._genero + ", la zona en la que me ubico es " + self._zona.getNombre() + ", en el " + self._zona.getZoo().getNombre()
        else:
            imprimible = "Mi nombre es " + self._nombre + ", tengo una edad de " + str(self._edad) + ", habito en " + self._habitat + " y mi genero es " + self._genero
        return imprimible
    
    def getZona(self):
        return self._zona
    
    def setZona(self, zona):
        self._zona = zona

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad
    
    def setEdad(self, edad):
        self._edad= edad

    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero
    
    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona
    
    def setZona(self, zona):
        self._zona = zona

    @classmethod
    def getTotalAnimales(cls):
        return Animal._totalAnimales