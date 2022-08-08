import random

print("###################################")
print("# Bem-Vindo ao Jogo da Advinhação #")
print("###################################")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
pontos = 1000
pontos_perdidos = 0

print("Escolha um nível de dificuldade")
print("(1) Fácil  (2) Médio (3) Difícil")
nivel = int(input())

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):  # Usando o laço for para incrementar as rodadas
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um Número entre 1 e 100: ")
    chute = int(chute_str)

    print("Você digitou", chute)

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100.")
        continue  # Usamos o continue para pular para a próxima iteração.

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Parabéns, você acertou. Você fez {} pontos".format(pontos))
        break  # Usamos o break para sair do laço for quando o usuário acertar.
    else:
        if maior:
            print("Você errou! O seu chute foi maior que o número secreto.")
            if rodada == total_de_tentativas:
                print("Número secreto era {}.".format(numero_secreto))
        elif menor:
            print("Você errou! O seu chute foi menor que o número secreto.")
            print("Número secreto era {}.".format(numero_secreto))
    pontos_perdidos = abs(numero_secreto - chute)
    pontos = pontos - pontos_perdidos
    print("Pontuação: {}". format(pontos))
#    rodada = rodada + 1  <-- não precisa mais somar, pois o laço for já faz isso.

print("Fim de Jogo.".format(pontos))
