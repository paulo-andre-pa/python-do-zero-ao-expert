# Capítulo 7 — Dicionários e conjuntos
# Secção: Dicionários aninhados: modelar o mundo real

encomenda = {
    "id": 10452,
    "cliente": {"nome": "Sofia Mendes", "email": "sofia@exemplo.pt"},
    "linhas": [
        {"produto": "Livro Python", "qtd": 1, "preco": 34.90},
        {"produto": "Caneca", "qtd": 2, "preco": 8.50},
    ],
    "pago": True,
}
print(encomenda["cliente"]["nome"])
total = sum(l["qtd"] * l["preco"] for l in encomenda["linhas"])
print(f"Encomenda {encomenda['id']}: {total:.2f} €")
