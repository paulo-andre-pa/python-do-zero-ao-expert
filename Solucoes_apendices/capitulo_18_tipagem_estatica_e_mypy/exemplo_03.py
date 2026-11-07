# Capítulo 18 — Tipagem estática e mypy
# Secção: Tipos para estruturas de dados

from typing import Literal, Final

Moeda = Literal["EUR", "USD", "AOA", "BRL"]
TAXA_IVA: Final = 0.23

def converter(valor: float, de: Moeda, para: Moeda) -> float:
    taxas: dict[str, float] = {"EUR": 1.0, "USD": 1.08,
                               "AOA": 980.0, "BRL": 5.9}
    return round(valor / taxas[de] * taxas[para], 2)

print(converter(100, "EUR", "USD"))
