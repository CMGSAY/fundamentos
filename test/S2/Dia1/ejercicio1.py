# acomodar 47 latas en filas de 10

latas = 47
soporte_estante = 10
estantes_llenenos = latas // soporte_estante
sobrante = latas % soporte_estante

print('\nAcomodacion de latas de atun:')
print('%32s:%10d' %('Cantidad de estantes llenos',  (estantes_llenenos)))
print('%32s:%10d' %('Latas que sobrarain', (sobrante)))

