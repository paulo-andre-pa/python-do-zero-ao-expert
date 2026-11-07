# Capítulo 22 — Engenharia de software em Python
# Secção: Configuração e segredos

import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Configuracao:
    url_bd: str
    nivel_log: str
    modo_debug: bool
    chave_api: str

    @classmethod
    def do_ambiente(cls) -> "Configuracao":
        chave = os.environ.get("APP_CHAVE_API")
        if not chave:
            raise RuntimeError("Defina a variável APP_CHAVE_API")
        return cls(
            url_bd=os.environ.get("APP_URL_BD", "sqlite:///local.db"),
            nivel_log=os.environ.get("APP_NIVEL_LOG", "INFO"),
            modo_debug=os.environ.get("APP_DEBUG", "0") == "1",
            chave_api=chave,
        )

os.environ["APP_CHAVE_API"] = "teste-123"   # na realidade, vem de fora
cfg = Configuracao.do_ambiente()
print(cfg.url_bd, cfg.nivel_log, cfg.modo_debug)
