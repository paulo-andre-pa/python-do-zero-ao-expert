# Capítulo 6 — Listas e tuplos
# Secção: Tuplos: sequências imutáveis

registo = ("Lúcia", "Ferreira", 29, "Coimbra")
nome, apelido, idade, cidade = registo
print(apelido, cidade)

primeiro, *meio, ultimo = [10, 20, 30, 40, 50]
print(primeiro, meio, ultimo)

_, _, idade, _ = registo     # _ para valores a ignorar
print(idade)
