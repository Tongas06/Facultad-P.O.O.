from conjunto import Conjunto

def main():
    print("Ingrese los elementos del conjunto A separados por comas:")
    elementos_a = list(map(int, input().split(",")))
    conjunto_a = Conjunto(elementos_a)

    print("Ingrese los elementos del conjunto B separados por comas:")
    elementos_b = list(map(int, input().split(",")))
    conjunto_b = Conjunto(elementos_b)

    while True:
        print("\nMenú de opciones:")
        print("1. Unión de conjuntos")
        print("2. Diferencia de conjuntos")
        print("3. Verificar si dos conjuntos son iguales")
        print("4. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            union = conjunto_a + conjunto_b
            print("Unión: ", union)
        elif opcion == 2:
            diferencia = conjunto_a - conjunto_b
            print("Diferencia: ", diferencia)
        elif opcion == 3:
            igualdad = conjunto_a == conjunto_b
            print("Los conjuntos son iguales" if igualdad else "Los conjuntos no son iguales")
        elif opcion == 4:
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()