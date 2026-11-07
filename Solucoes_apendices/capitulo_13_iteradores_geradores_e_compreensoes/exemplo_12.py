# Capítulo 13 — Iteradores, geradores e compreensões
# Secção: O módulo itertools

from itertools import (count, islice, cycle, chain, accumulate,
                       groupby, product, combinations, permutations,
                       pairwise, batched)

print(list(islice(count(10, 5), 4)))          # 10, 15, 20, 25
print(list(islice(cycle("ABC"), 7)))
print(list(chain([1, 2], (3, 4), "xy")))
print(list(accumulate([100, -30, 50, -80])))  # saldos acumulados
print(list(pairwise([1, 4, 9, 16])))          # pares consecutivos
print(list(batched(range(7), 3)))             # lotes de 3 (Python 3.12+)
