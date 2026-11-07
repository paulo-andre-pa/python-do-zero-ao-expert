# Projeto 3 — Painel de análise de vendas
# Secção: Utilização

from painel import limpeza, indicadores as ind
import logging
logging.getLogger("painel").setLevel(logging.WARNING)

df = limpeza.limpar(limpeza.ler("vendas_s1_2026.csv"))
for k, (v, var) in ind.comparar_ultimo_mes(df).items():
    print(f"{k:<14}{v:>12,.2f}  ({var:+.1%} face ao mês anterior)")
print()
print(ind.por_loja(df).round(2).to_string(
    formatters={"quota": "{:.1%}".format}))
print()
print(ind.top_produtos(df).round(2).to_string())
print(ind.clientes(df))
