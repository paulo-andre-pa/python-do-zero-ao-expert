# Capítulo 9 — Ficheiros e exceções
# Secção: EAFP versus LBYL

dados = {"nome": "Ana"}

# LBYL
if "idade" in dados:
    idade = dados["idade"]
else:
    idade = 0

# EAFP
try:
    idade = dados["idade"]
except KeyError:
    idade = 0
print(idade)
