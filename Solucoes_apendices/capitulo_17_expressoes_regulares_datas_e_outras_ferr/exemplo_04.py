# Capítulo 17 — Expressões regulares, datas e outras ferramentas essenciais
# Secção: Expressões regulares

texto = "Entregas: 2026-03-15, 2026-04-02 e 2026-12-24."
print(re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", texto))

def mascarar(m):
    return m.group()[:2] + "*" * (len(m.group()) - 4) + m.group()[-2:]
print(re.sub(r"\b\d{9}\b", mascarar, "Cliente com telefone 912345678"))
