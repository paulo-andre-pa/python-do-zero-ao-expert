# Capítulo 5 — Ciclos: while e for
# Secção: Padrões clássicos

vendas = [120.5, 89.0, 230.0, 45.9, 310.2, 99.9]

# Acumulador: somar
total = 0
for v in vendas:
    total += v

# Contador: contar os que cumprem uma condição
acima_100 = 0
for v in vendas:
    if v > 100:
        acima_100 += 1

# Máximo: guardar o melhor até agora
maior = vendas[0]
for v in vendas[1:]:
    if v > maior:
        maior = v

print(f"Total: {total:.2f} | >100: {acima_100} | Máximo: {maior}")
# As funções embutidas fazem o mesmo de forma mais concisa:
print(sum(vendas), sum(1 for v in vendas if v > 100), max(vendas))
