"""Micro-framework WSGI: rotas por expressão regular e respostas JSON."""
import json
import re
from collections.abc import Callable
from http import HTTPStatus
from urllib.parse import parse_qs

class ErroHTTP(Exception):
    def __init__(self, estado: int, mensagem: str) -> None:
        super().__init__(mensagem)
        self.estado = estado

class Pedido:
    def __init__(self, environ: dict) -> None:
        self.metodo = environ["REQUEST_METHOD"]
        self.caminho = environ.get("PATH_INFO", "/")
        self.query = {k: v[0] for k, v in
                      parse_qs(environ.get("QUERY_STRING", "")).items()}
        tamanho = int(environ.get("CONTENT_LENGTH") or 0)
        entrada = environ["wsgi.input"]
        self._corpo = entrada.read(tamanho) if tamanho else b""

    def json(self) -> dict:
        try:
            dados = json.loads(self._corpo or b"{}")
        except json.JSONDecodeError:
            raise ErroHTTP(400, "JSON inválido") from None
        if not isinstance(dados, dict):
            raise ErroHTTP(400, "esperava-se um objeto JSON")
        return dados

class App:
    def __init__(self) -> None:
        self.rotas: list[tuple[str, re.Pattern, Callable]] = []

    def rota(self, metodo: str, padrao: str):
        regex = re.compile("^" + re.sub(r"{(\w+)}", r"(?P<\1>\\d+)",
                                        padrao) + "$")
        def decorador(funcao):
            self.rotas.append((metodo, regex, funcao))
            return funcao
        return decorador

    def __call__(self, environ, start_response):
        pedido = Pedido(environ)
        try:
            estado, corpo = self._despachar(pedido)
        except ErroHTTP as e:
            estado, corpo = e.estado, {"erro": str(e)}
        frase = HTTPStatus(estado).phrase
        dados = b"" if corpo is None else json.dumps(
            corpo, ensure_ascii=False).encode()
        start_response(f"{estado} {frase}", [
            ("Content-Type", "application/json; charset=utf-8"),
            ("Content-Length", str(len(dados)))])
        return [dados]

    def _despachar(self, pedido: Pedido):
        caminho_existe = False
        for metodo, regex, funcao in self.rotas:
            m = regex.match(pedido.caminho)
            if m:
                caminho_existe = True
                if metodo == pedido.metodo:
                    args = {k: int(v) for k, v in m.groupdict().items()}
                    return funcao(pedido, **args)
        if caminho_existe:
            raise ErroHTTP(405, "método não permitido")
        raise ErroHTTP(404, "rota inexistente")
