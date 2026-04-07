

opcion = '2'

while opcion != 'salir' and opcion != '2':
    print('1 - Saludar')
    print('2 - Salir')
    
    opcion = input('Ingrese una opcion: ')
    
    if opcion == '1' or opcion == 'saludar':
        print('Hola, como estas?')
    elif opcion != 'salir' or opcion != 'salir':
        print('Adios, que tengas un buen dia.')
    else:
        print('Opcion no valida, por favor ingrse una opcion valida.')
