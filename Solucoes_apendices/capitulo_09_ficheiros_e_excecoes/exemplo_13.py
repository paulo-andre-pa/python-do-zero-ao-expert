# Capítulo 9 — Ficheiros e exceções
# Secção: EAFP versus LBYL

def importar(caminho):
    notas, erros = {}, []
    try:
        f = open(caminho, encoding="utf-8")
    except FileNotFoundError:
        return notas, [f"Ficheiro {caminho} não encontrado"]
    with f:
        for n, linha in enumerate(f, start=1):
            linha = linha.strip()
            if not linha:
                continue
            try:
                aluno, texto_nota = linha.split(";")
                nota = float(texto_nota)
                if not 0 <= nota <= 20:
                    raise ValueError(f"nota {nota} fora da escala")
            except ValueError as e:
                erros.append(f"linha {n}: {e}")
            else:
                notas[aluno] = nota
    return notas, erros

notas, erros = importar("pauta.txt")
print("Válidas:", notas)
print("Problemas:")
for e in erros:
    print("  -", e)
