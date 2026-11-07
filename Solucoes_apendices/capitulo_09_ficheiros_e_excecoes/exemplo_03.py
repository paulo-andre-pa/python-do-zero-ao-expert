# Capítulo 9 — Ficheiros e exceções
# Secção: Escrever e ler

from datetime import datetime

def registar(mensagem, ficheiro="app.log"):
    agora = datetime(2026, 3, 14, 9, 30)   # fixo para o exemplo
    with open(ficheiro, "a", encoding="utf-8") as f:
        f.write(f"{agora:%Y-%m-%d %H:%M} {mensagem}\n")

registar("Aplicação iniciada")
registar("Utilizador ana entrou")
print(open("app.log", encoding="utf-8").read())
