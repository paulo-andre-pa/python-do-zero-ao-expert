# Capítulo 8 — Funções
# Secção: Tipos de argumentos

def adicionar_mau(item, lista=[]):
    lista.append(item)
    return lista

print(adicionar_mau("a"))
print(adicionar_mau("b"))   # surpresa: o "a" ainda lá está!

def adicionar(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista

print(adicionar("a"), adicionar("b"))
