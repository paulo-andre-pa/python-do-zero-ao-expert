# Capítulo 8 — Funções
# Secção: Tipos de argumentos

def transferir(origem, destino, /, valor, *, urgente=False):
    modo = "URGENTE" if urgente else "normal"
    return f"{valor} € de {origem} para {destino} ({modo})"

print(transferir("PT50-001", "PT50-002", 250, urgente=True))
