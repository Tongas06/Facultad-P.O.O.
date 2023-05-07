class Conjunto:
    __elementos=""
    def __init__(self, elementos=""):
        self.__elementos = set(elementos)

    def __add__(self, otro_conjunto):
        union = self.__elementos | otro_conjunto.__elementos
        return Conjunto(union)

    def __sub__(self, otro_conjunto):
        diferencia = self.__elementos - otro_conjunto.__elementos
        return Conjunto(diferencia)

    def __eq__(self, otro_conjunto):
        return self.__elementos == otro_conjunto.__elementos

    def __str__(self):
        return "{" + ", ".join(map(str, self.__elementos)) + "}"