import random

def jogar():
    print("**************************************")
    print("Olá, bem vindo ao jogo de adivinhação.")
    print("**************************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1)-Fácil (2)-Médio (3)-Difícil")

    nivel = int(input("Digite o nível desejado: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {} tentativas".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")

        chute = int(chute_str)
        
        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        
        acertou = numero_secreto == chute
        menor = chute > numero_secreto
        maior = chute < numero_secreto


        if (acertou): 
            print("Você acertou e fez {} pontos! O número secreto é: ".format(pontos), chute)
            break
        else:
            if(maior):
                print("O número secreto é maior que ", chute)
            elif(menor):
                print("O número secreto é menor que ", chute)
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        
            
        
    print("**************************************")
    print("FIM DO JOGO")
    print("**************************************")

if (__name__ == "__main__"):
    jogar()