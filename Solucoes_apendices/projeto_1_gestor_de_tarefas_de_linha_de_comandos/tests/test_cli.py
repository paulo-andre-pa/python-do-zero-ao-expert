from datetime import date
from tarefas.cli import main
from tarefas.repositorio import RepositorioTarefas
from tarefas.servicos import GestorTarefas

def novo_gestor():
    hoje = date(2026, 5, 10)
    return GestorTarefas(RepositorioTarefas(), hoje=lambda: hoje)

def test_adicionar_e_listar(capsys):
    g = novo_gestor()
    assert main(["add", "Enviar proposta", "-p", "alta"], g) == 0
    assert main(["ls"], g) == 0
    assert "Enviar proposta" in capsys.readouterr().out

def test_erro_devolve_codigo_1(capsys):
    assert main(["feito", "42"], novo_gestor()) == 1
    assert "não existe a tarefa" in capsys.readouterr().err
