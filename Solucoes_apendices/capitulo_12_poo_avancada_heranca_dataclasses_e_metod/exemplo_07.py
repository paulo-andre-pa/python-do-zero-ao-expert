# Capítulo 12 — POO avançada: herança, dataclasses e métodos especiais
# Secção: Métodos especiais (dunder)

from functools import total_ordering

@total_ordering
class Dinheiro:
    def __init__(self, cents, moeda="EUR"):
        self.cents, self.moeda = int(cents), moeda

    @classmethod
    def de_euros(cls, valor):
        return cls(round(valor * 100))

    def _verificar(self, outro):
        if not isinstance(outro, Dinheiro) or outro.moeda != self.moeda:
            return NotImplemented
        return outro

    def __add__(self, outro):
        if self._verificar(outro) is NotImplemented:
            return NotImplemented
        return Dinheiro(self.cents + outro.cents, self.moeda)

    def __mul__(self, fator):
        return Dinheiro(round(self.cents * fator), self.moeda)

    __rmul__ = __mul__           # permite 3 * dinheiro

    def __eq__(self, outro):
        return isinstance(outro, Dinheiro) and \
            (self.cents, self.moeda) == (outro.cents, outro.moeda)

    def __lt__(self, outro):
        return self.cents < outro.cents

    def __hash__(self):
        return hash((self.cents, self.moeda))

    def __bool__(self):
        return self.cents != 0

    def __repr__(self):
        return f"Dinheiro.de_euros({self.cents / 100:.2f})"

    def __str__(self):
        return f"{self.cents / 100:,.2f} {self.moeda}"

a, b = Dinheiro.de_euros(19.99), Dinheiro.de_euros(5.01)
print(a + b, 3 * a, a > b, max(a, b), bool(Dinheiro(0)))
print(sorted([a, b, Dinheiro(1)]))
