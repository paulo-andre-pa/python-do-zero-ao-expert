import pytest

def nif_valido(nif: str) -> bool:
    if len(nif) != 9 or not nif.isdigit():
        return False
    soma = sum(int(d) * p for d, p in zip(nif, range(9, 1, -1)))
    controlo = 0 if soma % 11 < 2 else 11 - soma % 11
    return controlo == int(nif[8])

@pytest.mark.parametrize("nif, esperado", [
    ("123456789", True),
    ("123456780", False),   # dígito de controlo errado
    ("12345678", False),    # curto demais
    ("12345678A", False),   # não numérico
    ("", False),
])
def test_nif(nif, esperado):
    assert nif_valido(nif) is esperado
