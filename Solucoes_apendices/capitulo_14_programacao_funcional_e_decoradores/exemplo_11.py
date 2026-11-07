# Capítulo 14 — Programação funcional e decoradores
# Secção: Decoradores

import functools

def repetir(tentativas=3, excecoes=(ConnectionError,)):
    def decorador(func):
        @functools.wraps(func)
        def envolvente(*args, **kwargs):
            for n in range(1, tentativas + 1):
                try:
                    return func(*args, **kwargs)
                except excecoes as e:
                    print(f"tentativa {n} falhou: {e}")
                    if n == tentativas:
                        raise
        return envolvente
    return decorador

chamadas = {"n": 0}

@repetir(tentativas=4)
def obter_cotacao():
    chamadas["n"] += 1
    if chamadas["n"] < 3:
        raise ConnectionError("servidor indisponível")
    return 1.0842

print("cotação:", obter_cotacao())
