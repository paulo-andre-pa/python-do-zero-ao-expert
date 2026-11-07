# Capítulo 17 — Expressões regulares, datas e outras ferramentas essenciais
# Secção: Expressões regulares

import re

texto = "Contactos: ana.silva@empresa.pt, rui@mail.com e geral@loja.co.ao"
emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", texto)
print(emails)
