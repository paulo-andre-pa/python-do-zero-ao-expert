# Capítulo 13 — Iteradores, geradores e compreensões
# Secção: O protocolo de iteração

nomes = ["Ana", "Rui", "Eva"]
it = iter(nomes)
print(next(it))
print(next(it))
print(next(it))
try:
    next(it)
except StopIteration:
    print("Iterador esgotado")
