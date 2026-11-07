# Capítulo 14 — Programação funcional e decoradores
# Secção: functools.partial

from functools import partial

def preco_final(preco, iva, desconto=0):
    return round(preco * (1 - desconto) * (1 + iva), 2)

preco_pt = partial(preco_final, iva=0.23)
preco_reduzido = partial(preco_final, iva=0.06)
print(preco_pt(100), preco_reduzido(100), preco_pt(100, desconto=0.5))
