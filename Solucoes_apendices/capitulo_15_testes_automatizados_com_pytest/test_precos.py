import pytest
from precos import preco_com_iva, aplicar_desconto

def test_iva_normal():
    assert preco_com_iva(100) == 123.0

def test_iva_reduzido():
    assert preco_com_iva(100, taxa=0.06) == 106.0

def test_preco_zero():
    assert preco_com_iva(0) == 0

def test_preco_negativo_lanca_erro():
    with pytest.raises(ValueError, match="negativo"):
        preco_com_iva(-1)

def test_desconto():
    assert aplicar_desconto(80, 25) == 60.0
