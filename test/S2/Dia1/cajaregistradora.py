# Caja registradora
print('Bienvenido a la tienda ')
nombre_producto = input('Ingrese el   nombre del producto')
precio_producto = float(input('Ingrese el precio del producto: '))
cantidad_producto = (input('Ingrese la cantidad del producto: '))
cantidad_producto = int(cantidad_producto)

# Procesamiento de la informacion
subtotal =  precio_producto * cantidad_producto
impuesto = subtotal * 0.15
total = subtotal + impuesto

# Impresion de los resultados
print('\n --- resumen de la compra ---')
print('%25s: %10s' %('Nombre del producto', nombre_producto))
print('%25s:%10.2f' %('precio del producto', precio_producto))
print('%25s: %10d' %('Cantidad del producto', cantidad_producto))
print('%25s: %10.2f' %('Subtotal', subtotal))
print('%25s: %10.2f' %('Impuesto', impuesto))
print('%25s: %10.2f' %('Total', total))

