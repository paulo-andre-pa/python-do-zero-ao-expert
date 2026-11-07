import pytest
from app import criar_app

@pytest.fixture
def cliente(tmp_path):
    app = criar_app({"TESTING": True, "BASE_DADOS": str(tmp_path / "t.db"),
                     "SECRET_KEY": "teste"})
    return app.test_client()

def entrar(cliente, nome="ana", senha="segura123"):
    cliente.post("/auth/registar", data={"nome": nome, "senha": senha})
    return cliente.post("/auth/entrar", data={"nome": nome, "senha": senha})

def test_pagina_inicial_exige_sessao(cliente):
    r = cliente.get("/")
    assert r.status_code == 302 and "/auth/entrar" in r.location

def test_palavra_passe_curta_e_recusada(cliente):
    r = cliente.post("/auth/registar", data={"nome": "rui", "senha": "123"})
    assert "pelo menos 8" in r.get_data(as_text=True)

def test_criar_e_listar_tarefas(cliente):
    entrar(cliente)
    cliente.post("/nova", data={"titulo": "Pagar a luz"})
    assert "Pagar a luz" in cliente.get("/").get_data(as_text=True)

def test_senha_errada(cliente):
    entrar(cliente)
    cliente.get("/auth/sair")
    dados = {"nome": "ana", "senha": "errada!!"}
    r = cliente.post("/auth/entrar", data=dados)
    assert "incorretos" in r.get_data(as_text=True)

def test_nao_pode_concluir_tarefas_de_outros(cliente):
    entrar(cliente, "ana")
    cliente.post("/nova", data={"titulo": "privada"})
    cliente.get("/auth/sair")
    entrar(cliente, "eva")
    assert cliente.post("/1/feita").status_code == 404
