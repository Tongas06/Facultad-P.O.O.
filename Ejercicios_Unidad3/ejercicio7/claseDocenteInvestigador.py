from claseDocente import Docente
from claseInvestigador import Investigador

class DocenteInvestigador(Docente, Investigador):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion, categoria, importe_extra):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra)
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion)
        self.__categoria = categoria
        self.__importe_extra = importe_extra

    def __str__(self):
        return f"{super().__str__()}, {super().__str__()}, {self.__categoria}, {self.__importe_extra}"
    
    def get_categoria(self):
        return self.__categoria
    
    def get_importe_extra(self):
        return self.__importe_extra
    
    def get_categoria_programa(self):
        return self.__categoría_programa
    
    def to_dict(self):
        base_dict = super(Docente, self).to_dict()  # Obtener atributos de la clase Docente
        base_dict.update(super(Investigador, self).to_dict())  # Obtener atributos de la clase Investigador
        base_dict.update({
            "categoría_programa": self.get_categoria_programa(),
            "importe_extra": self.get_importe_extra(),
            # ... (otros atributos)
        })
        return base_dict