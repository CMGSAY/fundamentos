

print('Tienda de abarrote')

precios_pasillos = [
    [10.0, 55.0, 20.0],
    [45.0, 80.0, 12.0],
    [100.0, 30.0, 48.0]
]

for fila in precios_pasillos:
    for precio in fila:
        
        if precio < 50:
            incremento = precio * 0.10
            nuevo_precio = precio + incremento
            
            fila[fila.index(precio)] = nuevo_precio
            
print('Precios actualizados: ')

for fila in precios_pasillos:
    print('')
    for precio in fila:
        print(f'{precio} ', end= ' ')
