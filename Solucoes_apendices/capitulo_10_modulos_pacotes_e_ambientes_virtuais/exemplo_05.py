# Capítulo 10 — Módulos, pacotes e ambientes virtuais
# Secção: A biblioteca padrão

import statistics, secrets, hashlib, random
from datetime import date

notas = [12, 15, 17, 9, 14, 15]
print(statistics.mean(notas), statistics.median(notas),
      round(statistics.stdev(notas), 2))
print(len(secrets.token_hex(16)))        # token seguro
print(hashlib.sha256(b"python").hexdigest()[:16])
print(random.choice(["pedra", "papel", "tesoura"]))
print((date(2026, 12, 25) - date(2026, 11, 7)).days, "dias até ao Natal")
