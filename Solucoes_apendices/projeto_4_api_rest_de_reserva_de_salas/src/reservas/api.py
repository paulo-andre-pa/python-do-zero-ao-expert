"""Rotas da API de reservas."""
from datetime import date, datetime

from reservas.regras import Intervalo, ReservaInvalida, validar
from reservas.repositorio import Repositorio
from reservas.web import App, ErroHTTP

def _data_hora(texto: str | None, campo: str) -> datetime:
    try:
        return datetime.fromisoformat(str(texto))
    except ValueError:
        raise ErroHTTP(400, f"'{campo}': use AAAA-MM-DDTHH:MM") from None

def criar_app(repo: Repositorio) -> App:
    app = App()

    @app.rota("GET", "/salas")
    def listar_salas(pedido):
        return 200, repo.salas()

    @app.rota("GET", "/salas/{sala_id}/reservas")
    def reservas_da_sala(pedido, sala_id):
        if repo.sala(sala_id) is None:
            raise ErroHTTP(404, "sala inexistente")
        try:
            dia = date.fromisoformat(pedido.query.get("dia", ""))
        except ValueError:
            raise ErroHTTP(400, "indique ?dia=AAAA-MM-DD") from None
        return 200, repo.reservas_do_dia(sala_id, dia)

    @app.rota("GET", "/disponiveis")
    def disponiveis(pedido):
        q = pedido.query
        inicio = _data_hora(q.get("inicio"), "inicio")
        fim = _data_hora(q.get("fim"), "fim")
        pessoas = int(q.get("pessoas", "1"))
        ocupadas = repo.ocupadas(inicio, fim)
        return 200, [s for s in repo.salas()
                     if s["capacidade"] >= pessoas
                     and s["id"] not in ocupadas]

    @app.rota("POST", "/reservas")
    def criar_reserva(pedido):
        d = pedido.json()
        sala = repo.sala(int(d.get("sala_id", 0)))
        if sala is None:
            raise ErroHTTP(404, "sala inexistente")
        if not str(d.get("responsavel", "")).strip():
            raise ErroHTTP(400, "o responsável é obrigatório")
        intervalo = Intervalo(_data_hora(d.get("inicio"), "inicio"),
                              _data_hora(d.get("fim"), "fim"))
        participantes = int(d.get("participantes", 1))
        try:
            validar(intervalo, participantes, sala["capacidade"])
        except ReservaInvalida as e:
            raise ErroHTTP(400, str(e)) from None
        if sala["id"] in repo.ocupadas(intervalo.inicio, intervalo.fim):
            raise ErroHTTP(409, "a sala já está reservada nesse intervalo")
        novo_id = repo.criar_reserva(sala["id"], d["responsavel"].strip(),
                                     participantes, intervalo.inicio,
                                     intervalo.fim)
        return 201, {"id": novo_id, **d}

    @app.rota("DELETE", "/reservas/{reserva_id}")
    def cancelar(pedido, reserva_id):
        if not repo.apagar_reserva(reserva_id):
            raise ErroHTTP(404, "reserva inexistente")
        return 204, None

    return app
