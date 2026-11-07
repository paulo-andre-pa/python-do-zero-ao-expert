# Capítulo 8 — Funções
# Secção: Funções são objetos

def dobro(x):
    return 2 * x

def quadrado(x):
    return x * x

def aplicar(funcao, valores):
    return [funcao(v) for v in valores]

print(aplicar(dobro, [1, 2, 3]))
print(aplicar(quadrado, [1, 2, 3]))

operacoes = {"+": lambda a, b: a + b, "*": lambda a, b: a * b}
print(operacoes["*"](6, 7))
