# Capítulo 24 — Análise de dados com NumPy, pandas e Matplotlib
# Secção: pandas: dados tabulares

resumo.to_csv("resumo_lojas.csv")
desempenho.to_json("desempenho.json", orient="records", force_ascii=False)
print(open("resumo_lojas.csv", encoding="utf-8").read())
