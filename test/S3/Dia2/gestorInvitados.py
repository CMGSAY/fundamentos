# funcion para mostrar el menu
def menu():
    print('\nMenu de usuario. ')
    print('1. Registrar nuevo invitado.')
    print('2. Ver lista completa.')
    print('3. Eliminar a alguien (por si se porta mal).')
    print('4. Salir.')
    
# Funcion para registrar un nuevo invitado
def registrar_usuario(nombre, lista_invitados):
    lista_invitados.append(nombre)
    return lista_invitados

# funcion para mostrar la lista de Invitados
def mostrar_lista (lista_invitados):
    for nombre_invitado in lista_invitados:
        print(f'nombre: {nombre_invitado}')

# funcion para eliminar de la lista a un usaurio
def eliminar_usuario(nombre, lista_invitados):
    lista_invitados.remove(nombre)
    return lista_invitados
        
    
    

lista_invitados = []
salir = 'no'

while salir == 'no':
    menu()
    opcion = input('Seleccione la opcion que de sea realizar: ')
    match opcion:
        case '1':
            print('\n1. Registrar nuevo invitado.')
            nombre = input('Ingrese el nombre del invitado: ')
            lista_invitados = registrar_usuario(nombre, lista_invitados)
            
            
        
        case '2':
            print('\n2. Ver lista completa.')
            mostrar_lista(lista_invitados)
            
            nombre_buscar = input('Ingrese el nombre del invitado que deasea buscar: ')
            if mostrar_lista(lista_invitados) == nombre_buscar:
                print('No puede usar este nombre.')
            else:
                print('Este nombre no se encuentra en tu lista lo puedes agregar.')
            
        case '3':
            print('\n3. Eliminar a alguien (por si se porta mal).')
            nombre = input('Ingrese el nombre: ')
            lista_invitados = eliminar_usuario(nombre, lista_invitados)
            
            print('\nLista Actualizada: ')
            mostrar_lista(lista_invitados)
            
        case '4':
            print('\nGracias por Venir.')
            salir = 'si'
        
        case _:
            print('Error dato equivocado.')
            
