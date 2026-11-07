# Capítulo 24 — Análise de dados com NumPy, pandas e Matplotlib
# Secção: NumPy: cálculo vetorizado

import numpy as np

precos = np.array([12.5, 3.2, 47.0, 8.9, 21.0])
quantidades = np.array([10, 40, 2, 15, 7])

print(precos * 1.23)                     # IVA em todos de uma vez
print(precos * quantidades)              # elemento a elemento
print((precos * quantidades).sum(), precos.mean(), precos.max())
print(precos[precos > 10])               # filtragem booleana
