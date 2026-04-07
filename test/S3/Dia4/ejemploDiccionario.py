producto = {
    'nombre': 'arroz',
    'precio':  1200.00,
    'cantidad':  5
}

print(producto['nombre'])
print(producto['precio'])
print(producto['cantidad'])

total = producto['cantidad'] * producto['precio']
print(f'El total de los productos son: {total}')

print(producto)

producto['precio'] = 1500.1

print(producto)

producto['cantidad'] = producto['cantidad'] - 1

print(producto)

# agregar
producto['categoria'] = 'Granos'
print(producto)

for clave in producto:
    print(f'Clave: {clave}: Valor: {producto[clave]}')
    
for clave, valor in producto.items():
    print(f'clave: {clave}: valor: {valor}')
