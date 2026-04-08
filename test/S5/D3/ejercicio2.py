class TermostatoDigital:
    # se protege colocando la temperatura de forma privada
    def __init__ (self):
        self.__temperatura = 20
        
    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, nueva_temperatura):
        if  nueva_temperatura < 5:
            print('No puedes bajar la temperatura menos de 5 Grados')
        elif nueva_temperatura > 35:
            print('Por seguridad no puedes subir la temperatura mas de 35 Grados')
        elif 5 <= nueva_temperatura <= 35:
            self.__temperatura = nueva_temperatura
            print(f'Temperatura modificada Exitosamente. Temperatura actual: {self.__temperatura}')
    
    

termostato_uno = TermostatoDigital()



modificar_temperatura = True

while modificar_temperatura == True:
    print('''
          Menu de temperatura
          
          1. Consultar temperatura
          2. Modificar temperatura
          3. Salir
          ''')
    opcion = int(input('Eliga una opcion: '))
    
    if opcion == 1:
        print(f'Temperatura actual: {termostato_uno.temperatura} Grados')
    elif opcion == 2:
        termostato_uno.temperatura = int(input('Ingrese la Temperatura que desea entre 5 a 35 : '))
    elif opcion == 3:
        print('Saliendo del programa.')
        break
    else: 
        print('Opcion invalida')
        
    
     # 1) se protege colocando la temperatura de forma privada
     # 2) Al usar @property nos permite poder conocer el atributo pirvado que seria temperatura
     # 3) 