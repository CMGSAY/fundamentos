class Bateria:
    def __init__(self):
        self.bateria = 100
        
    def descargar(self, bateria):
        self.bateria = bateria - 10
        print(f'Bateria al {self.bateria}%')
        

class Celular:
    def __init__(self, marca):
        self.marca = marca
        self.energia = Bateria()
        
        
        
    def usar_app(self):
        print('Abriendo aplicacion...')
        
        self.energia.descargar
        
cel1 = Celular('android')

cel1.usar_app()
cel1.usar_app()