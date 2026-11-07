# Capítulo 18 — Tipagem estática e mypy
# Secção: Funções como tipos: Callable

from collections.abc import Callable, Iterable, Iterator

def aplicar(f: Callable[[float], float],
            valores: Iterable[float]) -> list[float]:
    return [f(v) for v in valores]

def pares(limite: int) -> Iterator[int]:
    yield from range(0, limite, 2)

print(aplicar(abs, [-1.5, 2.0]), list(pares(7)))
