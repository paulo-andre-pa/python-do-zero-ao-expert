# Capítulo 2 — Variáveis, tipos e operadores
# Secção: Números inteiros e decimais

import math
from decimal import Decimal

print(round(0.1 + 0.2, 2))                   # 1. arredondar ao mostrar
print(math.isclose(0.1 + 0.2, 0.3))          # 2. comparar com tolerância
print(Decimal("0.1") + Decimal("0.2"))       # 3. aritmética decimal exata
