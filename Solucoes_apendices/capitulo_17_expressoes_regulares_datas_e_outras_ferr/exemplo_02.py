# Capítulo 17 — Expressões regulares, datas e outras ferramentas essenciais
# Secção: Expressões regulares

import re

print(re.search(r"\d+", "Encomenda nº 4521 enviada").group())
print(re.fullmatch(r"\d{4}-\d{3}", "1200-195") is not None)   # CP português
print(re.findall(r"\b[A-Z]\w+", "O Rui e a Ana foram a Braga"))
print(re.sub(r"\s+", " ", "texto   com    espaços   a mais"))
print(re.split(r"[;,]\s*", "maçã, pera;uva ,  kiwi"))
