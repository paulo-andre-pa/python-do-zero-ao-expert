# Capítulo 15 — Testes automatizados com pytest
# Secção: Mocks: isolar dependências

from unittest.mock import Mock, patch
from datetime import date

def saudacao_aniversario(cliente, hoje=None):
    hoje = hoje or date.today()
    if (cliente["nascimento"].month, cliente["nascimento"].day) == \
       (hoje.month, hoje.day):
        return f"Parabéns, {cliente['nome']}!"
    return None

cli = {"nome": "Rosa", "nascimento": date(1990, 11, 7)}
msg = saudacao_aniversario(cli, hoje=date(2026, 11, 7))
assert msg == "Parabéns, Rosa!"
assert saudacao_aniversario(cli, hoje=date(2026, 11, 8)) is None

def notificar(cliente, enviar_email):
    msg = saudacao_aniversario(cliente, hoje=date(2026, 11, 7))
    if msg:
        enviar_email(cliente["nome"], msg)

falso_envio = Mock()
notificar(cli, falso_envio)
falso_envio.assert_called_once_with("Rosa", "Parabéns, Rosa!")
print("chamadas registadas:", falso_envio.call_args_list)
