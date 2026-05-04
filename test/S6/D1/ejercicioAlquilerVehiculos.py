class Vehiculos:
    tarifa_diaria = 100
    vehiculos_disponibles = 0
    def __init__(self, placa, marca, modelo):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.tarifa = Vehiculos.tarifa_diaria
        self.__kilometraje = 0
        Vehiculos.vehiculos_disponibles += 1
        
    @property
    def kilometraje(self):
        return self.__kilometraje
    
    def vehiculos_disponibles(self):
        print(f'Vehiculos disponibles: {Vehiculos.vehiculos_disponibles}')
    
    def alquilar(self):
        if Vehiculos.vehiculos_disponibles > 0:
            Vehiculos.vehiculos_disponibles -= 1
            print('Has alquilado el vehículo .')
        else:
            print('No hay vehículos disponibles para alquilar.')
    
    def devolver(self, kilometraje_recorrido):
        Vehiculos.vehiculos_disponibles += 1
        self.__kilometraje = kilometraje_recorrido
        print('Has devuelto el vehículo.')
    
    def calcular_costo_tarifa(self, dias):
        costo_total = self.tarifa * dias
        print(f'El costo total del alquiler por {dias} días es: ${costo_total}')

    def cambiar_tarifa(cls, nueva_tarifa):
        cls.tarifa_diaria = nueva_tarifa
        print(f'La tarifa diaria ha sido actualizada a: ${cls.tarifa_diaria}')
        


class Auto(Vehiculos):
    def __init__(self, placa, marca, modelo):
        super().__init__(placa, marca, modelo)
         
class Moto(Vehiculos):
    def __init__(self, placa, marca, modelo):
        super().__init__(placa, marca, modelo)

carro1 = Auto('ABC123', 'Toyota', 'Corolla')
moto1 = Moto('XYZ789', 'Honda', 'CBR500R')

print('\nInformación del Auto:')
print(f'Placa: {carro1.placa}, Marca: {carro1.marca}, Modelo: {carro1.modelo}')

print('\nInformación de la Moto:')
print(f'Placa: {moto1.placa}, Marca: {moto1.marca}, Modelo: {moto1.modelo}')