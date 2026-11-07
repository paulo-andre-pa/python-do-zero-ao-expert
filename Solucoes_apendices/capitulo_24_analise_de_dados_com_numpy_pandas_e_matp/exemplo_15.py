# Capítulo 24 — Análise de dados com NumPy, pandas e Matplotlib
# Secção: Matplotlib: visualizar

por_mes_loja = df.pivot_table(index="mes", columns="loja", values="total",
                              aggfunc="sum", fill_value=0)
fig, ax = plt.subplots(figsize=(7, 3.4))
estilos = {"Porto": ("0.1", "-", "o"), "Lisboa": ("0.4", "--", "s"),
           "Faro": ("0.6", ":", "^")}
for loja, (cor, linha, marca) in estilos.items():
    ax.plot(por_mes_loja.index.astype(str), por_mes_loja[loja],
            color=cor, linestyle=linha, marker=marca, label=loja)
ax.set_title("Evolução mensal da faturação", loc="left", fontweight="bold")
ax.set_ylabel("Euros")
ax.legend(frameon=False)
fig.tight_layout()
