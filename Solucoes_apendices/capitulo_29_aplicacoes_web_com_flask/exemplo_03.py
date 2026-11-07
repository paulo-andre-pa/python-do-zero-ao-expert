# Capítulo 29 — Aplicações web com Flask
# Secção: Uma sessão completa

from app import criar_app

app = criar_app({"BASE_DADOS": os.path.abspath("demo.db"),
                 "SECRET_KEY": "demonstracao"})
c = app.test_client()
c.post("/auth/registar", data={"nome": "sofia", "senha": "Lisboa2026"})
c.post("/auth/entrar", data={"nome": "sofia", "senha": "Lisboa2026"})
for t in ["Rever proposta", "Ligar ao contabilista"]:
    c.post("/nova", data={"titulo": t})
c.post("/1/feita")
print(c.get("/").get_data(as_text=True))
print("cookie de sessão:", c.get_cookie("session").value[:24] + "...")
