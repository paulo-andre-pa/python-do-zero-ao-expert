# Apêndice B — Soluções de exercícios selecionados
# Secção: Capítulo 5 — Ciclos

from functools import cache

@cache
def comprimento(n: int) -> int:
    if n == 1:
        return 1
    return 1 + comprimento(n // 2 if n % 2 == 0 else 3 * n + 1)

melhor = max(range(1, 10_000), key=comprimento)
print(melhor, comprimento(melhor))
