# Apêndice C — Preparação para entrevistas técnicas
# Secção: Exercícios típicos (com soluções)

from collections import defaultdict

def agrupar_anagramas(palavras: list[str]) -> list[list[str]]:
    grupos = defaultdict(list)
    for p in palavras:
        grupos["".join(sorted(p))].append(p)
    return list(grupos.values())

palavras = ["amor", "roma", "ramo", "mora", "sol", "los", "mar"]
print(agrupar_anagramas(palavras))
