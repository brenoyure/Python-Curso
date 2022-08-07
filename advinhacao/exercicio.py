print("###################################")
print("# Bem-Vindo ao Jogo da Advinhação #")
print("###################################")

numero_secreto = 42
total_de_tentativas = 3

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
        print("Parabéns, você acertou.")
        break  # Usamos o break para sair do laço for quando o usuário acertar.
    else:
        if maior:
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif menor:
            print("Você errou! O seu chute foi menor que o número secreto.")

#    rodada = rodada + 1  <-- não precisa mais somar, pois o laço for já faz isso.

print("Fim de Jogo")
