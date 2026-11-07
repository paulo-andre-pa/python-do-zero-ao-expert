# Capítulo 16 — Dados persistentes: CSV, JSON e SQLite
# Secção: SQLite: uma base de dados completa num ficheiro

consulta = """
SELECT p.categoria,
       COUNT(*)                     AS num_vendas,
       SUM(v.quantidade)            AS unidades,
       ROUND(SUM(v.quantidade * p.preco), 2) AS faturacao
FROM vendas v
JOIN produtos p ON p.id = v.produto_id
GROUP BY p.categoria
ORDER BY faturacao DESC
"""
for linha in con.execute(consulta):
    print(dict(linha))
