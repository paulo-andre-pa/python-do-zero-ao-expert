# Capítulo 24 — Análise de dados com NumPy, pandas e Matplotlib
# Secção: pandas: dados tabulares

objetivos = pd.DataFrame({"loja": ["Porto", "Lisboa", "Faro"],
                          "objetivo_t1": [7000, 5500, 2500]})
desempenho = resumo.reset_index().merge(objetivos, on="loja")
desempenho["cumprimento"] = (desempenho["faturacao"]
                             / desempenho["objetivo_t1"])
print(desempenho[["loja", "faturacao", "objetivo_t1", "cumprimento"]]
      .to_string(index=False, formatters={"cumprimento": "{:.0%}".format}))
