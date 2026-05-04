class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __add__(self, otra_persona):
        return self.edad + otra_persona.edad

p1 = Persona("Juan", 30)
p2 = Persona("María", 25)

print(p1 + p2)    

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __gt__(self, otro_producto):
        return self.precio > otro_producto.precio   

producto1 = Producto("Laptop", 800)
producto2 = Producto("Celular", 500)

print(producto1 > producto2)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, otro_vector):
        return Vector(self.x + otro_vector.x, self.y + otro_vector.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
vector1 = Vector(2, 3)
vector2 = Vector(4, 5)

print(vector1 + vector2)