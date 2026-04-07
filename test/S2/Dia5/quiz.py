# Acceso al laboratorio de impresion 3d con compra de minutos extras

print('=========================')
print('Bienvenido al laboratorio')
print('=========================')

nombreEstudiante = input('Ingrese su nombre: ')
edadEstudiante = int(input('Ingrese su edad: '))
autorizacionProfe = input('Tiene autorizacion por el profesor? (si/no): ')
saldoDisponible = float(input('Ingrese el saldo diponible del estudiante: '))
costoMinExtra = float(input('Ingrese el costo del minuto extra: '))
contador = 0
acceso = ' '
compra = 'si'

if (edadEstudiante >= 15 ) and (autorizacionProfe == 'si'):
    #Ingresa
    print(f'\nBinevenido {nombreEstudiante} al laboratorio 3D. ')
    print('Usa las instalciones con responsabilidad.')
    acceso = 'Aprobado'
    
    while (saldoDisponible >= costoMinExtra) and (compra == 'si'):
        compra = input('\nDeseas comprar minutos extras? (si/no): ')
        if compra == 'si':
            print('Felicidades has comprado un paquete de minutos.')
            turno = 1
            contador = contador + turno
            saldoDisponible = saldoDisponible - costoMinExtra
        elif compra == 'no':
            
            print('No cuentas con minutos extras.')
        else:
            print('\nDatos incorrectos.')
    
    print('paquetes comprados')        
            
elif (autorizacionProfe == 'no'):
    print('\nNececitas la autorizacion del profesor para ingresar')
    acceso = 'Denegado'
elif(edadEstudiante <15 ):
    print('\nNececitas tener 15 años para poder entrar. ')
    acceso = 'Denegado'
else:
    print('\nDatos incorrectos.')
    acceso = 'Denegado'
    

print(f'''
      Acceso {acceso} al labaratorio 3D para: {nombreEstudiante}
      Compra realizada.
      Paquetes comprados: {contador}
      Saldo restante: {saldoDisponible}
      
      Gracias por visitarnos.
      ''')