# Capítulo 5 — Ciclos: while e for
# Secção: O ciclo while
# Este exemplo pede dados ao utilizador.

while True:
    texto = input("Idade (0-120): ")
    if texto.isdigit() and 0 <= int(texto) <= 120:
        idade = int(texto)
        break
    print("Valor inválido, tente de novo.")
print("Idade registada:", idade)
