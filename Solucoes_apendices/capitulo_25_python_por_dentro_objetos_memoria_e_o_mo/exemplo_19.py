# Capítulo 25 — Python por dentro: objetos, memória e o modelo de dados
# Secção: Âmbitos e *closures* por dentro

funcoes = [lambda: i for i in range(3)]
print([f() for f in funcoes])          # todas veem i = 2

funcoes = [lambda i=i: i for i in range(3)]
print([f() for f in funcoes])          # valor por omissão captura cada i
