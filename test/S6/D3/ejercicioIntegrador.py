from abc import ABC, abstractmethod

class VehiculoTerrestre(ABC):
    @abstractmethod
    def conducir_ruedas(self):
        pass

class VehiculoAcuatico(ABC):
    @abstractmethod
    def encender_helices(self):
        pass

class VehiculoAnfibio(VehiculoTerrestre, VehiculoAcuatico):
    @abstractmethod
    def conducir_ruedas(self):
        pass
    
    @abstractmethod
    def encender_helices(self):
        pass

class AutoComun(VehiculoTerrestre):
    def conducir_ruedas(self):
        print("Encendiendo ruedas y avanzando por carretera.")

class Lancha(VehiculoAcuatico):
    def encender_helices(self):
        print("Encendiendo hélices y navegando en el agua.")

class Anfibio(VehiculoAnfibio):
    def conducir_ruedas(self):
        print("Activando tracción 4x4 en terreno rocoso.")
    
    def encender_helices(self):
        print("Retrayendo ruedas y activando propulsión acuática.")


    


# Instanciar autos
auto1 = AutoComun()
auto2 = AutoComun()

# Instanciar Lanchas
lancha1 = Lancha()
lancha2 = Lancha()

# Instanciar los anfibios
anfibio1 = Anfibio()
anfibio2 = Anfibio()

auto1.conducir_ruedas()
lancha1.encender_helices()
anfibio1.conducir_ruedas()
anfibio1.encender_helices()

