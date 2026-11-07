# Capítulo 3 — Texto: trabalhar com strings
# Secção: Métodos essenciais

for s in ["2026", "abc", "abc123", "   ", "Lisboa"]:
    print(f"{s!r:10} digito={s.isdigit()} alfa={s.isalpha()} "
          f"alnum={s.isalnum()} espaço={s.isspace()}")
