# Capítulo 3 — Texto: trabalhar com strings
# Secção: Métodos essenciais

linha = "Ana;23;Porto;Engenharia"
campos = linha.split(";")
print(campos)
print(campos[0], "tem", campos[1], "anos")

palavras = "  muitos   espaços   aqui  ".split()   # sem argumento
print(palavras)
print("-".join(palavras))
print(" | ".join(["A", "B", "C"]))
