# Capítulo 6 — Listas e tuplos
# Secção: Listas de listas: dados tabulares

vendas = [
    # mês, norte, centro, sul
    ("Jan", 1200, 980, 1500),
    ("Fev", 1100, 1020, 1430),
    ("Mar", 1350, 1110, 1610),
]
print(f"{'Mês':<5}{'Norte':>8}{'Centro':>8}{'Sul':>8}{'Total':>9}")
for mes, *regioes in vendas:
    print(f"{mes:<5}" + "".join(f"{v:>8}" for v in regioes)
          + f"{sum(regioes):>9}")
colunas = list(zip(*vendas))          # transpõe a tabela
totais = [sum(col) for col in colunas[1:]]
print(f"{'Total':<5}" + "".join(f"{t:>8}" for t in totais))
