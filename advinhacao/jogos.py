import advinhacao
import forca


def exibir_menu():
    print("###################################")
    print("###### Escolha um Jogo ############")
    print("###################################")

    print("1. Advinhação    2. Forca    3. SAIR")
    opcao = int(input())

    if opcao == 1:
        advinhacao.jogar()
    elif opcao == 2:
        forca.jogar()


if __name__ == "__main__":
    exibir_menu()
