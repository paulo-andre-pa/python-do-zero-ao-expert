# Capítulo 8 — Funções
# Secção: Decompor problemas

def digito_controlo(oito_digitos: str) -> int:
    soma = sum(int(d) * peso
               for d, peso in zip(oito_digitos, range(9, 1, -1)))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def nif_valido(nif: str) -> bool:
    nif = nif.replace(" ", "")
    if len(nif) != 9 or not nif.isdigit():
        return False
    return digito_controlo(nif[:8]) == int(nif[8])

for n in ["123456789", "123 456 780", "12345", "999999990"]:
    print(f"{n:<12} {'válido' if nif_valido(n) else 'inválido'}")
