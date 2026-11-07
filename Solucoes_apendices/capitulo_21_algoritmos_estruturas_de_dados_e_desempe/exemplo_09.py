# Capítulo 21 — Algoritmos, estruturas de dados e desempenho
# Secção: Medir antes de otimizar

import cProfile, pstats, io

def normalizar(texto):
    return texto.strip().lower()

def contar_palavras_lento(linhas, proibidas):
    contagem = {}
    for linha in linhas:
        for p in linha.split():
            p = normalizar(p)
            if p not in proibidas:            # proibidas é uma lista!
                contagem[p] = contagem.get(p, 0) + 1
    return contagem

linhas = ["O rato roeu a rolha da garrafa do rei da Rússia"] * 3000
proibidas = ["o", "a", "da", "do", "de"] * 200

perfil = cProfile.Profile()
perfil.enable()
contar_palavras_lento(linhas, proibidas)
perfil.disable()
saida = io.StringIO()
pstats.Stats(perfil, stream=saida).sort_stats("tottime").print_stats(3)
linhas = saida.getvalue().splitlines()
i = next(n for n, l in enumerate(linhas) if "ncalls" in l)
print("\n".join(l[:80] for l in linhas[i:i + 4]))
