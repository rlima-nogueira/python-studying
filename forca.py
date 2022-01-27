import random 



def jogar():
    imprimir_mensagem_boas_vindas()

    palavra_secreta = escolher_palavra_secreta()
    
    letras_acertadas = inicializar_letras(palavra_secreta)
    
    quantidade_erros = 0
    enforcou = False
    acertou = False
    
    print("A palavra tem {} letras".format(letras_acertadas))
    
    while (not enforcou and not acertou):
        chute = pedir_chute_jogador()
        
        if(chute in palavra_secreta):
            posicao_letra = 0
            for letra in palavra_secreta:
                #transforma tudo pra maiusculo
                if (chute == letra):
                    letras_acertadas[posicao_letra] = letra
                posicao_letra += 1
        else: 
            quantidade_erros += 1
            desenha_forca(quantidade_erros)
        
        enforcou = quantidade_erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprimir_mensagem_ganhador()
    else: 
        imprimir_mensagem_perdedor(palavra_secreta)
        

    
    


def imprimir_mensagem_boas_vindas():
    print("**************************************")
    print("Olá, bem vindo ao jogo de forca.")
    print("**************************************")

def escolher_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    
    arquivo.close()
    
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializar_letras(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def pedir_chute_jogador(): 
    chute = input("Digite uma letra: ")
    #ignora os espaços
    chute = chute.strip().upper()
    return chute

def imprimir_mensagem_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprimir_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprimir_mensagem_fim_do_jogo():
    print("**************************************")
    print("FIM DO JOGO")
    print("**************************************")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == "__main__"):
    jogar()
