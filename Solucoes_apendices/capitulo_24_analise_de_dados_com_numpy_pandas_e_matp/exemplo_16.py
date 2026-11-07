# Capítulo 24 — Análise de dados com NumPy, pandas e Matplotlib
# Secção: Matplotlib: visualizar

por_vendedor = (df.groupby("vendedor")["total"]
                  .agg(faturacao="sum", vendas="count")
                  .assign(quota=lambda d: d["faturacao"]
                          / d["faturacao"].sum())
                  .sort_values("faturacao"))
cat = df.groupby(["vendedor", "categoria"])["total"].sum()
por_vendedor["melhor_categoria"] = (cat.groupby(level=0).idxmax()
                                       .str[1])
print(por_vendedor.round(2).to_string(
    formatters={"quota": "{:.0%}".format}))

fig, ax = plt.subplots(figsize=(7, 2.8))
ax.barh(por_vendedor.index, por_vendedor["faturacao"], color="0.4")
ax.set_title("Faturação por vendedor — T1 2026", loc="left",
             fontweight="bold")
ax.set_xlabel("Euros")
fig.tight_layout()
