# Manejo de archivos

## Metodo de apertura de un archivo
`open()` (puente del programa al sistema operativo).


Esta funcion requiere dos argumento obligatorios: el nombre del archivo y el "Modo" en el que quieremos abrirlo

### Modos de apertura:
1. **Modo `w`** (wriete / escribir).
    * Crea un archivo nuevo
    * Si el archivo no existe, lo crea
    * **Advertencia**: Si el archivo ya existe, el modo `'w'` lo destruye y lo sobrescribe desde cero.

2. **Modo `a`** (append / añadir).
    * Abre un archivo existente y coloca el cursor al final.
    * Todo lo que escribamos se agregara sin borrar lo anterior.

3. **Modo `r`** (read / leer).
    * Solo nos permite ver el contenido.
    * NO podemos modificar o agregar el archivo.
    * Si el archivo no existe, el programa se detendra con un error.

SIEMPRE que abro un archivo, hay que cerrar el archivo
`Close()`
Para escribir en mi archivo usamos al funcion `write`

```python
archivo_prueba = open("archivos.txt", "a")

archivo_prueba.write("Hoy aprendi a escribir en un archivo")

archivo_pruba.close()

```
## Administardor de  contexto `with open` 
```python
with open("archivo.txt", "a") as archivo_prueba:
    archivo_prueba.write("Hoy aprendi a escribir en un archivo\n")
    archivo_prueba.write("Ahora puedo escribir varias lineas\n")
```


## Leer nuestro archivo
```python
with open("archivo.txt", "a") as archivo_prueba:
    print('Contenido del archivo')

    for linea in archivo_prueba:
        # strip(): eliminar los espacion en blanco y los saltos en linea
        textlo_limpio = linea.strip()
        print(f"-> {texto_limpio}")
```


## el metodo `read()`
Python tomara todo el contenido del archivo y lo guardara en una sola variable de tipo cadena de texto (string).

``` python
whith open("cuento.txt", "r" ) as archivos:
    contenido = archivo.read()
    print("Contenido completo: ")
    print(contenido)

```