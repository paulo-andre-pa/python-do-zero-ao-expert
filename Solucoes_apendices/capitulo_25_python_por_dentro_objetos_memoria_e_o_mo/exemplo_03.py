# Capítulo 25 — Python por dentro: objetos, memória e o modelo de dados
# Secção: Tudo é um objeto

a, b = int("256"), int("256")
c, d = int("257"), int("257")
print(a is b, c is d)
print(a == b, c == d)
