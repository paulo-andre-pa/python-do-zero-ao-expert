# Capítulo 24 — Análise de dados com NumPy, pandas e Matplotlib
# Secção: pandas: dados tabulares

mensal = df.set_index("data")["total"].resample("ME").sum()
print(mensal.to_string())
print("variação mensal (%):",
      (mensal.pct_change() * 100).round(1).tolist()[1:])
