import random

print("**************************************")
print("Olá, bem vindo ao jogo de adivinhação.")
print("**************************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 3

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
        print("Você acertou! O número secreto é: ", chute)
        break
    else:
        if(maior):
            print("O número secreto é maior que ", chute)
        elif(menor):
            print("O número secreto é menor que ", chute)
    
        
    
print("**************************************")
print("FIM DO JOGO")
print("**************************************")