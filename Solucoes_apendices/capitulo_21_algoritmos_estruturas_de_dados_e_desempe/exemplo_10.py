# Capítulo 21 — Algoritmos, estruturas de dados e desempenho
# Secção: Medir antes de otimizar

import time
for nome, prob in [("lista", proibidas), ("conjunto", set(proibidas))]:
    t = time.perf_counter()
    contar_palavras_lento(linhas, prob)
    print(f"{nome:<9}{(time.perf_counter() - t) * 1000:8.1f} ms")
