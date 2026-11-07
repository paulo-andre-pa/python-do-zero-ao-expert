# Capítulo 9 — Ficheiros e exceções
# Secção: Lançar exceções
# Este exemplo termina, de propósito, com uma exceção.

def carregar_config(caminho):
    try:
        with open(caminho, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError as e:
        raise RuntimeError("Configuração em falta") from e

carregar_config("config.ini")
