# Capítulo 17 — Expressões regulares, datas e outras ferramentas essenciais
# Secção: Datas e horas

from datetime import date, time, datetime, timedelta

hoje = date(2026, 11, 7)            # num programa real: date.today()
reuniao = datetime(2026, 11, 12, 14, 30)
print(hoje, reuniao, hoje.weekday(), hoje.isoweekday())
print(hoje.year, hoje.month, reuniao.hour)
print(hoje.isocalendar().week, "ª semana do ano")
