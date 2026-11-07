# Capítulo 15 — Testes automatizados com pytest
# Secção: Fixtures
# Exemplo ilustrativo: pode exigir pacotes ou serviços externos.

@pytest.fixture
def base_de_dados():
    ligacao = sqlite3.connect(":memory:")
    criar_tabelas(ligacao)
    yield ligacao          # o teste corre aqui
    ligacao.close()        # limpeza
