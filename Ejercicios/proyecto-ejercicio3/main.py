from registro import Registro

def leer_archivo(archivo):
    registros = [[Registro(0, 0, 0) for _ in range(24)] for _ in range(31)]
    with open(archivo, "r") as file:
        for linea in file:
            dia, hora, temperatura, humedad, presion = map(
                float, linea.strip().split(','))
            dia, hora, humedad, presion = int(dia), int(hora), int(humedad), int(presion)
            registros[dia - 1][hora] = Registro(temperatura, humedad, presion)
    return registros



def menor_mayor_valor(registros):
    min_temp = max_temp = registros[0][0].get_temperatura()
    min_hum = max_hum = registros[0][0].get_humedad()
    min_pres = max_pres = registros[0][0].get_presion_atmosferica()
    min_temp_dia = max_temp_dia = min_hum_dia = max_hum_dia = min_pres_dia = max_pres_dia = 1
    min_temp_hora = max_temp_hora = min_hum_hora = max_hum_hora = min_pres_hora = max_pres_hora = 0

    for dia, horas in enumerate(registros, 1):
        for hora, registro in enumerate(horas):
            if registro.get_temperatura() < min_temp:
                min_temp, min_temp_dia, min_temp_hora = registro.get_temperatura(), dia, hora
            elif registro.get_temperatura() > max_temp:
                max_temp, max_temp_dia, max_temp_hora = registro.get_temperatura(), dia, hora

            if registro.get_humedad() < min_hum:
                min_hum, min_hum_dia, min_hum_hora = registro.get_humedad(), dia, hora
            elif registro.get_humedad() > max_hum:
                max_hum, max_hum_dia, max_hum_hora = registro.get_humedad(), dia, hora

            if registro.get_presion_atmosferica() < min_pres:
                min_pres, min_pres_dia, min_pres_hora = registro.get_presion_atmosferica(), dia, hora
            elif registro.get_presion_atmosferica() > max_pres:
                max_pres, max_pres_dia, max_pres_hora = registro.get_presion_atmosferica(), dia, hora

    print(
        f"Menor temperatura: {min_temp} en el día {min_temp_dia} a las {min_temp_hora} horas")
    print(
        f"Mayor temperatura: {max_temp} en el día {max_temp_dia} a las {max_temp_hora} horas")
    print(
        f"Menor humedad: {min_hum} en el día {min_hum_dia} a las {min_hum_hora} horas")
    print(
        f"Mayor humedad: {max_hum} en el día {max_hum_dia} a las {max_hum_hora} horas")
    print(
        f"Menor presión atmosférica: {min_pres} en el día {min_pres_dia} a las {min_pres_hora} horas")
    print(
        f"Mayor presión atmosférica: {max_pres} en el día {max_pres_dia} a las {max_pres_hora} horas")


def temperatura_promedio_mensual(registros):
    suma_temperaturas = [0] * 24
    dias = len(registros)

    for horas in registros:
        for hora, registro in enumerate(horas):
            suma_temperaturas[hora] += registro.get_temperatura()

    promedio_temperaturas = [suma_temp /
                             dias for suma_temp in suma_temperaturas]

    for hora, promedio in enumerate(promedio_temperaturas):
        print(f"Temperatura promedio a las {hora} horas: {promedio:.2f}")


def listar_valores_dia(registros, dia):
    if 1 <= dia <= len(registros):
        print(f"Valores para el día {dia}:")
        for hora, registro in enumerate(registros[dia - 1]):
            print(f"{hora} horas - Temperatura: {registro.get_temperatura()}, Humedad: {registro.get_humedad()}, Presión atmosférica: {registro.get_presion_atmosferica()}")
    else:
        print("El día ingresado no es válido.")


def main():
    registros = leer_archivo("datos.csv")
    while True:
        print("1. Mostrar día y hora de menor y mayor valor para cada variable")
        print("2. Indicar la temperatura promedio mensual por cada hora")
        print("3. Listar los valores de las tres variables para cada hora de un día dado")
        print("4. Salir")

        opcion = int(input("Ingrese la opción deseada: "))
        if opcion == 1:
            menor_mayor_valor(registros)
        elif opcion == 2:
            temperatura_promedio_mensual(registros)
        elif opcion == 3:
            dia = int(input("Ingrese el número de día: "))
            listar_valores_dia(registros, dia)
        elif opcion == 4:
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
    # test()
