# Capítulo 5 — Ciclos: while e for
# Secção: Padrões clássicos
# Este exemplo pede dados ao utilizador.

total = 0.0
while True:
    print("\n1) Adicionar valor  2) Ver total  0) Sair")
    opcao = input("Opção: ").strip()
    if opcao == "0":
        print("Até breve!")
        break
    elif opcao == "1":
        total += float(input("Valor: "))
    elif opcao == "2":
        print(f"Total acumulado: {total:.2f}")
    else:
        print("Opção inválida.")
