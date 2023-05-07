class Ventana:
    def __init__(self, titulo, x1=0, y1=0, x2=500, y2=500):
        self.__titulo = titulo
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2


    def moverDerecha(self, unidades=1):
        self.__x1 += unidades
        self.__x2 += unidades

    def moverIzquierda(self, unidades=1):
        self.__x1 -= unidades
        self.__x2 -= unidades

    def subir(self, unidades=1):
        self.__y1 -= unidades
        self.__y2 -= unidades

    def bajar(self, unidades=1):
        self.__y1 += unidades
        self.__y2 += unidades

    def alto(self):
        return self.__y2 - self.__y1

    def ancho(self):
        return self.__x2 - self.__x1

    def getTitulo(self):
        return self.__titulo

    def mostrar(self):
        print('Ventana: {} (x1: {}, y1: {}) (x2: {}, y2: {})'.format(self.__titulo, self.__x1, self.__y1, self.__x2, self.__y2))
