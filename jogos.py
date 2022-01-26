import forca
import adivinhacao2

def   escolher_jogo():
    print("**************************************")
    print("Olá, bem vindo!")
    print("**************************************")

    print("(1)-Forca (2)-Adivinhe o número")

    jogo = int(input("Escolha o seu jogo: "))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando adivinhe o número")
        adivinhacao2.jogar()

if (__name__ == "__main__"):
    escolher_jogo()