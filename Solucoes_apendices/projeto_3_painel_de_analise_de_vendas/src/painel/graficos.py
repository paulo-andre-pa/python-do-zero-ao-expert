"""Gráficos legíveis em preto e branco."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({"font.size": 9, "axes.spines.top": False,
                     "axes.spines.right": False})
ESTILOS = [("0.15", "-", "o"), ("0.55", "--", "s")]

def evolucao_mensal(tabela: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(7, 3))
    x = tabela.index.astype(str)
    for (cor, linha, marca), canal in zip(ESTILOS, tabela.columns):
        ax.plot(x, tabela[canal] / 1000, color=cor, linestyle=linha,
                marker=marca, label=canal)
    ax.set_title("Faturação mensal por canal (milhares de €)",
                 loc="left", fontweight="bold")
    ax.legend(frameon=False)
    ax.set_ylim(bottom=0)
    fig.tight_layout()
    return fig

def barras_lojas(resumo: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(7, 2.6))
    dados = resumo.sort_values("faturacao")
    barras = ax.barh(dados.index, dados["faturacao"] / 1000, color="0.4")
    ax.bar_label(barras, labels=[f"{q:.0%}" for q in dados["quota"]],
                 padding=3)
    ax.set_title("Faturação por loja (milhares de €) e quota",
                 loc="left", fontweight="bold")
    fig.tight_layout()
    return fig
