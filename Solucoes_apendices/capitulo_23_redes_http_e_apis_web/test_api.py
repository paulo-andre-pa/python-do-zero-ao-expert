import json, threading, urllib.request, urllib.error
import pytest
import api_tarefas

@pytest.fixture
def base():
    api_tarefas.TAREFAS.clear()
    srv = api_tarefas.criar_servidor(porta=0)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{srv.server_address[1]}"
    srv.shutdown()

def chamar(url, metodo="GET", corpo=None):
    dados = json.dumps(corpo).encode() if corpo is not None else None
    req = urllib.request.Request(url, data=dados, method=metodo)
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code

def test_criar_tarefa(base):
    assert chamar(base + "/tarefas", "POST", {"titulo": "X"}) == 201

def test_titulo_vazio_e_rejeitado(base):
    assert chamar(base + "/tarefas", "POST", {"titulo": ""}) == 400

def test_apagar_inexistente_da_404(base):
    assert chamar(base + "/tarefas/123", "DELETE") == 404
