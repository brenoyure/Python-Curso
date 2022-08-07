import advinhacao

print("###################################")
print("###### Escolha um Jogo ############")
print("###################################")

print("1. Advinhação")
opcao = int(input())

if opcao == 1:
    advinhacao.jogar()
