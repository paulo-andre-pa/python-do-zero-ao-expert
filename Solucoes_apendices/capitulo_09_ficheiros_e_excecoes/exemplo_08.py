# Capítulo 9 — Ficheiros e exceções
# Secção: Exceções: quando algo corre mal

try:
    with open("nao_existe.txt", encoding="utf-8") as f:
        dados = f.read()
except FileNotFoundError as erro:
    print("Ficheiro em falta:", erro.filename)
    print("Mensagem:", erro)
