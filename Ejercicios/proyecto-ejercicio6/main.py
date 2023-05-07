from viajero_frecuente import ViajeroFrecuente
import csv


def test():
    viajero = ViajeroFrecuente(46, '12345678', 'Juan', 'Pérez', 1000)
    assert viajero.cantidad_total_millas() == 1000
    assert viajero.acumular_millas(500) == 1500
    assert viajero.canjear_millas(1000) == 500
    try:
        viajero.canjear_millas(2000)
    except ValueError as e:
        assert str(e) == "La cantidad de millas a canjear: 2000, es mayor que la cantidad de millas acumuladas 500"

    # Crear instancias de ViajeroFrecuente
    v1 = ViajeroFrecuente(1, "12345678", "Ignacio", "Fuentes", 5000)
    v2 = ViajeroFrecuente(2, "23456789", "María", "Lopez", 7000)

    # Comparar instancias utilizando el operador >
    print(v1 > v2)  # False

    # Acumular millas utilizando el operador +
    v1 = v1 + 3000
    print(v1.cantidad_total_millas())  # 8000

    # Canjear millas utilizando el operador -
    v1 = v1 - 2000
    print(v1.cantidad_total_millas())  # 6000

def cargar_viajeros_desde_archivo(archivo):
    viajeros = []
    with open(archivo, 'r') as f:
        for linea in f.readlines():
            numero, dni, nombre, apellido, millas_acumuladas = linea.split(',')
            viajero = ViajeroFrecuente(int(numero), dni, nombre, apellido, int(millas_acumuladas))
            viajeros.append(viajero)
        # #reader = csv.reader(f, delimiter=',')
        # for row in reader:
        #     numero, dni, nombre, apellido, millas_acumuladas = row
        #     viajero = ViajeroFrecuente(
        #         int(numero), dni, nombre, apellido, int(millas_acumuladas))
        #     viajeros.append(viajero)
    return viajeros


def menu():
    print("1- Consultar Cantidad de Millas")
    print("2- Acumular Millas")
    print("3- Canjear Millas")
    print("4- Salir")
    return int(input("Ingrese la opción deseada: "))


def buscar_viajero_por_numero(viajeros, numero):
    return next((viajero for viajero in viajeros if viajero.get_numero() == numero), None)


def main():
    viajeros = cargar_viajeros_desde_archivo("viajeros.csv")
    numero = int(input("Ingrese algún número de viajero frecuente: "))
    viajero = buscar_viajero_por_numero(viajeros, numero)

    if not viajero:
        print("Viajero no encontrado")
        return

    while True:
        opcion = menu()
        if opcion == 1:
            print("Cantidad de Millas:", viajero.cantidad_total_millas())
        elif opcion == 2:
            millas = int(input("Ingrese la cantidad de millas a acumular: "))
            viajero.acumular_millas(millas)
        elif opcion == 3:
            millas = int(input("Ingrese la cantidad de millas a canjear: "))
            try:
                viajero.canjear_millas(millas)
            except ValueError as e:
                print(e)
        elif opcion == 4:
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
    test()
