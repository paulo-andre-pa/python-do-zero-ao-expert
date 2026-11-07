# Apêndice B — Soluções de exercícios selecionados
# Secção: Capítulo 14 — Programação funcional

from functools import reduce

def compor(*funcoes):
    return reduce(lambda f, g: lambda x: f(g(x)), funcoes)

limpar = compor(str.title, str.strip, lambda s: s.replace("_", " "))
print(repr(limpar("  joao_da_silva  ")))
