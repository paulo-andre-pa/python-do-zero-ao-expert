# Capítulo 3 — Texto: trabalhar com strings
# Secção: Unicode e codificação

print(ord("A"), ord("é"), chr(8364))
texto = "Olá"
dados = texto.encode("utf-8")      # str -> bytes
print(dados, len(texto), len(dados))
print(dados.decode("utf-8"))       # bytes -> str
