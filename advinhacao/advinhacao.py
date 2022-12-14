import random

import jogos


def jogar():
    print("###################################")
    print("# Bem-Vindo ao Jogo da Advinhação #")
    print("###################################")

    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1)Fácil (2)Médio (3) Difícil")
    nivel = int(input("Define um nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um Número entre 1 e 100: ")
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100.")
            continue

        print("Você digitou", chute)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Parabéns, você acertou. Você fez {} pontos.".format(pontos))
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif menor:
                print("Você errou! O seu chute foi menor que o número secreto.")
            ponto_perdidos = abs(numero_secreto - chute)
            pontos = pontos - ponto_perdidos

    print("Fim do Jogo")
    jogos.exibir_menu()


# Utilizamos esse if name fora da função, para conseguirmos executar o arquivo diretamente, sem passar pelo main.py

if __name__ == "__main__":
    jogar()
