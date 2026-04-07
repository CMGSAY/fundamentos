for producto in range(6):
    if producto == 3:
        continue
    
    print('Producto etiquetado: ', producto)
    
    
print('='*15)
print('escaner de Productos')
print('='*15)

# Ejemplo de un break buscanod un producto peligroso
for caja in range (1, 11):
    print(f'Escneando caja {caja}')
    
    # simulamos que la caja 5 es un producto peligroso
    if caja == 5:
        print('alerta')
        break
print('el scaner ha terminado su revisio de seguridad.')


print('\='*15)
print('Proceso de Pagos')
print('='*15)

for cliente in range (1, 6):
    print(f'Procesando pago del cliente {cliente}')
    
    # Simulamos que el cliente 5 tiene un error en su pago
    # Fondo insuficiente, tarjeta vencida, etc
    
    if cliente == 5:
        print('Erro!!! ')
        continue
    
    print('pago Procesado exitosamente.')
