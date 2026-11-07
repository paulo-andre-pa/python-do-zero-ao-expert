# Capítulo 13 — Iteradores, geradores e compreensões
# Secção: Compreensões

palavras = ["python", "java", "c", "javascript", "go", "rust"]
por_tamanho = {p: len(p) for p in palavras}
letras_iniciais = {p[0] for p in palavras}
print(por_tamanho, sorted(letras_iniciais), sep="\n")
