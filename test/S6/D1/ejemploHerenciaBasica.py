# class Animal:
#     def comer(self):
#         print("El animal está comiendo.")
    
# class Perro(Animal):
#     pass

# mi_mascota = Perro()
# mi_mascota.comer()

# class Vehiculo:
#     def encender_motor(self):
#         print('[Sistema] | El motor se ha encendido')

#     def apagar_motor(self):
#         print('[Sistema] | El motor se ha encendido')
# # Subclase 1(hijo)
# class Auto(Vehiculo):
#     def encender_aire(self):
#         print('[AUTO] | Aiere acondicionado es encendido')

# # Subclase 2(hijo)
# class Moto(Vehiculo):
#     def hacer_acrobacia(self):
#         print('[Moto] | Levantar la rueda delantera')

# carro = Auto()
# moto = Moto()

# print('\nacciones del Autro')
# carro.encender_motor()
# carro.encender_aire()

# print('\nacciones del moto')
# moto.encender_motor()
# moto.hacer_acrobacia()


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudinate(Persona):
    def __init__(self, nombre_ingresado, nota_ingresada):
        super().__init__(nombre_ingresado)
        self.nota = nota_ingresada

    def mostrar_info(self):
        print(f'Hola, mi nombre es: {self.nombre} y nota: {self.nota}')

estudinate1 = Estudinate('Juan', 8.5)
estudinate1.mostrar_info()