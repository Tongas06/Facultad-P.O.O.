import csv
from plan_ahorro import PlanAhorro

def leer_planes(archivo):
    planes = []
    with open(archivo, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            codigo, modelo, version, valor, cantidad_cuotas, cuotas_licitar = row
            plan = PlanAhorro(codigo, modelo, version, float(valor))
            planes.append(plan)
    return planes

def menu():
    print("1. Actualizar valor del vehículo")
    print("2. Mostrar planes con cuota inferior")
    print("3. Monto para licitar vehículo")
    print("4. Modificar cuotas para licitar")
    print("0. Salir")

def main():
    planes = leer_planes("planes.csv")
    opcion = -1
    while opcion != 0:
        menu()
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            for plan in planes:
                print(plan)
                nuevo_valor = float(input("Ingrese el nuevo valor del vehículo: "))
                plan.actualizar_valor(nuevo_valor)
        elif opcion == 2:
            valor = float(input("Ingrese un valor: "))
            for plan in planes:
                if plan.cuota_inferior(valor):
                    print(plan)
        elif opcion == 3:
            for plan in planes:
                monto = plan.monto_para_licitar()
                print(f"{plan} - Monto para licitar: {monto}")
        elif opcion == 4:
            codigo = input("Ingrese el código del plan: ")
            nuevas_cuotas = int(input("Ingrese la nueva cantidad de cuotas para licitar: "))
            for plan in planes:
                if plan.codigo == codigo:
                    plan.set_cuotas_licitar(nuevas_cuotas)
                    break
        elif opcion != 0:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
