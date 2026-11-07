# Capítulo 19 — Metaprogramação: gestores de contexto, descritores e metaclasses
# Secção: Gestores de contexto

import time

class Cronometro:
    def __init__(self, etiqueta):
        self.etiqueta = etiqueta

    def __enter__(self):
        self.inicio = time.perf_counter()
        return self                      # valor associado a "as"

    def __exit__(self, tipo_exc, exc, traceback):
        self.duracao = time.perf_counter() - self.inicio
        estado = "falhou" if tipo_exc else "ok"
        print(f"[{self.etiqueta}] {estado}")
        return False                     # não suprime exceções

with Cronometro("soma") as c:
    total = sum(range(1_000_000))
print(total, c.duracao > 0)

try:
    with Cronometro("divisão"):
        1 / 0
except ZeroDivisionError:
    print("exceção propagada normalmente")
