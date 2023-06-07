from claseInterfaz import IDirector
from abc import ABC, abstractmethod

class Director(ABC):
    def __init__(self, lista_agentes):
        self.lista_agentes = lista_agentes

    def modificarBasico(self, cuil, nuevoBasico):
        agente = self.lista_agentes.buscar_agente_por_cuil(cuil)
        if agente:
            agente.set_sueldo_basico(nuevoBasico)

    def modificarPorcentajeporcargo(self, cuil, nuevoPorcentaje):
        empleado = self.empleados.get(cuil)
        if empleado:
            empleado.porcentaje_por_cargo = nuevoPorcentaje
        else:
            print(f"Empleado con CUIL {cuil} no encontrado")

    def modificarPorcentajeporcategoría(self, cuil, nuevoPorcentaje):
        empleado = self.empleados.get(cuil)
        if empleado:
            empleado.porcentaje_por_categoria = nuevoPorcentaje
        else:
            print(f"Empleado con CUIL {cuil} no encontrado")

    def modificarImporteExtra(self, cuil, nuevoImporteExtra):
        empleado = self.empleados.get(cuil)
        if empleado:
            empleado.importe_extra = nuevoImporteExtra
        else:
            print(f"Empleado con CUIL {cuil} no encontrado")