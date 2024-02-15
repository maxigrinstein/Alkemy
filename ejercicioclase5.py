class Bicicleta:
    def __init__(self, rodado, precio, color, marca, modelo, velocidad):
        self.rodado = rodado
        self.precio = precio
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def pedalear(self):
        while(self.velocidad  0):
            self.velocidad += 1
           print("Acelerando..."{self.velocidad}')
            


    def frenar(self):
        while(self.velocidad > 0):
            self.velocidad -= 1
            print(f'Frenando... {self.velocidad}')
        
miBici = Bicicleta("29", 250000, "Rojo", "Venzo", "2000", 18)
