# Capítulo 26 — Python idiomático: boas práticas e armadilhas
# Secção: Erros e recursos

def ler_porta(texto):
    try:
        porta = int(texto)
    except ValueError:
        raise ValueError(f"porta inválida: {texto!r}") from None
    if not 1 <= porta <= 65535:
        raise ValueError(f"porta fora do intervalo: {porta}")
    return porta

for t in ["8080", "http", "70000"]:
    try:
        print(ler_porta(t))
    except ValueError as e:
        print("Erro:", e)
