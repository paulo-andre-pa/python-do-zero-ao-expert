# Capítulo 13 — Iteradores, geradores e compreensões
# Secção: O protocolo de iteração

class Contagem:
    """Iterador de contagem decrescente."""
    def __init__(self, inicio):
        self.atual = inicio

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual < 0:
            raise StopIteration
        valor = self.atual
        self.atual -= 1
        return valor

for n in Contagem(5):
    print(n, end=" ")
print()
print(list(Contagem(3)), sum(Contagem(100)))
