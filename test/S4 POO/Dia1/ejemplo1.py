# paso1: definir la clase
#tenemos que usar `class` y aplicamos la convension de Pascal Case para nombrar la clase, 
# al final del nombre de la clase se debe de colocar `:`
class ClienteFrecuente: 
    pass

# parte 2: la instanciacion: qu se crea un objeo apartir de la clase. es deci, se crea una instancia
cliente1 = ClienteFrecuente()
cliente2 = ClienteFrecuente()

print(ClienteFrecuente)
print(cliente1)
print(cliente2)

# comprobando el plano (clase)

print(type(cliente1))
# comprobando que son objtos diferentes
print(id(cliente1))
print(id(cliente2))

# paso 3: una variable y una funcion
#nombre_cliente = 'Juan Perez'

#def registar_cliente():
#    print('El cliente se ah Guarado.')

