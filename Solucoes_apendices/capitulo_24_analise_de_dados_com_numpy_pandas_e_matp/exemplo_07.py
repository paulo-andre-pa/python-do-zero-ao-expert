# Capítulo 24 — Análise de dados com NumPy, pandas e Matplotlib
# Secção: pandas: dados tabulares

df = (df.drop_duplicates()
        .assign(loja=lambda d: d["loja"].str.strip().str.title())
        .dropna(subset=["quantidade"])
        .astype({"quantidade": int}))
df["total"] = df["quantidade"] * df["preco_unit"]
df["mes"] = df["data"].dt.to_period("M")
print(df.shape, sorted(df["loja"].unique()))
