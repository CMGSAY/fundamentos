import random
from random import choice
import math as matematicas

numero_random = random.randint(1, 10)

print(f'El numero al azar es: {numero_random}')

#------------------------------------------

nombres = ['Ana', 'Luis', 'Carlos']
nombre_azar = choice(nombres)
print(f'El nombre es: {nombre_azar}')

#------------------------------------------

redondear = matematicas.ceil(4.2)
print(f'El resultado es: {redondear}')