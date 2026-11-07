# Capítulo 11 — Programação orientada a objetos
# Secção: A primeira classe

a = ContaBancaria("Ana")
b = ContaBancaria("Bruno", 500)
a.depositar(20)
print(a.saldo, b.saldo)
print(isinstance(a, ContaBancaria))
