def menasaje_bienvenida():
    print('Bienvenido al sistma de ventas')
    print('Esperamos que tenga un buena compra.')

def saludar_cliente():
    nombre = input('Ingrese su nombre: ')
    print(f'\nHola {nombre}, bienvenido al gimansio.')

def calcular_total(precio):
    total = precio * cantidad
    return total




menasaje_bienvenida()
saludar_cliente()

precio = float(input('Ingrese el precio del producto: '))
cantidad = int(input('Ingrse la cantidad de productos: '))
precio_toal= calcular_total(precio)
print(f'El precio total es: {precio_toal}')