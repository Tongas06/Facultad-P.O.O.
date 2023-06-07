import csv
from claseEmpleado_planta import EmpleadoPlanta
from claseEmpleado_contratado import EmpleadoContratado
from claseEmpleado_externo import EmpleadoExterno
from claseColeccion import ColeccionEmpleados

def cargar_empleados(archivo, funcion_crear_empleado, coleccion):
    with open(archivo, 'r', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            empleado = funcion_crear_empleado(row)
            coleccion.agregar_empleado(empleado)

def main():
    coleccion = ColeccionEmpleados(10)

    cargar_empleados('planta.csv', EmpleadoPlanta.desde_dict, coleccion)
    cargar_empleados('contratados.csv', EmpleadoContratado.desde_dict, coleccion)
    cargar_empleados('externos.csv', EmpleadoExterno.desde_dict, coleccion)

    print("Listado de empleados:")
    coleccion.listar_empleados()

    print("\nSueldo total de empleados de planta:")
    print(coleccion.calcular_sueldo_por_tipo(EmpleadoPlanta))

    print("\nSueldo total de empleados contratados:")
    print(coleccion.calcular_sueldo_por_tipo(EmpleadoContratado))

    print("\nSueldo total de empleados externos:")
    print(coleccion.calcular_sueldo_por_tipo(EmpleadoExterno))

    print("\nEmpleado con mayor sueldo:")
    empleado_mayor_sueldo = coleccion.obtener_empleado_con_mayor_sueldo()
    print(f"DNI: {empleado_mayor_sueldo.get_dni()}, Nombre: {empleado_mayor_sueldo.get_nombre()}, Sueldo: {empleado_mayor_sueldo.calcular_sueldo()}")

    # Registrar horas
    dni = input("\nIngrese el DNI del empleado para registrar horas trabajadas: ")
    horas = int(input("Ingrese la cantidad de horas trabajadas: "))
    coleccion.registrar_horas(dni, horas)

    # Total de tarea
    tarea = input("\nIngrese el nombre de la tarea para obtener el monto a pagar: ")
    coleccion.total_tarea(tarea)

    # Ayuda económica
    print("\nListado de empleados con ayuda económica:")
    coleccion.ayuda_economica()

    # Calcular sueldo
    print("\nSueldo de todos los empleados:")
    coleccion.calcular_sueldo()

if __name__ == '__main__':
    main()