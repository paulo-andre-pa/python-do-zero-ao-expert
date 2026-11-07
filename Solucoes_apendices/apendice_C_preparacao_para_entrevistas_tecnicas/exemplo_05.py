# Apêndice C — Preparação para entrevistas técnicas
# Secção: Exercícios típicos (com soluções)

from collections import Counter

def primeiro_unico(texto: str) -> str | None:
    contagem = Counter(texto)
    return next((c for c in texto if contagem[c] == 1), None)

print(primeiro_unico("programacao"), primeiro_unico("aabb"))
