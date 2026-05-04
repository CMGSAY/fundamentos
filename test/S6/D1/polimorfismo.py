# class PersonaMayor():
#     def saludar(self):
#         print('Buenas tardes estimado, como se encuentra usted el dia de hoy es un pracer saludarlo.')

# class Adolecente(PersonaMayor):
#     def saludar(self):
#         print('Hola, todo bien?')

# senor = PersonaMayor()
# chico = Adolecente()

# senor.saludar()
# chico.saludar() 

# class Animal:
#     def __init__(self, nombre):
#         self.nombre = nombre
    
#     def hacer_sonido(self):
#         print(f'{self.nombre} Hace un sonido generico')

# class Perro(Animal):
#     def hacer_sonido(self):
#         print(f'{self.nombre} | el perro hace: Guau, Guauuuu')

# class Gato(Animal):
#     def hacer_sonido(self):
#         print(f'{self.nombre} | el gato hace: Miauu, Miaaauuuu')

# class Pato(Animal):
#     def hacer_sonido(self):
#         print(f'{self.nombre} | el pato hace: Cuac, Cuaaac')

# animal1 = Perro('Pochiberto')
# animal2 = Gato('Porticio')
# animal3 = Pato('Pancracio')


# lista_granja = []
# lista_granja.append(animal3)

# animal_desconocido = Animal('Extraterrestre')

# lista_granja.append(animal_desconocido)

# print(lista_granja)


class EmpleadoBase:
    def iniciar_rutina(self):
        print('1. LLegar al trabajo 8:00 am')
        print('2. Revisar correos')
        print('3. Planificar el dia')

class Programador(EmpleadoBase):
    def iniciar_rutina(self):
        super().iniciar_rutina()
        
        print('4. Escribir codigo')
        
trabajador1 = Programador()
trabajador1.iniciar_rutina()

