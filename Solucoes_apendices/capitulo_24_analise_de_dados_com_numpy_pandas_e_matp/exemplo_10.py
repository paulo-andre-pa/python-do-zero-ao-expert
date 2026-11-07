# Capítulo 24 — Análise de dados com NumPy, pandas e Matplotlib
# Secção: pandas: dados tabulares

pivo = df.pivot_table(index="loja", columns="mes", values="total",
                      aggfunc="sum", fill_value=0, margins=True,
                      margins_name="Total")
print(pivo.round(0).to_string())
