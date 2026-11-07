# Capítulo 16 — Dados persistentes: CSV, JSON e SQLite
# Secção: CSV

from collections import defaultdict

totais = defaultdict(float)
with open("funcionarios.csv", newline="", encoding="utf-8") as f:
    for linha in csv.DictReader(f, delimiter=";"):
        totais[linha["departamento"]] += float(linha["salario"])
        print(f"{linha['nome']:<18} {linha['departamento']}")
print(dict(totais))
