# Capítulo 7 — Dicionários e conjuntos
# Secção: Conjuntos

crm = {"C001", "C002", "C003", "C005"}
faturacao = {"C001", "C003", "C004", "C005"}
print("Sem faturação:", sorted(crm - faturacao))
print("Sem ficha CRM:", sorted(faturacao - crm))
