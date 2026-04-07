# Estructura de datos
## Lista
## Craer una lista
###forma 1: con elementos
mi_lista = [10, 'hola', 3.14, ]

### forma 2: sin elementos
lista_vacia = []

## acceder a los elementos
### Dos pasos
mi_lista[1]
saludo = mi_lista[1]
print(saludo)

### un paso
print(mi_lista[1])

lista_vacia.append('Diego')

print(lista_vacia[0])

mi_lista.append('mundo')

print(mi_lista)

#forma 1: con un ciclo 'for'
for elemento in mi_lista:
    print(elemento)
    
    if elemento == 3.14:
        print('Encontre el numero pi.')
        break
    
# forma 2: Usando los indices
len(mi_lista) #Devuelve la cantidad de elementos que tiene la lista
for indice in range(len(mi_lista)):
    print(mi_lista[indice])
    
    
## forma 2: indices negativos
print(mi_lista[-1])

print(mi_lista[1:2])

print(mi_lista[0:4:2])

mi_lista[1] = 'HOLA'

print(mi_lista)


mi_lista.remove(10)

print(mi_lista)

