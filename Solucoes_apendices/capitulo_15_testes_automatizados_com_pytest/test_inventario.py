import pytest

class Inventario:
    def __init__(self):
        self.stock = {}
    def entrada(self, produto, qtd):
        self.stock[produto] = self.stock.get(produto, 0) + qtd
    def saida(self, produto, qtd):
        if self.stock.get(produto, 0) < qtd:
            raise ValueError("stock insuficiente")
        self.stock[produto] -= qtd

@pytest.fixture
def inventario():
    inv = Inventario()
    inv.entrada("parafuso", 100)
    return inv

def test_saida_reduz_stock(inventario):
    inventario.saida("parafuso", 30)
    assert inventario.stock["parafuso"] == 70

def test_saida_sem_stock_falha(inventario):
    with pytest.raises(ValueError):
        inventario.saida("parafuso", 101)

def test_ficheiro_de_exportacao(inventario, tmp_path):
    destino = tmp_path / "stock.csv"
    destino.write_text("\n".join(f"{p};{q}" for p, q
                                 in inventario.stock.items()))
    assert destino.read_text() == "parafuso;100"
