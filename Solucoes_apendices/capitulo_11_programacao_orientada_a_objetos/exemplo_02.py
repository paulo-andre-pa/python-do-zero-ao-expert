# Capítulo 11 — Programação orientada a objetos
# Secção: A primeira classe

class ContaBancaria:
    """Uma conta bancária simples."""

    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def levantar(self, valor):
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor

conta = ContaBancaria("Marta Lopes", 100)
conta.depositar(50)
conta.levantar(30)
print(conta.titular, conta.saldo)
