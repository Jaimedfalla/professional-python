class A:

    def __init__(self) -> None:
        self.__cuenta=0
        self.__contador = 0

    @property
    def cuenta(self) -> int:
        return self.__cuenta

    @property
    def contador(self)->int:
        return self.__contador

a=A()
print(a.cuenta)