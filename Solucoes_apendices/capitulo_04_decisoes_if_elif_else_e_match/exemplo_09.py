# Capítulo 4 — Decisões: if, elif, else e match
# Secção: Correspondência de padrões com match

def executar(comando):
    match comando.split():
        case ["sair"]:
            return "A terminar..."
        case ["ir", direcao] if direcao in ("norte", "sul"):
            return f"A caminhar para {direcao}."
        case ["apanhar", objeto]:
            return f"Apanhou: {objeto}"
        case ["largar", *objetos]:
            return f"Largou {len(objetos)} objeto(s): {', '.join(objetos)}"
        case _:
            return "Comando inválido."

for c in ["ir norte", "ir oeste", "apanhar chave",
          "largar mapa espada", "sair", "dançar"]:
    print(f"{c!r:22} -> {executar(c)}")
