# Capítulo 4 — Decisões: if, elif, else e match
# Secção: Planear decisões

def preco_bilhete(idade, estudante, dia):
    if idade < 12:
        return 0
    if idade >= 65:
        return 4
    if estudante:
        return 5
    return 6 if dia == "domingo" else 10

casos = [(8, False, "sábado"), (70, False, "terça"),
         (20, True, "sexta"), (40, False, "domingo"),
         (40, False, "quarta")]
for c in casos:
    print(c, "->", preco_bilhete(*c), "€")
