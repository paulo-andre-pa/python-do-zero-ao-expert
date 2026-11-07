# Capítulo 7 — Dicionários e conjuntos
# Secção: Conjuntos

emails = ["a@x.pt", "b@x.pt", "a@x.pt", "c@x.pt", "b@x.pt"]
unicos = set(emails)
print(len(emails), len(unicos))
print("c@x.pt" in unicos)
unicos.add("d@x.pt")
unicos.discard("zzz@x.pt")   # não dá erro se não existir
print(sorted(unicos))
