# Apêndice B — Soluções de exercícios selecionados
# Secção: Capítulo 7 — Dicionários e conjuntos

from collections import defaultdict

def inverter(d: dict) -> dict:
    resultado = defaultdict(list)
    for chave, valor in d.items():
        resultado[valor].append(chave)
    return dict(resultado)

print(inverter({"a": 1, "b": 2, "c": 1}))
