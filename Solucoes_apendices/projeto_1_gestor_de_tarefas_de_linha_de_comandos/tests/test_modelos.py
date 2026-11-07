from datetime import date
import pytest
from tarefas.modelos import Prioridade, Tarefa

def test_titulo_vazio_e_recusado():
    with pytest.raises(ValueError):
        Tarefa("   ")

def test_etiquetas_normalizadas_e_sem_repetidos():
    t = Tarefa("x", etiquetas=["Web", " web", "", "Cliente"])
    assert t.etiquetas == ["cliente", "web"]

@pytest.mark.parametrize("texto, esperado", [
    ("alta", Prioridade.ALTA), ("Média", Prioridade.MEDIA),
    ("BAIXA", Prioridade.BAIXA)], ids=["simples", "acento", "maiusculas"])
def test_prioridade_de_texto(texto, esperado):
    assert Prioridade.de_texto(texto) is esperado

def test_atrasada_so_se_pendente_e_prazo_passado():
    hoje = date(2026, 5, 10)
    assert Tarefa("a", prazo=date(2026, 5, 9)).atrasada(hoje)
    assert not Tarefa("b", prazo=date(2026, 5, 10)).atrasada(hoje)
    assert not Tarefa("c", prazo=date(2026, 5, 1),
                      concluida=True).atrasada(hoje)
