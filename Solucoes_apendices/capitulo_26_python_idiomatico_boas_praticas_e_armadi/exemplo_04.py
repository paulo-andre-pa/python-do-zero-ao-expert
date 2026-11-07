# Capítulo 26 — Python idiomático: boas práticas e armadilhas
# Secção: Iteração

numeros = [1, 2, 2, 3, 2, 4]

# errado: salta elementos, porque os índices mudam durante a remoção
errado = numeros.copy()
for n in errado:
    if n == 2:
        errado.remove(n)

# certo: construir uma nova lista
certo = [n for n in numeros if n != 2]
print(errado, certo)
