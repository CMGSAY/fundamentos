# Molde (aun vacio) para la clase Producto
class Prducto:
    pass
# Fabricar dos objetos fisicos e independiente

articulo_1 = Prducto()
articulo_2 = Prducto()

# les vamos asiganar atributos (caracteristicas) a cada uno
# Sintaxis: objeto.atributo = valor
articulo_1.nombre = 'Camisetas'
articulo_1.precio = 19.99
articulo_1.cantidad = 10

articulo_2.nombre = 'Pantalon'
articulo_2.precio = 39.99
articulo_2.cantidad = 5

# Mostrar los atributos de cada articulo
print(f'Articulo 1: {articulo_1.nombre}, precio: {articulo_1.precio}, cantidad: {articulo_1.cantidad}')
print(f'Articulo 2: {articulo_2.nombre}, precio: {articulo_2.precio}, cantidad: {articulo_2.cantidad}')



