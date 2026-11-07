# Capítulo 14 — Programação funcional e decoradores
# Secção: Funções puras e imutabilidade

# Impura: altera a lista recebida
def aplicar_desconto_impuro(precos, d):
    for i in range(len(precos)):
        precos[i] *= 1 - d
    return precos

# Pura: devolve uma nova lista
def aplicar_desconto(precos, d):
    return [p * (1 - d) for p in precos]

originais = [100, 50]
novos = aplicar_desconto(originais, 0.1)
print(originais, novos)
