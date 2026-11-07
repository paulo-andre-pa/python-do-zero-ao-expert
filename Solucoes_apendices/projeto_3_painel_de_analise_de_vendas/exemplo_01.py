# Projeto 3 — Painel de análise de vendas
# Secção: Utilização

import os, sys
sys.path.insert(0, os.path.abspath("src"))
from painel.gerador import gerar
from painel.__main__ import main

gerar().to_csv("vendas_s1_2026.csv", index=False)
main(["vendas_s1_2026.csv", "relatorio.html"])
