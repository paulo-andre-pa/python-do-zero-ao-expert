from datetime import datetime as dt
import pytest
from reservas.regras import Intervalo, ReservaInvalida, validar

SEG = "2026-06-01"          # uma segunda-feira

def iv(a, b, dia=SEG):
    return Intervalo(dt.fromisoformat(f"{dia}T{a}"),
                     dt.fromisoformat(f"{dia}T{b}"))

@pytest.mark.parametrize("a, b, esperado", [
    (("09:00", "10:00"), ("10:00", "11:00"), False),   # consecutivas
    (("09:00", "10:30"), ("10:00", "11:00"), True),
    (("09:00", "12:00"), ("10:00", "11:00"), True),    # contida
], ids=["consecutivas", "parcial", "contida"])
def test_n4_sobreposicao(a, b, esperado):
    assert iv(*a).sobrepoe(iv(*b)) is esperado
    assert iv(*b).sobrepoe(iv(*a)) is esperado         # simétrica

@pytest.mark.parametrize("intervalo, pessoas, mensagem", [
    (iv("10:00", "09:00"), 2, "posterior"),
    (iv("10:00", "11:00", "2026-06-06"), 2, "dias úteis"),
    (iv("07:30", "09:00"), 2, "horário"),
    (iv("09:00", "13:30"), 2, "4 horas"),
    (iv("09:00", "10:00"), 9, "entre 1 e 8"),
], ids=["N1-fim", "N2-sabado", "N2-horario", "N2-duracao", "N3-lotacao"])
def test_n1_n2_n3_invalidas(intervalo, pessoas, mensagem):
    with pytest.raises(ReservaInvalida, match=mensagem):
        validar(intervalo, pessoas, capacidade=8)
