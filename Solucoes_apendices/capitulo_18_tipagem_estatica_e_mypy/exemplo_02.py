# Capítulo 18 — Tipagem estática e mypy
# Secção: Anotações básicas

def procurar_email(nome: str, agenda: dict[str, str]) -> str | None:
    return agenda.get(nome)

def normalizar(valor: int | float | str) -> float:
    return float(valor)

email = procurar_email("Ana", {"Ana": "ana@ex.pt"})
if email is not None:          # o verificador exige esta verificação
    print(email.upper())
print(normalizar("3.5"), normalizar(2))
