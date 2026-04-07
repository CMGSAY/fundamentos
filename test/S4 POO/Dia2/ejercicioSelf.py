class Empleado:
    def saludar_cliente(self):
        print(f'Hola me llamo {self.nombre}')


# fabricamos el objeto
cajero = Empleado()
bodeguero= Empleado()

cajero.nombre = 'Diego'
bodeguero.nombre = 'Luis'

cajero.saludar_cliente()
bodeguero.saludar_cliente()

