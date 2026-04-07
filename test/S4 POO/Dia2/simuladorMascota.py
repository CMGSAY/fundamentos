class Mascota:
    def alimentar_mascota(self):
        if self.energia == 100:
            print('La mascota tiene energia full. ')
        else:
            energia_alimentacion = 20
            self.energia = self.energia + energia_alimentacion
            print(f'La energia actual de {self.nombre} es: {self.energia} ')
    
    def jugar_mascota(self):
        if 1 <= self.energia <= 100 :
            self.energia = self.energia - 30
            print(f'{self.energia}')
            
# funcion de comer+20
# funcion de jugar -30

mascota1 = Mascota()
mascota1.nombre = 'Charizar'
mascota1.energia = 100

mascota1.jugar_mascota()
mascota1.jugar_mascota()
