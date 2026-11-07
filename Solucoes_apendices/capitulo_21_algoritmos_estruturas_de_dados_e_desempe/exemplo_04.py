# Capítulo 21 — Algoritmos, estruturas de dados e desempenho
# Secção: Ordenação

def merge_sort(v):
    if len(v) <= 1:
        return v
    meio = len(v) // 2
    esq, dir = merge_sort(v[:meio]), merge_sort(v[meio:])
    resultado, i, j = [], 0, 0
    while i < len(esq) and j < len(dir):       # fusão de duas listas
        if esq[i] <= dir[j]:
            resultado.append(esq[i]); i += 1
        else:
            resultado.append(dir[j]); j += 1
    return resultado + esq[i:] + dir[j:]

import random
dados = random.sample(range(100), 12)
print(dados)
print(merge_sort(dados))
assert merge_sort(dados) == sorted(dados)
