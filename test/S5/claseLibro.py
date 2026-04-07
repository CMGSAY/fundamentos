class LibroFisico:
    # 1. el constructor pide solamente lo esencial de afuera
    def __init__(self, titulo, autor, precio = 100):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        # 2. Atributro interno, por defecto siempre inicia en True
        self.disponible = True
        
    # 3. un metodo de la clase
    def prestar_libro(self):
        if self.disponible == False:
            print(f'El libro {self.titulo} no esta disponible')
        else:
            print(f'El libro {self.titulo} disponible!, Libro prestado y su precio es {self.precio}')
            self.disponible = False 
    
    def cambiar_nombre(self, nuevo_nombre):
        self.titulo = nuevo_nombre
        print(f'El nuevo nombre es: {self.titulo}')


libro1 = LibroFisico('El Quijote', 'Miguel Cervantes', 200)
libro2 = LibroFisico('Cien años de soledad', 'Gabriel Garcia Marquez')

#intento 1
libro1.prestar_libro() # Libro disponible!

libro1.prestar_libro() # El libro no esta disponible

libro2.prestar_libro()
libro1.cambiar_nombre('El Quijote de la Mancha ')