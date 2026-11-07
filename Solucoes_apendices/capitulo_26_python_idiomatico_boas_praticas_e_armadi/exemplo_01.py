# Capítulo 26 — Python idiomático: boas práticas e armadilhas
# Secção: Iteração

cores = ["vermelho", "verde", "azul"]

# antes
for i in range(len(cores)):
    print(i, cores[i])

# depois
for i, cor in enumerate(cores):
    print(i, cor)
