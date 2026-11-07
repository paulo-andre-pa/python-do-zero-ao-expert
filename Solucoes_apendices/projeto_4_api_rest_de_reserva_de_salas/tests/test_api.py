import pytest
from cliente import Cliente
from reservas.api import criar_app
from reservas.servidor import preparar

@pytest.fixture
def api():
    return Cliente(criar_app(preparar(":memory:")))

def reserva(sala=2, inicio="2026-06-01T09:00", fim="2026-06-01T10:00",
            pessoas=4):
    return {"sala_id": sala, "responsavel": "Equipa A",
            "participantes": pessoas, "inicio": inicio, "fim": fim}

def test_listar_salas(api):
    codigo, salas = api.pedido("GET", "/salas")
    assert codigo == 200 and len(salas) == 6

def test_criar_e_conflito(api):
    assert api.pedido("POST", "/reservas", reserva())[0] == 201
    codigo, corpo = api.pedido("POST", "/reservas", reserva(
        inicio="2026-06-01T09:30", fim="2026-06-01T11:00"))
    assert codigo == 409 and "reservada" in corpo["erro"]

def test_dados_invalidos(api):
    assert api.pedido("POST", "/reservas", reserva(pessoas=50))[0] == 400
    assert api.pedido("POST", "/reservas", reserva(sala=99))[0] == 404

def test_n5_disponiveis_por_capacidade(api):
    api.pedido("POST", "/reservas", reserva(sala=3))   # Coimbra, 8 lugares
    _, livres = api.pedido("GET", "/disponiveis?inicio=2026-06-01T09:00"
                                  "&fim=2026-06-01T10:00&pessoas=7")
    assert [s["nome"] for s in livres] == ["Braga", "Faro", "Auditório"]

def test_cancelar(api):
    _, r = api.pedido("POST", "/reservas", reserva())
    assert api.pedido("DELETE", f"/reservas/{r['id']}")[0] == 204
    assert api.pedido("DELETE", f"/reservas/{r['id']}")[0] == 404

def test_rotas_e_metodos(api):
    assert api.pedido("GET", "/inexistente")[0] == 404
    assert api.pedido("PUT", "/salas")[0] == 405
