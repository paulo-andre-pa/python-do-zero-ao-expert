# Apêndice B — Soluções de exercícios selecionados
# Secção: Capítulo 21 — Algoritmos

def troco_minimo(valor: int, moedas: list[int]) -> list[int] | None:
    melhor: list[list[int] | None] = [[]] + [None] * valor
    for v in range(1, valor + 1):
        for m in moedas:
            anterior = melhor[v - m] if m <= v else None
            if anterior is None:
                continue
            atual = melhor[v]
            if atual is None or len(anterior) + 1 < len(atual):
                melhor[v] = anterior + [m]
    return melhor[valor]

print(troco_minimo(6, [1, 3, 4]))      # o método ganancioso daria 4+1+1
print(troco_minimo(387, [200, 100, 50, 20, 10, 5, 2, 1]))
print(troco_minimo(7, [2, 4]))         # impossível
