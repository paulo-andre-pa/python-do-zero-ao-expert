# Capítulo 26 — Python idiomático: boas práticas e armadilhas
# Secção: Coleções

from collections import defaultdict

vendas = [("Porto", 10), ("Faro", 5), ("Porto", 7)]

# antes
totais = {}
for loja, v in vendas:
    if loja not in totais:
        totais[loja] = 0
    totais[loja] += v

# depois
totais2 = defaultdict(int)
for loja, v in vendas:
    totais2[loja] += v
print(totais == dict(totais2), dict(totais2))
