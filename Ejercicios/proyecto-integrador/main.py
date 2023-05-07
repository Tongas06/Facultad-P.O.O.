import numpy as np
import csv
from alumno import Alumno

class MateriaAprobada:
    def __init__(self, dni, nombre_materia, fecha, nota, aprobacion):
        self.dni = int(dni)
        self.nombre_materia = nombre_materia
        self.fecha = fecha
        self.nota = float(nota)
        self.aprobacion = aprobacion

def cargar_alumnos():
    alumnos = []
    with open('alumnos.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        header = next(csvreader)  # Saltar la fila del encabezado
        for row in csvreader:
            if row:  # Verifica que la fila no esté vacía
                alumnos.append(Alumno(*row))
    return np.array(alumnos)

def cargar_materias_aprobadas():
    materias_aprobadas = []
    with open('materiasAprobadas.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        header = next(csvreader)  # Saltar la fila del encabezado
        for row in csvreader:
            if row:  # Verifica que la fila no esté vacía
                materias_aprobadas.append(MateriaAprobada(*row))
    return materias_aprobadas

def calcular_promedio(alumnos, materias_aprobadas):
    promedios = []
    for alumno in alumnos:
        notas = [materia.nota for materia in materias_aprobadas if materia.dni == alumno.dni]
        if len(notas) == 0:
            promedio_total = "N/A"
            promedio_sin_aplazos = "N/A"
        else:
            promedio_total = sum(notas) / len(notas)
            notas_sin_aplazos = [nota for nota in notas if nota >= 4]
            if len(notas_sin_aplazos) == 0:
                promedio_sin_aplazos = "N/A"
            else:
                promedio_sin_aplazos = sum(notas_sin_aplazos) / len(notas_sin_aplazos)
        promedios.append((alumno, promedio_total, promedio_sin_aplazos))
    return promedios

def mostrar_promedio(dni, promedios):
    for alumno, promedio_total, promedio_sin_aplazos in promedios:
        if alumno.dni == dni:
            print(f"Promedio total: {promedio_total}")
            print(f"Promedio sin aplazos: {promedio_sin_aplazos}")
            return
    print("DNI no encontrado")

class Alumno:
    def __init__(self, dni, apellido, nombre, carrera, anioquecursa):
        self.dni = int(dni)
        self.apellido = apellido
        self.nombre = nombre
        self.carrera = carrera
        self.anio_cursa = int(anioquecursa)

    def __lt__(self, otro_alumno):
        if self.anio_cursa != otro_alumno.anio_cursa:
            return self.anio_cursa < otro_alumno.anio_cursa
        else:
            if self.apellido != otro_alumno.apellido:
                return self.apellido < otro_alumno.apellido
            else:
                return self.nombre < otro_alumno.nombre

def listar_estudiantes_promocionales(alumnos, materias_aprobadas):
    materia = input("Ingrese el nombre de la materia: ")
    print("DNI\tApellido y nombre\t\tFecha\t\tNota\tAño que cursa")
    for materia_aprobada in materias_aprobadas:
        if materia_aprobada.nombre_materia == materia and materia_aprobada.nota >= 7:
            alumno = next((alumno for alumno in alumnos if alumno.dni == materia_aprobada.dni), None)
            if alumno:
                print(f"{alumno.dni}\t{alumno.apellido} {alumno.nombre}\t{materia_aprobada.fecha}\t{materia_aprobada.nota}\t{alumno.anio_cursa}")

def listar_alumnos_ordenados(alumnos):
    alumnos_ordenados = sorted(alumnos)
    for alumno in alumnos_ordenados:
        print(f"{alumno.dni} {alumno.apellido} {alumno.nombre} {alumno.carrera} {alumno.anio_cursa}")

def menu():
    alumnos = cargar_alumnos()
    materias_aprobadas = cargar_materias_aprobadas()
    while True:
        print("Seleccione una opción:")
        print("1. Ingresar DNI de un alumno y mostrar su promedio con y sin aplazos")
        print("2. Ingresar nombre de una materia y mostrar estudiantes que aprobaron en forma promocional")
        print("3. Obtener listado de alumnos ordenado por año que cursan y alfabéticamente por apellido y nombre")
        print("4. Salir")

        opcion = int(input())

        if opcion == 1:
            dni = int(input("Ingrese el DNI del alumno: "))
            promedios = calcular_promedio(alumnos, materias_aprobadas)
            mostrar_promedio(dni, promedios)
        elif opcion == 2:
            listar_estudiantes_promocionales(alumnos, materias_aprobadas)
        elif opcion == 3:
            listar_alumnos_ordenados(alumnos)
        elif opcion == 4:
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()