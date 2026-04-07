# Generar Un inventario
print('======================')
print('Invetario de productos')
print('======================')

print("\nIngrese 3 Productos ")

producto1 = input('\nIngrese el nombre del primer Producto: ')
preciPro1 = input(f'Ingrese el precio de {producto1}: ')
canPro1 = input(f'Ingrese la cantidad disponible de {producto1}: ')

producto2 = input('\nIngrese el nombre del segundo Producto: ')
preciPro2 = input(f'Ingrese el precio de {producto2}: ')
canPro2 = input(f'Ingrese la cantidad disponible de {producto2}: ')

producto3 = input('\nIngrese el nombre del tercer Producto: ')
preciPro3 = input(f'Ingrese el precio de {producto3}: ')
canPro3 = input(f'Ingrese la cantidad disponible de {producto3}: ')

print("\nInventario")
print("Nombre \t\t Precio \t Cantidad ")
print(f"{producto1:10s} \t {preciPro1:5s} \t\t {canPro1:5s}")
print(f"{producto2:10s} \t {preciPro2:5s} \t\t {canPro2:5s}")
print(f"{producto3:10s} \t {preciPro3:5s} \t\t {canPro3:5s}")
