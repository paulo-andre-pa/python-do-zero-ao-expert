# Capítulo 2 — Variáveis, tipos e operadores
# Secção: Constantes e o módulo math
# Este exemplo pede dados ao utilizador.

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / altura ** 2
print(f"IMC: {imc:.1f}")
print("Peso dentro do intervalo de referência:", 18.5 <= imc < 25)
