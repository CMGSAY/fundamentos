# Proyecto: Linea de produccion
# menu de bienvenida
print('='*30)
print('Linea de produccion')
print('='*30)

# Funcion para guardar los codigos ingresados en una lista
def guardar_codigo(lista, codigo):
    lista.append(codigo)

# Funcion para mostrar todos los codigos ingresados hasta el momento
def mostrar_codigos(codigos):
    print('Los codigos ingresados son: ')
    for codigo in codigos:
        print(codigo)

# Funcion que divide cada codigo en sus partes:
# [producto (1-3), cantidad (100-999), estado (0 o 1)]
# Si el codigo no cumple con el formato, se marca como error
def dividir_codigo(lista_codigos):
    
    lista_codigo_dividido = []

    for codigo in lista_codigos:
        
        if len(codigo) == 5 and codigo.isdigit():
            codigo_dividido = [ int(codigo[0]), int(codigo[1:4]), int(codigo[4]) ]
        else:
            codigo_dividido = ['Error']
        
        lista_codigo_dividido.append(codigo_dividido)

    return lista_codigo_dividido

# Funcion para validar los codigos ya divididos
# Se verifica:
# - Producto entre 1 y 3
# - Cantidad entre 100 y 999
# - Estado entre 0 y 1
# Los codigos invalidos se almacenan aparte
def codigo_valido(lista_codigo_dividido):
    
    lista_codigos_validos = []
    lista_codigos_invalidos = []

    for codigo in lista_codigo_dividido:
        
        if codigo == ['Error']:
            lista_codigos_invalidos.append(codigo)
            continue
        
        if (1 <= codigo[0] <= 3) and (100 <= codigo[1] <= 999) and (0 <= codigo[2] <= 1):
            lista_codigos_validos.append(codigo)
        else:
            lista_codigos_invalidos.append(codigo)

    return lista_codigos_validos, lista_codigos_invalidos


# Funcion para clasificar los codigos validos por tipo de producto
# Se separan en tres diccionarios: fertilizante, insecticida y herbicida
def clasificar_lote(lista_codigos_validos):
    diccionario_lote_uno = {
        'nombre': 'Fertilizante',
        'lotes': [],
        'cantidades': [],
        'estados': []
    }
    diccionario_lote_dos = {
        'nombre': 'Insecticida',
        'lotes': [],
        'cantidades': [],
        'estados': []
    }
    diccionario_lote_tres = {
        'nombre': 'Herbicida',
        'lotes': [],
        'cantidades': [],
        'estados': []
    }

    # Clasificacion segun el tipo de producto (codigo[0])
    for codigo in lista_codigos_validos:        
        lote = codigo[0]
        cantidad = codigo[1]
        estado = codigo[2]

        if lote == 1:
            diccionario_lote_uno['lotes'].append(lote)
            diccionario_lote_uno['cantidades'].append(cantidad) #Sourcery . Extract duplicated code into function (remove comment)
            diccionario_lote_uno['estados'].append(estado)

        elif lote == 2:
            diccionario_lote_dos['lotes'].append(lote)
            diccionario_lote_dos['cantidades'].append(cantidad)
            diccionario_lote_dos['estados'].append(estado)

        elif lote == 3:
            diccionario_lote_tres['lotes'].append(lote)
            diccionario_lote_tres['cantidades'].append(cantidad)
            diccionario_lote_tres['estados'].append(estado)

    return diccionario_lote_uno, diccionario_lote_dos, diccionario_lote_tres

# Funcion para determinar la categoria segun el promedio de unidades por lote
def determinar_categoria(cantidad):
    if 0 <= cantidad <= 99:
        return 'Insuficiente'
    elif 100 <= cantidad <= 299:
        return 'Regular'
    elif 300 <= cantidad <= 599:
        return 'Idóneo'
    elif 600 <= cantidad <= 999:
        return 'Sobreproducción'
    else:
        return 'Cantidad fuera de rango'

# Listas vacias donde se almacenaran los codigos ingresados
lista_codigos = [ ]


# Bucle while para ingresar codigos hasta que se ingrese 'FIN'
while True:
    codigo = input('\nIngrese un codigo: ')
    
    if codigo == 'FIN':
        print('Fin del programa')
        break
    
    # Guardar y mostrar codigos ingresados
    guardar_codigo(lista_codigos, codigo)
    mostrar_codigos(lista_codigos)    
    print(f'El codigo ingresado es: {codigo}')       

# dividir los codigos ingresados y validar los codigos
lista_codigo_dividido = dividir_codigo(lista_codigos)
lista_codigos_validos, lista_codigos_invalidos = codigo_valido(lista_codigo_dividido)

