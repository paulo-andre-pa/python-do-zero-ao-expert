# Capítulo 3 — Texto: trabalhar com strings
# Secção: Formatação avançada com f-strings

preco = 1234.5678
print(f"{preco:.2f}")       # 2 casas decimais
print(f"{preco:,.2f}")      # separador de milhares
print(f"{preco:10.1f}|")    # largura 10
print(f"{0.256:.1%}")       # percentagem
print(f"{42:05d}")          # preencher com zeros
print(f"{255:b} {255:x}")   # binário e hexadecimal
