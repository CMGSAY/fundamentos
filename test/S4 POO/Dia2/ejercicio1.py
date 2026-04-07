class Empleado():
    pass

empleado_1 = Empleado()
empleado_2 = Empleado()
empleado_3 = Empleado()

empleado_1.nombre = 'Carlos'
empleado_1.cargo = 'Gerente'
empleado_1.salario = 5000.00

empleado_2.nombre = 'Daniel'
empleado_2.cargo = 'Cajero'
empleado_2.salario = 4500.00

empleado_3.nombre = 'Joel'
empleado_3.cargo = 'Bodeguero'
empleado_3.salario = 4000.00

print('Datos Empleados: ')
print(f'Empleado 1: {empleado_1.nombre}, Cargo: {empleado_1.cargo}, Salario: {empleado_1.salario} ')
print(f'Empleado 2: {empleado_2.nombre}, Cargo: {empleado_2.cargo}, Salario: {empleado_2.salario} ')
print(f'Empleado 3: {empleado_3.nombre}, Cargo: {empleado_3.cargo}, Salario: {empleado_3.salario} ')

