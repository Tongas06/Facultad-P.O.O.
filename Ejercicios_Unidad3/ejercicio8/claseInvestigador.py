from claseAgente import Agente

class Investigador(Agente):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self.__area_investigacion = area_investigacion
        self.__tipo_investigacion = tipo_investigacion

    def __str__(self):
        return f"{super().__str__()}, {self.__area_investigacion}, {self.__tipo_investigacion}"
    
    def get_area_investigacion(self):
        return self.__area_investigacion
    
    def get_tipo_investigacion(self):
        return self.__tipo_investigacion
    
    def to_dict(self):
        return {
            "nombre": self.get_nombre(),
            "apellido": self.get_apellido(),
            "sueldo_basico": self.get_sueldo_basico(),
            "antiguedad": self.get_antiguedad(),
            "categoría_investigación": self.get_categoría_investigación(),
        }