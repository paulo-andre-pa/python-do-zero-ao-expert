# Capítulo 13 — Iteradores, geradores e compreensões
# Secção: Geradores

vendas = [120, 80, 300, 45, 210]
print(sum(v for v in vendas if v > 100))
print(max((v, i) for i, v in enumerate(vendas)))   # valor e posição
print(any(v > 250 for v in vendas), all(v > 0 for v in vendas))
