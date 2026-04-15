import random as rd 

class SableDeLuz:
    def __init__(self):
        self.energia = 100
    
    def __add__ (self, recargar=10 ):
        self.energia = self.energia + recargar
        return self.energia
            
    def __sub__(self, descarga=10):
        self.energia = self.energia - descarga
        
        
    
sable = SableDeLuz()
print("Energía inicial:", sable.energia)

sable
print("Energía tras recarga:", sable.energia)
