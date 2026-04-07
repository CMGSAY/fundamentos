
ahorro= 0.00
meta = 100000.00
print('Bienvenido al programa de ahorro')
print(f'La meta de ahorro es de: {meta}')

while ahorro < meta:
    deposito = float(input('\nIngrese la cantidad que desea ahorrar hoy: '))
    ahorro += deposito
    print(f'El total ahorrado es de: {ahorro}')
    print(f'Faltan {meta - ahorro} para alcanzar la meta de ahorro')

print('\n¡Felicidades! Has alcanzado tu meta de ahorro')