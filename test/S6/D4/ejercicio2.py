class Arma:
    def __init__(self, nombre, puntos_dano):
        self.nombre = nombre 
        self.puntos_dano = puntos_dano
    

class Guerrero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.arma = arma_equipada
    
    def atacar(self):
        print(f'{self.nombre} ataca con {self.arma.nombre} causando daño')
        

espada1 = Arma('espeda Larga', 50)
guerrero1 = Guerro('carlos')