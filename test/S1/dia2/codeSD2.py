# --- IGNORE ---
# Saludo inicial de la tienda digital
print('==============================')
print('Bienvenido a la tienda digital')
print('==============================')
# print('Que desea comprar')

nombreProducto = input('\nQue desea comprar: ')
edadCliente = input('Cual es tu edad? ')

# Opcion 1 | dos print separados
print('\n1. El Producto que escogio es: ', end='')
print(nombreProducto)

# Opcion 2 | un solo print con formato
print(f'\n2. El Producto que escogio es: {nombreProducto}. y la edad del cliente es: {edadCliente}')

# Opcion 3 | un solo print con concatenacion
print('\n3. El producto que escogio es: ' + nombreProducto )



print("1. leche")
print("2. cafe")
print("3. Arroz")

print("1. leche\n2. Cafe\n3. Arroz")

print("Prdouctos\t Precio")
print("1. Leche\t $2.50")
print("2. Cafe\t $3.00")
print("3. Arrroz\t $1.5")