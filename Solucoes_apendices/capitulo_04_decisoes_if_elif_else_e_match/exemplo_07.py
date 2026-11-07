# Capítulo 4 — Decisões: if, elif, else e match
# Secção: A expressão condicional

idade = 15
bilhete = "jovem" if idade < 18 else "adulto"
print(bilhete)

n = 7
print(f"{n} é {'par' if n % 2 == 0 else 'ímpar'}")
