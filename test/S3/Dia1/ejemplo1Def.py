def saludo(nombre):
    print('Hola como estas?')
    print(f'como estas, {nombre}')
    
def despedida(nombre):
    print('adios, que tengas un buen dia.')
    
def caculo_impuestos(precio):
    impuesto = precio * 0.15
    total = precio + impuesto
    return total

# funcion con varios puntos de retorno
def generar_mensaje(nombre):
    if nombre == 'alice':
        return 'Hola Alice, como estas?'
    elif nombre == 'bob':
        return'Hola, Bob como estas?'
    else:
        return 'Hola, como estas?'


def menu():
    print('1. Saludar: ')
    print('2.Despedirse: ')
    print('3. Salir')
    print('4. calcular impuesto')
    
    opcion = input('selccione una opcion: ')
    nombre = input('Ingrese su nombre: ')
    
    while opcion != '3':
        match opcion:
            case '1':
                saludo(nombre)
            case '2':
                despedida(nombre)
            case '3':
                print('Saliendo... ')
            case '4':
                precio = float(input('Ingrese el precio: '))
                precio_total = caculo_impuestos(precio)
                
                print(f'el precio total con imuestos es {precio_total}')
            case _:
                print('Opcion no valida')
        opcion = input('selccione una opcion.')

menu()
