class UsuarioBancario:
    def __init__(self, nombre_ingresado, pin_ingresado):
        self.nombre = nombre_ingresado
        #atributo privado
        self.__pin = pin_ingresado

    #get tradicionales (ventanilla para consultor)
    def get_pin(self):
        return self.__pin 

    def set_pin(self, nuevo_pin):
        #validacion
        if len(str(nuevo_pin)) == 4:
            self.__pin = nuevo_pin
            print('Operacion exitosa Pin actualizados.' )
        else: 
            print('Error: el PIN debe tener exactamente 4 digitos')

#Programa principal
print('--- Sistema de seguridad ---')
cliente = UsuarioBancario('Diego', 1234)

#Primer intento de Hackeo: intento directamente al atributo privado
print(cliente.get_pin())

pin_cliente = cliente.get_pin()
print(pin_cliente)

cliente.set_pin(5544)

pin_cliente = cliente.get_pin()
print(pin_cliente)
