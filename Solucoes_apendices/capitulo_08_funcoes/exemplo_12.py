# Capítulo 8 — Funções
# Secção: Recursividade

def fatorial(n):
    if n <= 1:              # caso base
        return 1
    return n * fatorial(n - 1)

def tamanho_total(pasta):
    """Soma os tamanhos de uma árvore de pastas (dicionários aninhados)."""
    total = 0
    for nome, conteudo in pasta.items():
        if isinstance(conteudo, dict):
            total += tamanho_total(conteudo)   # subpasta
        else:
            total += conteudo                  # ficheiro
    return total

disco = {"docs": {"cv.pdf": 120, "fotos": {"a.jpg": 800, "b.jpg": 650}},
         "notas.txt": 4}
print(fatorial(6), tamanho_total(disco))
