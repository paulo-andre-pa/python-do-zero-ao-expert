# Capítulo 3 — Texto: trabalhar com strings
# Secção: Métodos essenciais

frase = "Python é simples. Python é poderoso."
print(frase.count("Python"))
print(frase.find("simples"))      # índice ou -1 se não existir
print("poderoso" in frase)        # teste de pertença
print(frase.startswith("Py"), frase.endswith("."))
print(frase.replace("Python", "Ruby", 1))
