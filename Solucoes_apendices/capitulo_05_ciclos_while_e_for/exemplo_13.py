# Capítulo 5 — Ciclos: while e for
# Secção: Padrões clássicos
# Este exemplo pede dados ao utilizador.

import random

secreto = random.randint(1, 100)
for tentativa in range(1, 8):
    palpite = int(input(f"Tentativa {tentativa}/7: "))
    if palpite == secreto:
        print(f"Acertou em {tentativa} tentativas!")
        break
    print("Maior!" if secreto > palpite else "Menor!")
else:
    print(f"Perdeu. O número era {secreto}.")
