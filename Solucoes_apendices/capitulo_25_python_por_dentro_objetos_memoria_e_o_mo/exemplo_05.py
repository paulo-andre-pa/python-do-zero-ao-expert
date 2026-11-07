# Capítulo 25 — Python por dentro: objetos, memória e o modelo de dados
# Secção: Mutabilidade e passagem de argumentos
# Este exemplo termina, de propósito, com uma exceção.

t = (1, [2, 3])
t[1].append(4)       # funciona: altera a lista, não o tuplo
print(t)
t[1] += [5]          # erro... mas a lista é alterada antes do erro!
