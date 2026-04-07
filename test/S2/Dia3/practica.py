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

