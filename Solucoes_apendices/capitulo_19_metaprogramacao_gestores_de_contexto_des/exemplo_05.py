# Capítulo 19 — Metaprogramação: gestores de contexto, descritores e metaclasses
# Secção: Controlar o acesso a atributos

class Config:
    def __init__(self, dados: dict):
        self._dados = dados

    def __getattr__(self, nome):
        try:
            valor = self._dados[nome]
        except KeyError:
            raise AttributeError(f"configuração sem '{nome}'") from None
        return Config(valor) if isinstance(valor, dict) else valor

cfg = Config({"bd": {"host": "localhost", "porta": 5432}, "debug": True})
print(cfg.bd.host, cfg.bd.porta, cfg.debug)
try:
    cfg.timeout
except AttributeError as e:
    print(e)
