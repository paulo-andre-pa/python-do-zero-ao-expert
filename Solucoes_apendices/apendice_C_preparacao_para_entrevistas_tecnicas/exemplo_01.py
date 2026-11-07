# Apêndice C — Preparação para entrevistas técnicas
# Secção: Perguntas sobre a linguagem

import functools, time

def cronometrar(func):
    @functools.wraps(func)
    def envolvente(*args, **kwargs):
        t = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            ms = (time.perf_counter() - t) * 1000
            print(f"[{func.__name__} terminou em {ms:.0f} ms]")
    return envolvente

@cronometrar
def somar(a, b):
    return a + b

print(somar(2, 3))
