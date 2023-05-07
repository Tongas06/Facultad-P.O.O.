class Registro:
    def __init__(self, temperatura, humedad, presion_atmosferica):
        #self.__chequear_tipo(temperatura, float)
        self.__chequear_tipo(humedad, int)
        self.__chequear_tipo(presion_atmosferica, int)
        
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion_atmosferica = presion_atmosferica

    def get_temperatura(self):
        return self.__temperatura
    
    def get_humedad(self):
        return self.__humedad
    
    def get_presion_atmosferica(self):
        return self.__presion_atmosferica

    def __chequear_tipo(self, parametro, tipo_esperado):
        if not isinstance(parametro, tipo_esperado):
            raise TypeError(
                f"Se esperaba un valor de tipo {tipo_esperado}, pero se recibió {type(parametro)}")
