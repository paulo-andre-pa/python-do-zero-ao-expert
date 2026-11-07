# Capítulo 20 — Concorrência: threads, processos e asyncio
# Secção: Processos: paralelismo real para CPU
# Exemplo ilustrativo: pode exigir pacotes ou serviços externos.

import math, time
from concurrent.futures import ProcessPoolExecutor

def contar_primos(intervalo):
    a, b = intervalo
    return sum(1 for n in range(a, b)
               if n > 1 and all(n % d for d in range(2, math.isqrt(n) + 1)))

if __name__ == "__main__":           # obrigatório com processos
    blocos = [(i, i + 250_000) for i in range(0, 1_000_000, 250_000)]

    t = time.perf_counter()
    total = sum(map(contar_primos, blocos))
    print(f"sequencial: {total} primos em {time.perf_counter() - t:.1f}s")

    t = time.perf_counter()
    with ProcessPoolExecutor() as ex:
        total = sum(ex.map(contar_primos, blocos))
    print(f"em paralelo: {total} primos em {time.perf_counter() - t:.1f}s")
