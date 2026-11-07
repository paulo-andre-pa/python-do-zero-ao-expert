# Capítulo 25 — Python por dentro: objetos, memória e o modelo de dados
# Secção: Bytecode: o que o interpretador executa

import dis

def area(largura, altura):
    return largura * altura * 0.5

dis.dis(area)
