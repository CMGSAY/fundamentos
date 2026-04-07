def mostrar_inventario(lista_productos):
    #forma 1
    for num_articulo in range(len (lista_productos)):
        print(lista_productos[num_articulo]['nombre'])
        print(lista_productos[num_articulo]['precio'])
        print(lista_productos[num_articulo]['cantidad'])
    
    #forma 2
    for num_articulo in range(len (lista_productos)):
        articulo = lista_productos[num_articulo]['nombre'] + '-' + str(lista_productos[num_articulo]['precio'])  + '-' + str(lista_productos[num_articulo]['cantidad'])
        print(articulo)
         
   
            
            
        

print('Inventario de productos.')

lista_productos = []

while True:
    nombre_producto = input('\nDeseas Ingresar un producto o FIN para salir: ')
    
    if nombre_producto == 'FIN':
        mostrar_inventario(lista_productos)
        break
    precio = float(input('Ingrese el precio del producto: '))
    cantidad = int(input('Ingrese la cantidad del producto: '))
    
    productito = {
        'nombre' : nombre_producto,
        'precio' : precio,
        'cantidad' : cantidad
    }
    lista_productos.append(productito)
    

