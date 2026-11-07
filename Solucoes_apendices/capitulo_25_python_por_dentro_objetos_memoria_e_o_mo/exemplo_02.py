# Capítulo 25 — Python por dentro: objetos, memória e o modelo de dados
# Secção: Tudo é um objeto

a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b, a is b)    # valores iguais, objetos diferentes
print(a == c, a is c)    # o mesmo objeto
