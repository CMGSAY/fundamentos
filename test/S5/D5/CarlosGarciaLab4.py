# Creamos el archivo "txt" para almacenar los datos
with open("registros.txt", "w") as datos_calderas:
    datos_calderas.write("Registro de  calderas \n")
    datos_calderas.write("Caldera-Norte\n")
    datos_calderas.write("120\n")
    datos_calderas.write("Caldera-Sur\n")
    datos_calderas.write("250\n")
    datos_calderas.write("Reactor-Principal\n")
    datos_calderas.write("80\n")
    datos_calderas.write("Turbina-Alfa\n")
    datos_calderas.write("300\n")

# Creamos la clase sensor presion 
class SensorPresion:
    # creamos el atributo Global de limite maximo de presion
    limite_peligro = 200
    # Creamos el atributo de clase para contar la cantidad de calderas creadas
    calderas_creadas = 0
    # Asifnamos el constructor de la clase y los atributos de la clase, presion sera un atributo privado
    def __init__(self, nombre_caldera, presion):
        self.nombre_caldera = nombre_caldera
        self.__presion = presion
        SensorPresion.calderas_creadas += 1
    
   # Creamos un metodo para mostrar la informacion de la presion
    @property
    def presion(self):
        return self.__presion
    
    # creamos un metodo setter para la presion 
    @presion.setter
    def presion(self, nueva_presion):
        #creamos las validacion para la presion, para poder cambiar el dato
        if nueva_presion > SensorPresion.limite_peligro:
            print(f'[ALERTA] | Presion peligrosa detectada en {self.nombre_caldera}. Presion actual: {nueva_presion}')
        elif nueva_presion < 0:
            print(f'[ERROR] | Presion no puede ser negativa. Caldera: {self.nombre_caldera} | valor ingresado: {nueva_presion}')
        else:
            self.__presion = nueva_presion
            print(f'[SISTEMA] | Cambio de presion. caldera: {self.nombre_caldera} | nueva presion: {nueva_presion}')
            
            return self.__presion

#creamos un metodo para si la caldera esta en peligro
    def en_peligro(self):
        return self.__presion > SensorPresion.limite_peligro
    

# Creamos una lista para almacenar los datos del archivo registros.txt
sensores = []
print('--- SISTEMA DE MONITOREO INDUSTRIAL ---')
print('Leyendo registros de presion...')

# Leemos los datos que tenemos en el archivo registros.txt
with open('registros.txt', 'r') as datos_calderas:
    lineas = [linea.strip() for linea in datos_calderas.readlines()]
    # saltamos la primera línea
    lineas = lineas[1:]

# creamos un ciclo para recorrer las lineas del archivo, de dos en dos, para obtener el nombre de la caldera y su presion
for caldera in range(0, len(lineas), 2):
    nombre = lineas[caldera]
    #  llenamos la lista de sensores y creamos los objetos de la clase SensorPresion
    if lineas[caldera+1].isdigit():
        presion = int(lineas[caldera+1])
        sensor = SensorPresion(nombre, presion)
        sensores.append(sensor)
    else:
        print(f'[ERROR] La línea "{lineas[caldera+1]}".')

# Creamos una lista para almacenar las alertas
alertas = []
# Clasificamos si tenemos una caldera en peligro y lo mandamos a la lista alerta
for sensor in sensores:
    if sensor.en_peligro():
        alertas.append(sensor.nombre_caldera)
        estado = '¡PELIGRO!' 
    else:
        estado = 'Seguro'
        
    print(f"Analizando: {sensor.nombre_caldera} | Estado: {estado}")
    

# Guardar archivo de alertas
with open("alertas.txt", "w") as salida:
    salida.write("REPORTE DE INCIDENCIAS - CALDERAS CRÍTICAS\n")
    salida.write("-----------------------------------------\n")
    contador = 0
    for nombre_caldera in alertas:
        
        salida.write(f"{contador + 1}. {nombre_caldera}\n")
        contador += 1

print(f"\n[AUDITORÍA] Se han generado alertas en el archivo 'alertas.txt'")
print(f"[RESUMEN] Total de sensores procesados: {SensorPresion.calderas_creadas}")
print("--------------------------------------")
