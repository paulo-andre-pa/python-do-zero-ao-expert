# Capítulo 3 — Texto: trabalhar com strings
# Secção: Formatação avançada com f-strings

produtos = [("Teclado", 2, 24.9), ("Rato sem fios", 1, 15.0),
            ("Monitor 27''", 1, 219.99)]
print(f"{'Produto':<16}{'Qtd':>5}{'Preço':>10}")
print("-" * 31)
for nome, qtd, preco in produtos:
    print(f"{nome:<16}{qtd:>5}{preco:>10.2f}")
print(f"{'FIM':^31}")
