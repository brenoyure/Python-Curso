# Veja a declaração das 4 variáveis:
dia_ini = 24
dia_fim = 28
mes = "fevereiro"
ano = 2017

# Pedro precisa criar a seguinte string:
# Em 2017 o Carnaval acontece em fevereiro do dia 24 até o dia 28

# Resposta
frase = "Em {} o Carnaval acontece em {} do dia {} até o dia {}".format(ano, mes, dia_ini, dia_fim)
print(frase)