# clasificar los codigos validos por lote, cantidad y estado
diccionario_lote_uno, diccionario_lote_dos, diccionario_lote_tres = clasificar_lote(lista_codigos_validos)

# variables para almacenar la cantidad y lotes de cada producto
cantidad_lote_uno = 0
numero_lotes_uno = 0
cantidad_lote_dos = 0
numero_lotes_dos = 0
cantidad_lote_tres = 0
numero_lotes_tres = 0

# for para calcular la cantidad total y el numero de lotes de cada producto
for cantidad in diccionario_lote_uno['cantidades']:
    cantidad_lote_uno += cantidad
    numero_lotes_uno += 1

for cantidad in diccionario_lote_dos['cantidades']:
    cantidad_lote_dos += cantidad
    numero_lotes_dos += 1

for cantidad in diccionario_lote_tres['cantidades']:
    cantidad_lote_tres += cantidad
    numero_lotes_tres += 1
    
# variables para almacenar el promedio de cada lote
promedio_lote_uno = 0
promedio_lote_dos = 0 
promedio_lote_tres = 0

# Determinar el producto con mayor cantidad de lotes, evitando la division por cero
if numero_lotes_uno > 0:
    promedio_lote_uno = cantidad_lote_uno / numero_lotes_uno

if numero_lotes_dos > 0:
    promedio_lote_dos = cantidad_lote_dos / numero_lotes_dos

if numero_lotes_tres > 0:
    promedio_lote_tres = cantidad_lote_tres / numero_lotes_tres

# Determinar categoria de cada producto segun su promedio
categoria_lote_uno = determinar_categoria(promedio_lote_uno)
categoria_lote_dos = determinar_categoria(promedio_lote_dos)
categoria_lote_tres = determinar_categoria(promedio_lote_tres)

# variable para almacenar el producto mas producido
producto_mas_producido = ''

# Determinar el producto con mayor produccion total
if cantidad_lote_uno >= cantidad_lote_dos and cantidad_lote_uno >= cantidad_lote_tres:
    producto_mas_producido = 'Fertilizante'
elif cantidad_lote_dos >= cantidad_lote_uno and cantidad_lote_dos >= cantidad_lote_tres:
    producto_mas_producido = 'Insecticida'  
else:
    producto_mas_producido = 'Herbicida'

# variable para almacenar el producto con mas lotes
producto_mas_lotes = ''
# Determinar el producto con mayor cantidad de lotes
if numero_lotes_uno >= numero_lotes_dos and numero_lotes_uno >= numero_lotes_tres:
    producto_mas_lotes = 'Fertilizante'
elif numero_lotes_dos >= numero_lotes_uno and numero_lotes_dos >= numero_lotes_tres:
    producto_mas_lotes = 'Insecticida'
else:
    producto_mas_lotes = 'Herbicida'

# Almacenar el promedio de productos producidos por lote
promedio_productos_producido = 0

# Almacenar el total de lotes
lotes_totales = numero_lotes_uno + numero_lotes_dos + numero_lotes_tres

# Almacenar el total de productos producidos
productos_totales = promedio_lote_uno + promedio_lote_dos + promedio_lote_tres

# Calcular el promedio total de produccion.
if productos_totales > 0:
    promedio_productos_producido = productos_totales / 3

# mostrar los resultados finales
print('\nSalida de los datos ingresados: ')

print('Los codigos invalidos: ')
print(lista_codigos_invalidos)

print('\n--- RESULTADOS FINALES ---')

print(f'{"Producto":<15} {"Lotes":<15} {"Total Unidades":<15} {"Promedio Lote":<15} {"Categoria":<15}')
print('-'*75)

print(f'{diccionario_lote_uno["nombre"]:<15} {numero_lotes_uno:<15} {cantidad_lote_uno:<15} {promedio_lote_uno:<15.2f} {categoria_lote_uno:<15}')
print(f'{diccionario_lote_dos["nombre"]:<15} {numero_lotes_dos:<15} {cantidad_lote_dos:<15} {promedio_lote_dos:<15.2f} {categoria_lote_dos:<15}')
print(f'{diccionario_lote_tres["nombre"]:<15} {numero_lotes_tres:<15} {cantidad_lote_tres:<15} {promedio_lote_tres:<15.2f} {categoria_lote_tres:<15}')

print('-'*75)
print(f' Producto mas producido: {producto_mas_producido}') 
print(f' Producto con mas lotes: {producto_mas_lotes}')
print(f' Promedio de productos producidos por lote: {promedio_productos_producido:.2f}')

# 13120 12481 33610 06001 38860 29080 17251