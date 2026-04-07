# Generar una tabla de multiplicar del 1 al 10

print('Bjienvenido al programa de tablas de multiplicar')
numero = int(input('Ingrese el numero para generar su tabla de multiplicar: '))

for indice in range (11):
    resultado = numero * indice
    print(f'{numero} x {indice} = {resultado}')