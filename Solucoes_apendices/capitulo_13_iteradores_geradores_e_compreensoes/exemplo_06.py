# Capítulo 13 — Iteradores, geradores e compreensões
# Secção: Compreensões

import math
valores = [4, -1, 9, 16, -25, 2]
raizes = [r for v in valores if v >= 0 and (r := math.sqrt(v)).is_integer()]
print(raizes)
