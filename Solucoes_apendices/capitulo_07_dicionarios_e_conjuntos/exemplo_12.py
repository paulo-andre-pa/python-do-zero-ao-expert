# Capítulo 7 — Dicionários e conjuntos
# Secção: Contar e agrupar

from collections import defaultdict

funcionarios = [("Ana", "TI"), ("Rui", "Vendas"), ("Eva", "TI"),
                ("Tó", "RH"), ("Lia", "Vendas")]
por_departamento = defaultdict(list)
for nome, dep in funcionarios:
    por_departamento[dep].append(nome)
for dep, nomes in sorted(por_departamento.items()):
    print(f"{dep:<7}: {', '.join(nomes)}")
