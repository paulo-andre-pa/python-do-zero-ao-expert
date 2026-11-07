# Capítulo 6 — Listas e tuplos
# Secção: Ordenar

palavras = ["banana", "Kiwi", "maçã", "abacate", "Uva"]
print(sorted(palavras))                  # maiúsculas vêm primeiro
print(sorted(palavras, key=str.lower))   # ignora maiúsculas
print(sorted(palavras, key=len))         # por comprimento
