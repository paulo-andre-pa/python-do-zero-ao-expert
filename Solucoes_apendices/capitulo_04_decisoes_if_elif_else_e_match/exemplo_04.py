# Capítulo 4 — Decisões: if, elif, else e match
# Secção: Condições compostas

idade = 34
rendimento_anual = 21000
tem_dividas = False

maior_idade = idade >= 18
rendimento_ok = rendimento_anual >= 15000

if maior_idade and rendimento_ok and not tem_dividas:
    print("Crédito pré-aprovado.")
else:
    print("Pedido em análise manual.")
