class Empleado:
    
    def __init__(self):
        self.__salario = 300
    @property    
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self, nuevo_salario):
        if nuevo_salario <= 300:
            print('No se puede actualizar el nuevo salario')
        elif nuevo_salario > 300:
            self.__salario = nuevo_salario
            print('Salario actualizados exitosamente.')
        else: 
            print('Error en los datos')
            

empleado1 = Empleado()

print(empleado1.salario)
empleado1.salario = 350
print(empleado1.salario)