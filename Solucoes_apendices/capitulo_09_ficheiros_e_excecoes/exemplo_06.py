# Capítulo 9 — Ficheiros e exceções
# Secção: Exceções: quando algo corre mal

def ler_inteiro(texto):
    try:
        return int(texto)
    except ValueError:
        print(f"'{texto}' não é um número inteiro.")
        return None

print(ler_inteiro("42"))
print(ler_inteiro("quarenta"))
