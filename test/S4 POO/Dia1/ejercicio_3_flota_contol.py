# Definicion de Moldes
class Camion:
    pass

class ControlLogitico:
    pass

# Fabricacion en serie
camion1 = Camion()
camion2 = Camion()
camion3 = Camion()
camion4 = Camion()
camion5 = Camion()

print('-'*45)
print('Gestion de Flota y Control de Capacidad')
print('-'*45)

# Creacion de lista 
garaje_principal = [camion1, camion2, camion3, camion4, camion5]

# Conteo y aritmetica
impuesto_camion = 500

imuesto_total = (len(garaje_principal)) * impuesto_camion

print(f'Cantidad de impuesto pagado por {(len(garaje_principal))} camiones: {imuesto_total}')

print('\nID de los camiones ingresados: ')
for camion in range( len (garaje_principal)):
    print(f'Id del camion {camion +1}: ',id(camion))

if (len(garaje_principal)) >= 4:
    print('\nCapacidad excedida! Debe de mover camiones a otra sucursal')
else:
    print('\nCapacidad óptima.')