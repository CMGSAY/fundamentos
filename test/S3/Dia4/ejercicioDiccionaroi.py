cliente = {
    'nombre': ' ',
    'edad': 0,
    'ciudad' : ' '
}

nombre= input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))
ciudad = input('Ingrese su ciudad: ')

cliente['nombre'] = nombre
cliente['edad'] = edad
cliente['ciudad'] = ciudad

print('Datos clientes: ')
print(cliente)

print('Datos modificados: ')
ciudad_nueva = input('Ingrese una nueva ciudad: ')
edad_extra = int(input('Cuanto quieres incrementar a la edad: '))
cliente['edad'] = cliente['edad'] + edad_extra
cliente['ciudad'] = ciudad_nueva

print(cliente)