# Capítulo 7 — Dicionários e conjuntos
# Secção: Métodos essenciais

nomes = ["ana", "bruno", "carlos"]
comprimentos = {n: len(n) for n in nomes}
print(comprimentos)

precos = {"café": 0.8, "bolo": 2.5, "água": 1.0}
com_iva = {p: round(v * 1.23, 2) for p, v in precos.items()}
caros = {p: v for p, v in precos.items() if v > 0.9}
invertido = {v: k for k, v in comprimentos.items()}
print(com_iva, caros, invertido, sep="\n")
