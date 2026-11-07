# Capítulo 26 — Python idiomático: boas práticas e armadilhas
# Secção: Coleções

partes = [f"linha {i}" for i in range(5)]
texto = "\n".join(partes)
print(texto.count("\n") + 1, "linhas")
