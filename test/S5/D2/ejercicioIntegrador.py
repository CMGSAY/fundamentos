class RegistroAcademico:
    def __init__(self, nombre_alumno, nota_inicial):
        self.nombre = nombre_alumno
        self.__nota = nota_inicial
        self.cuenta_activa = True
    
    def get_nota(self):
        return self.__nota
    
    def bloquear_cuenta(self):
        self.cuenta_activa = False
    
    def set_nota(self, nueva_nota):
        
        if self.cuenta_activa == 'False':
            
            return -2
        elif 0 <= nueva_nota <= 100:
            self.__nota = nueva_nota
            
            return 1
        else:
            
            return -1
    
    
print('--- Notas Academicas ---')
estudiante = RegistroAcademico('Laura', 85)

intentos_permitidos = 3

while intentos_permitidos > 0:        
    nota_estudiante = estudiante.get_nota()
    print(f'Nota actual: {nota_estudiante}')
    
    nueva_nota= int(input('Ingrese la nueva nota: '))

    numero = estudiante.set_nota(nueva_nota)
    
    if numero == 1:
        print('felicidades, nota modificada con exito.')
        break
    elif numero == -1:
        print('No cumple con los requisitos')
        intentos_permitidos -= 1
    elif numero == -2:
        print('Dato Invalido')
        intentos_permitidos -= 1
        
    
    
                