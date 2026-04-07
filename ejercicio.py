# funcion de fibonacci

numero = int(input('Ingrese el numero de terminos de la serie de fibonacci que desea generar: '))

a = 0
b = 1

print(a)
print(b)
for indice in range (numero - 2):
    c = a + b
    print(c)
    a = b
    b = c
