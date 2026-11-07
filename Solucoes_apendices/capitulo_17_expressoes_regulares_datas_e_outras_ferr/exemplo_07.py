# Capítulo 17 — Expressões regulares, datas e outras ferramentas essenciais
# Secção: Datas e horas

from datetime import date, datetime, timedelta

emissao = date(2026, 11, 7)
vencimento = emissao + timedelta(days=30)
print("Vence em", vencimento)
faltam = (date(2026, 12, 31) - emissao).days
print("Faltam", faltam, "dias para o fim do ano")

inicio = datetime(2026, 11, 7, 8, 47)
fim = datetime(2026, 11, 7, 17, 15)
duracao = fim - inicio
horas, resto = divmod(duracao.seconds, 3600)
decimal = duracao.total_seconds() / 3600
print(f"Turno: {horas}h{resto // 60:02d} ({decimal:.2f} h)")
