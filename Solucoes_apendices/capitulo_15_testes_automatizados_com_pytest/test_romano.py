import pytest
from romano import para_romano

@pytest.mark.parametrize("n, esperado", [
    (1, "I"), (4, "IV"), (9, "IX"), (14, "XIV"), (40, "XL"),
    (90, "XC"), (400, "CD"), (1994, "MCMXCIV"), (2026, "MMXXVI"),
])
def test_conversao(n, esperado):
    assert para_romano(n) == esperado

@pytest.mark.parametrize("n", [0, 4000, -5])
def test_fora_do_intervalo(n):
    with pytest.raises(ValueError):
        para_romano(n)
