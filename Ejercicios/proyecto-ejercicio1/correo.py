class Email:
    def __init__(self, id_cuenta, dominio, tipo_dominio, contraseña):
        self.__chequear_tipo(id_cuenta, str)
        self.__chequear_tipo(dominio, str)
        self.__chequear_tipo(tipo_dominio, str)
        self.__chequear_tipo(contraseña, str)

        self.__id_cuenta = id_cuenta
        self.__dominio = dominio
        self.__tipo_dominio = tipo_dominio
        self.__contraseña = contraseña

    def retorna_email(self):
        return f"{self.__id_cuenta}@{self.__dominio}.{self.__tipo_dominio}"

    def get_dominio(self):
        return self.__dominio

    def crear_cuenta(self, email):
        partes_email = email.split('@')
        if len(partes_email) == 2:
            self.__id_cuenta, resto = partes_email
            partes_dominio = resto.split('.')
            if len(partes_dominio) == 2:
                self.__dominio, self.__tipo_dominio = partes_dominio
            else:
                raise ValueError("Formato de correo electrónico incorrecto")
        else:
            raise ValueError("Formato de correo electrónico incorrecto")

    def cambiar_contraseña(self, contraseña_actual, nueva_contraseña):
        self.__chequear_tipo(contraseña_actual, str)
        self.__chequear_tipo(nueva_contraseña, str)

        resultado = False
        if contraseña_actual == self.__contraseña:
            self.__contraseña = nueva_contraseña
            resultado = True

        return resultado

    def __chequear_tipo(self, parametro, tipo_esperado):
        if not isinstance(parametro, tipo_esperado):
            raise TypeError(
                f"Se esperaba un valor de tipo {tipo_esperado}, pero se recibió {type(parametro)}")
