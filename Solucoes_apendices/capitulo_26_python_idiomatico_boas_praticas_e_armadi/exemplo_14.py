# Capítulo 26 — Python idiomático: boas práticas e armadilhas
# Secção: Armadilhas famosas

lista_compras = ["pão", "leite"]
# list = ["pão"]    <- a partir daqui, list() deixaria de funcionar
total = len(lista_compras)  # evite nomes como list, dict, str, sum
print(total)
