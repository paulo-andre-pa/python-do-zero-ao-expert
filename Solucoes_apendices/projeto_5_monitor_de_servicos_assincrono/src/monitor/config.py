"""Leitura e validação do ficheiro de configuração TOML."""
import tomllib
from dataclasses import dataclass
from pathlib import Path

from monitor.verificadores import (Verificador, VerificadorHTTP,
                                   VerificadorTCP)

@dataclass(frozen=True)
class ConfigServico:
    nome: str
    verificador: Verificador
    timeout: float = 2.0
    limite_falhas: int = 3

def criar_verificador(dados: dict) -> Verificador:
    match dados:
        case {"tipo": "http", "url": str(url)}:
            return VerificadorHTTP(url)
        case {"tipo": "tcp", "host": str(host), "porta": int(porta)}:
            return VerificadorTCP(host, porta)
        case _:
            raise ValueError(f"serviço mal configurado: {dados}")

def carregar(caminho: Path) -> list[ConfigServico]:
    with caminho.open("rb") as f:
        dados = tomllib.load(f)
    omissoes = dados.get("omissoes", {})
    servicos = []
    for s in dados.get("servico", []):
        s = omissoes | s
        servicos.append(ConfigServico(
            s["nome"], criar_verificador(s),
            float(s.get("timeout", 2.0)), int(s.get("limite_falhas", 3))))
    nomes = [s.nome for s in servicos]
    if len(nomes) != len(set(nomes)):
        raise ValueError("há nomes de serviço repetidos")
    return servicos
