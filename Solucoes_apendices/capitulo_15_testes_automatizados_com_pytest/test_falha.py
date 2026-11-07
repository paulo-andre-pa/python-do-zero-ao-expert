from precos_errado import aplicar_desconto

def test_desconto():
    assert aplicar_desconto(80, 25) == 60.0
