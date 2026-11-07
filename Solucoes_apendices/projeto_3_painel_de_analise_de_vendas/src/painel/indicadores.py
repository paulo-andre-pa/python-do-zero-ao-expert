"""Cálculo dos indicadores (funções puras)."""
import pandas as pd

def kpis(df: pd.DataFrame) -> dict[str, float]:
    media = round(df["total"].mean(), 2) if len(df) else 0.0
    return {"faturacao": round(df["total"].sum(), 2),
            "vendas": len(df),
            "ticket_medio": media,
            "clientes": df["cliente"].nunique()}

def variacao(atual: float, anterior: float) -> float | None:
    return None if anterior == 0 else (atual - anterior) / anterior

def comparar_ultimo_mes(df: pd.DataFrame) -> dict[str, tuple]:
    meses = sorted(df["mes"].unique())
    atual = kpis(df[df["mes"] == meses[-1]])
    anterior = kpis(df[df["mes"] == meses[-2]])
    return {k: (atual[k], variacao(atual[k], anterior[k])) for k in atual}

def mensal(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot_table(index="mes", columns="canal", values="total",
                          aggfunc="sum", fill_value=0)

def por_loja(df: pd.DataFrame) -> pd.DataFrame:
    r = df.groupby("loja").agg(faturacao=("total", "sum"),
                               vendas=("total", "size"),
                               ticket_medio=("total", "mean"))
    r["quota"] = r["faturacao"] / r["faturacao"].sum()
    return r.sort_values("faturacao", ascending=False)

def top_produtos(df: pd.DataFrame, n: int = 5) -> pd.Series:
    return df.groupby("produto")["total"].sum().nlargest(n)

def clientes(df: pd.DataFrame) -> dict[str, float]:
    por_cliente = df.groupby("cliente")["total"].sum().sort_values(
        ascending=False)
    compras = df.groupby("cliente").size()
    acumulado = por_cliente.cumsum() / por_cliente.sum()
    n80 = int((acumulado < 0.8).sum()) + 1
    return {"recorrentes": round(float((compras > 1).mean()), 3),
            "clientes_80pct": n80,
            "pct_clientes_80pct": round(n80 / len(por_cliente), 3)}
