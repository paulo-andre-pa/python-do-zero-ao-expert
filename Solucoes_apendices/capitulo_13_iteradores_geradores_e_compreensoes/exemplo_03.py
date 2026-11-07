# Capítulo 13 — Iteradores, geradores e compreensões
# Secção: Compreensões

precos = [12.5, 3.0, 47.9, 8.25, 102.0]

com_iva = [round(p * 1.23, 2) for p in precos]
baratos = [p for p in precos if p < 10]
classes = ["caro" if p > 40 else "normal" for p in precos]
print(com_iva, baratos, classes, sep="\n")
