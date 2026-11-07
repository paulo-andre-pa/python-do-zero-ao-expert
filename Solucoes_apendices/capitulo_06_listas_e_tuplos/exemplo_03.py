# Capítulo 6 — Listas e tuplos
# Secção: Acrescentar, inserir e remover

compras = ["pão", "leite"]
compras.append("ovos")              # no fim
compras.insert(0, "café")           # numa posição
compras.extend(["fruta", "arroz"])  # vários de uma vez
print(compras)

compras.remove("leite")      # pelo valor (a primeira ocorrência)
ultimo = compras.pop()       # remove e devolve o último
primeiro = compras.pop(0)    # remove e devolve pelo índice
del compras[0]               # remove pelo índice
print(compras, ultimo, primeiro)
