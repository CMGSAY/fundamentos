print('Bienvenido al al tienda')

#datos del cliente

cliente_vip = True
articulos_comprados = 6
dia_semana = 'Lunes'

# regla 1 = Descuento mayoritario si la compra de 5 articulos y es vip
aplica_mayoristas = (articulos_comprados > 5) and (cliente_vip == True )
print(f'Aplica descuento de mayoristas? {aplica_mayoristas}')

# Regla 2: Descuento especial de lunes si es lunes o vip
descuento = (dia_semana == 'Lunes' ) or (cliente_vip == True)

# Regra 3: Verificar que la tienda no este cerrada
tienda_cerrada = False
podemos_vender = not tienda_cerrada
print(f'podemos vender? {podemos_vender}')