edad = int(input('Digite su edad: '))
precioEntrada = 2000

if edad <= 12:
    print('el cliente es un niño, tiene un descuento del 50%')
    total  = precioEntrada * 0.5
elif edad >= 60:
    print('El cliente es un adulto mayor. tiene un descuento del 25%')
    total = precioEntrada * 0.75
else:
    print('el cliente es un adulto, no tiene descuento')
    total = precioEntrada

print('El precio total de la entrada es : ', total)

