"""Arranque: python -m reservas.servidor"""
from wsgiref.simple_server import make_server
from reservas.api import criar_app
from reservas.repositorio import Repositorio

def preparar(caminho: str = "reservas.db") -> Repositorio:
    repo = Repositorio(caminho)
    if not repo.salas():
        for nome, cap in [("Lisboa", 4), ("Porto", 6), ("Coimbra", 8),
                          ("Braga", 12), ("Faro", 20), ("Auditório", 60)]:
            repo.criar_sala(nome, cap)
    return repo

if __name__ == "__main__":
    with make_server("127.0.0.1", 8000, criar_app(preparar())) as srv:
        print("API em http://127.0.0.1:8000")
        srv.serve_forever()
