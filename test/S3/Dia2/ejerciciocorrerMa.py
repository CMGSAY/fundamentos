print('Iniciando Inventario ')

estante = [
    ['pizza', 'Pollo frito', 'Arroz chino'],
    ['agua', 'red bull', 'coca cola']
]

# ciclo externo, viaje por las filas completas
for fila in estante:
    # ciclo interno, viaja por cada producto dentro de la fina
    for producto in fila:
        if producto == 'agua':
            fila[fila.idex(producto)] == 'vacio'
            break

print('='*15)



# manera dos de hacerlo
for fila in range(len(estante)): # 0,1,2
    for columna in range ( len(estante[fila])):
        if estante[fila][columna] == 'vacio':
            
            estante[fila][columna] = 'pepsi'
            break
    