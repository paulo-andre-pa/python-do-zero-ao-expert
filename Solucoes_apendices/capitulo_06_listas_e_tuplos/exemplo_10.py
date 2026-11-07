# Capítulo 6 — Listas e tuplos
# Secção: Referências e cópias

import copy

matriz = [[1, 2], [3, 4]]
superficial = matriz.copy()
profunda = copy.deepcopy(matriz)
matriz[0][0] = 99
print(superficial)   # afetada!
print(profunda)      # independente
