# Capítulo 7 — Dicionários e conjuntos
# Secção: Conjuntos

python = {"Ana", "Bruno", "Carla", "Duarte"}
java = {"Carla", "Duarte", "Eva"}
print(python & java)    # interseção: sabem as duas
print(python | java)    # união: sabem pelo menos uma
print(python - java)    # diferença: só Python
print(python ^ java)    # diferença simétrica: só uma delas
print({"Ana"} <= python)  # subconjunto
