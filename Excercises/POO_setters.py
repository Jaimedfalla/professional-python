class A:

    def __init__(self) -> None:
        self.__cuenta=0
        self.__contador = 0

    @property #get
    def cuenta(self) -> int:
        return self.__cuenta

    @cuenta.setter #set
    def cuenta(self,value:int)->None:
        self.__cuenta = value

    @property
    def contador(self)->int:
        return self.__contador

    @contador.setter
    def contador(self,value:int)->None:
        self.__contador = value

a=A()
print(a.cuenta)
a.cuenta = 90
a.contador=10
print(a.cuenta)
print(a.contador)