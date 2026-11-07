# Capítulo 21 — Algoritmos, estruturas de dados e desempenho
# Secção: Pesquisa binária

import bisect

limites = [0, 8_000, 20_000, 50_000]       # escalões (Capítulo 4)
taxas = [0.0, 0.15, 0.28, 0.40]
for rendimento in (5_000, 8_000, 35_000, 90_000):
    i = bisect.bisect_right(limites, rendimento) - 1
    print(rendimento, "-> taxa marginal", taxas[i])
