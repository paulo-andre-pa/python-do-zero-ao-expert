# Capítulo 9 — Ficheiros e exceções
# Secção: Lançar exceções

def levantar(saldo, valor):
    if valor <= 0:
        raise ValueError("O valor tem de ser positivo.")
    if valor > saldo:
        raise ValueError(f"Saldo insuficiente ({saldo} €).")
    return saldo - valor

try:
    levantar(100, 250)
except ValueError as e:
    print("Operação recusada:", e)
