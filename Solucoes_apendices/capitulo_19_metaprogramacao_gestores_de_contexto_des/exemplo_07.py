# Capítulo 19 — Metaprogramação: gestores de contexto, descritores e metaclasses
# Secção: Controlar o acesso a atributos

import sys

class PontoNormal:
    def __init__(self, x, y):
        self.x, self.y = x, y

class PontoSlots:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x, self.y = x, y

a, b = PontoNormal(1, 2), PontoSlots(1, 2)
print(sys.getsizeof(a) + sys.getsizeof(a.__dict__), sys.getsizeof(b))
try:
    b.z = 3
except AttributeError as e:
    print("Erro:", e)
