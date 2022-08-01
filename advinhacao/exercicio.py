print("###################################")
print("# Bem-Vindo ao Jogo da Advinhação #")
print("###################################")

numero_secreto = 42

chute_str = input("Digite um Número: ")
chute = int(chute_str)

print("Você digitou", chute)

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

if acertou:
    print("Parabéns, você acertou")
elif maior:
    print("Chute foi Maior")
else:
    print("Chute Foi Menor")

print("Fim do Jogo")