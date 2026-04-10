class DronVigilancia: 
    def __init__(self, nombre, modelo):
        self.nombre = nombre
        self.modelo = modelo
        self.bateria = 100
        self.estado_vuelo = 'En Tierra'
        
    def despegar(self):
        if self.bateria >= 25:
            self.estado_vuelo = 'En Vuelo'
            print(f'{self.nombre} ha despegado.')
        else:
            print(f'{self.nombre} no tiene suficiente batería para despegar, aterriza en tierra para recargar.')
        
    def parullaje(self):
        if self.estado_vuelo == 'En Vuelo':
            consumo_energia = self.bateria * 0.30
            self.bateria -= consumo_energia
            print(f'{self.nombre} está realizando un patrullaje. Batería restante: {self.bateria:.2f}')
        else:
            print(f'{self.nombre} no está en vuelo, no puede realizar un patrullaje.')
            
    def aterrizar(self):
        if self.estado_vuelo == 'En Vuelo':
            self.estado_vuelo = 'En Tierra'
            print(f'{self.nombre} ha aterrizado.')
        else:
            print(f'{self.nombre} ya está en tierra.')
    
    def recargar(self):
        if self.estado_vuelo == 'En Tierra':
            self.bateria = 100
            print(f'{self.nombre} se ha recargado completamente.')
        else:
            print(f'{self.nombre} no puede recargar mientras está en vuelo, aterriza primero.')


print('>>> INICIANDO SISTEMA SKYWATCH <<<' )

dron_uno = DronVigilancia(
    nombre=input('Ingrese el nombre del dron: '),
    modelo=input('Ingrese el modelo del dron: ')
)


inicio = True
while inicio:
    print(f'\nESTADO ACTUAL: {dron_uno.nombre} [{dron_uno.modelo}] ---')
    print (f'Batería: {dron_uno.bateria:.2f}% | Estado: {dron_uno.estado_vuelo}')
    print('\nSeleccione una acción:')
    print('1. Despegar')
    print('2. Patrullar')
    print('3. Aterrizar')
    print('4. Recargar')
    print('5. Salir')
    
    opcion = input('Ingrese el número de la acción que desea realizar: ')
    
    if opcion == '1':
        dron_uno.despegar()
    elif opcion == '2':
        dron_uno.parullaje()
    elif opcion == '3':
        dron_uno.aterrizar()
    elif opcion == '4':
        dron_uno.recargar()
    elif opcion == '5':
        inicio = False
        print('Saliendo del sistema SKYWATCH. ¡Hasta luego!')
    else:
        print('Opción no válida, por favor intente nuevamente.')