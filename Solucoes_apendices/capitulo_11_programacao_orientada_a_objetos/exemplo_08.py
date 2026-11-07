# Capítulo 11 — Programação orientada a objetos
# Secção: Encapsulamento

class Conta:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self._saldo = 0.0
        self.saldo = saldo           # passa pela validação

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("O saldo não pode ser negativo")
        self._saldo = round(valor, 2)

    @property
    def em_risco(self):              # propriedade calculada, só leitura
        return self._saldo < 50

c = Conta("Nuno", 120.456)
print(c.saldo, c.em_risco)
c.saldo = 30
print(c.saldo, c.em_risco)
try:
    c.saldo = -5
except ValueError as e:
    print("Erro:", e)
