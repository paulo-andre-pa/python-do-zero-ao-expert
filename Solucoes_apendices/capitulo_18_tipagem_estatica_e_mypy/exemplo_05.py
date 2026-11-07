# Capítulo 18 — Tipagem estática e mypy
# Secção: Tipos para estruturas de dados

type Matriz = list[list[float]]
type Grafo = dict[str, set[str]]

def identidade(n: int) -> Matriz:
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

rede: Grafo = {"A": {"B", "C"}, "B": {"C"}, "C": set()}
print(identidade(3), sorted(rede["A"]))
