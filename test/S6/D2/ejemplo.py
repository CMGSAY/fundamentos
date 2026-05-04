print('\n --- SIMULACION DE SOBRECARGA DE METODOS ---')

class CalculadoraRRHH:
    def procesar_pago(self, salario_base, bono=0, deducciones=0):
        print(f'Procesando pago (Base: {salario_base}, Bono{bono}, deducciones {deducciones})')
        
        # La navaj suiza analiza el contexto
        total = salario_base + bono - deducciones
        print(f'Total a depositar: {total}')
        
        sistema = CalculadoraRRHH()
        
        