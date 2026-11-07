# Capítulo 25 — Python por dentro: objetos, memória e o modelo de dados
# Secção: O caminho de uma operação

class Metros:
    def __init__(self, v):
        self.v = v
    def __add__(self, outro):
        print("Metros.__add__")
        if isinstance(outro, Metros):
            return Metros(self.v + outro.v)
        if isinstance(outro, (int, float)):
            return Metros(self.v + outro)
        return NotImplemented
    def __radd__(self, outro):
        print("Metros.__radd__")
        return self.__add__(outro)
    def __repr__(self):
        return f"Metros({self.v})"

print(Metros(3) + 2)
print(2 + Metros(3))         # int.__add__ devolve NotImplemented
print(sum([Metros(1), Metros(2)], Metros(0)))
