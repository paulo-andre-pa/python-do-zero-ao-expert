import pytest
from triagem.servico import Triagem

class ClassificadorFalso:
    """Devolve sempre as mesmas probabilidades (definidas pelo teste)."""
    classes_ = ["conta", "entregas", "faturacao", "tecnico"]
    def __init__(self, probs):
        self.probs = probs
    def predict_proba(self, textos):
        return [self.probs]

def test_encaminha_para_a_equipa_da_categoria():
    falso = ClassificadorFalso([0.05, 0.05, 0.85, 0.05])
    d = Triagem(falso).classificar("x")
    assert d.categoria == "faturacao"
    assert (d.equipa, d.manual) == ("Faturação", False)

def test_baixa_confianca_vai_para_triagem_manual():
    d = Triagem(ClassificadorFalso([0.3, 0.2, 0.25, 0.25])).classificar("x")
    assert d.manual and d.equipa == "Triagem manual"

@pytest.mark.parametrize("texto, urgente", [
    ("Estou SEM INTERNET DESDE sábado", True),
    ("vou mudar de operador", True),
    ("não funciona nada lá em casa", True),
    ("se não resolverem vou cancelar o contrato", True),
    ("vou apresentar queixa na DECO", True),
    ("a internet está lenta à noite", False),
    ("quero cancelar a encomenda de um cabo", False),
], ids=["sem-servico", "operador", "nada-funciona", "cancelar-contrato",
        "deco", "lenta", "cancelar-encomenda"])
def test_regras_de_urgencia(texto, urgente):
    d = Triagem(ClassificadorFalso([0.1, 0.1, 0.1, 0.7])).classificar(texto)
    assert d.urgente is urgente
    assert (d.prazo_horas <= 2) is urgente

def test_validacoes():
    with pytest.raises(ValueError):
        Triagem(ClassificadorFalso([1, 0, 0, 0]), limiar=1.5)
    with pytest.raises(ValueError):
        Triagem(ClassificadorFalso([1, 0, 0, 0])).classificar("   ")
