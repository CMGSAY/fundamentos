for index in range(5, 10, 4):
    print(index)
    

for numerTurno in range(5):
        print('BEEP: producto escaneado: (turno es: ', numerTurno + 1, ')')

for pasillo in range (0, 10, 2):
    print('Limpiando el pasilo ', pasillo +2)
    
    
total = 0.0

for articulo in range(4):
    precio = float(input('Ingrese el precio del articulo: '))
    # total = total + precio
    total += precio
    
print('El total a pagar es:', total)