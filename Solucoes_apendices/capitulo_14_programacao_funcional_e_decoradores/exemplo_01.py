# Capítulo 14 — Programação funcional e decoradores
# Secção: Funções lambda

produtos = [("Rato", 15.0, 40), ("Teclado", 35.0, 12),
            ("Monitor", 189.0, 5), ("Cabo HDMI", 7.5, 120)]

por_preco = sorted(produtos, key=lambda p: p[1])
por_valor_stock = max(produtos, key=lambda p: p[1] * p[2])
print([p[0] for p in por_preco])
print(por_valor_stock[0])
