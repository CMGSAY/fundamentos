bodega = [
    ['Arroz', 'Frijol', 'Lentejas'],
    ['Atun', 'Sardinas', 'Sopa'],
    ['agua', 'jugo', 'Refresco']
]

producto_buscado = bodega[1][1]
print('producto extraido: ', producto_buscado )

print('Bebida seleccionada: ', bodega[2][0])

bodega[2][1] = 'Te'
print('fila de bebida seleccionada ', bodega[2][1])