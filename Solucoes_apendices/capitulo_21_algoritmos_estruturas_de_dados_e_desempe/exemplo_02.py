# Capítulo 21 — Algoritmos, estruturas de dados e desempenho
# Secção: Pesquisa binária

def pesquisa_binaria(ordenada, alvo):
    esq, dir = 0, len(ordenada) - 1
    passos = 0
    while esq <= dir:
        passos += 1
        meio = (esq + dir) // 2
        if ordenada[meio] == alvo:
            return meio, passos
        if ordenada[meio] < alvo:
            esq = meio + 1
        else:
            dir = meio - 1
    return -1, passos

numeros = list(range(0, 2_000_000, 2))     # um milhão de pares
print(pesquisa_binaria(numeros, 1_234_566))
print(pesquisa_binaria(numeros, 7))        # ímpar: não existe
