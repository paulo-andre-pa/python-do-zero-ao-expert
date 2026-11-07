# Capítulo 13 — Iteradores, geradores e compreensões
# Secção: Geradores

def achatar(estrutura):
    """Percorre listas aninhadas a qualquer profundidade."""
    for elem in estrutura:
        if isinstance(elem, list):
            yield from achatar(elem)
        else:
            yield elem

print(list(achatar([1, [2, [3, 4], 5], [[6]], 7])))
