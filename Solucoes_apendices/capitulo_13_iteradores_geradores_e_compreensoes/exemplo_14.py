# Capítulo 13 — Iteradores, geradores e compreensões
# Secção: O módulo itertools

vendas = [("Porto", 30), ("Lisboa", 50), ("Porto", 20),
          ("Faro", 15), ("Lisboa", 10)]
vendas.sort(key=lambda v: v[0])
for loja, grupo in groupby(vendas, key=lambda v: v[0]):
    print(loja, sum(valor for _, valor in grupo))
