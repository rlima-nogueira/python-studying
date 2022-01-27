import random 

def jogar():
    print("**************************************")
    print("Olá, bem vindo ao jogo de forca.")
    print("**************************************")

    arquivo = open("palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    
    arquivo.close()
    
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    
    letras_acertadas = ["_" for letra in palavra_secreta]
    quantidade_erros = 0
    enforcou = False
    acertou = False
    
    print("A palavra tem {} letras".format(letras_acertadas))
    
    while (not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        #ignora os espaços
        chute = chute.strip().upper()
        
        if(chute in palavra_secreta):
            posicao_letra = 0
            for letra in palavra_secreta:
                #transforma tudo pra maiusculo
                if (chute == letra):
                    letras_acertadas[posicao_letra] = letra
                posicao_letra += 1
        else: 
            quantidade_erros += 1
        
        enforcou = quantidade_erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("PARABÉNS, VOCÊ GANHOU!")    
    else: 
        print("Você perdeu. Tente novamente!")
        print("A palavra era: {}".format(palavra_secreta))
        
    print("**************************************")
    print("FIM DO JOGO")
    print("**************************************")

if (__name__ == "__main__"):
    jogar()