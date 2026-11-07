# Capítulo 24 — Análise de dados com NumPy, pandas e Matplotlib
# Secção: pandas: dados tabulares

grandes = df.loc[df["total"] > 1000, ["data", "loja", "produto", "total"]]
print(grandes.to_string(index=False))
filtro = "categoria == 'Informática' and loja == 'Porto'"
informatica_porto = df.query(filtro)
print(len(informatica_porto), "vendas de informática no Porto")
