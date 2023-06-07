from collections import Counter
from claseHelado import Helado

class ManejaHelados:
    def __init__(self):
        self.__helados = []

    def registrar_helado(self, helado):
        self.__helados.append(helado)

    # Aquí se pueden agregar los métodos para las opciones del menú.

    def mostrar_5_mas_pedidos(self):
        contador_sabores = Counter()
        idx_helado = 0
        while idx_helado < len(self.__helados):
            helado = self.__helados[idx_helado]
            idx_sabor = 0
            while idx_sabor < len(helado._Helado__sabores):
                sabor = helado._Helado__sabores[idx_sabor]
                contador_sabores[sabor._Sabor__idSabor] += 1
                idx_sabor += 1
            idx_helado += 1

        top_5_sabores = contador_sabores.most_common(5)

        print("Los 5 sabores más pedidos son:")
        for sabor, cantidad in top_5_sabores:
            print(f"ID del sabor: {sabor}, cantidad de pedidos: {cantidad}")

    def estimar_gramos_vendidos(self, num_sabor):
        gramos_vendidos = 0
        idx_helado = 0
        while idx_helado < len(self.__helados):
            helado = self.__helados[idx_helado]
            idx_sabor = 0
            while idx_sabor < len(helado._Helado__sabores):
                sabor = helado._Helado__sabores[idx_sabor]
                if sabor._Sabor__idSabor == num_sabor:
                    gramos_vendidos += helado._Helado__gramos
                    break
                idx_sabor += 1
            idx_helado += 1

        print(f"Se vendieron aproximadamente {gramos_vendidos} gramos del sabor {num_sabor}")

    def mostrar_sabores_por_tamano(self, tamano):
        sabores_tamano = set()
        idx_helado = 0
        while idx_helado < len(self.__helados):
            helado = self.__helados[idx_helado]
            if helado._Helado__gramos == tamano:
                idx_sabor = 0
                while idx_sabor < len(helado._Helado__sabores):
                    sabor = helado._Helado__sabores[idx_sabor]
                    sabores_tamano.add(sabor._Sabor__idSabor)
                    idx_sabor += 1
            idx_helado += 1

        print(f"Sabores vendidos en helados de {tamano} gramos:")
        for sabor in sabores_tamano:
            print(f"ID del sabor: {sabor}")

    def calcular_importe_total(self):
        importe_total = 0
        idx_helado = 0
        while idx_helado < len(self.__helados):
            helado = self.__helados[idx_helado]
            importe_total += helado._Helado__precio
            idx_helado += 1

        print(f"El importe total recaudado es de ${importe_total:.2f} pesos")
