# archivo_prueba = open("archivo.txt", "a")

# archivo_prueba.write("Hoy aprendi a escribir en un archivo")

# archivo_prueba.close()

# with open("archivo.txt", "a") as archivo_prueba:
#     archivo_prueba.write("Hoy aprendi a escribir en un archivo\n")
#     archivo_prueba.write("Ahora puedo escribir varias lineas\n")
    
# print()

with open("archivo.txt", "r") as archivo_prueba:
    print('Contenido del archivo')

    for linea in archivo_prueba:
        # strip(): eliminar los espacion en blanco y los saltos en linea
        textlo_limpio = linea.strip()
        print(f"-> {textlo_limpio}")