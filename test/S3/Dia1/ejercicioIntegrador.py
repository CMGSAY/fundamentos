# Sala de video Juegos
def bienvendia_clientes():
    print('Bienvenido al sistema de la tienda de videojuegos.')

def cuantas_fichas_compra(dinero_disponible):
    fichas_compra = dinero_disponible // 500
    
    return fichas_compra

def dinero_sobra(dinero_disponible):
    vuelto = dinero_disponible % 500
    
    return vuelto
    
    
    
    
def menu():
    bienvendia_clientes()
    print('1.Deseas comprar fichas ')
    print('2. Salir')

    opcion = input('selccione una opcion: ')
    match opcion:
        case '1':
            print(' \nCompra de fichas ')
            nombre = input('Ingrese su nombre: ')
            dinero_disponible = float(input('Ingrese el dinero que tines: ')) 
            fichas_total = cuantas_fichas_compra(dinero_disponible)
            cambio = dinero_sobra(dinero_disponible)
            print(f'Usted puede comprar {fichas_total} fichas.')
            print(f'Dinero que le sobraria {cambio}')
            
            comprar = 'si'
            
            while comprar == 'si':
                if (fichas_total >= 1):
                    comprar = input('Quieres comprar monedas? (si/no)')
                    if (comprar == 'si'):
                        print(f'bienvenido a la compra de monedas {nombre}')
                        compra_monedas = int(input())
                        
                    elif(comprar == 'no'):
                        print('No compraste moneds. Saliendo del programa')
                        
                    else:
                        print('Error')
                
                elif(fichas_total < 1):
                    print('No tienes el dinero suficiente para comprar las fichas.')
                    comprar = 'no'
                
                else:
                    print('Error ')  
                
            
            
            
        case '2':
            print('salir')
        case _:
            print('Error ')



menu()