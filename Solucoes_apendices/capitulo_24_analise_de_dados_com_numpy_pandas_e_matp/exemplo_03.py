# Capítulo 24 — Análise de dados com NumPy, pandas e Matplotlib
# Secção: NumPy: cálculo vetorizado

# Vendas: 3 lojas (linhas) x 4 trimestres (colunas)
vendas = np.array([[120, 135, 150, 170],
                   [ 90,  95, 110, 100],
                   [200, 180, 210, 240]])
print(vendas.shape, vendas.dtype)
print("por loja:", vendas.sum(axis=1))         # soma das colunas
print("por trimestre:", vendas.sum(axis=0))    # soma das linhas
print("crescimento T1->T4 (%):", np.round((vendas[:, 3] / vendas[:, 0] - 1)
                                          * 100, 1))
print(vendas[vendas > 150])
