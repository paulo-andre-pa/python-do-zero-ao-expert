# Capítulo 9 — Ficheiros e exceções
# Secção: Lançar exceções

class ErroBancario(Exception):
    """Erro base da aplicação bancária."""

class SaldoInsuficiente(ErroBancario):
    def __init__(self, saldo, pedido):
        super().__init__(f"pedido de {pedido} € com saldo de {saldo} €")
        self.em_falta = pedido - saldo

def levantar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficiente(saldo, valor)
    return saldo - valor

try:
    levantar(80, 120)
except SaldoInsuficiente as e:
    print(f"Recusado: {e}. Faltam {e.em_falta} €.")
