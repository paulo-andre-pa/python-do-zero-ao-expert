# Apêndice B — Soluções de exercícios selecionados
# Secção: Capítulo 15 — Testes

def iban_pt_valido(iban: str) -> bool:
    iban = iban.replace(" ", "").upper()
    if len(iban) != 25 or not iban.startswith("PT") \
            or not iban[2:].isdigit():
        return False
    reorganizado = iban[4:] + iban[:4]          # move "PTkk" para o fim
    numerico = "".join(str(int(c, 36)) for c in reorganizado)  # P=25, T=29
    return int(numerico) % 97 == 1

for iban in ["PT50 0002 0123 1234 5678 9015 4",
             "PT50 0002 0123 1234 5678 9015 5", "PT50 123"]:
    print(f"{iban:<33} {iban_pt_valido(iban)}")
