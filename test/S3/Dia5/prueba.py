def valor_total_producto(inventario):
    for producto in inventario:
        for precio in producto:
            cantidad = precio[1]
            costo =  precio[2]
            #if precio[1]:
                #cantidad = precio[1]
            print(cantidad)
            #elif precio[2]:
            #    costo = precio[2]
            print(costo)

def producto_disponible (inventario):
    for producto in inventario:
        for cantidad in producto:
            if cantidad[1] == 0:
                print('Producto no disponible')
            
                
inventario = [
    ['Croquetas', 15, 20, 0],
    ['Juguetes', 10, 5, 0],
    ['champu', 5, 12, 0]
]

invertido_producto1 =inventario[0][1] * inventario[0][2]
invertido_producto2 =inventario[1][1] * inventario[1][2]
invertido_producto3 =inventario[2][1] * inventario[2][2]

inventario[0][3] = invertido_producto1
inventario[1][3] = invertido_producto2
inventario[2][3] = invertido_producto3

while True:
    print('Inventario disponible: ')
    print(inventario)
    opcion = input('Que deseas Hacer')
    
    match opcion:
        case 'vender':
            nombre_producto = input('Ingrese nombre producto: ')
            if nombre_producto == inventario[0][0]:
                venta = int(input('cuanto quieres vender: '))
                
                if venta <= inventario[0][1]:
                    print('venta exitosa')
                    inventario[0][1] = inventario[0][1] - venta
                else: 
                    print('error')
                
            elif nombre_producto == inventario[1][0]:
                venta = int(input('cuanto quieres vender: '))
                
                if venta <= inventario[1][1]:
                    print('venta exitosa')
                    inventario[1][1] = inventario[1][1] - venta
                else: 
                    print('error')
                
            elif nombre_producto == inventario[2][0]:
                venta = int(input('cuanto quieres vender: '))
                
                if venta <= inventario[2][1]:
                    print('venta exitosa')
                    inventario[2][1] = inventario[2][1] - venta
                else: 
                    print('error')
                
            else:
                print('Producto no existe.')
                        
        case 'agregar':
            print('agregar xd')
            nombre = input(' Ingrese el nombre del nuevo producto: ')
            cantidad = int(input('Ingrese la cantidad: '))
            precio = float(input('Inlese el precio'))
            total = cantidad * precio
            
            inventario.append (nombre, cantidad, precio, total)
            
        case 'eliminar':
            print('eliminar xd')
            nombre = input(' Ingrese el nombre del  producto: ')
            inventario
            
        case 'salir':
            print('saliendo')
            break 
        case _:
            print('error')