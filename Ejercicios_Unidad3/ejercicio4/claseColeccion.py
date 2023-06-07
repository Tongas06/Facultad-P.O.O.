import numpy as np
from claseEmpleado import Empleado
from claseEmpleado_planta import EmpleadoPlanta
from claseEmpleado_contratado import EmpleadoContratado
from claseEmpleado_externo import EmpleadoExterno

class ColeccionEmpleados:
    def __init__(self, max_empleados):
        self.__empleados = []
        self.__max_empleados = max_empleados

    def agregar_empleado(self, empleado):
        if len(self.__empleados) == self.__max_empleados:
            print("No se pueden agregar más empleados.")
        else:
            self.__empleados.append(empleado)

    def registrar_horas(self, dni, horas_trabajadas):
        empleado = self.buscar_empleado(dni)
        if empleado is not None:
            if isinstance(empleado, EmpleadoContratado):
                empleado.registrar_horas(horas_trabajadas)
            else:
                print(f"El empleado con DNI {dni} no es un empleado contratado.")
        else:
            print(f"No se encontró ningún empleado con DNI {dni}.")

    def total_tarea(self, tarea):
        total = 0
        for empleado in self.__empleados:
            if isinstance(empleado, EmpleadoExterno) and empleado.get_tarea() == tarea and not empleado.finalizo_tarea():
                total += empleado.calcular_pago()
        print(f"El monto a pagar por la tarea {tarea} es de ${total}.")

    def listar_empleados(self):
        i = 0
        while i < len(self.__empleados):
            empleado = self.__empleados[i]
            if empleado is not None:
                print(f"DNI: {empleado.get_dni()}, Nombre: {empleado.get_nombre()}, Sueldo: {empleado.calcular_sueldo()}")
            i += 1

    def calcular_sueldo_por_tipo(self, tipo_empleado):
        sueldo_total = 0
        i = 0
        while i < len(self.__empleados):
            empleado = self.__empleados[i]
            if isinstance(empleado, tipo_empleado):
                sueldo_total += empleado.calcular_sueldo()
            i += 1
        return sueldo_total

    def obtener_empleado_con_mayor_sueldo(self):
        empleado_mayor_sueldo = None
        i = 0
        while i < len(self.__empleados):
            empleado = self.__empleados[i]
            if empleado_mayor_sueldo is None or empleado.calcular_sueldo() > empleado_mayor_sueldo.calcular_sueldo():
                empleado_mayor_sueldo = empleado
            i += 1
        return empleado_mayor_sueldo

    def ayuda_economica(self):
        print("Empleados que les corresponde ayuda económica:")
        i = 0
        while i < len(self.__empleados):
            empleado = self.__empleados[i]
            if empleado.calcular_sueldo() < 150000:
                print(f"Nombre: {empleado.get_nombre()}, Dirección: {empleado.get_direccion()}, DNI: {empleado.get_dni()}")
            i += 1

    def calcular_sueldo(self):
        print("Sueldo de todos los empleados:")
        i = 0
        while i < len(self.__empleados):
            empleado = self.__empleados[i]
            print(f"Nombre: {empleado.get_nombre()}, Teléfono: {empleado.get_telefono()}, Sueldo: {empleado.calcular_sueldo()}")
            i += 1

    def buscar_empleado(self, dni):
        i = 0
        while i < len(self.__empleados):
            empleado = self.__empleados[i]
            if empleado.get_dni() == dni:
                return empleado
            i += 1
        return None