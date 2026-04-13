#Clase padre
class PersonajeBase:
    def caminar(self):
        print("El Personaje esta avanzando por el mapa")
        
    def descansar(self):
        print("El Personaje esta recuperando energia")


# clase hija 1
class Mago(PersonajeBase):
    def lanzar_hechizo(self):
        print("El Mago lanza una bola de fuego.")
        
# clase hija 2
class guerrero(PersonajeBase):
    def bloquear_ataque(self):
        print("El Guerrero levanta su escudo de metal.")
        
        
# Crear instancias de cada clase
mi_mago = Mago()
mi_guerrero = guerrero()

# Mostrar las acciones de cada personaje
print('\nAcciones del Mago')
mi_mago.caminar()
mi_mago.descansar()
mi_mago.lanzar_hechizo()

print('\nAcciones del Guerrero')
mi_guerrero.caminar()
mi_guerrero.descansar()
mi_guerrero.bloquear_ataque()

