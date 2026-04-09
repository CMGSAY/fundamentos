with open("registro.txt", "a") as archivo_prueba:
    archivo_prueba.write("Registro de actividades\n")
    archivo_prueba.write("Actividad 1: Aprender a escribir en un archivo\n")
    archivo_prueba.write("Actividad 2: Aprender a leer un archivo\n")
    
cantidad = 0
with open("registro.txt", "r") as archivo_prueba:
    for leer_linea in archivo_prueba:
        texto_limpio = leer_linea.strip() 
        cantidad += 1
        print(f'{cantidad}: {texto_limpio}')


print(f"Cantidad de lineas leidas: {cantidad}")