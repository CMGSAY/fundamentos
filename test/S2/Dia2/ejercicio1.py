edadCliente = int(input('Ingrese su edad: '))
entradaDisponible = input('Cunta con entradas para la pelicual? (si/no): ')
edadPelicula = 18

if (edadCliente >= edadPelicula ) and (entradaDisponible == "si"):
    print('Bienvenido al cine que disfrutes de la pelicula.')
else:
    print('No cumples con los requisitos de ver esta pelicula.')
    
print('Gracias por su visita, Vuelva pronto')