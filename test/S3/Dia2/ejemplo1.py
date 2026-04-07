# Ambito Global
nombre_publico = 'Diego'

def informacion_privada(nombre):
    # Ambito local
    nombre_privado = 'Juan Jose'
    apellido_privado = 'Mayen'
    
    print(f'Mi nobre completo es: {nombre_privado} {apellido_privado}')
    #print(f'Mi nombre publico es: {nombre_publico}')
    print(f'Mi nombre publico es: {nombre}')
    nombre = 'Carlos'

informacion_privada(nombre_publico)
#print(nombre_privado)
print(f'Mi nombre publico es: {nombre_publico}')