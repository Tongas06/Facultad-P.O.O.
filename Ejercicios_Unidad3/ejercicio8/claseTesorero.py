from claseInterfaz import ITesorero
from abc import ABC, abstractmethod

class Tesorero(ABC):
    def __init__(self, lista_agentes):
        self.lista_agentes = lista_agentes

    def gastosSueldoPorEmpleado(self, cuil):
        agente = self.lista_agentes.buscar_agente_por_cuil(cuil)
        if agente:
            return agente.calcular_sueldo()
        return None