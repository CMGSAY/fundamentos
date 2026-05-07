from abc import ABC, abstractmethod

# Excepción personalizada
class EnergiaInvalidaError(Exception):
    pass


# Clase Nucleo (Composición)
class Nucleo:
    def __init__(self, identificador_unico):
        self.identificador_unico = identificador_unico
        self.activo = True

    def destruir(self):
        self.activo = False


# Clase abstracta
class EntidadBase(ABC):
    def __init__(self, energia_inicial, identificador_unico):
        self.energia = energia_inicial
        self.nucleo = Nucleo(identificador_unico)

    # Getter y Setter para validar energía
    @property
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, valor):
        if valor < 0:
            raise EnergiaInvalidaError("La energía no puede ser negativa.")
        self._energia = valor

    @abstractmethod
    def alimentarse(self, cantidad=10):
        pass

    def esta_activa(self):
        return self.nucleo.activo

    # Sobrecarga del operador suma
    def __add__(self, otra_entidad):
        if not isinstance(otra_entidad, EntidadBase):
            raise TypeError("Solo se pueden sumar entidades entre sí.")
        return self.energia + otra_entidad.energia

    def __str__(self):
        return f"Entidad ID={self.nucleo.identificador_unico}, Energía={self.energia}"


# Clase Sintetizador
class Sintetizador(EntidadBase):
    def alimentarse(self, cantidad=10):
        if not self.esta_activa():
            print("El sintetizador está inactivo.")
            return

        self.energia += cantidad
        print(f"Sintetizador {self.nucleo.identificador_unico} generó energía. Total: {self.energia}")


# Clase Consumidor
class Consumidor(EntidadBase):
    def alimentarse(self, cantidad=10):
        if not self.esta_activa():
            print("El consumidor está inactivo.")
            return

        self.energia += cantidad // 2
        print(f"Consumidor {self.nucleo.identificador_unico} obtuvo energía. Total: {self.energia}")


# Clase Híbrido (Herencia múltiple)
class Hibrido(Sintetizador, Consumidor):
    def __init__(self, energia_inicial, identificador_unico):
        super().__init__(energia_inicial, identificador_unico)

    def alimentarse(self, cantidad=10):
        if not self.esta_activa():
            print("El híbrido está inactivo.")
            return

        # Usa ambos comportamientos
        Sintetizador.alimentarse(self, cantidad)
        Consumidor.alimentarse(self, cantidad)


# Función de polimorfismo
def iniciar_ciclo_vital(lista_entidades):
    for entidad in lista_entidades:
        entidad.alimentarse()


# Simulación de interacción con el usuario
def simulacion():
    lista_entidades = []
    contador_identificadores = 1

    while True:
        print("\n¿Qué tipo de entidad desea crear?")
        print("1. Sintetizador")
        print("2. Híbrido")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "0":
            break
        elif opcion not in ["1", "2"]:
            print("Opción no válida, intente de nuevo.")
            continue

        try:
            energia_inicial = int(input("Ingrese la energía inicial: "))

            if opcion == "1":
                nueva_entidad = Sintetizador(energia_inicial, contador_identificadores)
            elif opcion == "2":
                nueva_entidad = Hibrido(energia_inicial, contador_identificadores)

            lista_entidades.append(nueva_entidad)
            print(f"Entidad creada con ID {contador_identificadores} y energía {energia_inicial}")

            contador_identificadores += 1

        except ValueError:
            print("Error: Debe ingresar un número entero.")
        except EnergiaInvalidaError as error:
            print(f"Error: {error}")

    print("\n--- Iniciando ciclo vital ---")
    iniciar_ciclo_vital(lista_entidades)

    if lista_entidades:
        energia_total = lista_entidades[0]
        for entidad in lista_entidades[1:]:
            energia_total += entidad
    else:
        energia_total = 0

    print("Energía total de la colonia:", energia_total)


if __name__ == "__main__":
    simulacion()