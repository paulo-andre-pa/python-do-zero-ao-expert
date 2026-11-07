# Apêndice B — Soluções de exercícios selecionados
# Secção: Capítulo 25 — Python por dentro

class Vetor:
    __slots__ = ("_x", "_y")
    def __init__(self, x, y):
        object.__setattr__(self, "_x", x)
        object.__setattr__(self, "_y", y)
    def __setattr__(self, nome, valor):
        raise AttributeError("Vetor é imutável")
    def __eq__(self, outro):
        return (isinstance(outro, Vetor)
                and (self._x, self._y) == (outro._x, outro._y))
    def __hash__(self):
        return hash((self._x, self._y))
    def __repr__(self):
        return f"Vetor({self._x}, {self._y})"

distancias = {Vetor(0, 0): "origem"}
print(distancias[Vetor(0, 0)])           # um objeto igual encontra a chave

class VetorEstragado(Vetor):
    __slots__ = ()
    def __hash__(self):
        return id(self)          # objetos iguais, hashes diferentes

d = {VetorEstragado(1, 1): "x"}
print(VetorEstragado(1, 1) in d)         # deveria ser True!
