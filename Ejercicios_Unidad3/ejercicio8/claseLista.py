from ast import Tuple
import json
from typing import List, Tuple
from claseAgente import Agente
from claseDocenteInvestigador import DocenteInvestigador

class Lista:
    def __init__(self):
        self.__agentes = []

    def agregar_agente(self, agente: Agente):
        self.__agentes.append(agente)

    def agregar_agente_a_posicion(self, posicion: int, agente: Agente):
        self.__agentes.insert(posicion, agente)

    def mostrar_agente_por_posicion(self, posicion: int) -> Agente:
        return self.__agentes[posicion]

    def generar_listado_docentes_investigadores_por_area(self, area_investigacion: str) -> List[DocenteInvestigador]:
        listado = []
        i = 0
        while i < len(self.__agentes):
            agente = self.__agentes[i]
            if isinstance(agente, DocenteInvestigador) and agente.__área_investigación == area_investigacion:
                listado.append(agente)
            i += 1
        return listado

    def generar_listado_agentes_por_categoria(self, categoria_investigacion):
        listado = []
        i = 0
        while i < len(self.__agentes):
            agente = self.__agentes[i]
            if isinstance(agente, DocenteInvestigador) and agente.get_categoria_programa() == categoria_investigacion:
                listado.append(agente)
            i += 1
        return listado

    def recorrer_lista_e_generar_listado(self):
        listado = []
        i = 0
        while i < len(self.__agentes):
            agente = self.__agentes[i]
            sueldo = agente.get_sueldo_basico() + agente.get_antiguedad() * 0.1
            if isinstance(agente, DocenteInvestigador):
                sueldo += agente.get_importe_extra()     
            cargo = agente.get_cargo()
            catedra = agente.get_catedra()
            listado.append((agente.get_nombre(), agente.get_apellido(), cargo, catedra, sueldo))
            i += 1
        return listado

    def buscar_agente_por_cuil(self, cuil):
        i = 0
        while i < len(self.__agentes):
            agente = self.__agentes[i]
            if agente.get_cuil() == cuil:
                return agente
            i += 1
        return None

    def almacenar_agentes_en_archivo(self):
        with open('personal.json', 'w') as archivo:
            agentes_dict = [agente.to_dict() for agente in self.__agentes]
            json.dump(agentes_dict, archivo)
