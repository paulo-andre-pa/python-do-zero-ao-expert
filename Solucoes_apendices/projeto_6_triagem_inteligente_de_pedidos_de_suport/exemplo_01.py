# Projeto 6 — Triagem inteligente de pedidos de suporte
# Secção: Utilização

import os, sys
sys.path.insert(0, os.path.abspath("src"))
from triagem import dados, modelo

textos, rotulos = dados.gerar(4000)
print("Exemplo de pedido gerado:", textos[3])
m, (X_te, y_te), relatorio = modelo.treinar(textos, rotulos)
print(relatorio)
for cat, palavras in modelo.palavras_chave(m, 4).items():
    print(f"{cat:<10} {', '.join(palavras)}")
