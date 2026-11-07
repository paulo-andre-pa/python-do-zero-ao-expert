# Capítulo 25 — Python por dentro: objetos, memória e o modelo de dados
# Secção: Âmbitos e *closures* por dentro

def contador():
    total = 0
    def incrementar():
        nonlocal total
        total += 1
        return total
    return incrementar

c = contador()
c(); c()
print(c.__code__.co_freevars, c.__closure__[0].cell_contents)
