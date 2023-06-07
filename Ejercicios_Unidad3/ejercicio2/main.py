from ManejaHelados import ManejaHelados
from claseHelado import Helado
from claseSabor import Sabor
from ManejaSabores import ManejaSabores

def main():
    maneja_sabores = ManejaSabores()
    maneja_sabores.load_sabores("sabores.csv")
    maneja_helados = ManejaHelados()

    while True:
        print("Menú de opciones:")
        print("1. Registrar un helado vendido (instancia de la clase helado)")
        print("2. Mostrar el nombre de los 5 sabores de helado más pedidos")
        print("3. Ingresar un número de sabor y estimar el total de gramos vendidos. Para un helado se estima la cantidad de gramos de cada sabor dividiendo los gramos del helado en la cantidad de sabores. Por ejemplo, si se vendió un helado de 1000 gr de chocolate, frutilla, limón y americana. Se estima que en este helado se vendió de cada sabor 1000 / 4 = 250gr.")
        print("4. Ingresar por teclado un tipo de helado y mostrar los sabores vendidos en ese tamaño considerando todos los helados vendidos")
        print("5. Determinar el importe total recaudado por la Heladería, por cada tipo de helado")
        print("6. Salir")

        opcion = int(input("Ingrese el número de la opción deseada: "))

        if opcion == 1:
            print("Opciones de sabores:")
            for sabor in maneja_sabores._ManejaSabores__sabores:
                print(f"{sabor._Sabor__idSabor}. {sabor._Sabor__nombreSabor}")
            id_sabores = input("Ingrese los IDs de los sabores separados por comas: ")
            id_sabores = [int(id_sabor) for id_sabor in id_sabores.split(",")]
            gramos = int(input("Ingrese los gramos del helado: "))
            precio = float(input("Ingrese el precio del helado: "))
            sabores = [sabor for sabor in maneja_sabores._ManejaSabores__sabores if sabor._Sabor__idSabor in id_sabores]
            helado = Helado(gramos, precio, sabores)
            maneja_helados.registrar_helado(helado)
            print("Helado registrado exitosamente.")
        elif opcion == 2:
            maneja_helados.mostrar_5_mas_pedidos()
        elif opcion == 3:
            num_sabor = int(input("Ingrese el número del sabor: "))
            maneja_helados.estimar_gramos_vendidos(num_sabor)
        elif opcion == 4:
            tamano = int(input("Ingrese el tamaño del helado (100, 150, 250, 500, 1000): "))
            maneja_helados.mostrar_sabores_por_tamano(tamano)
        elif opcion == 5:
            maneja_helados.calcular_importe_total()
        elif opcion == 6:
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()