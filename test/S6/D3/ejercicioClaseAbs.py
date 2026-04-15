from abc import ABC, abstractmethod

class Trabajador(ABC):
    def __init__(self, ):
        self.titulo = 'titulo'
    
    @abstractmethod
    def realizar_tarea(self):
        pass

class Ingeniero(Trabajador):
    def realizar_tarea(self):
        print('Diseñando Planos')
    
class Medico(Trabajador):
    def realizar_tarea(self):
        pass

ing1 = Ingeniero()
ing1.realizar_tarea()

doc1 = Medico()
doc1.realizar_tarea()

try: 
    tarea_invalida = Trabajador('Tarea')
except:
    print('[Error en la tarea.]')
    