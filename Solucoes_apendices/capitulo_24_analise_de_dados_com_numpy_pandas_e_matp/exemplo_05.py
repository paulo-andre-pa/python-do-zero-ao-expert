# Capítulo 24 — Análise de dados com NumPy, pandas e Matplotlib
# Secção: pandas: dados tabulares

import pandas as pd

df = pd.read_csv("vendas_2026.csv", parse_dates=["data"])
print(df.shape)
print(df.head(4).to_string())
print(df.dtypes.to_string())
