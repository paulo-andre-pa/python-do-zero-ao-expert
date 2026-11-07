# Capítulo 15 — Testes automatizados com pytest
# Secção: Organizar bons testes
# Exemplo ilustrativo: pode exigir pacotes ou serviços externos.

def test_carrinho_com_mais_de_50_euros_nao_paga_portes():
    # Arrange
    carrinho = Carrinho()
    carrinho.adicionar("Casaco", 60.0)
    # Act
    portes = carrinho.portes
    # Assert
    assert portes == 0
