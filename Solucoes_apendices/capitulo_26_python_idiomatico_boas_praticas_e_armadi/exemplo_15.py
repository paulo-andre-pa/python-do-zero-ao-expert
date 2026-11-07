# Capítulo 26 — Python idiomático: boas práticas e armadilhas
# Secção: Desempenho sem sacrificar a legibilidade

import re, time

linhas = ["erro: disco cheio", "info: ok", "erro: rede"] * 20_000

t = time.perf_counter()
n1 = sum(1 for l in linhas if re.compile(r"^erro:").match(l))
t1 = time.perf_counter() - t

padrao = re.compile(r"^erro:")              # compilado uma só vez
t = time.perf_counter()
n2 = sum(1 for l in linhas if padrao.match(l))
t2 = time.perf_counter() - t

t = time.perf_counter()
n3 = sum(1 for l in linhas if l.startswith("erro:"))  # sem regex
t3 = time.perf_counter() - t
print(n1 == n2 == n3,
      f"{t1 / t3:.0f}x e {t2 / t3:.0f}x mais lento que startswith")
