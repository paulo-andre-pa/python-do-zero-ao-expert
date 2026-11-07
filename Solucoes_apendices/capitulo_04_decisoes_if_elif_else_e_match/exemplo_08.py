# Capítulo 4 — Decisões: if, elif, else e match
# Secção: Correspondência de padrões com match

def descrever_codigo_http(codigo):
    match codigo:
        case 200:
            return "OK"
        case 301 | 302:
            return "Redirecionamento"
        case 404:
            return "Não encontrado"
        case 500:
            return "Erro interno do servidor"
        case _:
            return "Código desconhecido"

for c in (200, 302, 404, 418):
    print(c, descrever_codigo_http(c))
