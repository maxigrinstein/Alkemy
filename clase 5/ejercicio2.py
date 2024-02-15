class Animal:
    def __init__(self, cantidad_patas, tipo):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo
    
    def comer(self):
        return "estoy comiendo"


class Perro(Animal):
    def __init__(self, cantidad_patas, tipo, nombre, raza):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo
        self.nombre = nombre
        self.raza = raza
    
    def correr(self):
        return "estoy corriendo"


class Aguila(Animal):
    def volar(self):
        return "estoy volando"

animal_random = Animal(4, "vertebrado")
print("soy un animal y", animal_random.comer())

mi_perro = Perro(4, "vertebrado", "Max", "Border Collie")
print("soy un perro y", mi_perro.comer())
print("soy un perro y", mi_perro.correr())

mi_aguila = Aguila(2, "vertebrado")
print("soy un aguila y", mi_aguila.comer())
print("soy un aguila y", mi_aguila.volar())
