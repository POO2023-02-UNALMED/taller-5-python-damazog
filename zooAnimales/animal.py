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
    def total_por_tipo(cls):
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
        if self._zona != None:
            imprimible = "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad + ", habito en " + self._habitat + " y mi genero es " + self._genero + ", la zona en la que me ubico es " + self._zona + ", en el " + self._zona.getZoo()
        else:
            imprimible = "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad + ", habito en " + self._habitat + " y mi genero es " + self._genero
        return imprimible