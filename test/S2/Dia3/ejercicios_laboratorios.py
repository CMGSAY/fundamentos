# ---------------------------
#         Ejercicio 1
# ---------------------------

# Control de entrada a un Torneo

print('Bienvenido al Torneo ')

nombreParticipante = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))
inscripcionConfirmada = input('Tiene inscripcion Confirmada? (si/no) ')

if (edad >= 15) and (inscripcionConfirmada == 'si'):
    print('Participante autorizado para ingresar al torneo. ')
elif (inscripcionConfirmada == 'no'):
    print('No tienes la inscripcion confirmada para este torneo. ')
elif (edad < 15 ):
    print('No cumples aun con la edad minima para entrar al torneo. ')
else:
    print('Datos incorrectos.')
    

# ---------------------------
#         Ejercicio 2
# ---------------------------

# Bateria de celular
bateria = int(input("Ingrese el porcentaje de bateria: "))

if (bateria <= 20):
    print("Debe cargar el celular")
else:
    print("La batería es suficiente")
    

# ---------------------------
#         Ejercicio 3
# ---------------------------

# Clasificacion de envio

print('Bienvenido a la clasificacion de pesos')

peso = float(input('Ingrese el peso en KG de su paquete: '))

if (peso < 1):
    print('paquete liviano. ')
elif (1 <= peso <= 5):
    print('Paquete estandar. ')
elif (peso > 5):
    print('Paquete Pesado. ')
else:
    print('Valor incorrecto. ')
    

# ---------------------------
#         Ejercicio 4
# ---------------------------

# Semaforo

color = input("Ingrese el color del semaforo: ")
if color == "verde":
    print("Avanzar")
elif color == "amarillo":
    print("Precaución")
else:
    print("Detenerse")


# ---------------------------
#         Ejercicio 5
# ---------------------------

# Acceso VIP a concierto con compras de bebida

print('Bienvenido al area VIP')
nombreCliente = input('Ingrese su nombre: ')
edadCliente = int(input('Ingrese su edad: '))
tipoEntrada = input('Ingrese el tipo de entrada que tiene (General/VIP): ')
valorBebida = float(input('Ingrese el valor de la bebida especial: '))
dineroCliente = float(input('Ingrese el dinero del cliente: '))
cambio = 0.00

if (tipoEntrada == 'vip') and (edadCliente >= 18):
    print('\nBienvenido al area VIP')
    print('Disfrtua el concierto ')
    
    
    compraBebida = input('\nDeseas comprar la bebida especial? (si/no)')
    if (compraBebida == 'si'):
        print('\nCon esta bebida disfrutaras mejor del concierto')
        cambio = dineroCliente - valorBebida
        
        
        if (valorBebida <= dineroCliente):
            print(f'\nSu cambio es: {cambio}')
            print('Gracias por su compra')
            
            
        elif(valorBebida > dineroCliente):
            print('No puedes comprar la bebida especial.')
            print(' Dinero insuficiente.')
        else:
            print('Datos incorrectos. ')
    
    
    elif(compraBebida == 'no'):
        print('Disfruta el concierto, regrasa si quieres la bebida.')
    
    
    else:
        print('Error con el dato ingresado.')
 
    
elif(tipoEntrada == 'general'):
    print('No puedes ingresar al area VIP con etrada General')


elif(edadCliente < 18):
    print('No cumples con la edad minima para disfutar del area VIP. ')


else:
    print('Datos de entrada incorrecto. ')


# ---------------------------
#         Ejercicio 6
# ---------------------------

# Sistemas de Becas estudiantiles y condicion economica

print('Binvenido al sistema de becas Estudiantiles')

nombreEstudiante = input('\nIngrese su nombre: ')
promedioFinal = float(input('Ingrese su promedi final: '))
ingresoFamiliar = float(input('Cual es el ingreso mensual de su familia: '))
materiasAprobadas = int(input('Materias aprobadas: '))

if (promedioFinal < 70):
    print(f'Estudiante: {nombreEstudiante}')
    print('No recibe beca')
elif (70 <= promedioFinal <= 84) and (ingresoFamiliar <= 400000):
    print(f'Estudiante: {nombreEstudiante}')
    print('Recibe Beca parcial')
    print('Monto asignado:50000')
    
elif (promedioFinal >= 85):
    print(f'Estudiante: {nombreEstudiante}')
    if (materiasAprobadas >= 5) and (ingresoFamiliar <= 400000):
        print('Recibe Beca Completa')
        print('Monto asignado:100000')
    else:
        print('Recibe Beca parcial')
        print('Monto asignado:50000')


# ---------------------------
#         Ejercicio 7
# ---------------------------

# Tarifa de Hotel con cargo y descuento

print('Bienvenido al hotel buena vista')
nombreCliente = input('Ingrese su nombre: ')
temporada = input('Ingrese la temporada ( alta , media , baja )')
cantidadNoches = int(input('Ingrese la cantidad de noches: '))
precioBaseNoches = float(input('Ingrese el precio base por noche: '))
mebresia = input('Tiene membresía ( si/no )')

subTotal= cantidadNoches * precioBaseNoches
recargo = 0.00
descuento = 0.00

if (temporada == 'alta'):
    recargo = subTotal * 0.20
