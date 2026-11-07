# Capítulo 7 — Dicionários e conjuntos
# Secção: Dicionários: dados por chave

stock = {"maçã": 40, "pera": 0}
print("banana" in stock)
print(stock.get("banana"))          # None
print(stock.get("banana", 0))       # valor por omissão
