# Capítulo 26 — Python idiomático: boas práticas e armadilhas
# Secção: Lista de verificação para revisões de código

def relatorio(dados, separador=",", resultado=[]):
    str = ""
    for i in range(len(dados)):
        if dados[i]["ativo"] == True:
            try:
                valor = float(dados[i]["saldo"])
                nome = dados[i]["nome"].strip().title()
                str += nome + separador + "%.2f" % valor + "\n"
                resultado.append(nome)
            except:
                pass
    if len(resultado) == 0:
        return False
    return str
