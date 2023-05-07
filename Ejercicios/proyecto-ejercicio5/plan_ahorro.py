class PlanAhorro:
    cantidad_cuotas = 60
    cuotas_licitar = 10

    def __init__(self, codigo, modelo, version, valor):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor
    
    @classmethod
    def set_cuotas_plan(cls, cuotas):
        cls.cantidad_cuotas = cuotas

    @classmethod
    def set_cuotas_licitar(cls, cuotas):
        cls.cuotas_licitar = cuotas

    def actualizar_valor(self, nuevo_valor):
        self.__valor = nuevo_valor

    def valor_cuota(self):
        return (self.__valor / PlanAhorro.cantidad_cuotas) + (self.__valor * 0.10)

    def monto_para_licitar(self):
        return PlanAhorro.cuotas_licitar * self.valor_cuota()

    def __str__(self):
        return f"Código: {self.__codigo}, Modelo: {self.__modelo}, Versión: {self.__version}, Valor: {self.__valor}"

    def cuota_inferior(self, valor):
        return self.valor_cuota() < valor

    @property
    def codigo(self):
        return self.__codigo
