# Capítulo 17 — Expressões regulares, datas e outras ferramentas essenciais
# Secção: Datas e horas

from datetime import datetime

d = datetime(2026, 11, 7, 14, 30)
print(d.strftime("%d/%m/%Y %H:%M"))
print(d.isoformat())
print(datetime.strptime("25/12/2026 18:00", "%d/%m/%Y %H:%M"))
print(datetime.fromisoformat("2026-03-15T09:00:00"))
