# Capítulo 13 — Iteradores, geradores e compreensões
# Secção: Compreensões

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
plana = [x for linha in matriz for x in linha]
transposta = [[linha[i] for linha in matriz] for i in range(3)]
pares = [(c, n) for c in "AB" for n in range(1, 3)]
print(plana, transposta, pares, sep="\n")
