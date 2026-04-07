# Manual Basico de Bornaut

# titulo principal (Nivel 1)

## subtitulo (Nivel 2)

### Seccion (Nivel 3)

#### Subseccion(Nivel 4)

Esto es un ejemplo de *Cursiva*. Continuar con el texto

Esto es un ejemplo de **Negrita**.

#Viñetas
## Listas desordenadas
ingredientes
- Huevos
- Harina
- Azucar 
    Azucar Moreno

## Lista ordenada
1. Precalentar
2. Mezclar
3. Hornear

# Enlaces
[Enlace de interes](google.com)

# imagenes
![ejemplo de imagen](nombre.png)

# Citas
Hola esto es un ejemplo:

# Bloques de codigo
## en una linea
`print("Hola Mundo")`

## Variables lineales
``` Python
    print("Hola MUndo )
    print("Hola mundo)
    intput()
   ```

   # Tablas 
   |Nombre | Apellido|
   |-------|---------|
   | Diego |  Orozco |


# Las bases del codigo
# Que es programar?
- Crear
- Dar instrucciones
- Secunecia de pasos
- encontrar una solucion finita
- Programar es dar instrucciones claras y ordenadas para una comutadora ejecuta tarea.

## Algoritmo
- Secuncia de pasos, ordenados finitos para resolver un problema
- Un algoritmo no es un codigo

    1. finito 
    2. Preciso
    3. Definido

# Actividad
El algoritmo exacto para que el empleado le venda una bolsa de arroz al cliente que acaba de entrar a la tienda

    1. Inicio
    2. Cliente hace el pedido de la bolsa de arroz
    3. Empleado verifica si tiene disponible la cantidad de arroz
    4. El empleado le dice el precio
    5. El cliente acepta 
    6. El empleado se dirige donde tiene el arroz
    7. El empleado toma el arroz
    8. El empleado regresa al mostrador
    9. El empleado entrega el arroz al cliente
    10. El  cliente paga
    11. El empleado registra la compra
    12. El cliente sale de la tienda satisfecho 
    13. fin

# Entrar y salida
## salida
### La funcion `print()`
* Todo en minuscula. `print`
    `PRINT` X
    `Print` X
* Lo que vayamos a decir, va en parentesis `()`
* El texto debe ir entre comillas ' ' o " "

Ejemplo:
    `print("Hola Mundo")`

Ejemplo2:
    `print('Bienvenido en la tienda dijital')`


## Entrada
### La funcion `input()`
sintaxis:
* Todo en minuscula. `input`
    `INPUT` X
    `Input` X
* Lo que vayamos a decir, va en parentesis `()`
* Espera una respuesta
- Siempre el input me va a devolver el dato en tipo string
- Almacenar el dato en una variable

```python
print('Bienvenido a la tienda digital')
# print('Que desea comprar')

nombre_producto = input('Que desea comprar: ')

print('El Producto que escogio es: ')
print(nombre_producto)
```

# conversiones
## camel case
    ejemplo: miNombreApellido
## snake case
    ejemplo: mi_nombre_apellido
## pascal case
    ejemplo: MiNombreApellido


## Ejercicio prctico de entrada y salida
### ejercicio 1:
### Soucion
```python
# salida de la tienda
print('======')
print('Salida')
print('======')
productoFav = input('\nCual es su producto Favorito? ')
calificacionTienda = input('\nDel 1 al 10 Que Calificacion le da a la tienda? ')

print(f'\nEl producto favorito es {productoFav} y la calificacion es {calificacionTienda}')
print('\nGracias por su compra vuelva pronto. ')
```

## caracteres de escape (\n y \t)
* \n: salto de linea (Enter)
* \t: el tab (da un espacio largo)

```python
print("1. leche")
print("2. cafe")
print("3. Arroz")

print("1. leche\n2. Cafe\n3. Arroz")

print("Prdouctos\t Precio")
print("1. Leche\t $2.50")
print("2. Cafe\t $3.00")
print("3. Arrroz\t $1.5")
```

# Variables
Una variable es un **Espacio en memoria** con un **Nombre** (etiqueta) donde se guarda un valor 

## crear variables
'nombreVariable + signoIgual + el valor'

'nombre      =              "Diego"'

## Reglas basicas en los nombres de las variables
- no usar espacios
- no se puede iniciar con numeros
- deben de ser descriptivos
- apegar a una convencion

Malo:
```python
4x = 522
x="Hola"
mi nombre = "Diego"
```


ejercicio2:

Declarar 3 productos (El usuario va a decir cuales productos)
preguntar el precio de cada producto
preguntar la cantidad disponible de productos

Generar una factura de inventario; Encabezado, producto: nombre | Precio: ### | cantidad: #