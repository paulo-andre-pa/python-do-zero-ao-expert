# Capítulo 17 — Expressões regulares, datas e outras ferramentas essenciais
# Secção: Expressões regulares

codigo_postal = re.compile(r"""
    ^(?P<zona>\d{4})      # quatro dígitos
    -                     # hífen
    (?P<rua>\d{3})$       # três dígitos
""", re.VERBOSE)
for cp in ["4000-322", "4000322", "1000-01"]:
    print(cp, bool(codigo_postal.match(cp)))
