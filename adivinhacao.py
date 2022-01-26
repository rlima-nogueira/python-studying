print("**************************************")
print("Olá, bem vindo ao jogo de adivinhação.")
print("**************************************")

numero_secreto = 52
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {} tentativas".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ")

    chute = int(chute_str)
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
    
    rodada = rodada +1
        
    
print("**************************************")
print("FIM DO JOGO")
print("**************************************")