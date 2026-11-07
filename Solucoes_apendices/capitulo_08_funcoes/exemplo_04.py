# Capítulo 8 — Funções
# Secção: Tipos de argumentos

def preco_final(preco, iva=0.23, desconto=0.0):
    return round(preco * (1 - desconto) * (1 + iva), 2)

print(preco_final(100))
print(preco_final(100, iva=0.06))
print(preco_final(100, desconto=0.1))
