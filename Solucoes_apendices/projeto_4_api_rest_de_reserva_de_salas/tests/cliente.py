import io, json
from wsgiref.util import setup_testing_defaults

class Cliente:
    def __init__(self, app):
        self.app = app

    def pedido(self, metodo, caminho, corpo=None):
        caminho, _, query = caminho.partition("?")
        dados = json.dumps(corpo).encode() if corpo is not None else b""
        environ = {"REQUEST_METHOD": metodo, "PATH_INFO": caminho,
                   "QUERY_STRING": query, "CONTENT_LENGTH": str(len(dados)),
                   "wsgi.input": io.BytesIO(dados)}
        setup_testing_defaults(environ)
        estado = {}
        def start_response(status, headers):
            estado["codigo"] = int(status.split()[0])
        corpo_resposta = b"".join(self.app(environ, start_response))
        return estado["codigo"], (json.loads(corpo_resposta)
                                  if corpo_resposta else None)
