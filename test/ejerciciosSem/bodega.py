class AgenteSeguridad:
    def evaluar_entrada(self, nombre, nivel_acceso):
        self.nombre = nombre
        self.nivel_acceso = nivel_acceso
        nivel_seguridad_puerta = int(input('Ingrese el nivel de seguridad de la puerta 1-5: '))
        if self.nivel_acceso >= nivel_seguridad_puerta:
            print(f'Acceso permitido a {self.nombre} con nivel de acceso {self.nivel_acceso}.')
        else:
            print(f'Acceso denegado a {self.nombre} con nivel de acceso {self.nivel_acceso}.')

guardia_turno_uno = AgenteSeguridad()

guardia_turno_uno.nombre = 'Juan'
guardia_turno_uno.nivel_acceso = 1

guardia_turno_uno.evaluar_entrada(guardia_turno_uno.nombre, guardia_turno_uno.nivel_acceso)
