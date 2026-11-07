# Capítulo 7 — Dicionários e conjuntos
# Secção: Dicionários: dados por chave

precos = {"café": 0.80, "água": 1.00, "sumo": 1.50}
print(precos["café"])
precos["chá"] = 0.90          # acrescenta
precos["café"] = 0.85         # atualiza
del precos["água"]            # remove
print(precos, len(precos))
