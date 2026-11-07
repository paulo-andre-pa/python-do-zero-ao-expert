# Capítulo 17 — Expressões regulares, datas e outras ferramentas essenciais
# Secção: Mais estruturas de dados

from collections import deque, ChainMap
import heapq

# deque: fila de dupla entrada, eficiente nas duas pontas
historico = deque(maxlen=3)
for pagina in ["/", "/produtos", "/carrinho", "/checkout"]:
    historico.append(pagina)
print(list(historico))

# heapq: obter os N maiores/menores sem ordenar tudo; filas de prioridade
vendas = {"Ana": 8200, "Rui": 12100, "Eva": 9900, "Tó": 15300, "Lia": 7100}
print(heapq.nlargest(3, vendas.items(), key=lambda kv: kv[1]))

fila = []
heapq.heappush(fila, (2, "responder e-mails"))
heapq.heappush(fila, (1, "servidor em baixo!"))
heapq.heappush(fila, (3, "atualizar documentação"))
print(heapq.heappop(fila))

# ChainMap: procurar em vários dicionários por ordem de prioridade
omissao = {"tema": "claro", "idioma": "pt", "fonte": 12}
ambiente = {"idioma": "en"}
linha_comandos = {"fonte": 14}
config = ChainMap(linha_comandos, ambiente, omissao)
print(config["tema"], config["idioma"], config["fonte"])
