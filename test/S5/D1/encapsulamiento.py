class Cuenta:
    def __int__(self, saldo_inicial):
        self.nombre = 'Publica'
        self.__saldo = saldo_inicial
        
mi_cuenta = Cuenta(1000)

print(mi_cuenta.nombre)
print(mi_cuenta.__saldo)