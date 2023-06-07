from claseAgente import Agente

class PersonalApoyo(Agente):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self.__categoria = categoria

    def __str__(self):
        return f"{super().__str__()}, {self.__categoria}"
    
    def get_categoria(self):
        return self.__categoria
    
    def to_dict(self):
        return {
            "nombre": self.get_nombre(),
            "apellido": self.get_apellido(),
            "sueldo_basico": self.get_sueldo_basico(),
            "antiguedad": self.get_antiguedad(),
            "categoria": self.get_categoria(),
            # ... (otros atributos)
        }