# Capítulo 24 — Análise de dados com NumPy, pandas e Matplotlib
# Secção: Matplotlib: visualizar

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                     "axes.spines.right": False})

fig, ax = plt.subplots(figsize=(7, 3.4))
lojas = resumo.index
barras = ax.bar(lojas, resumo["faturacao"], color="0.35", width=0.6)
ax.bar_label(barras, fmt="{:,.0f} €", padding=3)
ax.set_title("Faturação por loja — 1.º trimestre 2026", loc="left",
             fontweight="bold")
ax.set_ylabel("Euros")
ax.set_ylim(0, resumo["faturacao"].max() * 1.15)
fig.tight_layout()
