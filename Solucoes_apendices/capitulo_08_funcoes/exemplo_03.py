# Capítulo 8 — Funções
# Secção: Tipos de argumentos

def descrever(nome, idade, cidade):
    return f"{nome}, {idade} anos, vive em {cidade}"

print(descrever("Rui", 30, "Braga"))                    # posicionais
print(descrever(cidade="Faro", nome="Eva", idade=25))   # nomeados
print(descrever("Ana", cidade="Évora", idade=41))       # mistos
