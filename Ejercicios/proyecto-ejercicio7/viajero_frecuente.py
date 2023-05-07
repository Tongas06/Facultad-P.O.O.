class ViajeroFrecuente:
    def __init__(self, numero, dni, nombre, apellido, millas_acum):
        self.__chequear_tipo(numero, int)
        self.__chequear_tipo(dni, str)
        self.__chequear_tipo(nombre, str)
        self.__chequear_tipo(apellido, str)
        self.__chequear_tipo(millas_acum, int)

        self.__numero = numero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum

    def get_numero(self):
        return self.__numero

    def cantidad_total_millas(self):
        return self.__millas_acum

    def acumular_millas(self, millas_recorridas):
        self.__chequear_tipo(millas_recorridas, int)

        self.__millas_acum += millas_recorridas
        return self.__millas_acum
    
    def canjear_millas(self, cantidad):
        self.__chequear_tipo(cantidad, int)

        if cantidad <= self.__millas_acum:
            self.__millas_acum -= cantidad
            return self.__millas_acum
        else:#duda excepcion o solo print de error
            raise ValueError(f"La cantidad de millas a canjear: {cantidad}, es mayor que la cantidad de millas acumuladas {self.cantidad_total_millas()}")

    def __gt__(self, other):
        if isinstance(other, ViajeroFrecuente):
            return self.__millas_acum > other.__millas_acum
        raise TypeError("El objeto comparado debe ser una instancia de ViajeroFrecuente")

    def __add__(self, millas_recorridas):
        if isinstance(millas_recorridas, int):
            return ViajeroFrecuente(self.__numero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum + millas_recorridas)
        raise TypeError("Las millas a acumular deben ser un entero")

    def __sub__(self, cantidad):
        if isinstance(cantidad, int):
            if cantidad <= self.__millas_acum:
                return ViajeroFrecuente(self.__numero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum - cantidad)
            else:
                raise ValueError(f"La cantidad de millas a canjear: {cantidad}, es mayor que la cantidad de millas acumuladas {self.cantidad_total_millas()}")
        raise TypeError("La cantidad de millas a canjear debe ser un entero")
    
    def __eq__(self, other):
        if isinstance(other, int):
            return self.cantidad_total_millas() == other
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, int):
            return self.__add__(other)
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, int):
            return self.__sub__(other)
        return NotImplemented

    def __chequear_tipo(self, parametro, tipo_esperado):
        if not isinstance(parametro, tipo_esperado):
            raise TypeError(
                f"Se esperaba un valor de tipo {tipo_esperado}, pero se recibió {type(parametro)}")

