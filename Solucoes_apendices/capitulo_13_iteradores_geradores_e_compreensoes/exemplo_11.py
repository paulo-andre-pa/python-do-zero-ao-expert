# Capítulo 13 — Iteradores, geradores e compreensões
# Secção: Pipelines de dados

def ler_linhas(caminho):
    with open(caminho, encoding="utf-8") as f:
        next(f)                       # salta o cabeçalho
        for linha in f:
            yield linha.rstrip("\n")

def analisar(linhas):
    for linha in linhas:
        partes = linha.split(";")
        if len(partes) != 5:
            continue                  # ignora linhas inválidas
        data, loja, produto, qtd, preco = partes
        yield {"loja": loja, "produto": produto,
               "total": int(qtd) * float(preco)}

def filtrar_loja(registos, loja):
    return (r for r in registos if r["loja"] == loja)

pipeline = filtrar_loja(analisar(ler_linhas("vendas.csv")), "Porto")
print(f"Faturação Porto: {sum(r['total'] for r in pipeline):.2f} €")
