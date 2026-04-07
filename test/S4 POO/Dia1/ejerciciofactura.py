
class FacturaEmitida: 
    pass

class TerminalPago:
    pass

factura_001 = FacturaEmitida()
factura_002 = FacturaEmitida()

terminal_principal = TerminalPago()

print('Datos de facturacion ')

print('Tipo de dato que usa la Terminal Principal: ', type(terminal_principal))

print('Numero de memoria factura 001: ', id(factura_001))
print('Numero de memoria factura 002: ', id(factura_002))

if (id(factura_001)) == (id(factura_002)):
    print('Los numeros de cedula son iguales. ')
    
else:
    print('Los numeros de cedula son diferentes. ')

    