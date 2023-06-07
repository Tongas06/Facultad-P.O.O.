class Agente:
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldo_basico = sueldo_basico
        self.__antiguedad = antiguedad

    def __str__(self):
        return f"{self.__apellido}, {self.__nombre}"
    
    def get_cuil(self):
        return self.__cuil
    
    def get_apellido(self):
        return self.__apellido
    
    def get_nombre(self):
        return self.__nombre
    
    def get_sueldo_basico(self):
        return self.__sueldo_basico
    
    def get_antiguedad(self):
        return self.__antiguedad
    
    def calcular_sueldo(self):
        sueldo_extra = self.calculate_sueldo_extra()
        total_sueldo = self.__sueldo_basico + sueldo_extra
        return total_sueldo

    def set_sueldo_basico(self, nuevoBasico):
        self.__sueldo_basico = nuevoBasico

    def calculate_sueldo_extra(self):
        # Asumiendo un porcentaje fijo para el ejemplo
        porcentaje_extra = 0.1
        sueldo_extra = self.__sueldo_basico * porcentaje_extra
        return sueldo_extra