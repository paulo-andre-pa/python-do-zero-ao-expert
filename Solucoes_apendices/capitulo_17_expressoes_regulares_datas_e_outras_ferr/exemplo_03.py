# Capítulo 17 — Expressões regulares, datas e outras ferramentas essenciais
# Secção: Expressões regulares

linha = ('192.168.1.20 - - [07/Nov/2026:10:15:32] '
         '"GET /api/clientes HTTP/1.1" 200 512')
padrao = re.compile(
    r'(?P<ip>[\d.]+) .* \[(?P<quando>[^\]]+)\] '
    r'"(?P<metodo>\w+) (?P<caminho>\S+) [^"]*" '
    r'(?P<codigo>\d{3}) (?P<bytes>\d+)'
)
m = padrao.search(linha)
print(m.group("ip"), m.group("metodo"), m.group("caminho"), m["codigo"])
print(m.groupdict())
