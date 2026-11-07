# Capítulo 10 — Módulos, pacotes e ambientes virtuais
# Secção: Pacotes

import loja
from loja.pagamentos import mbway

p = loja.Produto("Mochila", 39.9)
print(p, loja.__version__)
print(mbway.pagar(p, "912 345 678"))
