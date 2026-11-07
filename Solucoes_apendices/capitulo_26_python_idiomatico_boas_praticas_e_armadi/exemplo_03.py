# Capítulo 26 — Python idiomático: boas práticas e armadilhas
# Secção: Iteração

utilizadores = [{"id": 7, "nome": "Ana"}, {"id": 9, "nome": "Rui"}]
encontrado = next((u for u in utilizadores if u["id"] == 9), None)
inexistente = next((u for u in utilizadores if u["id"] == 42), None)
print(encontrado, inexistente)
