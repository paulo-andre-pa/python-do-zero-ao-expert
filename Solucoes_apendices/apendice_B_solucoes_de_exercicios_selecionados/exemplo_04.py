# Apêndice B — Soluções de exercícios selecionados
# Secção: Capítulo 3 — Strings

def cesar(texto: str, k: int) -> str:
    resultado = []
    for c in texto:
        if c.isascii() and c.isalpha():
            base = ord("A") if c.isupper() else ord("a")
            resultado.append(chr((ord(c) - base + k) % 26 + base))
        else:
            resultado.append(c)
    return "".join(resultado)

cifrado = cesar("Ataque ao amanhecer!", 3)
print(cifrado, "|", cesar(cifrado, -3))
