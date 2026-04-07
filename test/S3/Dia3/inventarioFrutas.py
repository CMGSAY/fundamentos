# calcular cuantas frutas totales hay
# de los que tengan mayor a 5 o que sean numeros par



            

print('='*34)
print(' Inventario de Tienda de frutas' )
print('='*34)


inventario = [
    [10, 4, 8],
    [5, 12, 3],
    [7, 20, 6]
]

frutas_aceptadas = []

for filas in inventario:
    for frutas in filas:
        if (frutas > 5) and (frutas % 2 == 0):
            frutas_aceptadas.append(frutas)
        

print('Las frutas aceptadas son: ')
print(frutas_aceptadas)            

contador_frutas = 0

for frutas in frutas_aceptadas:
    contador_frutas = contador_frutas + frutas

print(f'Total de frutas: {contador_frutas}')
            
