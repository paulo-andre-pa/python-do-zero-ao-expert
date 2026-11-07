# Capítulo 24 — Análise de dados com NumPy, pandas e Matplotlib
# Secção: NumPy: cálculo vetorizado

quota = vendas / vendas.sum(axis=1, keepdims=True)
print(np.round(quota, 2))
