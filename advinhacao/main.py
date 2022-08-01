print("###################################")
print("# Bem vindo ao Jogo de Advinhação #")
print("###################################")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while total_de_tentativas > 0:
    print("Tentativa: ", rodada)
    chute_str = input("Digite um número: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if acertou:
        print("Você Acertou")
        total_de_tentativas = 0
    else:
        if maior:
            print("Chute foi maior")
            rodada = rodada + 1
        elif menor:
            print("Chute foi Menor")
            rodada = rodada + 1

    total_de_tentativas = total_de_tentativas -1
