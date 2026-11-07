# Capítulo 17 — Expressões regulares, datas e outras ferramentas essenciais
# Secção: Datas e horas

from datetime import datetime
from zoneinfo import ZoneInfo

reuniao_utc = datetime(2026, 7, 15, 13, 0, tzinfo=ZoneInfo("UTC"))
for cidade in ["Europe/Lisbon", "Africa/Luanda", "America/Sao_Paulo",
               "Africa/Maputo"]:
    local = reuniao_utc.astimezone(ZoneInfo(cidade))
    print(f"{cidade:<18}{local:%H:%M}  (UTC{local:%z})")
