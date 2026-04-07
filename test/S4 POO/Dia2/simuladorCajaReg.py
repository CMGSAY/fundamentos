class CajaRegistradora:
    def cobrar_producto( self):
        precio_producto = float(input('\nIngrese el precio del producto: '))
        self.dinero_acumulado = self.dinero_acumulado + precio_producto
        print(f'Combro exitoso. Llevamos acumulado: {self.dinero_acumulado}')
    
    def imprimir_cierre_turno(self):
        print('\nCierre de turno')
        print(f'Cajero encargado: {self.cajero_asignado}')
        print(f'Venta total del dia 24/03/2026: {self.dinero_acumulado}')

print('='*25)
print('Caja registradora super')
print('='*25)

caja_express = CajaRegistradora()

caja_express.cajero_asignado = 'Carlos Garcia'
caja_express.dinero_acumulado = 0.00

caja_express.cobrar_producto()
caja_express.cobrar_producto()
caja_express.imprimir_cierre_turno()