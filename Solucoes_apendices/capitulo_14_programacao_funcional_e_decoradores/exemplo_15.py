# Capítulo 14 — Programação funcional e decoradores
# Secção: singledispatch: funções genéricas

import functools, time
from collections import deque

class LimiteExcedido(Exception):
    pass

def limitar(max_chamadas, segundos):
    def decorador(func):
        instantes = deque()
        @functools.wraps(func)
        def envolvente(*args, **kwargs):
            agora = time.monotonic()
            while instantes and agora - instantes[0] > segundos:
                instantes.popleft()
            if len(instantes) >= max_chamadas:
                raise LimiteExcedido(
                    f"máximo de {max_chamadas} chamadas em {segundos}s")
            instantes.append(agora)
            return func(*args, **kwargs)
        return envolvente
    return decorador

@limitar(3, 1.0)
def consultar_api(n):
    return f"resposta {n}"

for i in range(1, 6):
    try:
        print(consultar_api(i))
    except LimiteExcedido as e:
        print(f"pedido {i} recusado: {e}")
