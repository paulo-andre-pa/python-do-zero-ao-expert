# Apêndice C — Preparação para entrevistas técnicas
# Secção: Exercícios típicos (com soluções)

def equilibrado(texto: str) -> bool:
    pares = {")": "(", "]": "[", "}": "{"}
    pilha = []
    for c in texto:
        if c in "([{":
            pilha.append(c)
        elif c in pares:
            if not pilha or pilha.pop() != pares[c]:
                return False
    return not pilha

print([equilibrado(t) for t in ["f(a[1], {b: 2})", "(]", "((", ""]])
