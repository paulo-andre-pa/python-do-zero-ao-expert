# Capítulo 24 — Análise de dados com NumPy, pandas e Matplotlib
# Secção: pandas: dados tabulares

resumo = (df.groupby("loja")
            .agg(vendas=("total", "count"),
                 faturacao=("total", "sum"),
                 ticket_medio=("total", "mean"))
            .sort_values("faturacao", ascending=False)
            .round(2))
print(resumo.to_string())
