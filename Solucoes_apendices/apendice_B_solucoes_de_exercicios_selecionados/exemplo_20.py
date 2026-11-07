# Apêndice B — Soluções de exercícios selecionados
# Secção: Capítulo 27 — Padrões de projeto

from collections.abc import Callable

Desconto = Callable[[list[float]], float]

def percentagem(p: float) -> Desconto:
    return lambda precos: sum(precos) * p

def valor_fixo(v: float) -> Desconto:
    return lambda precos: min(v, sum(precos))

def leve3_pague2(precos: list[float]) -> float:
    ordenados = sorted(precos)
    return sum(ordenados[:len(precos) // 3])   # oferece os mais baratos

def total(precos: list[float], desconto: Desconto) -> float:
    return round(sum(precos) - desconto(precos), 2)

carrinho = [12.0, 7.5, 20.0, 9.9, 15.0, 3.0]
for nome, d in [("10 %", percentagem(0.10)), ("5 € fixos", valor_fixo(5)),
                ("leve 3 pague 2", leve3_pague2)]:
    print(f"{nome:<15}{total(carrinho, d):>8.2f} €")
