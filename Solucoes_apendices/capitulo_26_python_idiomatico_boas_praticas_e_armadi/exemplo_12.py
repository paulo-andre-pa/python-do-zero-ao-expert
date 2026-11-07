# Capítulo 26 — Python idiomático: boas práticas e armadilhas
# Secção: Armadilhas famosas

lista = []
if not lista:                 # em vez de: if len(lista) == 0
    print("vazia")
valor = None
if valor is None:             # em vez de: if valor == None
    print("sem valor")
