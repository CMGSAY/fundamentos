class CajaRegistradora:
    def mostrar_dinero_actual(self):
        print(f'el dinero acual {self.dinero_inicial}')
    
    def procesar_venta(self):
        venta = 500
        print(f'Valor de la venta procesada: {venta}')
        self.dinero_inicial = self.dinero_inicial + venta
        
        
        

caja_registradora_1 = CajaRegistradora()

caja_registradora_1.dinero_inicial = 1500


caja_registradora_1.mostrar_dinero_actual()
caja_registradora_1.procesar_venta()
caja_registradora_1.mostrar_dinero_actual()