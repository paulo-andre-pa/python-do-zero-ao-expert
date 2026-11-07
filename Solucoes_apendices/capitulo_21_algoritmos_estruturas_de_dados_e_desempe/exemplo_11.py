# Capítulo 21 — Algoritmos, estruturas de dados e desempenho
# Secção: Técnicas de otimização, por ordem de impacto

import random, time
from collections import Counter, defaultdict
from itertools import combinations

produtos = [f"P{i:03d}" for i in range(150)]
encomendas = [set(random.sample(produtos, random.randint(1, 5)))
              for _ in range(20_000)]

def recomendar_simples(produto, encomendas, n=3):
    c = Counter()
    for e in encomendas:
        if produto in e:
            c.update(e - {produto})
    return [p for p, _ in c.most_common(n)]

def construir_indice(encomendas):
    juntos = defaultdict(Counter)
    for e in encomendas:
        for a, b in combinations(sorted(e), 2):
            juntos[a][b] += 1
            juntos[b][a] += 1
    return juntos

t = time.perf_counter()
simples = {p: recomendar_simples(p, encomendas) for p in produtos}
t_simples = time.perf_counter() - t

t = time.perf_counter()
indice = construir_indice(encomendas)
otimizado = {p: [q for q, _ in indice[p].most_common(3)] for p in produtos}
t_otimizado = time.perf_counter() - t

print("P007 ->", otimizado["P007"])
print(f"simples: {t_simples:.2f}s | índice: {t_otimizado:.2f}s | "
      f"ganho ~{t_simples / t_otimizado:.0f}x")
