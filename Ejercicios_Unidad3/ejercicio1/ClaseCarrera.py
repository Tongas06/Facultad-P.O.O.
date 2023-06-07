class Carrera:

    def __init__(self, codigo, nombre, fecha_incio, duracion, titulo):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__fecha_incio = fecha_incio
        self.__duracion = duracion
        self.__titulo = titulo

    def get_codigo(self):
        return self.__codigo
    
    def get_nombre(self):
        return self.__nombre
    
    def get_fecha_incio(self):
        return self.__fecha_incio
    
    def get_duracion(self):
        return self.__duracion
    
    def get_titulo(self):
        return self.__titulo