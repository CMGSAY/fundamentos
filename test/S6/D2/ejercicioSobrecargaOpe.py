class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.nombre = precio
        
    def __add__(self, otro_producto):
        suma_total = self.monto + otro_producto.monto
        return suma_total
    
    def __sub__(self, otro_producto):
        diferencia_productos = self.monto - otro_producto.monto
        return diferencia_productos
    def __gt__(self, otro_producto):
        return self.monto > otro_producto.monto
    

producto1 = Producto('Leche',)
