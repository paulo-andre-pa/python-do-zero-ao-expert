# Capítulo 18 — Tipagem estática e mypy
# Secção: Protocolos: duck typing verificado

from typing import Protocol, runtime_checkable

@runtime_checkable
class Notificavel(Protocol):
    def enviar(self, destino: str, mensagem: str) -> bool: ...

class Email:
    def enviar(self, destino: str, mensagem: str) -> bool:
        print(f"[email] {destino}: {mensagem}")
        return True

class SMS:
    def enviar(self, destino: str, mensagem: str) -> bool:
        print(f"[sms] {destino}: {mensagem[:20]}")
        return True

def alertar_todos(canais: list[Notificavel], msg: str) -> int:
    return sum(c.enviar("equipa", msg) for c in canais)

print(alertar_todos([Email(), SMS()], "Servidor reiniciado com sucesso"))
print(isinstance(SMS(), Notificavel))
