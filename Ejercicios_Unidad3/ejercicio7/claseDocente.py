from claseAgente import Agente

class Docente(Agente):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra

    def __str__(self):
        return f"{super().__str__()}, {self.__carrera}, {self.__cargo}, {self.__catedra}"
    
    def get_carrera(self):
        return self.__carrera
    
    def get_cargo(self):
        return self.__cargo
    
    def get_catedra(self):
        return self.__catedra
    
    def to_dict(self):
        return {
            "nombre": self.get_nombre(),
            "apellido": self.get_apellido(),
            "sueldo_basico": self.get_sueldo_basico(),
            "antiguedad": self.get_antiguedad(),
            "cargo": self.get_cargo(),
            "catedra": self.get_catedra(),
        }