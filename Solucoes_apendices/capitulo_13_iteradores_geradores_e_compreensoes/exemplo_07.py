# Capítulo 13 — Iteradores, geradores e compreensões
# Secção: Geradores

def contagem(inicio):
    while inicio >= 0:
        yield inicio
        inicio -= 1

g = contagem(3)
print(g)
print(next(g), next(g))
print(list(g))      # o que falta
