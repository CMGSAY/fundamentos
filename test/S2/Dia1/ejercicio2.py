# verificacion de estudiantes
print('Bienvendido al sistema de verificacion de estudiantes')

edad = int(input('Ingrese su edad: '))
membresiaPremium = input('Cuneta con membresia? (si / no )')

entrarSala = ( edad  >= 18 ) and (membresiaPremium == 'si')


print(f'Puede ingresar a la sala exclusiva: {entrarSala}')
