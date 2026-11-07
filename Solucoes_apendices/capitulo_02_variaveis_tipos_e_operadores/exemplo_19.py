# Capítulo 2 — Variáveis, tipos e operadores
# Secção: Conversão de tipos
# Este exemplo pede dados ao utilizador.

ano = input("Ano de nascimento: ")
print(type(ano))
idade = 2026 - int(ano)
print(f"Este ano faz {idade} anos.")
