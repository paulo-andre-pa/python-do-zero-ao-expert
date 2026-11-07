# Capítulo 25 — Python por dentro: objetos, memória e o modelo de dados
# Secção: Bytecode: o que o interpretador executa

def segundos_por_dia():
    return 24 * 60 * 60

print(segundos_por_dia.__code__.co_consts)
