import math


class circulo:
    pi=math.pi;

    @classmethod
    def area(cls,radio):
        return cls.pi*(radio**2)  #Utilizamos cls, para acceder al atributo pi

resultado=circulo.area(14);
print(resultado)