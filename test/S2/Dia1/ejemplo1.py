#Inventario basico de producto
#nombre_producto = 'Camiseta' # string
#precio_producto = 19.99     #float
#cantidad_producto = 50      #int
#descuento = False           #booleano

#print('Nombre del producto:', nombre_producto, 'tipo:', type(nombre_producto) )
#print('Precio del producto', precio_producto, 'tipo:', type(precio_producto))

# convertir despues de preguntar
cantidad = input('Cuantos cafes deas comprar? ')
cantidad = int(cantidad)


# forma2: convertir directamente al pedir el input
precio = float(input('Cual es el precio del cafe? '))
precio = float('10.5')
precio = 10.5

print('cantidad  de cafe: ', cantidad, 'tipo: ', type(cantidad))
print('Precio del cafe: ', precio, 'tipo: ', type(precio))


valor1 = 10
valor2 = 3

# Division normal
resultado = valor1 / valor2 # Resultado en float, aunque ambos sean enteros

#Division Entera
resultado_entero = valor1 // valor2 # Resultado es un int, aunque tenga decimales 

#modulo o resto de la division
resta = valor1 % valor2 # resultado es un int, aunque ambos valores son entero

print('Resultado de la division: ', resultado)
print('Resultado de la division Entera: ', resultado_entero)
print('Resto de la division', resta )


producto = 5
producto_nombre = 'Manzana'
precio_manzana = 500

print('----- Reporte-----')
#tenemos mas de 10 manzanas?
hay_mazanas = producto > 10
print('Hay mas de 10 manzanas?', hay_mazanas)

#Nos quedamos sin stock en la bodega
sin_stock = producto == 0
print(f'Nos quedamos sin stock en la bodega? {sin_stock}')

#Comparacion de nombres de productos
producto_buscado = "Manzana"

es_manzana = producto_nombre == producto_buscado
print(f'el Prducto buscado esta en la bodega? {es_manzana}')
