# Capítulo 27 — Padrões de projeto e arquitetura
# Secção: Decorator e Proxy: acrescentar comportamento

class RepositorioPrecos:
    def __init__(self):
        self.consultas = 0
    def preco(self, produto: str) -> float:
        self.consultas += 1                  # imagine uma consulta lenta
        return {"café": 0.8, "chá": 0.9}.get(produto, 0.0)

class ComCache:
    def __init__(self, interno):
        self._interno, self._cache = interno, {}
    def preco(self, produto: str) -> float:
        if produto not in self._cache:
            self._cache[produto] = self._interno.preco(produto)
        return self._cache[produto]

repo = RepositorioPrecos()
rapido = ComCache(repo)
for p in ["café", "chá", "café", "café"]:
    rapido.preco(p)
print("consultas reais:", repo.consultas)
