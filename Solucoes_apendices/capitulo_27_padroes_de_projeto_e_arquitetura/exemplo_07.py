# Capítulo 27 — Padrões de projeto e arquitetura
# Secção: Repository e Unit of Work

from typing import Protocol

class RepositorioClientes(Protocol):
    def obter(self, id_: int) -> dict | None: ...
    def guardar(self, cliente: dict) -> None: ...

class ClientesEmMemoria:
    def __init__(self):
        self._dados: dict[int, dict] = {}
    def obter(self, id_):
        return self._dados.get(id_)
    def guardar(self, cliente):
        self._dados[cliente["id"]] = cliente

def promover_a_vip(repo: RepositorioClientes, id_: int) -> dict:
    cliente = repo.obter(id_)
    if cliente is None:
        raise LookupError(f"cliente {id_} inexistente")
    cliente = {**cliente, "vip": True}
    repo.guardar(cliente)
    return cliente

repo = ClientesEmMemoria()
repo.guardar({"id": 1, "nome": "Lúcia", "vip": False})
print(promover_a_vip(repo, 1))
