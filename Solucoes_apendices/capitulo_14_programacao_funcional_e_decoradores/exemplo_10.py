# Capítulo 14 — Programação funcional e decoradores
# Secção: Decoradores

import functools, time

def cronometrar(func):
    @functools.wraps(func)
    def envolvente(*args, **kwargs):
        inicio = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            ms = (time.perf_counter() - inicio) * 1000
            envolvente.ultima_duracao_ms = ms
    return envolvente

@cronometrar
def soma_quadrados(n):
    """Soma os quadrados de 0 a n-1."""
    return sum(i * i for i in range(n))

print(soma_quadrados(100_000))
print(soma_quadrados.__name__, "-", soma_quadrados.__doc__)
print("duração registada:", soma_quadrados.ultima_duracao_ms > 0)
