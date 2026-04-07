opcion = input('Selecciones una opcion (1 - 3): ')

match opcion:
    case '1':
        print('Registro de producto')
    case '2':
        print('Mostrando inventario... ')
    case '3' | 'salir':
        print('saliendo...')
    case _:
        print('Opcion invalida')