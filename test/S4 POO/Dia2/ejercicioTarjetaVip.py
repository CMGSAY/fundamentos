class TarjetaVIP:
    def mostrar_puntos(self):
        print(f'Sus puntos Actuales son: {self.puntos}' )
        
    def sumar_puntos(self):
        puntos_compra = 50
        self.puntos = self.puntos + puntos_compra
        print(f'Usted gano {puntos_compra} puntos')
        

# mostrar puntos 
# sumar puntos

tarjeta_carlos = TarjetaVIP()

tarjeta_carlos.puntos = 100

print('Puntos acumulados')
tarjeta_carlos.mostrar_puntos()
tarjeta_carlos.sumar_puntos()
tarjeta_carlos.mostrar_puntos()