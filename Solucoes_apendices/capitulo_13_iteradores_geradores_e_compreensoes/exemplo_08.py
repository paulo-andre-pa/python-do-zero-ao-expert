# Capítulo 13 — Iteradores, geradores e compreensões
# Secção: Geradores

import sys

def numeros_primos():
    """Gera números primos indefinidamente."""
    encontrados = []
    n = 2
    while True:
        if all(n % p for p in encontrados if p * p <= n):
            encontrados.append(n)
            yield n
        n += 1

gen = numeros_primos()
print([next(gen) for _ in range(15)])

lista = [x * x for x in range(1_000_000)]
geradora = (x * x for x in range(1_000_000))
print(sys.getsizeof(lista), "bytes vs", sys.getsizeof(geradora), "bytes")
