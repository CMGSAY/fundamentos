class AireAcondicionado:
    def __init__ (self, grados):
        self.temperatura_inicial = 24
        self.grados = grados
        
    
    def bajar_temperatura(self):
        self.temperatura_final = self.temperatura_inicial - self.grados
        if self.temperatura_final < 16:
            print('Error: no puedes bajar mas de 16 grados')
            
        else: 
            print(f'temperatura bajo {self.temperatura_final}')
            

grados1 = AireAcondicionado(4)

#intento
grados1.bajar_temperatura()
