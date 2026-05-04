from abc import ABC, abstractmethod

class Documento(ABC):
    def __init__(self, titulo):
        self.titulo = titulo
    
    @abstractmethod
    def exportar(self):
        pass
    def mostrar_titulo(self): # Opcional: los padres abstracion pueden tener metodos normales
        print(f'Documentos: {self.titulo}')

class PDF(Documento):
    def exportar(self):
        print(f'Exportando {self.titulo} a PDF')

class Word(Documento):
    def exportar(self):
        print(f'Guardar {self.titulo} a word')

try:
    doc_invalido = Documento('Mi archivo')
except:
    print(f'[BLOQUEO DE SEGURIDAD]')