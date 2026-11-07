# Capítulo 26 — Python idiomático: boas práticas e armadilhas
# Secção: Funções

# antes: o que significam True e False?
# exportar("dados.csv", True, False)

def exportar(caminho, *, cabecalho=True, comprimir=False):
    return f"{caminho} cabecalho={cabecalho} comprimir={comprimir}"

print(exportar("dados.csv", comprimir=True))
