# Apêndice B — Soluções de exercícios selecionados
# Secção: Capítulo 3 — Strings

import unicodedata

def normalizar(texto: str) -> str:
    sem_acentos = unicodedata.normalize("NFD", texto)
    return "".join(c for c in sem_acentos.casefold() if c.isalnum())

def e_palindromo(texto: str) -> bool:
    t = normalizar(texto)
    return t == t[::-1]

for frase in ["Ana", "Olé! Maracujá, caju, caramelo", "Python"]:
    print(f"{frase!r}: {e_palindromo(frase)}")
