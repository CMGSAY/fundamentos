# # Reto integrador
# Actúas como el Arquitecto de Software en jefe. Debes programar el núcleo lógico de un Banco.

# **Instrucciones**

# 1. Crea la clase `CuentaBancaria`.
class CuentaBancaria:
# 2. **Atributos Compartidos**
    #     * El banco maneja una `tasa_interes_global` que nace en `0.05`
    tasa_interes_global = 0.05

    #     * El banco lleva un registro de `total_cuentas_creadas` que nace en `0`.
    total_cuentas_creadas = 0
    
    # 3. **El Constructor**
    def __init__ (self, nombre_titular):
        #     * Pide un parámetro: `nombre_titular`.
        self.nombre_titular = nombre_titular
        #     * Crea el atributo privado `__titular` usando el parámetro.
        self.__titular = self.nombre_titular  
        #     * Crea el atributo privado `__saldo` e inicialízalo por defecto en `0.0`.
        self.__saldo = 0.0
        #     * Súmale 1 al atributo de clase `total_cuentas_creadas`
        CuentaBancaria.total_cuentas_creadas += 1
    
    # 4. **Seguridad**
    #     * Crea un `@property` llamado `saldo` que actúe como Getter
    @property
    def saldo(self):
        return self.__saldo 

    #     * **OJO:** No hagas el Setter para el saldo, el saldo no se debe poder sobrescribir con un `=`, solo debe cambiar mediante depósitos y retiros.
    #     * Crea un `@property` llamado `titular` (Getter).
    @property
    def titular(self):
        return self.__titular
    
    #     * Crea su respectivo `@titular.setter`. La validación debe asegurar que el nombre no esté en blanco
    @titular.setter
    def titular(self, nuevo_nombre):
        if nuevo_nombre != "":
            
            print(f'[SISTEMA] | Cambio de titular. viejo titular: {self.__titular} | nuevo titular: {nuevo_nombre}')
            self.__titular = nuevo_nombre
        else:
            print("El nombre del titular no puede estar en blanco.")
    
    # 5. **Métodos de Instancia**
    #     * Crea un método `depositar(self, cantidad)`. Si la cantidad es mayor a 0, súmala al saldo
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        elif cantidad <= 0:
            print("La cantidad a depositar debe ser mayor a 0.") 
    #     * Crea un método `retirar(self, cantidad)`. Solo permite el retiro si hay suficiente dinero en la cuenta.
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")

        else:
            print("Cantidad inválida o fondos insuficientes.")
    #     * Crea un método `proyectar_interes(self)`. Este método debe multiplicar el saldo privado actual por la `tasa_interes_global` de la clase e imprimir cuánto dinero ganará el cliente este *año*.
    def proyectar_interes(self):
        ganancia = self.__saldo * CuentaBancaria.tasa_interes_global
        print(f"Con la tasa de interés actual del {CuentaBancaria.tasa_interes_global*100}%, ganarás {ganancia} este año.")
    # 6. **Método de Clase:**
    #     * Crea un `@classmethod` llamado `modificar_tasa_interes(cls, nueva_tasa)`. Este método debe actualizar la tasa global del banco.
    @classmethod
    def modificar_tasa_interes(cls, nueva_tasa):
        cls.tasa_interes_global = nueva_tasa


# **Simulación en el programa principal:**
# * Crea dos cuentas 
cuenta1 = CuentaBancaria("Carlos")
cuenta2 = CuentaBancaria("Miguel")

# * Imprime cuántas cuentas existen a nivel global.
print(f"Total de cuentas creadas: {CuentaBancaria.total_cuentas_creadas}")

# * Deposítale 10,000 a cuenta1
cuenta1.depositar(10000)
cuenta2.depositar(50000)

cuenta1.retirar(5000)
cuenta2.retirar(15000)

# * Proyecta el interés de cuenta1 con la tasa actual del 5%
cuenta1.proyectar_interes()
cuenta2.proyectar_interes()

# * Usa el método de clase para que el Banco suba la tasa de interés a 0.10 (10%).
CuentaBancaria.modificar_tasa_interes(0.10)

# * Vuelve a proyectar el interés de cuenta1 para ver cómo la ganancia se duplicó automáticamente.
cuenta1.proyectar_interes()
cuenta2.proyectar_interes()

# * Intenta cambiar el nombre de Carlos a un texto en blanco `""` para comprobar que el setter la bloquea.
cuenta1.titular = ""