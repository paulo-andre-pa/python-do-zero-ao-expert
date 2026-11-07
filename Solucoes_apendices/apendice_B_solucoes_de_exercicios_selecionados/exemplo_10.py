# Apêndice B — Soluções de exercícios selecionados
# Secção: Capítulo 6 — Listas e tuplos

def vencedor(t: list[list[str]]) -> str | None:
    linhas = t + [list(c) for c in zip(*t)]           # linhas e colunas
    linhas += [[t[i][i] for i in range(3)],
               [t[i][2 - i] for i in range(3)]]       # diagonais
    for l in linhas:
        if l[0] != " " and l.count(l[0]) == 3:
            return l[0]
    return None

tabuleiro = [["X", "O", "X"],
             ["O", "X", "O"],
             [" ", "O", "X"]]
print(vencedor(tabuleiro))
