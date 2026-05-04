class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    def __str__(self):
        return f'{self.titulo} escrito por {self.autor}'
  

class Biblioteca:
    def __init__(self, nombre_sucursal):
        self.nombre_sucursal = nombre_sucursal
        self.catalogo = []
        
    def agregar_libro(self, nuevo_libro):
        self.catalogo.append(nuevo_libro)
    
    def mostrar_inventario(self):
        print(f'Sucursal: {self.nombre_sucursal}')
        for libro in self.catalogo:
            print(libro)


# Crear libros
libro1 = Libro('Cien años de soledad', 'Gabriel García Márquez')
libro2 = Libro('Los nacimientos', 'Eduardo Galeano')
libro3 = Libro('La prision de Black Rock', 'Cesar Garcia')

# Crear biblioteca
biblioteca1 = Biblioteca('Biblioteca central')

# Agregar libros
biblioteca1.agregar_libro(libro1)
biblioteca1.agregar_libro(libro2)
biblioteca1.agregar_libro(libro3)

# Mostrar inventario
biblioteca1.mostrar_inventario()
