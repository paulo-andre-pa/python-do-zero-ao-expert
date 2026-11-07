# Apêndice B — Soluções de exercícios selecionados
# Secção: Capítulo 13 — Iteradores e geradores

from itertools import groupby
import re

def comprimir(s: str) -> str:
    return "".join(f"{c}{len(list(g))}" for c, g in groupby(s))

def descomprimir(s: str) -> str:
    return "".join(c * int(n) for c, n in re.findall(r"(\D)(\d+)", s))

c = comprimir("aaabccdddd")
print(c, descomprimir(c), descomprimir(c) == "aaabccdddd")
