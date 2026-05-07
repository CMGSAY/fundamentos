from abc import ABC, abstractmethod

# Clase abstracta
class PersonalMedico(ABC):
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
    
    @abstractmethod
    def realizar_labor(self):
        pass

# Subclase Doctor
class Doctor(PersonalMedico):
    def realizar_labor(self):
        print(f"Dr. {self.nombre} ({self.especialidad}): Está realizando un diagnóstico especializado.")

    def atender_paciente(self, objeto_paciente):
        print(f"Dr. {self.nombre} atiende al paciente {objeto_paciente.nombre}.")
        
        diagnostico = input("Ingrese nota para el Historial: ")
        objeto_paciente.historial_clinico.agregar_observacion(diagnostico)
        
        try:
            medicamento = int(input("Ingrese dosis de recuperación (1-50): "))
            nueva_salud = objeto_paciente.salud + medicamento
            objeto_paciente.agregar_salud(nueva_salud)
        except ValueError:
            print("Error: Debe ingresar un número válido para la dosis. El tratamiento no se aplicó.")
        
        objeto_paciente.estado_paciente()
        

class Enfermero(PersonalMedico):
    def realizar_labor(self):
        print(f"Enfermero {self.nombre} ({self.especialidad}): Está aplicando cuidados y revisando signos vitales.")


class HistorialClinico():
    def __init__(self):
        self.observaciones = []
    
    def agregar_observacion(self, texto):
        self.observaciones.append(texto)
    
    def mostrar_notas(self):
        print('----Notas del Historial----')
        for texto in self.observaciones:
            print(f'- {texto}')
        

class Paciente(HistorialClinico):
    def __init__(self, nombre, edad, salud = 50):
        self.nombre = nombre
        self.edad = edad
        self.historial_clinico = HistorialClinico()
        self.salud = salud
        self.estado_critico = False
        
    def agregar_salud(self, nueva_salud):
        if nueva_salud < 0:
            self.salud = 0
        elif nueva_salud > 100:
            self.salud = 100
        else:
            self.salud = nueva_salud
    
    def estado_paciente(self):
        if self.salud == 0:
            print('[ESTADO]: Paciente falleció')
        elif self.salud < 20:
            print('[ESTADO]: Crítico')
        else:
            print('[ESTADO]: Estable')
        
class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pacientes = []       
        self.personal_medico = [] 
    
    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)
        print(f'Paciente {paciente.nombre} registrado en el hospital {self.nombre}.')
    
    def contratar_personal(self, personal):
        self.personal_medico.append(personal)
        print(f'Personal {personal.nombre} contratado en el hospital {self.nombre}.')

    def mostrar_estado_paciente(self):
        print('--- Estado de todos los pacientes ---')
        print(f'{"Nombre":<8} {"Edad":<5} {"Salud":<11} {"Estado":<10}')
        print('-'*45)
        
        for paciente in self.pacientes:
            # Determinar estado textual
            if paciente.salud == 0:
                estado = "Falleció"
            elif paciente.salud < 20:
                estado = "Crítico"
            else:
                estado = "Estable"
            
            print(f'{paciente.nombre:<8} {paciente.edad:<5} {paciente.salud:<11} {estado:<10}')


#-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-//-/
#-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-//-/


hospital = Hospital("San José")

while True:
    print("\n--- Menú Hospital ---")
    print("1. Registrar paciente")
    print("2. Contratar personal")
    print("3. Realizar Consulta Medica")
    print("4. Ver reporte de Pabellon")
    print("5. Salir")
    
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        continue
    
    if opcion == 1:
        nombre = input("Ingrese nombre del paciente: ")
        try:
            edad = int(input("Ingrese edad del paciente: "))
        except ValueError:
            print("Error: La edad debe ser un número.")
            continue
        paciente = Paciente(nombre, edad)
        hospital.registrar_paciente(paciente)
    
    elif opcion == 2:
        nombre = input("Ingrese nombre del doctor: ")
        especialidad = input("Ingrese especialidad: ")
        doctor = Doctor(nombre, especialidad)
        hospital.contratar_personal(doctor)
    
    elif opcion == 3:
        if not hospital.personal_medico or not hospital.pacientes:
            print("Debe haber al menos un doctor y un paciente registrados.")
            continue
        
        doctor = hospital.personal_medico[0]
        paciente = hospital.pacientes[0]
        doctor.atender_paciente(paciente)
    
    elif opcion == 4:
        hospital.mostrar_estado_paciente()
        
    
    elif opcion == 5:
        print("Saliendo del sistema...")
        break
    
    else:
        print("Opción inválida, intente de nuevo.")
