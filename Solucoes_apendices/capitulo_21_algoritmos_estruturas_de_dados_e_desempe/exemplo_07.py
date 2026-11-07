# Capítulo 21 — Algoritmos, estruturas de dados e desempenho
# Secção: Programação dinâmica

def mochila(itens, capacidade):
    """itens: lista de (nome, peso, valor). Devolve (valor, escolhidos)."""
    n = len(itens)
    melhor = [[0] * (capacidade + 1) for _ in range(n + 1)]
    for i, (_, peso, valor) in enumerate(itens, 1):
        for c in range(capacidade + 1):
            melhor[i][c] = melhor[i - 1][c]
            if peso <= c:
                melhor[i][c] = max(melhor[i][c],
                                   melhor[i - 1][c - peso] + valor)
    escolhidos, c = [], capacidade
    for i in range(n, 0, -1):              # reconstruir a escolha
        if melhor[i][c] != melhor[i - 1][c]:
            escolhidos.append(itens[i - 1][0])
            c -= itens[i - 1][1]
    return melhor[n][capacidade], escolhidos[::-1]

# Projetos possíveis: (nome, dias de trabalho, lucro em milhares de €)
projetos = [("Site", 5, 12), ("App", 9, 25), ("ERP", 12, 30),
            ("Loja", 4, 9), ("Dashboard", 3, 8)]
print(mochila(projetos, capacidade=20))
