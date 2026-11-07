# Projeto 6 — Triagem inteligente de pedidos de suporte
# Secção: Utilização

from triagem.servico import Triagem

triagem = Triagem(m, limiar=0.6)
pedidos = [
    "Boa tarde, cobraram-me a mensalidade duas vezes este mês!",
    "Estou sem internet desde sexta, não funciona nada. Vou cancelar!",
    "O router que encomendei ainda não chegou",
    "Quero mudar o email associado à minha conta",
    "Olá, preciso de ajuda",
]
for p in pedidos:
    d = triagem.classificar(p)
    estado = "URGENTE " if d.urgente else ""
    print(f"{p[:44]:<46}-> {estado}{d.equipa} ({d.prazo_horas}h, "
          f"conf. {d.confianca:.2f})")
