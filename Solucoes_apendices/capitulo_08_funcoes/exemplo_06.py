# Capítulo 8 — Funções
# Secção: Tipos de argumentos

def media(*valores):
    return sum(valores) / len(valores) if valores else 0

def criar_utilizador(nome, **dados):
    return {"nome": nome, **dados}

print(media(10, 14, 18), media())
print(criar_utilizador("lia", email="lia@x.pt", ativo=True))
