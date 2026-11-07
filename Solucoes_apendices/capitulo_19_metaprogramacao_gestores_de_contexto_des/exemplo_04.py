# Capítulo 19 — Metaprogramação: gestores de contexto, descritores e metaclasses
# Secção: Gestores de contexto

from contextlib import suppress, ExitStack, redirect_stdout
import io, os

with suppress(FileNotFoundError):        # ignora um erro esperado
    os.remove("ficheiro_inexistente.tmp")

buffer = io.StringIO()
with redirect_stdout(buffer):            # captura o que é impresso
    print("isto vai para o buffer")
print("capturado:", buffer.getvalue().strip())

nomes = ["a.txt", "b.txt", "c.txt"]
with ExitStack() as pilha:               # número variável de contextos
    ficheiros = [pilha.enter_context(open(n, "w")) for n in nomes]
    for f in ficheiros:
        f.write("dados")
print(all(f.closed for f in ficheiros))
