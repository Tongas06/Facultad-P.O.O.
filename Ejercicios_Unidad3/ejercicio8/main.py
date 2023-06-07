from claseLista import Lista
from claseInvestigador import Investigador
from claseDocenteInvestigador import DocenteInvestigador
from claseDocente import Docente
from clasePersonalApoyo import PersonalApoyo
import json
from claseTesorero import Tesorero
from claseDirector import Director
from claseInterfaz import ITesorero, IDirector

def autenticar_usuario():
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")

    if usuario == "uTesorero" and contraseña == "ag@74ck":
        return "tesorero"
    elif usuario == "uDirector" and contraseña == "ufC77#!1":
        return "director"
    else:
        return None

def menu_tesorero(tesorero: ITesorero, lista_agentes: Lista):
    while True:
        print("1. Consultar gasto de sueldos por empleado")
        print("2. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            cuil = input("Ingrese el CUIL del empleado: ")
            gasto_sueldo = tesorero.gastosSueldoPorEmpleado(cuil)
            if gasto_sueldo:
                print(f"Gasto de sueldo para el empleado con CUIL {cuil}: {gasto_sueldo}")
            else:
                print("Empleado no encontrado.")
        elif opcion == 2:
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def menu_director(director: IDirector, lista_agentes: Lista):
    while True:
        print("1. Modificar sueldo básico de empleado")
        print("2. Modificar porcentaje por cargo de docente")
        print("3. Modificar porcentaje por categoría de personal de apoyo")
        print("4. Modificar importe extra de docente investigador")
        print("5. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion in [1, 2, 3, 4]:
            cuil = input("Ingrese el CUIL del agente: ")
            nuevo_valor = float(input("Ingrese el nuevo valor: "))
            if opcion == 1:
                director.modificarBasico(cuil, nuevo_valor)
            elif opcion == 2:
                director.modificarPorcentajeporcargo(cuil, nuevo_valor)
            elif opcion == 3:
                director.modificarPorcentajeporcategoría(cuil, nuevo_valor)
            elif opcion == 4:
                director.modificarImporteExtra(cuil, nuevo_valor)
        elif opcion == 5:
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def crear_agente():
    print("Seleccione el tipo de agente que desea crear:")
    print("1. Docente")
    print("2. Investigador")
    print("3. Docente Investigador")
    print("4. Personal de Apoyo")
    
    tipo_agente = int(input("Ingrese el número correspondiente al tipo de agente: "))
    
    cuil = input("Ingrese el CUIL del agente: ")
    nombre = input("Ingrese el nombre del agente: ")
    apellido = input("Ingrese el apellido del agente: ")
    sueldo_basico = float(input("Ingrese el sueldo básico del agente: "))
    antiguedad = int(input("Ingrese la antigüedad del agente: "))

    if tipo_agente == 1:
        carrera = input("Ingrese la carrera del docente: ")
        cargo = input("Ingrese el cargo del docente: ")
        catedra = input("Ingrese la cátedra del docente: ")
        docente = Docente(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra)
        return docente
    elif tipo_agente == 2:
        area_investigacion = input("Ingrese el área de investigación: ")
        tipo_investigacion = input("Ingrese el tipo de investigación: ")
        investigador = Investigador(cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion)
        return investigador
    elif tipo_agente == 3:
        carrera = input("Ingrese la carrera del docente investigador: ")
        cargo = input("Ingrese el cargo del docente investigador: ")
        catedra = input("Ingrese la cátedra del docente investigador: ")
        area_investigacion = input("Ingrese el área de investigación: ")
        tipo_investigacion = input("Ingrese el tipo de investigación: ")
        categoria_incentivos = input("Ingrese la categoría en el programa de incentivos de investigación: ")
        importe_extra = float(input("Ingrese el importe extra por docencia e investigación: "))
        docente_investigador = DocenteInvestigador(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion, categoria_incentivos, importe_extra)
        return docente_investigador
    elif tipo_agente == 4:
        categoria = input("Ingrese la categoría del personal de apoyo: ")
        personal_apoyo = PersonalApoyo(cuil, apellido, nombre, sueldo_basico, antiguedad, categoria)
        return personal_apoyo
    else:
        print("Opción no válida.")
        return None

def menu(lista_agentes: Lista):
    while True:
        print("1. Insertar agente a la colección")
        print("2. Agregar agente a la colección")
        print("3. Mostrar agente en posición:")
        print("4. Generar listado de docentes investigadores por área de investigación")
        print("5. Generar listado de agentes por categoría de investigación")
        print("6. Recorrer la colección y generar listado con nombre, apellido, tipo de Agente y sueldo")
        print("7. Almacenar los datos de todos los agentes en el archivo personal.json")
        print("8. Seleccionar rol de usuario (tesorero/director)")
        print("9. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            agente = crear_agente()
            posicion = int(input("Ingrese la posición en la que desea insertar el agente: "))
            lista_agentes.agregar_agente_a_posicion(posicion, agente)
            print(f"Agente {agente.get_nombre()} {agente.get_apellido()} insertado en la posición {posicion}.")
        elif opcion == 2:
            agente = crear_agente()
            lista_agentes.agregar_agente(agente)
            print(f"Agente {agente.get_nombre()} {agente.get_apellido()} agregado a la colección.")
        elif opcion == 3:
            posicion = int(input("Ingrese la posición: "))
            agente = lista_agentes.mostrar_agente_por_posicion(posicion)
            print(agente.get_apellido(), agente.get_nombre(), agente.get_cargo(), agente.get_catedra())
        elif opcion == 4:
            area_investigacion = input("Ingrese el área de investigación: ")
            docentes_investigadores = lista_agentes.generar_listado_docentes_investigadores_por_area(area_investigacion)
            for docente_investigador in docentes_investigadores:
                print(docente_investigador.get_apellido(), docente_investigador.get_nombre(), docente_investigador.get_cargo(), docente_investigador.get_catedra())
        elif opcion == 5:
            categoria_investigacion = input("Ingrese la categoría de investigación: ")
            agentes_por_categoria = lista_agentes.generar_listado_agentes_por_categoria(categoria_investigacion)
            for agente in agentes_por_categoria:
                print(agente.get_apellido(), agente.get_nombre(), agente.get_cargo(), agente.get_catedra())
        elif opcion == 6:
            listado = lista_agentes.recorrer_lista_e_generar_listado()
            for nombre, apellido, cargo, cátedra, sueldo in listado:
                print(f"{nombre} {apellido} - Cargo: {cargo} - Cátedra: {cátedra} - Sueldo: {sueldo}")
        elif opcion == 7:
            lista_agentes.almacenar_agentes_en_archivo()       
        elif opcion == 8:
            tipo_usuario = input("Ingrese el tipo de usuario (tesorero/director): ")
            if tipo_usuario == "tesorero" or tipo_usuario == "director":
                if autenticar_usuario() == tipo_usuario:
                    if tipo_usuario == "tesorero":
                        tesorero = Tesorero(lista_agentes)
                        menu_tesorero(tesorero, lista_agentes)
                    else:
                        director = Director(lista_agentes)
                        menu_director(director, lista_agentes)
                else:
                    print("Usuario o contraseña incorrecta.")
            else:
                print("Opción no válida. Por favor, seleccione tesorero o director.")
        elif opcion == 9:
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    lista_agentes = Lista()
    menu(lista_agentes)