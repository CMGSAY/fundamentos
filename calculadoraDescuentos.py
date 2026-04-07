def aplicar_decuento(precio, porcentaje_descuento):
    dinero_descuento = precio * (porcentaje_descuento / 100)
    nuevo_precio = precio - dinero_descuento
    return nuevo_precio


precio_producto = float(input('Ingrese el precio del producto: '))
porcentaje_descuento = float(input('Ingrese el porcentaje de descuento: '))
nuevo_precio = aplicar_decuento(precio_producto, porcentaje_descuento)
print(f'El nuevo precio del producto con el descuento aplicado es: {nuevo_precio}')
