# Apêndice C — Preparação para entrevistas técnicas
# Secção: Exercícios típicos (com soluções)

def dois_somam(numeros: list[int], alvo: int) -> tuple[int, int] | None:
    vistos: dict[int, int] = {}
    for i, n in enumerate(numeros):
        if alvo - n in vistos:
            return vistos[alvo - n], i
        vistos[n] = i
    return None

print(dois_somam([3, 8, 11, 4, 7], 11), dois_somam([1, 2], 9))
