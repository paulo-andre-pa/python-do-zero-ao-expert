# Capítulo 6 — Listas e tuplos
# Secção: Tuplos: sequências imutáveis

from collections import namedtuple

Produto = namedtuple("Produto", ["nome", "preco", "stock"])
p = Produto("Caneta", 1.2, 300)
print(p.nome, p.preco * p.stock, p)
