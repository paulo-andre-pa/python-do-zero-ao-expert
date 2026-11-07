# Capítulo 5 — Ciclos: while e for
# Secção: O ciclo for

tarefas = ["Rever relatório", "Enviar e-mails", "Reunião às 15h"]
for numero, tarefa in enumerate(tarefas, start=1):
    print(f"{numero}. {tarefa}")
