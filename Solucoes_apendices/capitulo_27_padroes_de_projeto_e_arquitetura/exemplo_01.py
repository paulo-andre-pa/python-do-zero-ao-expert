# Capítulo 27 — Padrões de projeto e arquitetura
# Secção: Strategy: trocar algoritmos

from dataclasses import dataclass
from collections.abc import Callable

@dataclass
class Encomenda:
    peso_kg: float
    valor: float
    destino: str = "continente"

def portes_ctt(e: Encomenda) -> float:
    return 3.5 + 0.8 * e.peso_kg

def portes_expresso(e: Encomenda) -> float:
    return 9.9 if e.peso_kg <= 5 else 9.9 + 1.5 * (e.peso_kg - 5)

def portes_gratis_acima_de(limite: float) -> Callable[[Encomenda], float]:
    def estrategia(e: Encomenda) -> float:
        return 0.0 if e.valor >= limite else portes_ctt(e)
    return estrategia

ESTRATEGIAS = {"ctt": portes_ctt, "expresso": portes_expresso,
               "promo": portes_gratis_acima_de(50)}

enc = Encomenda(peso_kg=7, valor=64)
for nome, calcular in ESTRATEGIAS.items():
    print(f"{nome:<9}{calcular(enc):6.2f} €")
