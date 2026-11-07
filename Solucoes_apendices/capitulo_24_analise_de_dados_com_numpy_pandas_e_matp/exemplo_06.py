# Capítulo 24 — Análise de dados com NumPy, pandas e Matplotlib
# Secção: pandas: dados tabulares

print(df.isna().sum()[lambda s: s > 0])
print(df["loja"].value_counts().to_dict())
print("duplicados:", df.duplicated().sum())
