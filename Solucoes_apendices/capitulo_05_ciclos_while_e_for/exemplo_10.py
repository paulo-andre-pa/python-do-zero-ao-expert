# Capítulo 5 — Ciclos: while e for
# Secção: Controlar o ciclo: break, continue e else

def primeiro_divisor(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            print(f"{n} não é primo (divisível por {d})")
            break
    else:
        print(f"{n} é primo")

primeiro_divisor(91)
primeiro_divisor(97)
