# Capítulo 16 — Dados persistentes: CSV, JSON e SQLite
# Secção: CSV

import csv

campos = ["numero", "nome", "departamento", "salario"]
dados = [(101, "Ana Martins", "TI", 2150),
         (102, "Rui Sá", "Vendas", 1720),
         (103, 'Eva "Lia" Costa', "TI", 2480)]
funcionarios = [dict(zip(campos, d)) for d in dados]
with open("funcionarios.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.DictWriter(f, fieldnames=funcionarios[0].keys(),
                              delimiter=";")
    escritor.writeheader()
    escritor.writerows(funcionarios)

print(open("funcionarios.csv", encoding="utf-8").read())
