# Capítulo 7 — Dicionários e conjuntos
# Secção: Contar e agrupar

texto = "o gato e o rato e o cão"
contagem = {}
for palavra in texto.split():
    contagem[palavra] = contagem.get(palavra, 0) + 1
print(contagem)
