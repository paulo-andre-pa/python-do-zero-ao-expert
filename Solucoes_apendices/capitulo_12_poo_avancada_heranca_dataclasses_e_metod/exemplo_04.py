# Capítulo 12 — POO avançada: herança, dataclasses e métodos especiais
# Secção: Classes abstratas

from abc import ABC, abstractmethod
import math

class Forma(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimetro(self) -> float: ...

    def descrever(self):           # método concreto partilhado
        return (f"{type(self).__name__}: área {self.area():.2f}, "
                f"perímetro {self.perimetro():.2f}")

class Circulo(Forma):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r ** 2
    def perimetro(self):
        return 2 * math.pi * self.r

class Retangulo(Forma):
    def __init__(self, l, a):
        self.l, self.a = l, a
    def area(self):
        return self.l * self.a
    def perimetro(self):
        return 2 * (self.l + self.a)

for f in (Circulo(1.5), Retangulo(3, 4)):
    print(f.descrever())
