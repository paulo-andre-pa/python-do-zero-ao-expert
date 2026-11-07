# Capítulo 6 — Listas e tuplos
# Secção: Funções úteis com listas

precos = [12.5, 3.2, 47.0, 8.9]
print(len(precos), sum(precos), min(precos), max(precos))
print(sum(precos) / len(precos))      # média
print(list(reversed(precos)))
print(any(p > 40 for p in precos), all(p > 1 for p in precos))
