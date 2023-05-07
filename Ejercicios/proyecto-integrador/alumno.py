class Alumno:
    def __init__(self, dni, apellido, nombre, carrera, anio_carrera):
        self.__dni = int(dni)
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__anio_carrera = int(anio_carrera)

    def __lt__(self, otro_alumno):
        if self.__anio_carrera != otro_alumno.__anio_carrera:
            return self.__anio_carrera < otro_alumno.__anio_carrera
        else:
            if self.__apellido != otro_alumno.__apellido:
                return self.__apellido < otro_alumno.__apellido
            else:
                return self.__nombre < otro_alumno.__nombre