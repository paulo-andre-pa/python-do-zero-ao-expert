# Apêndice B — Soluções de exercícios selecionados
# Secção: Capítulo 8 — Funções

def formatar_tabela(linhas: list[list], cabecalhos: list[str]) -> str:
    todas = [cabecalhos] + [[str(c) for c in l] for l in linhas]
    larguras = [max(len(l[i]) for l in todas)
                for i in range(len(cabecalhos))]
    def fmt(l):
        return " | ".join(c.ljust(w) for c, w in zip(l, larguras))
    separador = "-+-".join("-" * w for w in larguras)
    corpo = [fmt(l) for l in todas[1:]]
    return "\n".join([fmt(todas[0]), separador, *corpo])

print(formatar_tabela([["Ana", 17, "Porto"], ["Bruno", 9, "Viseu"]],
                      ["Nome", "Nota", "Cidade"]))
