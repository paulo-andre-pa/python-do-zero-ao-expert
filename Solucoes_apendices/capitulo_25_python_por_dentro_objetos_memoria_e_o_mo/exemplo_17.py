# Capítulo 25 — Python por dentro: objetos, memória e o modelo de dados
# Secção: Memória das estruturas de dados

dados = bytearray(b"cabecalho:conteudo-muito-grande")
vista = memoryview(dados)
cabecalho = vista[:9]          # não copia
cabecalho[0:1] = b"C"          # altera o buffer original
print(dados[:9], cabecalho.tobytes(), cabecalho.nbytes)
