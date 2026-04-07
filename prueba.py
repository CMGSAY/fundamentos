print('='*30)
print('Linea de produccion')
print('='*30)

# -------- FUNCIONES -------- #

def dividir_codigo(lista_codigos):
    lista_dividida = []
    
    for numero in lista_codigos:
        if len(numero) == 5 and numero.isdigit():
            resultado = [int(numero[0]), int(numero[1:4]), int(numero[4])]
        else:
            print(f'dato invalido {numero}')
            resultado = None
        
        lista_dividida.append(resultado)
    
    return lista_dividida


def validar_codigo(lista_codigos, lista_dividida):
    validos = []
    
    for i in range(len(lista_dividida)):
        codigo = lista_dividida[i]
        original = lista_codigos[i]
        
        if codigo is not None:
            if (1 <= codigo[0] <= 3) and (100 <= codigo[1] <= 999) and (0 <= codigo[2] <= 1):
                validos.append(codigo)
            else:
                print(f'dato invalido {original}')
    
    return validos


def determinar_categoria(promedio):
    if 0 <= promedio <= 99:
        return 'Insuficiente'
    elif 100 <= promedio <= 299:
        return 'Regular'
    elif 300 <= promedio <= 599:
        return 'Idoneo'
    elif 600 <= promedio <= 999:
        return 'Sobreproduccion'
    else:
        return 'Fuera rango'


# -------- PROGRAMA -------- #

lista_codigos = []

# Entrada de datos
while True:
    codigo = input('Ingrese un codigo (FIN para terminar): ')
    
    if codigo == 'FIN':
        break
    
    lista_codigos.append(codigo)

# Procesamiento
lista_dividida = dividir_codigo(lista_codigos)
lista_validos = validar_codigo(lista_codigos, lista_dividida)

# Listas para cálculo
totales = [0, 0, 0]
lotes = [0, 0, 0]

# Agrupar datos
for codigo in lista_validos:
    indice = codigo[0] - 1
    totales[indice] += codigo[1]
    lotes[indice] += 1

# Promedios
promedios = [0, 0, 0]

for i in range(3):
    if lotes[i] > 0:
        promedios[i] = totales[i] / lotes[i]

# Categorías
categorias = [
    determinar_categoria(promedios[0]),
    determinar_categoria(promedios[1]),
    determinar_categoria(promedios[2])
]

productos = ['Fertilizante', 'Insecticida', 'Herbicida']

# Mayor producción
mayor_produccion = productos[totales.index(max(totales))]

# Más lotes
mayor_lotes = productos[lotes.index(max(lotes))]

# Promedio general
total_unidades = sum(totales)
total_lotes = sum(lotes)

if total_lotes > 0:
    promedio_general = total_unidades / total_lotes
else:
    promedio_general = 0

# -------- SALIDA FORMATEADA -------- #

print('\n--- RESULTADOS FINALES ---\n')

print(f'{"Producto":<15} {"Lotes":<15} {"Total":<15} {"Promedio":<15} {"Categoria":<15}')
print('-'*75)

for i in range(3):
    print(f'{productos[i]:<15} {lotes[i]:<15} {totales[i]:<15} {promedios[i]:<15.2f} {categorias[i]:<15}')

print('-'*75)

print(f'Producto mas producido: {mayor_produccion}')
print(f'Producto con mas lotes: {mayor_lotes}')
print(f'Promedio general por lote: {promedio_general:.2f}')