elif(temporada == 'media'):
    recargo = subTotal * 0.10
elif(temporada == 'baja'):
    recargo = subTotal
else:
    print('Dato incorrecto. ')

recargoSubtotal = subTotal + recargo

if (mebresia == 'si') and (cantidadNoches >= 3):
    descuento = recargoSubtotal * 0.15
elif (mebresia == 'si') or (cantidadNoches == 2):
    descuento = recargoSubtotal * 0.05
else:
    descuento = 0


totalFinal = recargoSubtotal - descuento

print('\nDatos de la reservacion:')
print(f'Nombre: {nombreCliente}')
print(f'Subtotal con recargo: {recargoSubtotal}')
print(f'Descuento aplicado: {descuento}')
print(f'Total final: {totalFinal}')



# ---------------------------
#         Ejercicio 8
# ---------------------------

# menu de academia con permisos

print('Menu de la academia')
tipoUsuario = input('\nIngrese su tipo de usuario ( admin , profesor , estudiante): ')
promedioEstudiante = int(input('Ingrese su promedio: '))
print('''Ingrese la opcion a la que quiere ingresar
      
      1. Matricular
      2. notas
      3. Certificado
      4. salir''')
opcion = input('Opcion: ')


match opcion:
    case '1' | 'matricular':
        if (tipoUsuario == 'admin') or (tipoUsuario == 'profesor'):
            print('Puedes Matricular')
        else:
            ('Solo puede hacerlo el usuario admin o profesor.')
    case '2' | 'notas':
        if (tipoUsuario == 'profesor') or (tipoUsuario == 'estudiante'):
            print('Puedes ver las notas.')
        else:
            ('No tienes permitido ver las notas')
    case '3' | 'certificado' :
        if (tipoUsuario == 'estudiante') and (promedioEstudiante >= 70):
            print('Puedes generar el certificado.')
        else:
            ('No cumples con los requisitos para obtener el certificado. ')
        
    case '4' | 'salir':
        print('Gracias por usar nuestro servicio vuelva pronto. ')
    case _:
        print('Opcion invalida.')
        


# ---------------------------
#         Ejercicio 9
# ---------------------------

# Sistema de tienda gamer con promocions y validacion de stock

print('Bienvenido a la Tienda Gamer Super Mario')

nombreCliente = input('Ingrese su nombre: ')
nombreProducto = input('Ingrese el nombre del producto: ')
precioUnitario = float(input('Ingrese el precio unitario del producto: '))
cantidadDeseada = int(input('Ingrese la cantidad de productos que nececita: '))
cantidadStock = int(input('Cantidad del producto en stock: '))
membresiaGamer = input('Tiene membresia gamer (si/no): ')
subtotal = 0.00
descuento = 0.00

if (cantidadDeseada > cantidadStock): 
    print('No se puede hacer la venta. Lo sentimos ')
elif(cantidadStock >= cantidadDeseada):
    subtotal = precioUnitario * cantidadDeseada
    
    if (subtotal > 50000) and (membresiaGamer == 'si'):
        descuento = subtotal * 0.20
    elif(subtotal > 30000) or (membresiaGamer == 'si'):
        descuento = subtotal * 0.10
    else:
        descuento = 0
    
    totalFinal = subtotal - descuento
    
    print(f'''\n Venta aprobaada
          
          Subtotal: {subtotal}
          Descuento: {descuento}
          Total final: {totalFinal}
          
          Gracias por su compra
          ''')
    
    
# ---------------------------
#         Ejercicio 10
# ---------------------------

# Panel de misiones y Calculo de recompensas

print('Menu de misiones')

nombreJugador = input('Ingrese su nombre: ')
claseJugador = input('Ingrese su clase de jugador ( guerrero, mago, arquero): ')
nivelJugador = int(input('Ingrese su nivel de jugador (1-10): '))
enemigosDerrotados = int(input('Enemigos derrotados: '))

print('''Opcion de mision
        1 o bosque
        2 o castillo
        3 o dragón
        4 o salir
      ''')
menu = input('Seleccione una Opcion: ')

match menu:
    case '1' | 'bosque':
        if (nivelJugador >= 1):
            print('Recibiste una recompensa x 10 enemigos derrotados.')
            enemigosDerrotados * 10
        
    case '2' | 'castillo':
        if (nivelJugador >= 5):
           print('Recibiste una recompensa x 20 enemigos derrotados.')
           enemigosDerrotados * 20
           if (claseJugador == 'guerrero') or (claseJugador == 'mago'):
               print('Recibiste una recompensa + 50 enemigos derrotados.')
               enemigosDerrotados +50 
    case '3' | 'dragón':
        if (nivelJugador >= 10) and (claseJugador == 'guerrero' or claseJugador == 'mago'):
           print('Recibiste una recompensa x 50 enemigos derrotados.')
           enemigosDerrotados * 50
           if (enemigosDerrotados):
               print('Recibiste una recompensa + 50 enemigos derrotados.')
               enemigosDerrotados +50
        elif (nivelJugador < 10):
            print('no cumples con el nivel de 10' )
        elif (claseJugador == 'arquero'):
            print('Tu calse de jugador no aplica en esta partida.')
    case '4' | 'salir': 
        print('Regresa pronto... ')
    case _:
        print('Opcion invalida')

