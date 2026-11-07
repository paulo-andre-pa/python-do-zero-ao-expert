from datetime import date
import pytest
from tarefas.repositorio import RepositorioTarefas
from tarefas.servicos import GestorTarefas, TarefaInexistente

HOJE = date(2026, 5, 10)

@pytest.fixture
def gestor():
    return GestorTarefas(RepositorioTarefas(":memory:"), hoje=lambda: HOJE)

@pytest.mark.parametrize("texto, esperado", [
    ("hoje", date(2026, 5, 10)), ("amanha", date(2026, 5, 11)),
    ("+7", date(2026, 5, 17)), ("2026-12-01", date(2026, 12, 1)),
    (None, None)])
def test_prazos(gestor, texto, esperado):
    assert gestor.interpretar_prazo(texto) == esperado

def test_prazo_invalido(gestor):
    with pytest.raises(ValueError, match="prazo inválido"):
        gestor.interpretar_prazo("próxima semana")

def test_ordem_por_prioridade_e_prazo(gestor):
    gestor.adicionar("baixa", "baixa", "+1")
    gestor.adicionar("alta tarde", "alta", "+9")
    gestor.adicionar("alta cedo", "alta", "+2")
    assert [t.titulo for t in gestor.listar()] == \
        ["alta cedo", "alta tarde", "baixa"]

def test_concluir_e_estatisticas(gestor):
    t = gestor.adicionar("relatório", prazo="2026-05-01")
    gestor.adicionar("reunião", "alta")
    assert gestor.estatisticas()["atrasadas"] == 1
    gestor.concluir(t.id)
    stats = gestor.estatisticas()
    assert stats["concluidas"] == 1 and stats["atrasadas"] == 0

def test_concluir_inexistente(gestor):
    with pytest.raises(TarefaInexistente):
        gestor.concluir(99)
