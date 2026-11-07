# Capítulo 25 — Python por dentro: objetos, memória e o modelo de dados
# Secção: Mutabilidade e passagem de argumentos

def acrescentar(lista):
    lista.append(99)          # altera o objeto partilhado

def substituir(lista):
    lista = [0, 0, 0]         # só muda o nome local

dados = [1, 2]
acrescentar(dados)
substituir(dados)
print(dados)
