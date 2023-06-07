from facultad import Facultad
from carrera import Carrera
import csv

class ManejadorFacultades:
    def __init__(self):
        self.__facultades = []
        self.__carreras = {}

    def cargar_facultades(self):
        with open('facultades.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                if len(row) == 5:
                    # Esta línea contiene datos de una facultad
                    facultad = Facultad(int(row[0]), row[1], row[2], row[3], row[4])
                    self.__facultades.append(facultad)
                elif len(row) == 6:
                    # Esta línea contiene datos de una carrera
                    carrera = Carrera(int(row[1]), row[2], row[3], row[4], row[5])
                    facultad.agregar_carrera(carrera)

    def mostrar_carreras_por_facultad(self, codigo_facultad):
        facultad = None
        indice = 0
        bandera = False
        while indice < len(self.__facultades) and not bandera:
            if self.__facultades[indice].get_codigo() == codigo_facultad:
                bandera = True
                facultad = self.__facultades[indice]
            indice+=1

        if facultad is not None:
            print(f"Facultad: {facultad.get_nombre()}")
            for carrera in facultad.obtener_carreras() :
                print(f"  - {carrera.get_nombre()} ({carrera.get_duracion()})")
        else:
            print("No se encontró la facultad con el código proporcionado.")

    def mostrar_facultad_por_carrera(self, nombre_carrera):
        facultad_encontrada = None
        carrera_encontrada = None
        indice = 0

        while indice < len(self.__facultades) and facultad_encontrada is None:
            facultad = self.__facultades[indice]
            carreras = facultad.obtener_carreras()
            indice_carrera = 0
            while indice_carrera < len(carreras) and carrera_encontrada is None:
                carrera = carreras[indice_carrera]  
                if carrera.get_nombre().lower() == nombre_carrera.lower():
                    facultad_encontrada = facultad
                    carrera_encontrada = carrera
                indice_carrera+=1
            indice+=1
                
        if facultad_encontrada is not None and carrera_encontrada is not None:
            print(f"Código: {facultad_encontrada.get_codigo()}{carrera_encontrada.get_codigo()}")
            print(f"Nombre: {carrera_encontrada.get_nombre()}")
            print(f"Localidad: {facultad.get_localidad()}")
        else:
            print("No se encontró la carrera con el nombre proporcionado.")
