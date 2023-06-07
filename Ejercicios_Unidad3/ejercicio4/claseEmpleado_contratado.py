from claseEmpleado import Empleado

class EmpleadoContratado(Empleado):
    __fecha_inicio = 'str'
    __fecha_fin = 'str'
    __horas_trabajadas = 'int'
    __valor_hora = 'float'
    
    def __init__(self, dni, nombre, direccion, telefono, fecha_inicio, fecha_fin, horas_trabajadas, valor_hora):
        super().__init__(dni, nombre, direccion, telefono)
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__horas_trabajadas = horas_trabajadas
        self.__valor_hora = valor_hora

    # Métodos getter y setter, y método para calcular sueldo
    def get_fecha_inicio(self):
        return self.__fecha_inicio

    def set_fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    def get_fecha_fin(self):
        return self.__fecha_fin

    def set_fecha_fin(self, fecha_fin):
        self.__fecha_fin = fecha_fin

    def get_horas_trabajadas(self):
        return self.__horas_trabajadas

    def set_horas_trabajadas(self, horas_trabajadas):
        self.__horas_trabajadas = horas_trabajadas

    def get_valor_hora(self):
        return self.__valor_hora

    def set_valor_hora(self, valor_hora):
        self.__valor_hora = valor_hora

    def calcular_sueldo(self):
        return self.__horas_trabajadas * self.__valor_hora

    def registrar_horas(self, horas):
        self.__horas_trabajadas += horas

    @classmethod
    def desde_dict(cls, dict_empleado):
        return cls(dict_empleado['dni'],
                   dict_empleado['nombre'],
                   dict_empleado['direccion'],
                   dict_empleado['telefono'],
                   dict_empleado['fecha_inicio'],
                   dict_empleado['fecha_fin'],
                   int(dict_empleado['horas_trabajadas']),
                   float(dict_empleado['valor_hora']))
