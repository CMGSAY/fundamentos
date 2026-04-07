
def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

edad_usuario = int(input('Ingrese su edad: '))
if es_mayor_de_edad(edad_usuario):
    print('Puedes comprara alcohol')
else:
    print('venta denegada. ')
    
