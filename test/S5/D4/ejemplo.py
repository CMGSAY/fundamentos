# archivo_prueba = open("archivo.txt", "a")

# archivo_prueba.write("Hoy aprendi a escribir en un archivo")

# archivo_prueba.close()

# with open("archivo.txt", "a") as archivo_prueba:
#     archivo_prueba.write("Hoy aprendi a escribir en un archivo\n")
#     archivo_prueba.write("Ahora puedo escribir varias lineas\n")
    
# print()

# with open("archivo.txt", "r") as archivo_prueba:
#     print('Contenido del archivo')

#     for linea in archivo_prueba:
#         # strip(): eliminar los espacion en blanco y los saltos en linea
#         textlo_limpio = linea.strip()
#         print(f"-> {textlo_limpio}")


# Creamos el archivo de registros
with open("registros.txt", "w") as datos_calderas:
    datos_calderas.write("Caldera-Norte\n")
    datos_calderas.write("120\n")
    datos_calderas.write("Caldera-Sur\n")
    datos_calderas.write("250\n")
    datos_calderas.write("Reactor-Principal\n")
    datos_calderas.write("80\n")
    datos_calderas.write("Turbina-Alfa\n")
    datos_calderas.write("300\n")


# Clase SensorPresion
class SensorPresion:
    limite_peligro = 200
    calderas_creadas = 0

    def __init__(self, nombre_caldera, presion):
        if presion < 0:
            raise ValueError("La presión no puede ser negativa")
        self.nombre_caldera = nombre_caldera
        self.__presion = presion
        SensorPresion.calderas_creadas += 1

    @property
    def presion(self):
        return self.__presion

    @presion.setter
    def presion(self, nueva_presion):
        if nueva_presion < 0:
            print(f"[ERROR] Presión negativa en {self.nombre_caldera}")
        else:
            self.__presion = nueva_presion

    def en_peligro(self):
        return self.__presion > SensorPresion.limite_peligro


# --- PROGRAMA PRINCIPAL ---
sensores = []

print("--- SISTEMA DE MONITOREO INDUSTRIAL ---")
print("Leyendo registros de presión...")

# Leer todas las líneas y procesar en pares
with open("registros.txt", "r") as archivo:
    lineas = [linea.strip() for linea in archivo.readlines()]

for i in range(0, len(lineas), 2):
    nombre = lineas[i]
    presion = int(lineas[i+1])
    sensor = SensorPresion(nombre, presion)
    sensores.append(sensor)

# Evaluar cada sensor
alertas = []
for sensor in sensores:
    estado = "¡PELIGRO!" if sensor.en_peligro() else "Seguro"
    print(f"Analizando: {sensor.nombre_caldera} | Estado: {estado}")
    if sensor.en_peligro():
        alertas.append(sensor.nombre_caldera)

# Guardar archivo de alertas
with open("alertas.txt", "w") as salida:
    salida.write("REPORTE DE INCIDENCIAS - CALDERAS CRÍTICAS\n")
    salida.write("-----------------------------------------\n")
    for idx, nombre in enumerate(alertas, start=1):
        salida.write(f"{idx}. {nombre}\n")

print(f"[AUDITORÍA] Se han generado alertas en el archivo 'alertas.txt'")
print(f"[RESUMEN] Total de sensores procesados: {SensorPresion.calderas_creadas}")
print("--------------------------------------")
