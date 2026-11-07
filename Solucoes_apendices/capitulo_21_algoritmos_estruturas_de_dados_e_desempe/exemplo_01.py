# Capítulo 21 — Algoritmos, estruturas de dados e desempenho
# Secção: A notação O-grande

import time

def tem_duplicados_quadratico(itens):
    for i in range(len(itens)):
        for j in range(i + 1, len(itens)):
            if itens[i] == itens[j]:
                return True
    return False

def tem_duplicados_ordenando(itens):         # O(n log n)
    ordenados = sorted(itens)
    return any(a == b for a, b in zip(ordenados, ordenados[1:]))

def tem_duplicados_conjunto(itens):          # O(n)
    return len(set(itens)) != len(itens)

dados = list(range(3_000))                   # sem duplicados: pior caso
for f in (tem_duplicados_quadratico, tem_duplicados_ordenando,
          tem_duplicados_conjunto):
    t = time.perf_counter()
    f(dados)
    print(f"{f.__name__:<28}{(time.perf_counter() - t) * 1000:9.2f} ms")
