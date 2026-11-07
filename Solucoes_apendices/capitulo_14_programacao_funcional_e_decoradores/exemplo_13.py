# Capítulo 14 — Programação funcional e decoradores
# Secção: Memoização com cache

from functools import cache
import time

def fib_lento(n):
    return n if n < 2 else fib_lento(n - 1) + fib_lento(n - 2)

@cache
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

t = time.perf_counter(); fib_lento(27); lento = time.perf_counter() - t
t = time.perf_counter(); fib(27); rapido = time.perf_counter() - t
print(fib(27), f"com cache foi ~{lento / rapido:,.0f}x mais rápido")
print(fib(200))
print(fib.cache_info().hits > 0)
