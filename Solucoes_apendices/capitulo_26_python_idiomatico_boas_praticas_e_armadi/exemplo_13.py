# Capítulo 26 — Python idiomático: boas práticas e armadilhas
# Secção: Armadilhas famosas

errado = [[0] * 3] * 3        # três referências para a MESMA lista
errado[0][0] = 9
certo = [[0] * 3 for _ in range(3)]
certo[0][0] = 9
print(errado)
print(certo)
