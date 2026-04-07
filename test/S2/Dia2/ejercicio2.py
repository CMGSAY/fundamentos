# Control de inventario

cantidadCajas = int(input('Introduce la cantidad de cajas de leche disponible: '))

if (cantidadCajas > 20):
    print('Invetario saludable')
elif(cantidadCajas >= 1 ) and (cantidadCajas <= 20):
    print('Alerta: Hacer pedidos al proveedor')
elif(cantidadCajas == 0):
    print('Urgente: Producto Agotado')

print('\nVuelva Pronto ')