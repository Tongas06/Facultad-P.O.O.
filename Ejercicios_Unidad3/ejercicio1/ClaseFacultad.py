class Facultad:

    def __init__(self, codigo, nombre, direccion, localidad, telefono):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
        self.__carreras = []

    def get_codigo(self):
        return self.__codigo
    
    def get_nombre(self):
        return self.__nombre
    
    def get_direccion(self):
        return self.__direccion
    
    def get_localidad(self):
        return self.__localidad
    
    def get_telefono(self):
        return self.__telefono
    
    def agregar_carrera(self, carrera):
        self.__carreras.append(carrera)

    def obtener_carreras(self):
        return self.__carreras