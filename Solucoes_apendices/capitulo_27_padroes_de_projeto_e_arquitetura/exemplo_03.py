# Capítulo 27 — Padrões de projeto e arquitetura
# Secção: Adapter: integrar interfaces diferentes

class ClienteSmsFornecedor:
    """Biblioteca externa (não a podemos alterar)."""
    def send_message(self, phone_number: str, body: str, sender_id: str):
        return {"status": "queued", "to": phone_number, "chars": len(body)}

class AdaptadorSms:
    def __init__(self, cliente: ClienteSmsFornecedor, remetente: str):
        self._cliente, self._remetente = cliente, remetente

    def notificar(self, destino: str, mensagem: str) -> bool:
        numero = "+351" + destino.replace(" ", "")
        resposta = self._cliente.send_message(numero, mensagem[:160],
                                              self._remetente)
        return resposta["status"] == "queued"

canal = AdaptadorSms(ClienteSmsFornecedor(), "LOJA")
print(canal.notificar("912 345 678", "A sua encomenda foi enviada."))
