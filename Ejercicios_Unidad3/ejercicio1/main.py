def main():
        
    from manejador_facultades import ManejadorFacultades

    manejador = ManejadorFacultades()
    manejador.cargar_facultades()

    while True:
        print("\nMenú de opciones:")
        print("1. Mostrar carreras por facultad")
        print("2. Mostrar facultad por carrera")
        print("3. Salir")

        opcion = int(input("Ingrese la opción deseada: "))

        if opcion == 1:
            codigo_facultad = int(input("Ingrese el código de la facultad: "))
            manejador.mostrar_carreras_por_facultad(codigo_facultad)
        elif opcion == 2:
            nombre_carrera = input("Ingrese el nombre de la carrera: ")
            manejador.mostrar_facultad_por_carrera(nombre_carrera)
        elif opcion == 3:
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()