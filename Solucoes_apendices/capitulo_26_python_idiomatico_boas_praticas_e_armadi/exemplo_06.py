# Capítulo 26 — Python idiomático: boas práticas e armadilhas
# Secção: Coleções

ponto = (3, 4)
x, y = ponto                          # em vez de ponto[0], ponto[1]
primeiro, *meio, ultimo = range(6)
nome, _, dominio = "ana@empresa.pt".partition("@")
print(x, y, primeiro, meio, ultimo, nome, dominio)
