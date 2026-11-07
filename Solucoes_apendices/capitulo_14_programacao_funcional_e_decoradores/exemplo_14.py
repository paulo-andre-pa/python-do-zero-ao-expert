# Capítulo 14 — Programação funcional e decoradores
# Secção: singledispatch: funções genéricas

from functools import singledispatch
from datetime import date
from decimal import Decimal

@singledispatch
def formatar(valor):
    return str(valor)

@formatar.register
def _(valor: float):
    return f"{valor:,.2f}".replace(",", " ").replace(".", ",")

@formatar.register
def _(valor: Decimal):
    return formatar(float(valor)) + " €"

@formatar.register
def _(valor: date):
    return valor.strftime("%d/%m/%Y")

for v in [1234567.891, Decimal("99.9"), date(2026, 11, 7), "texto", 42]:
    print(formatar(v))
