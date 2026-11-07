# Capítulo 14 — Programação funcional e decoradores
# Secção: map, filter e reduce

from functools import reduce
from operator import mul

print(reduce(mul, range(1, 7)))                     # 6! = 720
descontos = [0.10, 0.05, 0.20]                       # descontos sucessivos
fator = reduce(lambda acc, d: acc * (1 - d), descontos, 1.0)
print(f"desconto total equivalente: {1 - fator:.1%}")
