def menu():
    print('Bienvenido al menu de opciones')
    print('1. Comprar fichas')
    print('2. Salir')

def comprar_fichas(cantidadDinero):
    precioFicha = 500
    cantidadFichas = cantidadDinero // precioFicha
    dineroVuelto = cantidadDinero % 500
    return cantidadFichas, dineroVuelto

opcion = ''

while opcion != '2':
    menu()
    opcion = input('Ingrese la opcion que desea realizar: ')
    
    if opcion == '1':
        nombre = input('Ingrese su nombre: ')
        cantidadDinero = float(input('Ingrese la cantidad de dinero que desea gastar: '))
        cantidadFichas, dineroVuelto = comprar_fichas(cantidadDinero)
        
        if cantidadFichas == 0:
            print('No tienes suficiente dinero para comprar fichas, por favor intenta de nuevo.')
        else:
            print('¡Disfruta tu juego!')
            print(f'Puedes comprar {cantidadFichas} fichas')
            print(f'Tu dinero restante es: {dineroVuelto}')
    elif opcion == '2':
        print('Gracias por visitar nuestro casino, vuelva pronto!')
    else:
        print('Opcion no valida, por favor intente de nuevo.')
        
        
        
